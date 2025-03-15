class Loop_Data:
    current_time : float = 0
    new_time : float = 0
    frame_time : float = 0
    accumulator : float = 0
    accumulator_each_second : float = 0

    max_fps : float = 120
    dt : float = 1/max_fps
    t : float = 0

    fps_counter : int = 0
    fps : int = 0
    update_counter: int = 0
    is_running : bool = True 
    is_drawing : bool = False

