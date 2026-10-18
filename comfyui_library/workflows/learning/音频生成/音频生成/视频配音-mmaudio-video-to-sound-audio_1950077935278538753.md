---
key: 音频生成/音频生成/视频配音-mmaudio-video-to-sound-audio_1950077935278538753.json
name: 视频配音-mmaudio-video-to-sound-audio_1950077935278538753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/视频配音-mmaudio-video-to-sound-audio_1950077935278538753.json
hash: 27b04223fbb20997
coverage: 1
learned_at: 2026-10-18 01:24:10
nodes: [VHS_VideoInfo, MMAudioModelLoader, MMAudioFeatureUtilsLoader, VHS_VideoCombine, SaveAudio, MMAudioSampler, VHS_LoadVideo]
patterns: []
missing: []
---

# 音频生成/音频生成/视频配音-mmaudio-video-to-sound-audio_1950077935278538753.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/视频配音-mmaudio-video-to-sound-audio_1950077935278538753.json`

## 结构

**生成流程**：Model → Sampling → Output → Other

**节点**（7 个）：
- `VHS_VideoInfo`
- `MMAudioModelLoader`
- `MMAudioFeatureUtilsLoader`
- `VHS_VideoCombine`
- `SaveAudio`
- `MMAudioSampler` ★核心
- `VHS_LoadVideo`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`VHS_VideoInfo`、`MMAudioModelLoader`、`MMAudioFeatureUtilsLoader`、`VHS_VideoCombine`、`SaveAudio`、`MMAudioSampler`、`VHS_LoadVideo`

**用到的条目**：MMAudioSampler、SaveAudio、VHS_LoadVideo、VHS_VideoCombine、VHS_VideoInfo、MMAudioFeatureUtilsLoader、MMAudioModelLoader、sd15-t2i-basic
