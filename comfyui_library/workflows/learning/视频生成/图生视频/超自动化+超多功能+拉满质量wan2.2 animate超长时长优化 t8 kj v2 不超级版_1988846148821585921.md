---
key: 视频生成/图生视频/超自动化+超多功能+拉满质量wan2.2 animate超长时长优化 t8 kj v2 不超级版_1988846148821585921.json
name: 超自动化+超多功能+拉满质量wan2.2 animate超长时长优化 t8 kj v2 不超级版_1988846148821585921.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/超自动化+超多功能+拉满质量wan2.2 animate超长时长优化 t8 kj v2 不超级版_1988846148821585921.json
hash: f688a07cc3154331
coverage: 0.480315
learned_at: 2026-10-15 22:33:04
nodes: [GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, GetNode, WanVideoContextOptions, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, GetNode, GetNode, GetNode, GetNode, PrimitiveStringMultiline, GetNode, SetNode, SetNode, easy showAnything, PoseAndFaceDetection, easy showAnything, PoseRetargetPromptHelper, SetNode, GetNode, Note, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, WanVideoTorchCompileSettings, SetNode, SetNode, GetNode, SetNode, GetNode, ACE_ImageFaceCrop, GetNode, SetNode, CLIPVisionLoader, GetNode, VHS_VideoCombine, SetNode, MarkdownNote, SetNode, WanVideoEncode, WanVideoUni3C_ControlnetLoader, Sam2Segmentation, GrowMask, BlockifyMask, DrawMaskOnImage, DownloadAndLoadSAM2Model, DrawViTPose, GetNode, GetNode, GetNode, SetNode, GetNode, VHS_VideoCombine, SimpleMath+, VHS_VideoCombine, DF_Text_Box, GetNode, WanVideoUni3C_embeds, LoadImage, PrimitiveStringMultiline, WanVideoVAELoader, SetNode, GetNode, Float to Int, Note, Note, WanVideoClipVisionEncode, GetNode, VHS_LoadVideo, ImageResizeKJv2, PointsEditor, easy float, JWInteger, JWInteger, WanVideoLoraSelectMulti, GetNode, WanVideoTextEncodeCached, GetNode, GetNode, WanVideoSetBlockSwap, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoModelLoader, VHS_VideoCombine, ImageConcatMulti, GetNode, VHS_VideoCombine, WanVideoDecode, GetImageSizeAndCount, SimpleMath+, SetNode, SetNode, VHS_LoadVideo, SetNode, JWLoopImageSequence, GetNode, WanVideoBlockSwap, LoadImage, GetImageSizeAndCount, SetNode, SetNode, ImageResizeKJv2, LayerUtility: PurgeVRAM, WanVideoSampler, easy forLoopStart, SetNode, easy forLoopEnd, MathExpression|pysssss, ImageBatch, ImageFromBatch+, JWInteger, Int, WanVideoAnimateEmbeds]
patterns: []
missing: []
---

# 视频生成/图生视频/超自动化+超多功能+拉满质量wan2.2 animate超长时长优化 t8 kj v2 不超级版_1988846148821585921.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988846148821585921.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（127 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `WanVideoContextOptions`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `PoseAndFaceDetection`
- `easy showAnything`
- `PoseRetargetPromptHelper`
- `SetNode`
- `GetNode`
- `Note`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `ACE_ImageFaceCrop`
- `GetNode`
- `SetNode`
- `CLIPVisionLoader`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `MarkdownNote`
- `SetNode`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `Sam2Segmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `DownloadAndLoadSAM2Model`
- `DrawViTPose`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SimpleMath+`
- `VHS_VideoCombine`
- `DF_Text_Box`
- `GetNode`
- `WanVideoUni3C_embeds`
- `LoadImage`
- `PrimitiveStringMultiline`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `Float to Int`
- `Note`
- `Note`
- `WanVideoClipVisionEncode`
- `GetNode`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `PointsEditor`
- `easy float`
- `JWInteger`
- `JWInteger`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `JWLoopImageSequence`
- `GetNode`
- `WanVideoBlockSwap`
- `LoadImage`
- `GetImageSizeAndCount`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `easy forLoopStart`
- `SetNode`
- `easy forLoopEnd`
- `MathExpression|pysssss`
- `ImageBatch`
- `ImageFromBatch+`
- `JWInteger`
- `Int`
- `WanVideoAnimateEmbeds`

## 知识

覆盖率 **48%**（61/127）

**有卡**：`ImageConcatMulti`、`WanVideoContextOptions`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`PoseRetargetPromptHelper`、`WanVideoTorchCompileSettings`、`ACE_ImageFaceCrop`、`CLIPVisionLoader`、`VHS_VideoCombine`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`Sam2Segmentation`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`DownloadAndLoadSAM2Model`、`DrawViTPose`、`SimpleMath+`、`DF_Text_Box`、`WanVideoUni3C_embeds`、`LoadImage`、`WanVideoVAELoader`、`Float to Int`、`WanVideoClipVisionEncode`、`VHS_LoadVideo`、`ImageResizeKJv2`、`PointsEditor`、`easy float`、`JWInteger`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoDecode`、`GetImageSizeAndCount`、`JWLoopImageSequence`、`WanVideoBlockSwap`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`easy forLoopStart`、`easy forLoopEnd`、`MathExpression|pysssss`、`ImageBatch`、`ImageFromBatch+`、`Int`、`WanVideoAnimateEmbeds`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
