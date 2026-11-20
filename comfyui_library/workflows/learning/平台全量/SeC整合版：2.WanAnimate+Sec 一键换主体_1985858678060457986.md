---
key: 平台全量/SeC整合版：2.WanAnimate+Sec 一键换主体_1985858678060457986.json
name: SeC整合版：2.WanAnimate+Sec 一键换主体_1985858678060457986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/SeC整合版：2.WanAnimate+Sec 一键换主体_1985858678060457986.json
hash: 72d9453b4317488a
coverage: 0.597403
learned_at: 2026-11-14 00:58:14
nodes: [VHS_VideoCombine, VHS_VideoCombine, CLIPTextEncode, CLIPTextEncode, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, VHS_VideoCombine, MaskToImage, SetNode, ImageConcatMulti, GetNode, Reroute, VHS_VideoCombine, VHS_VideoCombine, SeCModelLoader, SeCVideoSegmentation, LayerMask: LoadSegmentAnythingModels, PoseAndFaceDetection, LayerMask: SegmentAnythingUltra V3, OnnxDetectionModelLoader, VHS_VideoCombine, VHS_VideoCombine, GetNode, BlockifyMask, DrawMaskOnImage, SetNode, DrawMaskOnImage, GrowMaskWithBlur, ImageFromBatch, Textbox, WanVideoBlockSwap, WanVideoTorchCompileSettings, ImageResizeKJv2, SetNode, WanVideoTextEmbedBridge, GetNode, SetNode, SetNode, SetNode, WanVideoLoraSelectMulti, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, SetNode, GetNode, WanVideoAnimateEmbeds, SetNode, DrawViTPose, ImageConcatMulti, PreviewImage, SetNode, SetNode, SetNode, GetNode, WanVideoDecode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSetLoRAs, GetNode, GetNode, GetNode, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, INTConstant, INTConstant, VHS_LoadVideo, LoadImage, GetImageSizeAndCount, WanVideoModelLoader, Int]
patterns: []
missing: []
---

# 平台全量/SeC整合版：2.WanAnimate+Sec 一键换主体_1985858678060457986.json

> 来源文件 `comfyui_library/workflows/平台全量/SeC整合版：2.WanAnimate+Sec 一键换主体_1985858678060457986.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（77 个）：
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `MaskToImage`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `Reroute`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `LayerMask: LoadSegmentAnythingModels`
- `PoseAndFaceDetection`
- `LayerMask: SegmentAnythingUltra V3`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SetNode`
- `DrawMaskOnImage`
- `GrowMaskWithBlur`
- `ImageFromBatch`
- `Textbox`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJv2`
- `SetNode`
- `WanVideoTextEmbedBridge`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `SetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `SetNode`
- `DrawViTPose`
- `ImageConcatMulti`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `VHS_LoadVideo`
- `LoadImage`
- `GetImageSizeAndCount`
- `WanVideoModelLoader`
- `Int`

## 知识

覆盖率 **60%**（46/77）

**有卡**：`VHS_VideoCombine`、`CLIPTextEncode`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`MaskToImage`、`ImageConcatMulti`、`SeCModelLoader`、`SeCVideoSegmentation`、`LayerMask: LoadSegmentAnythingModels`、`PoseAndFaceDetection`、`LayerMask: SegmentAnythingUltra V3`、`OnnxDetectionModelLoader`、`BlockifyMask`、`DrawMaskOnImage`、`GrowMaskWithBlur`、`ImageFromBatch`、`Textbox`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`WanVideoTextEmbedBridge`、`WanVideoLoraSelectMulti`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAnimateEmbeds`、`DrawViTPose`、`WanVideoDecode`、`WanVideoSetLoRAs`、`WanVideoSampler`、`INTConstant`、`VHS_LoadVideo`、`LoadImage`、`GetImageSizeAndCount`、`WanVideoModelLoader`、`Int`

**用到的条目**：CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoVAELoader
