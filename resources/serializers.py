from __future__ import unicode_literals

from rest_framework import serializers

from .models import (
    People,
    Planet,
    Film,
    Species,
    Vehicle,
    Starship,
)


class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = People
        fields = (
            "id",
            "name",
            "height",
            "mass",
            "hair_color",
            "skin_color",
            "eye_color",
            "birth_year",
            "gender",
            "homeworld",
            "films",
            "species",
            "vehicles",
            "starships",
            "created",
            "edited",
            "url",
        )


class PlanetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Planet
        fields = (
            "id",
            "name",
            "rotation_period",
            "orbital_period",
            "diameter",
            "climate",
            "gravity",
            "terrain",
            "surface_water",
            "population",
            "residents",
            "films",
            "created",
            "edited",
            "url"
        )


class FilmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Film
        fields = (
            "id",
            "title",
            "episode_id",
            "opening_crawl",
            "director",
            "producer",
	        "release_date",
            "characters",
            "planets",
            "starships",
            "vehicles",
            "species",
            "created",
            "edited",
            "url"
        )


class SpeciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Species
        fields = (
            "id",
            "name",
            "classification",
            "designation",
            "average_height",
            "skin_colors",
            "hair_colors",
            "eye_colors",
            "average_lifespan",
            "homeworld",
            "language",
            "people",
            "films",
            "created",
            "edited",
            "url"
        )


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = (
            "id",
            "name",
            "model",
            "manufacturer",
            "cost_in_credits",
            "length",
            "max_atmosphering_speed",
            "crew",
            "passengers",
            "cargo_capacity",
            "consumables",
            "vehicle_class",
            "pilots",
            "films",
            "created",
            "edited",
            "url"
        )


class StarshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Starship
        fields = (
            "id",
            "name",
            "model",
            "manufacturer",
            "cost_in_credits",
            "length",
            "max_atmosphering_speed",
            "crew",
            "passengers",
            "cargo_capacity",
            "consumables",
            "hyperdrive_rating",
            "MGLT",
            "starship_class",
            "pilots",
            "films",
            "created",
            "edited",
            "url"
        )

