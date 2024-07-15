from auth import auth_bp


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'Logged in'


@auth_bp.route('/logout')
def logout():
    return 'Logged out'