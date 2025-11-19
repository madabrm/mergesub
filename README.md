# mergesub

**mergesub** is a flexible Python batch tool to automatically merge video files (MKV, MP4, WebM, AVI, MOV) with multi-language subtitle files (SRT, ASS, SSA, SUB, VTT, TIFF) using `mkvmerge`. It auto-detects language tracks based on the filename and can be easily installed using a Homebrew tap or run directly in terminal workflows.

## Features

- Automatically detects and processes all video and subtitle files in the current directory
- Supports a wide variety of video and subtitle formats
- Multi-language subtitle support using filename suffixes (e.g., `_EN`, `_FR`)
- Saves merged results to a dedicated `output/` subdirectory
- Easy installation with Homebrew, with all dependencies handled

## Installation (via Homebrew)

Make sure you have Homebrew installed on macOS or Linux.

Add the tap and install:
```
brew tap madabrm/tap
brew install madabrm/tap/mergesub
```
All dependencies (Python & mkvtoolnix) will be installed automatically by Homebrew if not already present.

## Usage

1. Open a terminal and navigate (cd) to the folder containing your videos and subtitles.
2. Run:
   ```
   mergesub
   ```
3. All supported video files in the folder will be merged with matching subtitles, placing results in `./output/`.

## Subtitle Naming for Multi-Language Support

- `[video_name].[ext]` → default language is Indonesian (`ind`)
- `[video_name]_EN.[ext]` → English subtitles  
- `[video_name]_FR.[ext]` → French subtitles  
- etc.
- Example:
  ```
  Movies.mkv
  Movies.srt
  Movies_EN.srt
  ```


## Dependencies

- Python 3.x (handled by Homebrew)
- mkvtoolnix / mkvmerge (handled by Homebrew)

## Contributing

Pull requests and issues are welcome! If you discover any bugs or want to suggest features, please open an issue.

---

> For more details on Homebrew tap best practices, see the [official Homebrew documentation](https://docs.brew.sh/How-to-Create-and-Maintain-a-Tap) and [Formula Cookbook](https://docs.brew.sh/Formula-Cookbook).
```
