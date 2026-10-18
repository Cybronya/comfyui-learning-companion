---
key: 视频生成/图生视频/Wan Animate2.2主体迁移（自动裁剪脸部，增强主体一致性）v3_1972998201764655106.json
name: Wan Animate2.2主体迁移（自动裁剪脸部，增强主体一致性）v3_1972998201764655106.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan Animate2.2主体迁移（自动裁剪脸部，增强主体一致性）v3_1972998201764655106.json
hash: 335ca800d90cb11a
coverage: 0.518987
learned_at: 2026-10-15 22:32:01
nodes: [ImageConcatMulti, GetNode, SetNode, ImageConcatMulti, WanVideoSetLoRAs, CLIPVisionLoader, GetNode, GetNode, SetNode, VHS_VideoCombine, ImageResizeKJv2, WanVideoDecode, GetNode, WanVideoAnimateEmbeds, WanVideoVAELoader, GetNode, SetNode, VHS_VideoCombine, DrawMaskOnImage, SetNode, BlockifyMask, PointsEditor, WanVideoClipVisionEncode, JWInteger, SetNode, CR Prompt Text, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoModelLoader, GetNode, LoadImage, SetNode, GetNode, GetNode, GetImageSizeAndCount, GetNode, SetNode, WanVideoBlockSwap, SetNode, DownloadAndLoadSAM2Model, SetNode, WanVideoTextEncodeCached, GetNode, GetNode, VHS_LoadVideo, ImageResizeKJv2, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, OnnxDetectionModelLoader, VHS_VideoCombine, WanVideoLoraSelectMulti, Sam2Segmentation, GrowMask, GetNode, GetNode, Reroute, GetNode, Reroute, easy showAnything, VHS_LoadVideo, WanVideoSampler, GetNode, GetNode, PoseAndFaceDetection, ACE_ImageFaceCrop, GetNode, PixelPerfectResolution, SetNode, easy showAnything, SetNode, JWInteger, Note, Note, PoseRetargetPromptHelper, DWPreprocessor]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan Animate2.2主体迁移（自动裁剪脸部，增强主体一致性）v3_1972998201764655106.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1972998201764655106.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（79 个）：
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `ImageConcatMulti`
- `WanVideoSetLoRAs`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `WanVideoDecode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoVAELoader`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `SetNode`
- `BlockifyMask`
- `PointsEditor`
- `WanVideoClipVisionEncode`
- `JWInteger`
- `SetNode`
- `CR Prompt Text`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `GetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `SetNode`
- `DownloadAndLoadSAM2Model`
- `SetNode`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `Sam2Segmentation`
- `GrowMask`
- `GetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `Reroute`
- `easy showAnything`
- `VHS_LoadVideo`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `ACE_ImageFaceCrop`
- `GetNode`
- `PixelPerfectResolution`
- `SetNode`
- `easy showAnything`
- `SetNode`
- `JWInteger`
- `Note`
- `Note`
- `PoseRetargetPromptHelper`
- `DWPreprocessor`

## 知识

覆盖率 **52%**（41/79）

**有卡**：`ImageConcatMulti`、`WanVideoSetLoRAs`、`CLIPVisionLoader`、`VHS_VideoCombine`、`ImageResizeKJv2`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`WanVideoVAELoader`、`DrawMaskOnImage`、`BlockifyMask`、`PointsEditor`、`WanVideoClipVisionEncode`、`JWInteger`、`CR Prompt Text`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`LoadImage`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`DownloadAndLoadSAM2Model`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`OnnxDetectionModelLoader`、`Sam2Segmentation`、`GrowMask`、`WanVideoSampler`、`PoseAndFaceDetection`、`ACE_ImageFaceCrop`、`PixelPerfectResolution`、`PoseRetargetPromptHelper`、`DWPreprocessor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
