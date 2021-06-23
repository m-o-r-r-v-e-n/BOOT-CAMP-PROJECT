{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "PBAlLJ6HU0mk"
      },
      "source": [
        "import requests\n",
        "#import os\n",
        "from datetime import datetime\n",
        "\n",
        "api_key = '87d845b0b6cf29baa1a73cc34b067a95'\n",
        "location = input(\"Enter the city name: \")\n",
        "\n",
        "complete_api_link = \"https://api.openweathermap.org/data/2.5/weather?q=\"+location+\"&appid=\"+api_key\n",
        "api_link = requests.get(complete_api_link)\n",
        "api_data = api_link.json()\n",
        "\n",
        "#create variables to store and display data\n",
        "temp_city = ((api_data['main']['temp']) - 273.15)\n",
        "weather_desc = api_data['weather'][0]['description']\n",
        "hmdt = api_data['main']['humidity']\n",
        "wind_spd = api_data['wind']['speed']\n",
        "date_time = datetime.now().strftime(\"%d %b %Y | %I:%M:%S %p\")\n",
        "\n",
        "print (\"-------------------------------------------------------------\")\n",
        "print (\"Weather Stats for - {}  || {}\".format(location.upper(), date_time))\n",
        "print (\"-------------------------------------------------------------\")\n",
        "\n",
        "print (\"Current temperature is: {:.2f} deg C\".format(temp_city))\n",
        "print (\"Current weather desc  :\",weather_desc)\n",
        "print (\"Current Humidity      :\",hmdt, '%')\n",
        "print (\"Current wind speed    :\",wind_spd ,'kmph')"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}