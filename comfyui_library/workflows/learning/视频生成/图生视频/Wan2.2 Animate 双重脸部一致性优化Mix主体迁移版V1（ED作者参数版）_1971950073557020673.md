---
key: 视频生成/图生视频/Wan2.2 Animate 双重脸部一致性优化Mix主体迁移版V1（ED作者参数版）_1971950073557020673.json
name: Wan2.2 Animate 双重脸部一致性优化Mix主体迁移版V1（ED作者参数版）_1971950073557020673.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1971950073557020673.json
hash: 067e30cc6ad54c5a
coverage: 0.567901
learned_at: 2026-10-15 22:31:58
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, Note, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, ImageResizeKJv2, SetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoEncode, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, CLIPVisionLoader, WanVideoVAELoader, WanVideoContextOptions, WanVideoSampler, GetNode, WanVideoUni3C_embeds, Note, Note, WanVideoModelLoader, SetNode, WanVideoTextEncodeCached, CR Prompt Text, WanVideoDecode, OnnxDetectionModelLoader, GrowMask, BlockifyMask, SetNode, easy showAnything, easy showAnything, PoseRetargetPromptHelper, SetNode, PoseAndFaceDetection, Sam2Segmentation, DownloadAndLoadSAM2Model, GetImageSizeAndCount, LoadImage, Reroute, DrawViTPose, VHS_LoadVideo, ACE_ImageFaceCrop, ImageResizeKJv2, WanVideoUni3C_ControlnetLoader, VHS_VideoCombine, PointsEditor, WanVideoClipVisionEncode, Note, VHS_VideoCombine, VHS_VideoCombine, JWInteger, VHS_LoadVideo, JWInteger, JWInteger, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate 双重脸部一致性优化Mix主体迁移版V1（ED作者参数版）_1971950073557020673.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971950073557020673.json`

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
- `GetNode`
- `WanVideoEncode`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
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
- `PointsEditor`
- `WanVideoClipVisionEncode`
- `Note`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **57%**（46/81）

**有卡**：`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`DrawMaskOnImage`、`WanVideoEncode`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoUni3C_embeds`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`CR Prompt Text`、`WanVideoDecode`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`PoseRetargetPromptHelper`、`PoseAndFaceDetection`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`LoadImage`、`DrawViTPose`、`VHS_LoadVideo`、`ACE_ImageFaceCrop`、`WanVideoUni3C_ControlnetLoader`、`PointsEditor`、`WanVideoClipVisionEncode`、`JWInteger`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
