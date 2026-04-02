{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "734f324b-10ac-435b-be5d-511af16d20bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "storage.py - Handles saving weather records to CSV and SQLite.\n",
    "TODO: Implemented by Teammate 3.\n",
    "\"\"\"\n",
    "\n",
    "\n",
    "def save_to_csv(records: list, filepath: str):\n",
    "    \"\"\"\n",
    "    Save records to a CSV file, appending if it already exists.\n",
    "\n",
    "    Args:\n",
    "        records:  list of dicts with weather data\n",
    "        filepath: path to the CSV file\n",
    "    \"\"\"\n",
    "    # TODO: Teammate 3 implements this\n",
    "    raise NotImplementedError(\"storage.py not yet implemented by teammate.\")\n",
    "\n",
    "\n",
    "def save_to_sqlite(records: list, filepath: str):\n",
    "    \"\"\"\n",
    "    Save records to a SQLite database, appending new rows each run.\n",
    "\n",
    "    Args:\n",
    "        records:  list of dicts with weather data\n",
    "        filepath: path to the SQLite .db file\n",
    "    \"\"\"\n",
    "    # TODO: Teammate 3 implements this\n",
    "    raise NotImplementedError(\"storage.py not yet implemented by teammate.\")"
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
