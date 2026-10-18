---
key: 视频生成/图生视频/SteadyDancer动作迁移Q版、真人等-舞蹈带货Motion Transfer_1999018425617932289.json
name: SteadyDancer动作迁移Q版、真人等-舞蹈带货Motion Transfer_1999018425617932289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/SteadyDancer动作迁移Q版、真人等-舞蹈带货Motion Transfer_1999018425617932289.json
hash: cac6c34121611c90
coverage: 0.539474
learned_at: 2026-10-15 22:33:35
nodes: [GetNode, SetNode, CLIPVisionLoader, SetNode, Int, Note, Note, Note, GetNode, ImageConcatMulti, WanVideoDecode, ImageConcatMulti, WanVideoSamplerFromSettings, WanVideoSamplerSettings, GetNode, WanVideoModelLoader, WanVideoLoraSelect, WanVideoBlockSwap, GetNode, WanVideoClipVisionEncode, GetImageRangeFromBatch, WanVideoEncode, GetNode, Note, GetNode, SetNode, GetNode, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, GetNode, GetNode, GetNode, GetNode, SetNode, ImageResizeKJv2, GetNode, GetNode, PoseDetectionOneToAllAnimation, OnnxDetectionModelLoader, SetNode, SetNode, PreviewImage, PreviewImage, ImageResizeKJv2, VHS_VideoCombine, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoScheduler, PrimitiveNode, PrimitiveNode, Int, WanVideoAddSteadyDancerEmbeds, Reroute, WanVideoContextOptions, WanVideoTorchCompileSettings, MarkdownNote, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, LoadImage, GetImageSizeAndCount, easy showAnything, Int, SimpleMath+, Int, Note, Int, easy convertAnything, PrimitiveFloat, Note, CR Prompt Text, WanVideoTextEncodeCached, DeepTranslatorTextNode, easy showAnything, Reroute]
patterns: []
missing: []
---

# 视频生成/图生视频/SteadyDancer动作迁移Q版、真人等-舞蹈带货Motion Transfer_1999018425617932289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1999018425617932289.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（76 个）：
- `GetNode`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `Int`
- `Note`
- `Note`
- `Note`
- `GetNode`
- `ImageConcatMulti`
- `WanVideoDecode`
- `ImageConcatMulti`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoSamplerSettings` ★核心
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetImageRangeFromBatch`
- `WanVideoEncode`
- `GetNode`
- `Note`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `PoseDetectionOneToAllAnimation`
- `OnnxDetectionModelLoader`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `PreviewImage`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoScheduler`
- `PrimitiveNode`
- `PrimitiveNode`
- `Int`
- `WanVideoAddSteadyDancerEmbeds`
- `Reroute`
- `WanVideoContextOptions`
- `WanVideoTorchCompileSettings`
- `MarkdownNote`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`
- `GetImageSizeAndCount`
- `easy showAnything`
- `Int`
- `SimpleMath+`
- `Int`
- `Note`
- `Int`
- `easy convertAnything`
- `PrimitiveFloat`
- `Note`
- `CR Prompt Text`
- `WanVideoTextEncodeCached`
- `DeepTranslatorTextNode`
- `easy showAnything`
- `Reroute`

## 知识

覆盖率 **54%**（41/76）

**有卡**：`CLIPVisionLoader`、`Int`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoSamplerFromSettings`、`WanVideoSamplerSettings`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`GetImageRangeFromBatch`、`WanVideoEncode`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`PoseDetectionOneToAllAnimation`、`OnnxDetectionModelLoader`、`VHS_VideoCombine`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoScheduler`、`WanVideoAddSteadyDancerEmbeds`、`WanVideoContextOptions`、`WanVideoTorchCompileSettings`、`VHS_LoadVideo`、`LoadImage`、`GetImageSizeAndCount`、`SimpleMath+`、`easy convertAnything`、`CR Prompt Text`、`WanVideoTextEncodeCached`、`DeepTranslatorTextNode`

**用到的条目**：LoadImage、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached
