"""Module for generating games by user report"""
import sqlite3
from django.shortcuts import render
from levelupapi.models import Event
from levelupreports.views import Connection


def userevent_list(request):
    """Function to build an HTML report of games by user"""
    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Query for all events, with related user info.
            db_cursor.execute("""
                SELECT
                    eg.id,
                    u.first_name || ' ' || u.last_name AS full_name,
                    u.id user_id,
                    eg.event_id,
                    e.location,
                    e.time,
                    e.day,
                    e.id event_id_number,
                    g.title
                    
                FROM levelupapi_eventgamer eg
                JOIN levelupapi_event e ON e.id = eg.event_id
                JOIN levelupapi_gamer gr ON gr.id = eg.gamer_id
                JOIN levelupapi_game g ON g.id = e.game_id
                JOIN auth_user u ON u.id = gr.user_id
            """)

            dataset = db_cursor.fetchall()
            events_by_user = {}

            for row in dataset:
                # Crete a Event instance and set its properties
                event = Event()
                event.id = row["event_id_number"]
                event.day = row["day"]
                event.time = row["time"]
                event.location = row["location"]
                event.title = row["title"]

                # Store the user's id
                uid = row["user_id"]

                # If the user's id is already a key in the dictionary...
                if uid in events_by_user:

                    # Add the current event to the `events` list for it
                    events_by_user[uid]['events'].append(event)

                else:
                    # Otherwise, create the key and dictionary value
                    events_by_user[uid] = {}
                    events_by_user[uid]["user_id"] = uid
                    events_by_user[uid]["full_name"] = row["full_name"]
                    events_by_user[uid]["events"] = [event]

        # Get only the values from the dictionary and create a list from them
        list_of_users_with_events = events_by_user.values()

        # Specify the Django template and provide data context
        template = 'users/list_with_events.html'
        context = {
            'userevents_list': list_of_users_with_events
        }

        return render(request, template, context)