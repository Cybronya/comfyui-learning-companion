---
key: 视频生成/文生视频/Wan2.2 Multitalk-超好用图生视频_1953496222059384834.json
name: Wan2.2 Multitalk-超好用图生视频_1953496222059384834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Multitalk-超好用图生视频_1953496222059384834.json
hash: 56140d0454c3ae3d
coverage: 1
learned_at: 2026-10-15 22:47:09
nodes: [WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoSampler, ImageResizeKJv2, DownloadAndLoadWav2VecModel, RH_GetAudioDuration, Int, MultiTalkWav2VecEmbeds, SimpleMath+, Float to Int, WanVideoLoraSelect, WanVideoLoraSelect, MultiTalkModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoSetLoRAs, GetImageSizeAndCount, CreateCFGScheduleFloatList, INTConstant, INTConstant, LoadImage, LoadAudio, WanVideoSampler, WanVideoTextEncode, WanVideoSetBlockSwap, WanVideoSetLoRAs, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 Multitalk-超好用图生视频_1953496222059384834.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Multitalk-超好用图生视频_1953496222059384834.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `DownloadAndLoadWav2VecModel`
- `RH_GetAudioDuration`
- `Int`
- `MultiTalkWav2VecEmbeds`
- `SimpleMath+`
- `Float to Int`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoSetLoRAs`
- `GetImageSizeAndCount`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `LoadAudio`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（32/32）

**有卡**：`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoSampler`、`ImageResizeKJv2`、`DownloadAndLoadWav2VecModel`、`RH_GetAudioDuration`、`Int`、`MultiTalkWav2VecEmbeds`、`SimpleMath+`、`Float to Int`、`WanVideoLoraSelect`、`MultiTalkModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`CreateCFGScheduleFloatList`、`INTConstant`、`LoadImage`、`LoadAudio`、`WanVideoTextEncode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
