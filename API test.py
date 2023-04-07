@api.route('/delete-key', methods=['POST'])
def delete_key():
    key = json.loads(request.data)
    keyid = key['keyID']
    key = APIKEY.query.get(keyid)
    if key:
        if current_user.user_type == 'admin':
            db.session.delete(key)
            db.session.commit()
            flash(f'Key: {keyid} was removed', category='success')
            return jsonify({})
        else:
            flash('Only Admins can remove Keys', category='error')
