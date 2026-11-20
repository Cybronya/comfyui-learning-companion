---
key: 平台全量/Wan2.2 Fun VACE 局部编辑_1966820969887227906.json
name: Wan2.2 Fun VACE 局部编辑_1966820969887227906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Fun VACE 局部编辑_1966820969887227906.json
hash: e943fb9d81af79f1
coverage: 0.794118
learned_at: 2026-11-14 01:05:27
nodes: [WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, SetNode, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoSetBlockSwap, SetNode, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoScheduler, GetNode, CreateCFGScheduleFloatList, WanVideoSigmaToStep, PrimitiveNode, PrimitiveNode, SetNode, AddLabel, AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, WanVideoDecode, ImageConcatMulti, ImageConcatMulti, WanVideoSampler, JWInteger, GetNode, GetNode, WanVideoScheduler, VHS_LoadVideo, QwenVLDetection, DownloadAndLoadQwenModel, LayerMask: SAM2VideoUltra, LayerUtility: PurgeVRAM V2, GetNode, WanVideoTextEncodeCached, BBoxesToSAM2, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfo, GetNode, ImageFromBatch, JWInteger, Text Multiline, VHS_VideoCombine, SimpleMath+, ImageFromBatch+, SetNode, WanVideoSampler, VHS_VideoCombine, AIO_Preprocessor, WanVideoVACEEncode, ImageResizeKJ, InpaintPreprocessor, GetImageSizeAndCount, LayerUtility: ImageBlend, GrowMaskWithBlur, CR Text, VHS_VideoCombine, LoadImage, ImageResizeKJv2, InspyrenetRembg, LayerUtility: ImageRemoveAlpha, SetNode, PreviewImage]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Fun VACE 局部编辑_1966820969887227906.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Fun VACE 局部编辑_1966820969887227906.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（68 个）：
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoScheduler`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `WanVideoSigmaToStep`
- `PrimitiveNode`
- `PrimitiveNode`
- `SetNode`
- `AddLabel`
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `JWInteger`
- `GetNode`
- `GetNode`
- `WanVideoScheduler`
- `VHS_LoadVideo`
- `QwenVLDetection`
- `DownloadAndLoadQwenModel`
- `LayerMask: SAM2VideoUltra`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `WanVideoTextEncodeCached`
- `BBoxesToSAM2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfo`
- `GetNode`
- `ImageFromBatch`
- `JWInteger`
- `Text Multiline`
- `VHS_VideoCombine`
- `SimpleMath+`
- `ImageFromBatch+`
- `SetNode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `AIO_Preprocessor`
- `WanVideoVACEEncode`
- `ImageResizeKJ`
- `InpaintPreprocessor`
- `GetImageSizeAndCount`
- `LayerUtility: ImageBlend`
- `GrowMaskWithBlur`
- `CR Text`
- `VHS_VideoCombine`
- `LoadImage`
- `ImageResizeKJv2`
- `InspyrenetRembg`
- `LayerUtility: ImageRemoveAlpha`
- `SetNode`
- `PreviewImage`

## 知识

覆盖率 **79%**（54/68）

**有卡**：`WanVideoLoraSelectMulti`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`WanVideoScheduler`、`CreateCFGScheduleFloatList`、`WanVideoSigmaToStep`、`AddLabel`、`EmptyImage`、`GetImageSizeAndCount`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoSampler`、`JWInteger`、`VHS_LoadVideo`、`QwenVLDetection`、`DownloadAndLoadQwenModel`、`LayerMask: SAM2VideoUltra`、`LayerUtility: PurgeVRAM V2`、`WanVideoTextEncodeCached`、`BBoxesToSAM2`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfo`、`ImageFromBatch`、`Text Multiline`、`VHS_VideoCombine`、`SimpleMath+`、`ImageFromBatch+`、`AIO_Preprocessor`、`WanVideoVACEEncode`、`ImageResizeKJ`、`InpaintPreprocessor`、`LayerUtility: ImageBlend`、`GrowMaskWithBlur`、`CR Text`、`LoadImage`、`ImageResizeKJv2`、`InspyrenetRembg`、`LayerUtility: ImageRemoveAlpha`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、CreateCFGScheduleFloatList、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVACEEncode、WanVideoVAELoader
