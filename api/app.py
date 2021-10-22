from flask import Flask, request, jsonify
from database import db, Person, PersonSchema, person_schema, Appointment
from datetime import timedelta, datetime
from http_status_codes import HTTP_200_OK, HTTP_400_BAD_REQUEST

# instantiate flask app
app = Flask(__name__)

# set configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# ENDPOINTS
# Create a person
@app.route('/person', methods=['POST'])
def person():

    try: 
        name = request.json['name']
        email = request.json['email']

        new_person = Person(name=name, email=email)

        db.session.add(new_person)
        db.session.commit()

        return person_schema.jsonify(new_person)
    except Exception as e:
        return jsonify({'Error': 'Invalid request'}), HTTP_400_BAD_REQUEST

# Create meeting involving one or more persons at a given time slot
@app.route('/meeting', methods=['POST'])
def meeting():

    title = request.json['content']
    content = request.json['content']
    start = datetime.fromtimestamp(request.json['start'])
    end = start + timedelta(hours=1)

    new_meeting = Appointment(title=title, content=content, start=start, end=end)
    db.session.add(new_meeting)
    db.session.commit()

    persons = request.json['persons']
    for p in persons:
        user = Person.query.get(p)
        new_meeting.meets.append(user)
        db.session.commit()

    return jsonify({'message': 'Success'}), HTTP_200_OK

# Show the schedule of a person
@app.route('/schedule/<int:person_id>', methods=['GET'])
def schedule(person_id):

    user = Person.query.get(person_id)

    data = []
    for meeting in user.meetings:
        data.append({
            'title': meeting.title,
            'content': meeting.content,
            'start': meeting.start,
            'end': meeting.end
        })
    return jsonify({'data': data}), HTTP_200_OK

if __name__ == '__main__':

    with app.app_context():
        print('app context')
        # db.drop_all()
        # db.create_all()

    app.run(debug=True)
