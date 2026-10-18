---
key: 视频生成/图生视频/Wan2.2 Animate 双重脸部一致性优化Mix主体迁移版V2（ED实验版）_1971886866809221121.json
name: Wan2.2 Animate 双重脸部一致性优化Mix主体迁移版V2（ED实验版）_1971886866809221121.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate 双重脸部一致性优化Mix主体迁移版V2（ED实验版）_1971886866809221121.json
hash: 665e14123f1605bb
coverage: 0.567901
learned_at: 2026-10-15 22:31:58
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, Note, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, ImageResizeKJv2, SetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, GetNode, GetNode, WanVideoEncode, WanVideoTorchCompileSettings, WanVideoBlockSwap, CLIPVisionLoader, WanVideoVAELoader, WanVideoContextOptions, GetNode, WanVideoUni3C_embeds, Note, Note, WanVideoModelLoader, SetNode, WanVideoTextEncodeCached, CR Prompt Text, WanVideoDecode, OnnxDetectionModelLoader, GrowMask, BlockifyMask, SetNode, easy showAnything, easy showAnything, PoseRetargetPromptHelper, SetNode, PoseAndFaceDetection, Sam2Segmentation, DownloadAndLoadSAM2Model, GetImageSizeAndCount, LoadImage, Reroute, DrawViTPose, VHS_LoadVideo, ACE_ImageFaceCrop, ImageResizeKJv2, WanVideoUni3C_ControlnetLoader, VHS_VideoCombine, JWInteger, PointsEditor, WanVideoClipVisionEncode, Note, VHS_VideoCombine, WanVideoLoraSelectMulti, VHS_VideoCombine, VHS_VideoCombine, GetNode, WanVideoSampler, VHS_LoadVideo, JWInteger, JWInteger, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate 双重脸部一致性优化Mix主体迁移版V2（ED实验版）_1971886866809221121.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971886866809221121.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（81 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
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
- `WanVideoEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `GetNode`
- `WanVideoUni3C_embeds`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `SetNode`
- `WanVideoTextEncodeCached`
- `CR Prompt Text`
- `WanVideoDecode`
- `OnnxDetectionModelLoader`
- `GrowMask`
- `BlockifyMask`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `PoseRetargetPromptHelper`
- `SetNode`
- `PoseAndFaceDetection`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `GetImageSizeAndCount`
- `LoadImage`
- `Reroute`
- `DrawViTPose`
- `VHS_LoadVideo`
- `ACE_ImageFaceCrop`
- `ImageResizeKJv2`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_VideoCombine`
- `JWInteger`
- `PointsEditor`
- `WanVideoClipVisionEncode`
- `Note`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **57%**（46/81）

**有卡**：`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`DrawMaskOnImage`、`WanVideoEncode`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoUni3C_embeds`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`CR Prompt Text`、`WanVideoDecode`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`PoseRetargetPromptHelper`、`PoseAndFaceDetection`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`LoadImage`、`DrawViTPose`、`VHS_LoadVideo`、`ACE_ImageFaceCrop`、`WanVideoUni3C_ControlnetLoader`、`VHS_VideoCombine`、`JWInteger`、`PointsEditor`、`WanVideoClipVisionEncode`、`WanVideoLoraSelectMulti`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
