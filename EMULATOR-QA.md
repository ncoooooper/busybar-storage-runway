# Emulator verification

Real file growth and real filesystem capacity on a temporary local folder; elapsed sampling interval was controlled.

Created a 2 MiB file between measurements. The adapter read allocated disk blocks and calculated estimated runway from the growth rate.

13 distinct frames were recorded on firmware 1.3.1. App io.ncoooooper.storagerunway exited: finished; heap peak 81.6 of 128 KiB. Screenshots are in screenshots/ and the recording is in media/.

## Display capture

Firmware 1.3.1 rendered both README examples. The display run replayed sample inputs in a separate emulator project. The source test above describes how those readings were obtained. Each square in a guide GIF is one front LED in a 16 × 16 cell. The production archive was built from the source in this repository.

## Screen transition capture

Firmware 1.3.1 rendered the display sequences in the README. The release archive also ran on a fresh emulator with rapid wheel reversals and Back during a transition. The guide uses a 14 × 14 lit area inside each 16 × 16 cell. Input sequences, frame counts and the release archive checksum are in [the capture record](media/screen-transitions.json).
