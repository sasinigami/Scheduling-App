## POST /person
Create persons with a name and unique email.
### Request body:
```bash
{
    "name": "test",
    "email": "email@gmail.com"
}
```

## POST /meeting
Create meetings involving one or more persons at a given time slot.
### Request body:
```bash
{
    "persons": [
        1
    ],
    "title": "title2",
    "content": "lorem ipsum2",
    "start": 1634799894.479386 # timestamp
}
```

## GET /schedule/[id]
- Show the schedule, i.e., the upcoming meetings, for a given person.
- Can be used to suggest available timeslots for meetings
No request body

## How to run
1. Install the requirements
2. Create database by uncommenting this db.create_all() on app.py
3. run this command after:
```bash
python app.py
```

## Unit test
run by this command
```bash
python api\test_api.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
