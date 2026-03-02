import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file_json:
        data_json = json.load(file_json)

    for player in data_json.keys():

        race, _ = Race.objects.get_or_create(
            name=data_json[player]["race"]["name"],
            description=data_json[player]["race"]["description"],
        )

        if data_json[player]["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=data_json[player]["guild"]["name"],
                description=data_json[player]["guild"]["description"],
            )
        else:
            guild = data_json[player]["guild"]

        for skills in data_json[player]["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skills["name"],
                bonus=skills["bonus"],
                race=race,
            )

        Player.objects.create(
            nickname=player,
            email=data_json[player]["email"],
            bio=data_json[player]["bio"],
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
