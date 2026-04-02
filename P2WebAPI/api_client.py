{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c6bcfe3-85e9-4b9d-addc-013fcc9ca7ae",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "api_client.py - Handles all HTTP requests to the Open-Meteo API.\n",
    "TODO: Implemented by Teammate 2.\n",
    "\"\"\"\n",
    "\n",
    "import requests\n",
    "\n",
    "BASE_URL = \"https://api.open-meteo.com/v1/forecast\"\n",
    "\n",
    "\n",
    "def fetch_weather_for_cities(cities: list) -> list:\n",
    "    \"\"\"\n",
    "    Fetch weather data for a list of cities.\n",
    "\n",
    "    Args:\n",
    "        cities: list of dicts with keys: name, latitude, longitude\n",
    "\n",
    "    Returns:\n",
    "        list of dicts with weather records\n",
    "    \"\"\"\n",
    "    # TODO: Teammate 2 implements this\n",
    "    # Should use requests.get with params=, error handling, and return list of records\n",
    "    raise NotImplementedError(\"api_client.py not yet implemented by teammate.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
