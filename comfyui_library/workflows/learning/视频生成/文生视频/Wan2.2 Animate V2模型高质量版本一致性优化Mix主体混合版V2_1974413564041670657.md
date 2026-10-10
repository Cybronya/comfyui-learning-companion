---
key: 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Mix主体混合版V2_1974413564041670657.json
name: Wan2.2 Animate V2模型高质量版本一致性优化Mix主体混合版V2_1974413564041670657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Mix主体混合版V2_1974413564041670657.json
hash: 0e51aa189c645736
coverage: 0.55
learned_at: 2026-10-10 23:06:40
nodes: [ImageConcatMulti, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, Note, GetNode, SetNode, ImageConcatMulti, GetNode, GetNode, GetImageSizeAndCount, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoSetLoRAs, MarkdownNote, ImageResizeKJv2, SetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoEncode, VHS_VideoCombine, WanVideoTorchCompileSettings, WanVideoBlockSwap, CLIPVisionLoader, WanVideoVAELoader, WanVideoContextOptions, GetNode, WanVideoUni3C_embeds, Note, Note, SetNode, WanVideoTextEncodeCached, CR Prompt Text, WanVideoDecode, OnnxDetectionModelLoader, GrowMask, BlockifyMask, SetNode, easy showAnything, easy showAnything, PoseRetargetPromptHelper, SetNode, PoseAndFaceDetection, Sam2Segmentation, DownloadAndLoadSAM2Model, GetImageSizeAndCount, LoadImage, Reroute, DrawViTPose, ACE_ImageFaceCrop, ImageResizeKJv2, WanVideoUni3C_ControlnetLoader, VHS_VideoCombine, PointsEditor, WanVideoClipVisionEncode, Note, JWInteger, VHS_LoadVideo, JWInteger, JWInteger, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, GetNode]
patterns: []
missing: [CR Prompt Text]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Mix主体混合版V2_1974413564041670657.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Mix主体混合版V2_1974413564041670657.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（80 个）：
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
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
- `ACE_ImageFaceCrop`
- `ImageResizeKJv2`
- `WanVideoUni3C_ControlnetLoader`
- `VHS_VideoCombine`
- `PointsEditor`
- `WanVideoClipVisionEncode`
- `Note`
- `JWInteger`
- `VHS_LoadVideo`
- `JWInteger`
- `JWInteger`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`

## 知识

覆盖率 **55%**（44/80）

**有卡**：`ImageConcatMulti`、`GetImageSizeAndCount`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`DrawMaskOnImage`、`WanVideoEncode`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoContextOptions`、`WanVideoUni3C_embeds`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`OnnxDetectionModelLoader`、`GrowMask`、`BlockifyMask`、`PoseRetargetPromptHelper`、`PoseAndFaceDetection`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`LoadImage`、`DrawViTPose`、`ACE_ImageFaceCrop`、`WanVideoUni3C_ControlnetLoader`、`PointsEditor`、`WanVideoClipVisionEncode`、`JWInteger`、`VHS_LoadVideo`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoSampler`

**缺卡**（1）：`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
