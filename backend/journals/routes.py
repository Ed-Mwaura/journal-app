from journals import journal_bp


@journal_bp.route('/home')
def home_page():
    return 'Home page'