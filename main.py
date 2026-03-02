import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as file_json:
        data_json = json.load(file_json)

    for player in data_json.keys():

        race, _ = Race.objects.get_or_create(
            name=data_json[player].get("race").get("name"),
            description=data_json[player].get("race").get("description"),
        )

        if data_json[player]["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=data_json[player].get("guild").get("name"),
                description=data_json[player].get("guild").get("description"),
            )
        else:
            guild = data_json[player].get("guild")

        for skills in data_json[player].get("race").get("skills"):
            Skill.objects.get_or_create(
                name=skills.get("name"),
                bonus=skills.get("bonus"),
                race=race,
            )

        Player.objects.create(
            nickname=player,
            email=data_json[player].get("email"),
            bio=data_json[player].get("bio"),
            race=race,
            guild=guild,
        )


if __name__ == "__main__":
    main()
