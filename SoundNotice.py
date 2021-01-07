def beep(freq, dur=100):
    """
        sound beep
        @param freq 
        @param dur time（ms）
    """
    # Windows
    import winsound
    winsound.Beep(freq, dur)
beep(2000, 800)