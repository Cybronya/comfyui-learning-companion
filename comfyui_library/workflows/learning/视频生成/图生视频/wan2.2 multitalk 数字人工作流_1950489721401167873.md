---
key: 视频生成/图生视频/wan2.2 multitalk 数字人工作流_1950489721401167873.json
name: wan2.2 multitalk 数字人工作流_1950489721401167873.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950489721401167873.json
hash: f537c068ea147a5a
coverage: 0.5
learned_at: 2026-10-15 22:30:55
nodes: [GetNode, GetNode, GetNode, WanVideoImageToVideoEncode, WanVideoUni3C_ControlnetLoader, GetNode, SetNode, DownloadAndLoadFlorence2Model, GetNode, Florence2Run, Audio Duration (mtb), SetNode, Display Int (rgthree), ShowText|pysssss, VHS_VideoCombine, SetNode, GetNode, GetNode, WanVideoEncode, WanVideoUni3C_embeds, SetNode, VHS_DuplicateImages, GetNode, GetNode, SetNode, WanVideoTeaCache, WanVideoExperimentalArgs, WanVideoSLG, GetNode, WanVideoContextOptions, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, SetNode, FloatConstant, SimpleMath+, SetNode, MultiTalkWav2VecEmbeds, AudioSeparation, GetNode, GetNode, DownloadAndLoadWav2VecModel, GetNode, SetNode, WanVideoContextOptions, WanVideoTeaCache, GetNode, Int, Int, WanVideoSLG, WanVideoExperimentalArgs, GetNode, CreateCFGScheduleFloatList, WanVideoSampler, LoadImage, ImageResizeKJv2, LoadAudio, AudioCrop, MultiTalkModelLoader, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoModelLoader, GetNode, GetNode, PreviewImage, GetNode, WanVideoDecode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, SetNode, SetNode, MultiTalkModelLoader, WanVideoEnhanceAVideo, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoLoraSelect, CLIPVisionLoader, WanVideoVAELoader, SetNode, GetNode, WanVideoTextEncode, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 multitalk 数字人工作流_1950489721401167873.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950489721401167873.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（96 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `GetNode`
- `SetNode`
- `DownloadAndLoadFlorence2Model`
- `GetNode`
- `Florence2Run`
- `Audio Duration (mtb)`
- `SetNode`
- `Display Int (rgthree)`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `SetNode`
- `VHS_DuplicateImages`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoTeaCache`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `GetNode`
- `WanVideoContextOptions`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `SetNode`
- `FloatConstant`
- `SimpleMath+`
- `SetNode`
- `MultiTalkWav2VecEmbeds`
- `AudioSeparation`
- `GetNode`
- `GetNode`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `SetNode`
- `WanVideoContextOptions`
- `WanVideoTeaCache`
- `GetNode`
- `Int`
- `Int`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `LoadAudio`
- `AudioCrop`
- `MultiTalkModelLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `SetNode`
- `MultiTalkModelLoader`
- `WanVideoEnhanceAVideo`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **50%**（48/96）

**有卡**：`WanVideoImageToVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`DownloadAndLoadFlorence2Model`、`Florence2Run`、`Audio Duration (mtb)`、`Display Int (rgthree)`、`VHS_VideoCombine`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`VHS_DuplicateImages`、`WanVideoTeaCache`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`WanVideoContextOptions`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`FloatConstant`、`SimpleMath+`、`MultiTalkWav2VecEmbeds`、`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`Int`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`LoadImage`、`ImageResizeKJv2`、`LoadAudio`、`AudioCrop`、`MultiTalkModelLoader`、`WanVideoEnhanceAVideo`、`WanVideoModelLoader`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
