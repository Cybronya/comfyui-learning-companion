---
key: 视频生成/图生视频/wan2.2 Multitalk 图生视频版_2054724195342405634.json
name: wan2.2 Multitalk 图生视频版_2054724195342405634.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 Multitalk 图生视频版_2054724195342405634.json
hash: 77ec649136b5a58f
coverage: 0.969697
learned_at: 2026-10-15 22:37:50
nodes: [Note, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, WanVideoTorchCompileSettings, RH_GetAudioDuration, Float to Int, DownloadAndLoadWav2VecModel, SimpleMath+, WanVideoImageToVideoEncode, WanVideoSetLoRAs, INTConstant, CreateCFGScheduleFloatList, WanVideoSetLoRAs, Int, INTConstant, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVAELoader, MultiTalkWav2VecEmbeds, WanVideoSampler, ImageResizeKJv2, WanVideoModelLoader, WanVideoModelLoader, MultiTalkModelLoader, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoTextEncode, LoadAudio, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 Multitalk 图生视频版_2054724195342405634.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054724195342405634.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTorchCompileSettings`
- `RH_GetAudioDuration`
- `Float to Int`
- `DownloadAndLoadWav2VecModel`
- `SimpleMath+`
- `WanVideoImageToVideoEncode`
- `WanVideoSetLoRAs`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `Int`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `MultiTalkWav2VecEmbeds`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `MultiTalkModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `LoadAudio`
- `LoadImage`

## 知识

覆盖率 **97%**（32/33）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoTorchCompileSettings`、`RH_GetAudioDuration`、`Float to Int`、`DownloadAndLoadWav2VecModel`、`SimpleMath+`、`WanVideoImageToVideoEncode`、`WanVideoSetLoRAs`、`INTConstant`、`CreateCFGScheduleFloatList`、`Int`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`MultiTalkWav2VecEmbeds`、`WanVideoSampler`、`ImageResizeKJv2`、`WanVideoModelLoader`、`MultiTalkModelLoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoTextEncode`、`LoadAudio`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
