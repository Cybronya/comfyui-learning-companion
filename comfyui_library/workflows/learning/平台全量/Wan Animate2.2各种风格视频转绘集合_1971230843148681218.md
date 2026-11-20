---
key: 平台全量/Wan Animate2.2各种风格视频转绘集合_1971230843148681218.json
name: Wan Animate2.2各种风格视频转绘集合_1971230843148681218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan Animate2.2各种风格视频转绘集合_1971230843148681218.json
hash: c4e5ea8169ec583a
coverage: 0.521277
learned_at: 2026-11-14 01:04:04
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, WanVideoSetLoRAs, MarkdownNote, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoBlockSwap, GetNode, WanVideoClipVisionEncode, SetNode, CLIPVisionLoader, Anything Everywhere, WanVideoSetBlockSwap, WanVideoVAELoader, Anything Everywhere, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, WanVideoTextEncodeCached, WanVideoEncode, WanVideoUni3C_ControlnetLoader, ImageResizeKJv2, WanVideoUni3C_embeds, SetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, PreviewImage, easy cleanGpuUsed, PreviewImage, SetNode, ImageResizeKJv2, VHS_LoadVideo, CR Prompt Text, PreviewImage, GetNode, GetNode, WanVideoDecode, ImageConcatMulti, ImageConcatMulti, PreviewImage, WanVideoSampler, VHS_LoadVideo, SetNode, ImageFromBatch+, SetNode, Int2String, GetNode, GetNode, GetNode, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, SetNode, SetNode, DrawViTPose, PoseAndFaceDetection, WanVideoModelLoader, Display Any (rgthree), TextSwitchCase, RunningHub OmniConsistency LoraLoader, RunningHub OmniConsistency Sampler, SetNode, PreviewImage, GetNode, GetNode, Text Concatenate, RH_Captioner, CR String To Combo, VHS_VideoCombine, WanVideoAnimateEmbeds, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, TextSwitchCase, JWInteger, JWInteger, JWInteger, Manual XY Entry Info, Primitive integer [Crystools], GetNode, GetNode, LoadImage, Switch any [Crystools]]
patterns: []
missing: []
---

# 平台全量/Wan Animate2.2各种风格视频转绘集合_1971230843148681218.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan Animate2.2各种风格视频转绘集合_1971230843148681218.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（94 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `CLIPVisionLoader`
- `Anything Everywhere`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `Anything Everywhere`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `ImageResizeKJv2`
- `WanVideoUni3C_embeds`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `easy cleanGpuUsed`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `CR Prompt Text`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `SetNode`
- `ImageFromBatch+`
- `SetNode`
- `Int2String`
- `GetNode`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `DrawViTPose`
- `PoseAndFaceDetection`
- `WanVideoModelLoader`
- `Display Any (rgthree)`
- `TextSwitchCase`
- `RunningHub OmniConsistency LoraLoader` ★核心
- `RunningHub OmniConsistency Sampler` ★核心
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `Text Concatenate`
- `RH_Captioner`
- `CR String To Combo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `TextSwitchCase`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Manual XY Entry Info`
- `Primitive integer [Crystools]`
- `GetNode`
- `GetNode`
- `LoadImage`
- `Switch any [Crystools]`

## 知识

覆盖率 **52%**（49/94）

**有卡**：`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`VHS_LoadVideo`、`CR Prompt Text`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoSampler`、`ImageFromBatch+`、`Int2String`、`OnnxDetectionModelLoader`、`DrawViTPose`、`PoseAndFaceDetection`、`WanVideoModelLoader`、`Display Any (rgthree)`、`TextSwitchCase`、`RunningHub OmniConsistency LoraLoader`、`RunningHub OmniConsistency Sampler`、`Text Concatenate`、`RH_Captioner`、`CR String To Combo`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`JWInteger`、`Manual XY Entry Info`、`Primitive integer [Crystools]`、`LoadImage`、`Switch any [Crystools]`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、RunningHub OmniConsistency Sampler、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncode、WanVideoTextEncodeCached
