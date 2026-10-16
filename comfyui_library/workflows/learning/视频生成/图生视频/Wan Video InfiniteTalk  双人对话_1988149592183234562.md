---
key: 视频生成/图生视频/Wan Video InfiniteTalk  双人对话_1988149592183234562.json
name: Wan Video InfiniteTalk  双人对话_1988149592183234562.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1988149592183234562.json
hash: 8caeddc37fcfab60
coverage: 0.931034
learned_at: 2026-10-15 22:33:01
nodes: [WanVideoLoraSelect, AudioSeparation, LoadWanVideoT5TextEncoder, WanVideoTextEncode, AudioSeparation, DownloadAndLoadWav2VecModel, SoundFlow_TrimAudio, SoundFlow_TrimAudio, LoadImage, WanVideoClipVisionEncode, CLIPVisionLoader, PreviewImage, easy showAnything, RH_GetAudioDuration, RH_GetAudioDuration, LoadAudio, WanVideoImageToVideoMultiTalk, WanVideoBlockSwap, MultiTalkModelLoader, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader, WanVideoDecode, LoadAudio, VHS_VideoCombine, ImageResizeKJv2, CR SDXL Aspect Ratio, SimpleMath+, MultiTalkWav2VecEmbeds]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan Video InfiniteTalk  双人对话_1988149592183234562.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988149592183234562.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（29 个）：
- `WanVideoLoraSelect`
- `AudioSeparation`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `AudioSeparation`
- `DownloadAndLoadWav2VecModel`
- `SoundFlow_TrimAudio`
- `SoundFlow_TrimAudio`
- `LoadImage`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `PreviewImage`
- `easy showAnything`
- `RH_GetAudioDuration`
- `RH_GetAudioDuration`
- `LoadAudio`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoBlockSwap`
- `MultiTalkModelLoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoDecode`
- `LoadAudio`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `CR SDXL Aspect Ratio`
- `SimpleMath+`
- `MultiTalkWav2VecEmbeds`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`WanVideoLoraSelect`、`AudioSeparation`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`DownloadAndLoadWav2VecModel`、`SoundFlow_TrimAudio`、`LoadImage`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`RH_GetAudioDuration`、`LoadAudio`、`WanVideoImageToVideoMultiTalk`、`WanVideoBlockSwap`、`MultiTalkModelLoader`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageResizeKJv2`、`CR SDXL Aspect Ratio`、`SimpleMath+`、`MultiTalkWav2VecEmbeds`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoLoraSelect
