from flask import Flask, render_template
from nhl_stats.serializers.data_serializer import DataSerializer
from nhl_stats.api.api import API

app = Flask(__name__)
app.secret_key = 'ASecretKey'
data_serializer = DataSerializer()
api = API()


@app.route('/')
def teams_page() -> 'html':
    teams = data_serializer.serialize(api.get_teams())
    return render_template('teams.html',
                           teams=teams)

if __name__ == '__main__':
    app.run(debug=True)