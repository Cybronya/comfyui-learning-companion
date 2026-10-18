---
key: 视频生成/图生视频/AIwood-Wan2.2 Multitalk 文生视频版_1952022803912577026.json
name: AIwood-Wan2.2 Multitalk 文生视频版_1952022803912577026.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AIwood-Wan2.2 Multitalk 文生视频版_1952022803912577026.json
hash: ae41b34528c0279a
coverage: 0.967742
learned_at: 2026-10-15 22:30:59
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, LoadWanVideoT5TextEncoder, WanVideoVAELoader, RH_GetAudioDuration, MultiTalkModelLoader, Int, Float to Int, WanVideoSetLoRAs, CreateCFGScheduleFloatList, INTConstant, WanVideoSetLoRAs, easy showAnything, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoTextEncode, INTConstant, WanVideoSampler, MultiTalkWav2VecEmbeds, DownloadAndLoadWav2VecModel, WanVideoSampler, WanVideoDecode, GetImageSizeAndCount, SimpleMath+, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoEmptyEmbeds, LoadAudio, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/AIwood-Wan2.2 Multitalk 文生视频版_1952022803912577026.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952022803912577026.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（31 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `RH_GetAudioDuration`
- `MultiTalkModelLoader`
- `Int`
- `Float to Int`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `WanVideoSetLoRAs`
- `easy showAnything`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `INTConstant`
- `WanVideoSampler` ★核心
- `MultiTalkWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `SimpleMath+`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoEmptyEmbeds`
- `LoadAudio`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`WanVideoSetBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`RH_GetAudioDuration`、`MultiTalkModelLoader`、`Int`、`Float to Int`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoSampler`、`MultiTalkWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`WanVideoDecode`、`GetImageSizeAndCount`、`SimpleMath+`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoEmptyEmbeds`、`LoadAudio`、`VHS_VideoCombine`

**用到的条目**：WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
