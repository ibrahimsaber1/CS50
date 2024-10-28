import pytest
import os
import csv
from project import (
    validate_application,
    store_application,
    select_random_winner,
    VALID_ENTRIES_FILE,
    INVALID_ENTRIES_FILE
)

# Sample valid application
@pytest.fixture
def sample_valid_application():
    return {
        "First Name": "ibrahim",
        "Last Name": "sebaq",
        "Middle Name": "saber mohamed",
        "Date of Birth": "2000-07-15",
        "City of Birth": "Giza",
        "Nationality": "Egypt",
        "Address": "4 medhat Street",
        "Email": "ibrahimsaber622@gmail.com",
        "Phone Number": "+201027624649",
        "Education": "Bachelor Degree"
    }

# Sample invalid application
@pytest.fixture
def sample_invalid_application():
    return {
        "First Name": "",
        "Last Name": "Smith",
        "Middle Name": "",
        "Date of Birth": "2008-10-20",
        "City of Birth": "Los Angeles",
        "Nationality": "China",
        "Address": "",
        "Email": "invalidemail@",
        "Phone Number": "12345",
        "Education": "Primary School"
    }

# Test for valid application
def test_validate_application_valid(sample_valid_application):
    is_valid, errors = validate_application(sample_valid_application)
    assert is_valid
    assert errors == []

# Test for invalid application
def test_validate_application_invalid(sample_invalid_application):
    is_valid, errors = validate_application(sample_invalid_application)
    assert not is_valid
    assert len(errors) >= 1  # At least one error

# Test storing a valid application
def test_store_application_valid(tmp_path, sample_valid_application):
    valid_file = tmp_path / "test_valid.csv"
    store_application(sample_valid_application, is_valid=True, valid_file=valid_file)

    with open(valid_file, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        entries = list(reader)
        assert len(entries) == 1
        assert entries[0]["First Name"] == "ibrahim"  # Updated to match sample data

# Test storing an invalid application
def test_store_application_invalid(tmp_path, sample_invalid_application):
    invalid_file = tmp_path / "test_invalid.csv"
    store_application(sample_invalid_application, is_valid=False, invalid_file=invalid_file)

    with open(invalid_file, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        entries = list(reader)
        assert len(entries) == 1
        assert entries[0]["Last Name"] == "Smith"  # Corrected syntax

# Test selecting a random winner from multiple valid entries
def test_select_random_winner(tmp_path):
    # Create a valid entries file with multiple entries
    valid_file = tmp_path / "test_valid.csv"
    entries = [
        {
            "First Name": "Alice",
            "Last Name": "Brown",
            "Middle Name": "B.",
            "Date of Birth": "1985-07-23",
            "City of Birth": "Toronto",
            "Nationality": "Australia",
            "Address": "456 Oak Avenue",
            "Email": "alice.brown@example.com",
            "Phone Number": "+1987654321",
            "Education": "Master"
        },
        {
            "First Name": "Bob",
            "Last Name": "Green",
            "Middle Name": "C.",
            "Date of Birth": "1978-11-30",
            "City of Birth": "Sydney",
            "Nationality": "United Kingdom",
            "Address": "789 Pine Road",
            "Email": "bob.green@example.com",
            "Phone Number": "+1123456789",
            "Education": "PhD"
        }
    ]

    # Write entries to the CSV file
    with open(valid_file, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = list(entries[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            writer.writerow(entry)

    # Select a random winner
    winner = select_random_winner(valid_file=str(valid_file))
    assert winner in entries

# Test selecting a winner when there are no entries
def test_select_random_winner_no_entries(tmp_path):
    empty_file = tmp_path / "empty_valid.csv"

    # Create an empty valid entries file
    with open(empty_file, mode='w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["First Name", "Last Name", "Middle Name", "Date of Birth", "City of Birth",
                         "Nationality", "Address", "Email", "Phone Number", "Education"])

    winner = select_random_winner(valid_file=str(empty_file))
    assert winner is None

# Test selecting a winner when the file does not exist
def test_select_random_winner_file_not_found():
    winner = select_random_winner(valid_file="non_existent_file.csv")
    assert winner is None
