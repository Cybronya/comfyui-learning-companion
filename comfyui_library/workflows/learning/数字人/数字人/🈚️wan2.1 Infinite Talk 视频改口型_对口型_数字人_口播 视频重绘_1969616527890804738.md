---
key: 数字人/数字人/🈚️wan2.1 Infinite Talk 视频改口型_对口型_数字人_口播 视频重绘_1969616527890804738.json
name: 🈚️wan2.1 Infinite Talk 视频改口型_对口型_数字人_口播 视频重绘_1969616527890804738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/🈚️wan2.1 Infinite Talk 视频改口型_对口型_数字人_口播 视频重绘_1969616527890804738.json
hash: dc6f99a5dd1aaaf2
coverage: 0.556604
learned_at: 2026-10-26 02:06:15
nodes: [SetNode, SetNode, PreviewAny, AudioSeparation, GetNode, GetNode, SetNode, DownloadAndLoadWav2VecModel, IndexTTS2Run, CR Prompt Text, SetNode, SetNode, GetNode, SetNode, ImageConcanate, SaveAudio, GetNode, SetNode, CLIPVisionLoader, ImagePass, GetNode, GetNode, Bjornulf_ShowInt, VHS_GetImageCount, MultiTalkSilentEmbeds, GetNode, SetNode, LoadAudio, LoadAudio, LoadAudio, SetNode, SetNode, GetNode, SetNode, WanVideoVAELoader, SetNode, LoadWanVideoT5TextEncoder, GetNode, GetImageSize, Bjornulf_ShowInt, MultiTalkWav2VecEmbeds, LoadAudio, WanVideoBlockSwap, GetNode, GetNode, WanVideoDecode, GetNode, GetNode, WanVideoTextEncode, VHS_GetImageCount, GetNode, Bjornulf_ShowInt, Bjornulf_ShowInt, GetNode, Note, SetNode, ReverseImageBatch, ImageBatchMulti, ImageResizeKJv2, RepeatImageBatch, SetNode, GetImageRangeFromBatch, SetNode, GetNode, GetNode, WanVideoEncode, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, Int, Int, GetNode, WanVideoLoraSelect, MultiTalkModelLoader, MultiTalkModelLoader, VHS_VideoCombine, VHS_VideoCombine, WanVideoClipVisionEncode, GetImageRangeFromBatch, WanVideoSampler, GetImageRangeFromBatch, PreviewImage, WanVideoImageToVideoMultiTalk, Bjornulf_ShowInt, GetNode, SetNode, Fast Groups Bypasser (rgthree), AudioBeforeAfterSilence, AudioCrop, ImpactSwitch, GetNode, GetNode, SetNode, PreviewAudio, Note, Note, WanVideoModelLoader, CR Prompt Text, SetNode, VHS_LoadVideo, SoundFlow_GetLength, ToInt, SimpleMath+]
patterns: []
missing: []
---

# 数字人/数字人/🈚️wan2.1 Infinite Talk 视频改口型_对口型_数字人_口播 视频重绘_1969616527890804738.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/🈚️wan2.1 Infinite Talk 视频改口型_对口型_数字人_口播 视频重绘_1969616527890804738.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（106 个）：
- `SetNode`
- `SetNode`
- `PreviewAny`
- `AudioSeparation`
- `GetNode`
- `GetNode`
- `SetNode`
- `DownloadAndLoadWav2VecModel`
- `IndexTTS2Run`
- `CR Prompt Text`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageConcanate`
- `SaveAudio`
- `GetNode`
- `SetNode`
- `CLIPVisionLoader`
- `ImagePass`
- `GetNode`
- `GetNode`
- `Bjornulf_ShowInt`
- `VHS_GetImageCount`
- `MultiTalkSilentEmbeds`
- `GetNode`
- `SetNode`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `GetImageSize`
- `Bjornulf_ShowInt`
- `MultiTalkWav2VecEmbeds`
- `LoadAudio`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncode`
- `VHS_GetImageCount`
- `GetNode`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowInt`
- `GetNode`
- `Note`
- `SetNode`
- `ReverseImageBatch`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `RepeatImageBatch`
- `SetNode`
- `GetImageRangeFromBatch`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetNode`
- `Int`
- `Int`
- `GetNode`
- `WanVideoLoraSelect`
- `MultiTalkModelLoader`
- `MultiTalkModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `GetImageRangeFromBatch`
- `WanVideoSampler` ★核心
- `GetImageRangeFromBatch`
- `PreviewImage`
- `WanVideoImageToVideoMultiTalk`
- `Bjornulf_ShowInt`
- `GetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `AudioBeforeAfterSilence`
- `AudioCrop`
- `ImpactSwitch`
- `GetNode`
- `GetNode`
- `SetNode`
- `PreviewAudio`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `CR Prompt Text`
- `SetNode`
- `VHS_LoadVideo`
- `SoundFlow_GetLength`
- `ToInt`
- `SimpleMath+`

## 知识

覆盖率 **56%**（59/106）

**有卡**：`AudioSeparation`、`DownloadAndLoadWav2VecModel`、`IndexTTS2Run`、`CR Prompt Text`、`ImageConcanate`、`SaveAudio`、`CLIPVisionLoader`、`ImagePass`、`Bjornulf_ShowInt`、`VHS_GetImageCount`、`MultiTalkSilentEmbeds`、`LoadAudio`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`GetImageSize`、`MultiTalkWav2VecEmbeds`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoTextEncode`、`ReverseImageBatch`、`ImageBatchMulti`、`ImageResizeKJv2`、`RepeatImageBatch`、`GetImageRangeFromBatch`、`WanVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`Int`、`MultiTalkModelLoader`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`WanVideoImageToVideoMultiTalk`、`AudioBeforeAfterSilence`、`AudioCrop`、`PreviewAudio`、`WanVideoModelLoader`、`VHS_LoadVideo`、`SoundFlow_GetLength`、`ToInt`、`SimpleMath+`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoEncode、WanVideoLoraSelect
