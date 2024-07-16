from flask import request, jsonify
from journals import journal_bp
from flask_login import login_required, current_user
from models import Journals
from datetime import datetime


# TODO: review http codes
@login_required
@journal_bp.route('/home')
def home_page():
    if current_user.is_authenticated:
        user_logged_in = current_user.id
        journals = Journals.query.filter_by(user_id=user_logged_in).all()
        journal_list = [journal.as_dict() for journal in journals]

        return jsonify(journal_list), 200
    else:
        return jsonify({'message': 'Login to access this page'}), 401


@login_required
@journal_bp.route('/add_journal', methods=['POST'])
def add_journal():
    if current_user.is_authenticated:
        user_logged_in = current_user.id 

        # journal details from frontend
        title = request.json.get('title')
        content = request.json.get('content')
        category = request.json.get('category')

        new_journal = Journals(title=title, 
                               content=content, category=category,user_id=user_logged_in)
        
        try:
            new_journal.save()
            return jsonify({'message': 'Journal added successfully'}), 201
        except Exception as e:
            print('Error: ', e)
            return jsonify({'error': 'Unable to add journal to database'}), 400
    else:
        return jsonify({'error': 'Login to access this page!'}), 401


@login_required
@journal_bp.route('/edit_journal/<id>', methods=['GET', 'POST'])
def edit_journal(id):
    if current_user.is_authenticated:
        user_logged_in = current_user.id

        editable_journal = Journals.query.filter_by(id=id, user_id=user_logged_in).first()
        if not editable_journal:
            return jsonify({'message': 'No journal found'}), 204 

        if request.method == 'GET':
            title = editable_journal.title 
            content = editable_journal.content
            category = editable_journal.category
            date_created = editable_journal.created_at

            return jsonify({
                'title': title,
                'content': content,
                'category': category,
                'date_created': date_created
            })
        
        elif request.method == 'POST':
            # the get request will save the data from db in text field and allow user to make
            # modifications on that. 
            # when saving, the request will have what the user modified 
            # in case user didn't modify, the value that was in the db originally will be passed as request
            request_title = request.json.get('title')
            request_content = request.json.get('content')
            request_category = request.json.get('category')

            if not request_category or not request_title or not request_content:
                return jsonify({'error': 'all required fields must be filled!'}), 400
            
            try:
                editable_journal.update(title=request_title, 
                                        content=request_content, category=request_category,
                                        last_modified=datetime.now())
                
                return jsonify({'message': 'Journal updated successfully'})
            except Exception as e:
                print('Error: ', e)
                return jsonify({'error': 'Error adding journal to database'}), 400
            
    else:
        return jsonify({'message': 'Login to access this page'}), 401


@login_required
@journal_bp.route('/delete_journal/<id>', methods=['GET'])
def delete_journal(id):
    if current_user.is_authenticated:
        journal = Journals.query.filter_by(id=id).first()

        if not journal:
            return jsonify({'error': 'journal not found'}), 404 
        
        try:
            journal.delete()
            return jsonify({'message': 'journal entry deleted'}), 200
        except Exception as e:
            print('Error', e)
            return jsonify({'error': f'Unable to delete journal. Error: {e}'}), 400
            
    else:
        return jsonify({'message': 'Login to access this page'}), 401

