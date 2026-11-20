---
key: 平台全量/Wan2.1_T2V_lynx+VACE视频换脸_1976890391054241794.json
name: Wan2.1_T2V_lynx+VACE视频换脸_1976890391054241794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1_T2V_lynx+VACE视频换脸_1976890391054241794.json
hash: 08f7aa6b316584b4
coverage: 0.794521
learned_at: 2026-11-14 01:04:43
nodes: [WanVideoBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings, LoadLynxResampler, Wan22PromptSelector, WanVideoSetLoRAs, WanVideoSetBlockSwap, ImpactSwitch, Text Concatenate, RH_LLMAPI_NODE, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoLoraSelectMulti, SetNode, WanVideoTextEncodeCached, CR Text, JWInteger, WanVideoTextEncodeCached, Note, Note, WanVideoVAELoader, SetNode, WanVideoVACEModelSelect, Note, MarkdownNote, GetNode, GetImageSizeAndCount, GrowMask, VHS_VideoCombine, WanVideoAddLynxEmbeds, LynxEncodeFaceIP, LoadImage, PreviewImage, ImageScale, PreviewImage, VHS_VideoCombine, BlockifyMask, DrawMaskOnImage, easy showAnything, SeCModelLoader, GrowMask, MaskPreview+, WanVideoSampler, WanVideoDecode, ImageFromBatch+, ImageFromBatch+, VHS_LoadVideo, ImageConcatMulti, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, easy showAnything, JWInteger, VHS_VideoCombine, ImageResizeKJ, easy imageColorMatch, LayerMask: SegmentAnythingUltra V3, LayerMask: LoadSegmentAnythingModels, ImageFromBatch, MaskPreview+, SeCModelLoader, SeCVideoSegmentation, BlockifyMask, DrawMaskOnImage, WanVideoVACEEncode, LynxInsightFaceCrop, Image Crop Face, PreviewImage, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, PointsEditor, SeCVideoSegmentation]
patterns: []
missing: []
---

# 平台全量/Wan2.1_T2V_lynx+VACE视频换脸_1976890391054241794.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1_T2V_lynx+VACE视频换脸_1976890391054241794.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（73 个）：
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `LoadLynxResampler` ★核心
- `Wan22PromptSelector`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `ImpactSwitch`
- `Text Concatenate`
- `RH_LLMAPI_NODE`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `WanVideoTextEncodeCached`
- `CR Text`
- `JWInteger`
- `WanVideoTextEncodeCached`
- `Note`
- `Note`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoVACEModelSelect`
- `Note`
- `MarkdownNote`
- `GetNode`
- `GetImageSizeAndCount`
- `GrowMask`
- `VHS_VideoCombine`
- `WanVideoAddLynxEmbeds`
- `LynxEncodeFaceIP`
- `LoadImage`
- `PreviewImage`
- `ImageScale`
- `PreviewImage`
- `VHS_VideoCombine`
- `BlockifyMask`
- `DrawMaskOnImage`
- `easy showAnything`
- `SeCModelLoader`
- `GrowMask`
- `MaskPreview+`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `VHS_LoadVideo`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `easy showAnything`
- `JWInteger`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `easy imageColorMatch`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerMask: LoadSegmentAnythingModels`
- `ImageFromBatch`
- `MaskPreview+`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `BlockifyMask`
- `DrawMaskOnImage`
- `WanVideoVACEEncode`
- `LynxInsightFaceCrop`
- `Image Crop Face`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PointsEditor`
- `SeCVideoSegmentation`

## 知识

覆盖率 **79%**（58/73）

**有卡**：`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`LoadLynxResampler`、`Wan22PromptSelector`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`Text Concatenate`、`RH_LLMAPI_NODE`、`WanVideoExtraModelSelect`、`WanVideoLoraSelectMulti`、`WanVideoTextEncodeCached`、`CR Text`、`JWInteger`、`WanVideoVAELoader`、`WanVideoVACEModelSelect`、`GetImageSizeAndCount`、`GrowMask`、`VHS_VideoCombine`、`WanVideoAddLynxEmbeds`、`LynxEncodeFaceIP`、`LoadImage`、`ImageScale`、`BlockifyMask`、`DrawMaskOnImage`、`SeCModelLoader`、`MaskPreview+`、`WanVideoSampler`、`WanVideoDecode`、`ImageFromBatch+`、`VHS_LoadVideo`、`ImageConcatMulti`、`ImageResizeKJ`、`easy imageColorMatch`、`LayerMask: SegmentAnythingUltra V3`、`LayerMask: LoadSegmentAnythingModels`、`ImageFromBatch`、`SeCVideoSegmentation`、`WanVideoVACEEncode`、`LynxInsightFaceCrop`、`Image Crop Face`、`LayerUtility: ImageScaleByAspectRatio V2`、`PointsEditor`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、LoadLynxResampler、WanVideoSampler、LynxEncodeFaceIP、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVACEEncode
