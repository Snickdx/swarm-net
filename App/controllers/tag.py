from App.models import (Tag, db)

def get_tag_by_id(id):
    print(f"Getting tag with ID: {id}")
    tag = Tag.query.filter_by(id=id).first()
    return tag


def create_new_tag(text, created_date):
    new_tag = Tag(text=text, created=created_date)
    print(f"Creating tag with text: {text}")

    db.session.add(new_tag)
    db.session.commit()
    return new_tag
    

def edit_tag(tag_id, text, created_date):
    tag = get_tag_by_id(tag_id)

    if tag:
        tag.text = text
        tag.created = created_date

        print(f"Updated tag: {tag_id}")
        db.session.add(tag)
        db.session.commit()
        return tag 
    else:
        return None


def delete_tag_by_id(id):
    tag = get_tag_by_id(id)

    if tag:
        print(f"Deleting tag with id: {id}")
        db.session.delete(tag)
        db.session.commit()
        return tag
    return None