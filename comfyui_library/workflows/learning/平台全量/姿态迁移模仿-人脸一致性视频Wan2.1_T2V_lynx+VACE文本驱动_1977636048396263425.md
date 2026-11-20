---
key: 平台全量/姿态迁移模仿-人脸一致性视频Wan2.1_T2V_lynx+VACE文本驱动_1977636048396263425.json
name: 姿态迁移模仿-人脸一致性视频Wan2.1_T2V_lynx+VACE文本驱动_1977636048396263425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/姿态迁移模仿-人脸一致性视频Wan2.1_T2V_lynx+VACE文本驱动_1977636048396263425.json
hash: e23428c1230385bd
coverage: 0.689189
learned_at: 2026-11-14 01:59:19
nodes: [WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoExtraModelSelect, WanVideoExtraModelSelect, WanVideoVACEModelSelect, WanVideoLoraSelectMulti, WanVideoDecode, PreviewImage, PreviewImage, LynxInsightFaceCrop, ImageFromBatch+, ImageConcatMulti, GetNode, GetNode, GetNode, SetNode, SetNode, PreviewImage, SetNode, WanVideoVAELoader, GetNode, GetNode, SetNode, LoadLynxResampler, SetNode, WanVideoTextEncodeCached, GetNode, GetNode, VHS_VideoCombine, Text Concatenate, easy showAnything, WanVideoModelLoader, easy cleanGpuUsed, ImageFromBatch+, ImageConcatMulti, SetNode, SeCModelLoader, GetNode, GetNode, easy showAnything, CR Text, GrowMask, VHS_VideoCombine, DrawMaskOnImage, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, LynxEncodeFaceIP, easy cleanGpuUsed, WanVideoSetBlockSwap, SeCVideoSegmentation, easy cleanGpuUsed, JWInteger, GetNode, SetNode, WanVideoAddLynxEmbeds, WanVideoTextEncodeCached, WanVideoSampler, LayerUtility: ImageScaleByAspectRatio V2, SetNode, PointsEditor, VHS_VideoCombine, ImageResizeKJ, VHS_VideoCombine, WanVideoSetLoRAs, easy cleanGpuUsed, GetImageSizeAndCount, WanVideoVACEEncode, easy cleanGpuUsed, easy cleanGpuUsed, VHS_LoadVideo, LoadImage, AIO_Preprocessor, Wan22PromptSelector]
patterns: []
missing: []
---

# 平台全量/姿态迁移模仿-人脸一致性视频Wan2.1_T2V_lynx+VACE文本驱动_1977636048396263425.json

> 来源文件 `comfyui_library/workflows/平台全量/姿态迁移模仿-人脸一致性视频Wan2.1_T2V_lynx+VACE文本驱动_1977636048396263425.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（74 个）：
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoExtraModelSelect`
- `WanVideoExtraModelSelect`
- `WanVideoVACEModelSelect`
- `WanVideoLoraSelectMulti`
- `WanVideoDecode`
- `PreviewImage`
- `PreviewImage`
- `LynxInsightFaceCrop`
- `ImageFromBatch+`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadLynxResampler` ★核心
- `SetNode`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Text Concatenate`
- `easy showAnything`
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `ImageFromBatch+`
- `ImageConcatMulti`
- `SetNode`
- `SeCModelLoader`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `CR Text`
- `GrowMask`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LynxEncodeFaceIP`
- `easy cleanGpuUsed`
- `WanVideoSetBlockSwap`
- `SeCVideoSegmentation`
- `easy cleanGpuUsed`
- `JWInteger`
- `GetNode`
- `SetNode`
- `WanVideoAddLynxEmbeds`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `PointsEditor`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `easy cleanGpuUsed`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VHS_LoadVideo`
- `LoadImage`
- `AIO_Preprocessor`
- `Wan22PromptSelector`

## 知识

覆盖率 **69%**（51/74）

**有卡**：`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoExtraModelSelect`、`WanVideoVACEModelSelect`、`WanVideoLoraSelectMulti`、`WanVideoDecode`、`LynxInsightFaceCrop`、`ImageFromBatch+`、`ImageConcatMulti`、`WanVideoVAELoader`、`LoadLynxResampler`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`Text Concatenate`、`WanVideoModelLoader`、`easy cleanGpuUsed`、`SeCModelLoader`、`CR Text`、`GrowMask`、`DrawMaskOnImage`、`LynxEncodeFaceIP`、`WanVideoSetBlockSwap`、`SeCVideoSegmentation`、`JWInteger`、`WanVideoAddLynxEmbeds`、`WanVideoSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`PointsEditor`、`ImageResizeKJ`、`WanVideoSetLoRAs`、`GetImageSizeAndCount`、`WanVideoVACEEncode`、`VHS_LoadVideo`、`LoadImage`、`AIO_Preprocessor`、`Wan22PromptSelector`

**用到的条目**：LayerUtility: ImageScaleByAspectRatio V2、LoadImage、LoadLynxResampler、WanVideoSampler、LynxEncodeFaceIP、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVACEEncode
