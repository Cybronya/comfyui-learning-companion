---
key: 数字人/数字人/SeC整合版：1.WanAnimate+Sec 一键换头_1985857562799218689.json
name: SeC整合版：1.WanAnimate+Sec 一键换头_1985857562799218689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/SeC整合版：1.WanAnimate+Sec 一键换头_1985857562799218689.json
hash: 46c51ec3ace7bc2a
coverage: 0.597403
learned_at: 2026-10-26 01:57:19
nodes: [CLIPTextEncode, CLIPTextEncode, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, INTConstant, INTConstant, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, SeCVideoSegmentation, SeCModelLoader, WanVideoTorchCompileSettings, Textbox, GetNode, ImageFromBatch, ImageResizeKJv2, SetNode, SetNode, SetNode, MaskToImage, WanVideoLoraSelectMulti, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, GetNode, SetNode, OnnxDetectionModelLoader, PoseAndFaceDetection, Reroute, GrowMaskWithBlur, BlockifyMask, DrawMaskOnImage, SetNode, DrawMaskOnImage, SetNode, ImageConcatMulti, GetNode, VHS_VideoCombine, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoDecode, PreviewImage, WanVideoBlockSwap, DrawViTPose, ImageConcatMulti, GetImageSizeAndCount, SetNode, GetNode, SetNode, GetNode, WanVideoTextEmbedBridge, GetNode, GetNode, WanVideoSampler, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSetLoRAs, GetNode, GetNode, GetNode, VHS_LoadVideo, LoadImage, WanVideoModelLoader, Int]
patterns: []
missing: []
---

# 数字人/数字人/SeC整合版：1.WanAnimate+Sec 一键换头_1985857562799218689.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/SeC整合版：1.WanAnimate+Sec 一键换头_1985857562799218689.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（77 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVAELoader`
- `INTConstant`
- `INTConstant`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `WanVideoTorchCompileSettings`
- `Textbox`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `SetNode`
- `MaskToImage`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `GetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `Reroute`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SetNode`
- `DrawMaskOnImage`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoDecode`
- `PreviewImage`
- `WanVideoBlockSwap`
- `DrawViTPose`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEmbedBridge`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoModelLoader`
- `Int`

## 知识

覆盖率 **60%**（46/77）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`INTConstant`、`VHS_VideoCombine`、`LayerMask: LoadSegmentAnythingModels`、`LayerMask: SegmentAnythingUltra V3`、`SeCVideoSegmentation`、`SeCModelLoader`、`WanVideoTorchCompileSettings`、`Textbox`、`ImageFromBatch`、`ImageResizeKJv2`、`MaskToImage`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`GrowMaskWithBlur`、`BlockifyMask`、`DrawMaskOnImage`、`ImageConcatMulti`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`WanVideoBlockSwap`、`DrawViTPose`、`GetImageSizeAndCount`、`WanVideoTextEmbedBridge`、`WanVideoSampler`、`WanVideoSetLoRAs`、`VHS_LoadVideo`、`LoadImage`、`WanVideoModelLoader`、`Int`

**用到的条目**：CLIPTextEncode、CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode
