---
key: 数字人/数字人/alan自用-主体替换sec video segmentation_1983904795276836866.json
name: alan自用-主体替换sec video segmentation_1983904795276836866
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/alan自用-主体替换sec video segmentation_1983904795276836866.json
hash: 9dd9de6edb555dc0
coverage: 0.571429
learned_at: 2026-10-26 01:58:26
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTorchCompileSettings, SetNode, WanVideoDecode, GetNode, WanVideoSetLoRAs, VHS_VideoCombine, GetNode, WanVideoBlockSwap, MarkdownNote, SetNode, WanVideoVAELoader, WanVideoTextEncodeCached, WanVideoModelLoader, SetNode, SetNode, WanVideoLoraSelectMulti, WanVideoSampler, SetNode, SetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, Reroute, DrawViTPose, OnnxDetectionModelLoader, CLIPVisionLoader, WanVideoClipVisionEncode, WanVideoSetBlockSwap, PoseAndFaceDetection, BlockifyMask, GrowMaskWithBlur, LayerUtility: ImageBlend, GetNode, Reroute, WanVideoAnimateEmbeds, GetNode, SetNode, DrawMaskOnImage, GetNode, GetNode, SetNode, Reroute, Reroute, MaskToImage, PreviewImage, SeCModelLoader, SeCVideoSegmentation, InvertMask, Reroute, PreviewImage, SetNode, VHS_VideoCombine, GetImageSizeAndCount, GetImageSizeAndCount, VHS_VideoCombine, JWInteger, PreviewImage, ImageConcanate, CR Text, INTConstant, INTConstant, Note, VHS_VideoCombine, ImageResizeKJv2, LoadImage, ImageResizeKJv2, VHS_LoadVideo, LoadImage, ImageFromBatch+, PointsEditor]
patterns: []
missing: []
---

# 数字人/数字人/alan自用-主体替换sec video segmentation_1983904795276836866.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/alan自用-主体替换sec video segmentation_1983904795276836866.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（77 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoSetLoRAs`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoBlockSwap`
- `MarkdownNote`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Reroute`
- `DrawViTPose`
- `OnnxDetectionModelLoader`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `WanVideoSetBlockSwap`
- `PoseAndFaceDetection`
- `BlockifyMask`
- `GrowMaskWithBlur`
- `LayerUtility: ImageBlend`
- `GetNode`
- `Reroute`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `Reroute`
- `Reroute`
- `MaskToImage`
- `PreviewImage`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `InvertMask`
- `Reroute`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `JWInteger`
- `PreviewImage`
- `ImageConcanate`
- `CR Text`
- `INTConstant`
- `INTConstant`
- `Note`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `LoadImage`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `LoadImage`
- `ImageFromBatch+`
- `PointsEditor`

## 知识

覆盖率 **57%**（44/77）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoDecode`、`WanVideoSetLoRAs`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`DrawViTPose`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`PoseAndFaceDetection`、`BlockifyMask`、`GrowMaskWithBlur`、`LayerUtility: ImageBlend`、`WanVideoAnimateEmbeds`、`DrawMaskOnImage`、`MaskToImage`、`SeCModelLoader`、`SeCVideoSegmentation`、`InvertMask`、`GetImageSizeAndCount`、`JWInteger`、`ImageConcanate`、`CR Text`、`INTConstant`、`ImageResizeKJv2`、`LoadImage`、`VHS_LoadVideo`、`ImageFromBatch+`、`PointsEditor`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
