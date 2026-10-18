---
key: 视频生成/图生视频/wanvideo fantasy talking 对口型_2045415712142925826.json
name: wanvideo fantasy talking 对口型_2045415712142925826.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wanvideo fantasy talking 对口型_2045415712142925826.json
hash: 430a3ba44098bec1
coverage: 0.534247
learned_at: 2026-10-15 22:36:48
nodes: [LoadImage, SetNode, CLIPVisionLoader, LayerUtility: ImageScaleByAspectRatio, GetNode, GetNode, INTConstant, INTConstant, PreviewImage, GetNode, VHS_VideoCombine, DF_Int_to_Float, SetNode, LoadAudio, ShowAnything|Mie, GetNode, GetNode, GetNode, SetNode, GetNode, JWImageResize, SetNode, GetNode, WanVideoDecode, INTConstant, SetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoImageToVideoEncode, WanVideoTextEncode, GetNode, LoadWanVideoT5TextEncoder, GetNode, DF_Int_to_Float, GetNode, WanVideoSLG, GetNode, AudioSeparation, SetNode, PreviewAudio, WanVideoBlockSwap, SetNode, WanVideoTorchCompileSettings, WanVideoVAELoader, SetNode, SetNode, WanVideoExperimentalArgs, ShowAnything|Mie, SimpleMath+, AudioCrop, RH_GetAudioDuration, SetNode, INTConstant, Reroute, SetNode, SimpleMath+, ShowAnything|Mie, FantasyTalkingModelLoader, GetNode, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSampler, FantasyTalkingWav2VecEmbeds, DownloadAndLoadWav2VecModel, CreateCFGScheduleFloatList, WanVideoExtraModelSelect, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/wanvideo fantasy talking 对口型_2045415712142925826.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2045415712142925826.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（73 个）：
- `LoadImage`
- `SetNode`
- `CLIPVisionLoader`
- `LayerUtility: ImageScaleByAspectRatio`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `PreviewImage`
- `GetNode`
- `VHS_VideoCombine`
- `DF_Int_to_Float`
- `SetNode`
- `LoadAudio`
- `ShowAnything|Mie`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `JWImageResize`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `INTConstant`
- `SetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncode`
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `DF_Int_to_Float`
- `GetNode`
- `WanVideoSLG`
- `GetNode`
- `AudioSeparation`
- `SetNode`
- `PreviewAudio`
- `WanVideoBlockSwap`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `WanVideoExperimentalArgs`
- `ShowAnything|Mie`
- `SimpleMath+`
- `AudioCrop`
- `RH_GetAudioDuration`
- `SetNode`
- `INTConstant`
- `Reroute`
- `SetNode`
- `SimpleMath+`
- `ShowAnything|Mie`
- `FantasyTalkingModelLoader`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `FantasyTalkingWav2VecEmbeds`
- `DownloadAndLoadWav2VecModel`
- `CreateCFGScheduleFloatList`
- `WanVideoExtraModelSelect`
- `Note`

## 知识

覆盖率 **53%**（39/73）

**有卡**：`LoadImage`、`CLIPVisionLoader`、`LayerUtility: ImageScaleByAspectRatio`、`INTConstant`、`VHS_VideoCombine`、`DF_Int_to_Float`、`LoadAudio`、`ShowAnything|Mie`、`JWImageResize`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoSLG`、`AudioSeparation`、`PreviewAudio`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoExperimentalArgs`、`SimpleMath+`、`AudioCrop`、`RH_GetAudioDuration`、`FantasyTalkingModelLoader`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSampler`、`FantasyTalkingWav2VecEmbeds`、`DownloadAndLoadWav2VecModel`、`CreateCFGScheduleFloatList`、`WanVideoExtraModelSelect`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
