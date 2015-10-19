from pydub import AudioSegment


def main():
    song = AudioSegment.from_mp3("sounds/sax.mp3")
    ol = 7324  # Length of 1 loop
    song = song + 5  # Increase volume
    result = []  # Segment array
    output = None

    intro_piano = AudioSegment.from_file("sounds/intro_piano.wav")
    intro_beats = AudioSegment.from_file("sounds/intro_beats.wav")
    are_you_ready = AudioSegment.from_file("sounds/are you ready.wav")
    static = AudioSegment.from_file("sounds/static.mp3")
    # Combine the intros
    intro = intro_piano + intro_beats
    # Overlay "Are you ready"
    intro = intro.overlay(are_you_ready, position=-5300)
    # Interrupt with static
    output = intro + (static[750:] - 10)

    # Loop the song trice
    two_loops = song[:ol*3]
    result.append(two_loops)

    # Glitch sound
    glitch = AudioSegment.from_file("sounds/glitch.mp3")
    result.append(glitch)

    # Reverse the song
    reverse = song[:ol*4].reverse()
    result.append(reverse)

    # Speed up the reverse
    speed_reverse = reverse[:ol*2].speedup(2.0)
    result.append(speed_reverse)

    # Play a glitched sound 10 times
    loop2 = speed_reverse[-130:] * 10
    result.append(loop2)

    # Some silence
    silence = AudioSegment.silent(duration=1500)
    result.append(silence)

    # Fade in the original song
    fade_in = song[ol:ol*3+150].fade_in(ol)
    result.append(fade_in)

    # Add drums to it
    drum_overlay = AudioSegment.from_file("sounds/drum.wav") * 15
    drum_overlay = drum_overlay.fade_in(ol)
    drum_overlay = song[:ol*3].overlay(drum_overlay)
    result.append(drum_overlay)

    # Outro. Suddenly static
    static_fade = ((static - 9) * 5).fade_out(5000)
    outro = (static[:250] - 5) + silence[:100] + (static[:150] - 9) + silence[:500] + static_fade
    result.append(outro)

    # Add all the segments together, export
    for segments in result:
        output += segments
    output.export("output.mp3", format="mp3")


if __name__ == '__main__':
    main()
