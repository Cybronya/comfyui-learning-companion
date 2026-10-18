---
key: 视频生成/图生视频/wan2.2-Multitalk图生视频_1952274805175341058.json
name: wan2.2-Multitalk图生视频_1952274805175341058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2-Multitalk图生视频_1952274805175341058.json
hash: ebbbca72365ee692
coverage: 1
learned_at: 2026-10-15 22:31:00
nodes: [WanVideoModelLoader, WanVideoModelLoader, WanVideoImageToVideoEncode, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, RH_GetAudioDuration, Float to Int, SimpleMath+, Int, CreateCFGScheduleFloatList, WanVideoVAELoader, WanVideoBlockSwap, GetImageSizeAndCount, WanVideoSetBlockSwap, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoDecode, MultiTalkWav2VecEmbeds, LoadAudio, ImageResizeKJv2, INTConstant, INTConstant, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, DownloadAndLoadWav2VecModel, LoadImage, VHS_VideoCombine, MultiTalkModelLoader, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, WanVideoSampler, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-Multitalk图生视频_1952274805175341058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952274805175341058.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `RH_GetAudioDuration`
- `Float to Int`
- `SimpleMath+`
- `Int`
- `CreateCFGScheduleFloatList`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `GetImageSizeAndCount`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `MultiTalkWav2VecEmbeds`
- `LoadAudio`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `DownloadAndLoadWav2VecModel`
- `LoadImage`
- `VHS_VideoCombine`
- `MultiTalkModelLoader`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心

## 知识

覆盖率 **100%**（34/34）

**有卡**：`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`RH_GetAudioDuration`、`Float to Int`、`SimpleMath+`、`Int`、`CreateCFGScheduleFloatList`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`GetImageSizeAndCount`、`WanVideoSetBlockSwap`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`MultiTalkWav2VecEmbeds`、`LoadAudio`、`ImageResizeKJv2`、`INTConstant`、`WanVideoSetLoRAs`、`DownloadAndLoadWav2VecModel`、`LoadImage`、`VHS_VideoCombine`、`MultiTalkModelLoader`、`LayerUtility: PurgeVRAM V2`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
