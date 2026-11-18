"""Tests for FS20 command encoding."""

import pytest

from rf_protocols import ModulationType, RadioFrequencyCommand
from rf_protocols.commands.kaku import KakuCommand
from rf_protocols.commands.fs20 import FS20Command, FS20CommandType

def test_fs20_command_frame_length() -> None:
    cmd = FS20Command(housecode="12341234", address="1234", command=FS20CommandType.ON_100_PERCENT, timebase_us=200)
    assert cmd.frequency == 868_350_000
    assert cmd.modulation == ModulationType.OOK
    assert cmd.repeat_count == 3
    timings = cmd.get_raw_timings()
    print(len(timings))
    assert len(timings) == 116

def test_fs20_command_frame_length_extended() -> None:
    cmd = FS20Command(housecode="12341234", address="1234", command=FS20CommandType.ON_100_PERCENT, extension=53, timebase_us=200)
    assert cmd.frequency == 868_350_000
    assert cmd.modulation == ModulationType.OOK
    assert cmd.repeat_count == 3
    timings = cmd.get_raw_timings()
    print(len(timings))
    assert len(timings) == 134