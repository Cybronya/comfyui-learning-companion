---
key: 平台全量/【直出高清】人物跳舞动作迁移Wan2.2+Animate+V2版本（超快5分钟）_1975571105782083586.json
name: 【直出高清】人物跳舞动作迁移Wan2.2+Animate+V2版本（超快5分钟）_1975571105782083586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【直出高清】人物跳舞动作迁移Wan2.2+Animate+V2版本（超快5分钟）_1975571105782083586.json
hash: 5caf0a23ba114a14
coverage: 0.54878
learned_at: 2026-11-14 01:24:47
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ImageConcatMulti, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, ImageResizeKJv2, SetNode, GetNode, GetNode, GetNode, WanVideoTorchCompileSettings, CLIPVisionLoader, WanVideoVAELoader, WanVideoContextOptions, Note, Note, SetNode, WanVideoDecode, OnnxDetectionModelLoader, SetNode, PoseAndFaceDetection, Reroute, DrawViTPose, ACE_ImageFaceCrop, Note, WanVideoLoraSelectMulti, WanVideoModelLoader, LoadImage, SetNode, RMBG, GrowMask, BlockifyMask, SetNode, GetNode, DrawMaskOnImage, SetNode, Note, ImageConcatMulti, GetNode, easy showAnything, PoseRetargetPromptHelper, SetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, WanVideoBlockSwap, WanVideoSampler, SetNode, SetNode, SetNode, JWInteger, VHS_LoadVideo, JWInteger, MathExpression|pysssss, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, DF_Int_to_Float, SetNode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, GetNode, WanVideoTextEncodeCached, Reroute, GetImageSizeAndCount, ImageResizeKJv2, JWInteger, CR Prompt Text, JWInteger, JWInteger]
patterns: []
missing: []
---

# 平台全量/【直出高清】人物跳舞动作迁移Wan2.2+Animate+V2版本（超快5分钟）_1975571105782083586.json

> 来源文件 `comfyui_library/workflows/平台全量/【直出高清】人物跳舞动作迁移Wan2.2+Animate+V2版本（超快5分钟）_1975571105782083586.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（82 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `WanVideoAnimateEmbeds`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `Note`
- `Note`
- `SetNode`
- `WanVideoDecode`
- `OnnxDetectionModelLoader`
- `SetNode`
- `PoseAndFaceDetection`
- `Reroute`
- `DrawViTPose`
- `ACE_ImageFaceCrop`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `LoadImage`
- `SetNode`
- `RMBG`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `Note`
- `ImageConcatMulti`
- `GetNode`
- `easy showAnything`
- `PoseRetargetPromptHelper`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `JWInteger`
- `VHS_LoadVideo`
- `JWInteger`
- `MathExpression|pysssss`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DF_Int_to_Float`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoTextEncodeCached`
- `Reroute`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `JWInteger`
- `CR Prompt Text`
- `JWInteger`
- `JWInteger`

## 知识

覆盖率 **55%**（45/82）

**有卡**：`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`WanVideoTorchCompileSettings`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoDecode`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`DrawViTPose`、`ACE_ImageFaceCrop`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`LoadImage`、`RMBG`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`PoseRetargetPromptHelper`、`VHS_VideoCombine`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`WanVideoSampler`、`JWInteger`、`VHS_LoadVideo`、`MathExpression|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`DF_Int_to_Float`、`WanVideoTextEncodeCached`、`CR Prompt Text`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
