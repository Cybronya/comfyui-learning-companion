---
key: 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本非人类一致性优化Mix主体混合版V1_1974415771805855745.json
name: Wan2.2 Animate V2模型高质量版本非人类一致性优化Mix主体混合版V1_1974415771805855745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Animate V2模型高质量版本非人类一致性优化Mix主体混合版V1_1974415771805855745.json
hash: 0859732bfcbf369d
coverage: 0.576471
learned_at: 2026-10-15 22:47:09
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, Note, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, ImageResizeKJv2, SetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoEncode, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, CLIPVisionLoader, WanVideoVAELoader, WanVideoContextOptions, GetNode, WanVideoUni3C_embeds, Note, Note, SetNode, WanVideoTextEncodeCached, WanVideoDecode, GrowMask, BlockifyMask, SetNode, easy showAnything, PoseAndFaceDetection, Sam2Segmentation, DownloadAndLoadSAM2Model, GetImageSizeAndCount, DrawViTPose, ImageResizeKJv2, WanVideoUni3C_ControlnetLoader, VHS_VideoCombine, WanVideoClipVisionEncode, Note, VHS_LoadVideo, JWInteger, JWInteger, WanVideoLoraSelectMulti, WanVideoModelLoader, VHS_VideoCombine, PointsEditor, easy promptConcat, ShowText, CR Prompt Text, RH_Captioner, LoadImage, easy showAnything, CR Prompt Text, JWInteger, WanVideoSampler, VHS_VideoCombine, OnnxDetectionModelLoader, Reroute, VHS_LoadVideo, ACE_ImageFaceCrop, PoseRetargetPromptHelper, easy showAnything, SetNode, GetNode, SetNode]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本非人类一致性优化Mix主体混合版V1_1974415771805855745.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Animate V2模型高质量版本非人类一致性优化Mix主体混合版V1_1974415771805855745.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（85 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoAnimateEmbeds`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `MarkdownNote`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `GetNode`
- `WanVideoUni3C_embeds`
- `Note`
- `Note`
- `SetNode`
- `WanVideoTextEncodeCached`
- `WanVideoDecode`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `easy showAnything`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `GetImageSizeAndCount`
- `DrawViTPose`
- `ImageResizeKJv2`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `Note`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `PointsEditor`
- `easy promptConcat`
- `ShowText`
- `CR Prompt Text`
- `RH_Captioner`
- `LoadImage`
- `easy showAnything`
- `CR Prompt Text`
- `JWInteger`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `Reroute`
- `VHS_LoadVideo`
- `ACE_ImageFaceCrop`
- `PoseRetargetPromptHelper`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `SetNode`

## 知识

覆盖率 **58%**（49/85）

**有卡**：`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`DrawMaskOnImage`、`WanVideoEncode`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoUni3C_embeds`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`GrowMask`、`BlockifyMask`、`PoseAndFaceDetection`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`DrawViTPose`、`WanVideoUni3C_ControlnetLoader`、`WanVideoClipVisionEncode`、`VHS_LoadVideo`、`JWInteger`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`PointsEditor`、`easy promptConcat`、`ShowText`、`CR Prompt Text`、`RH_Captioner`、`LoadImage`、`WanVideoSampler`、`OnnxDetectionModelLoader`、`ACE_ImageFaceCrop`、`PoseRetargetPromptHelper`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
