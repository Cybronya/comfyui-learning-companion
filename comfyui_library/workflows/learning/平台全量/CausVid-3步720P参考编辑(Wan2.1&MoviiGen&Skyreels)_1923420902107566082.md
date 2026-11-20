---
key: 平台全量/CausVid-3步720P参考编辑(Wan2.1&MoviiGen&Skyreels)_1923420902107566082.json
name: CausVid-3步720P参考编辑(Wan2.1&MoviiGen&Skyreels)_1923420902107566082
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/CausVid-3步720P参考编辑(Wan2.1&MoviiGen&Skyreels)_1923420902107566082.json
hash: 2bf8774c98fd5735
coverage: 0.96875
learned_at: 2026-11-14 00:22:07
nodes: [LoadWanVideoT5TextEncoder, LayerMask: ObjectDetectorFL2, WanVideoTextEncode, WanVideoDecode, VHS_VideoCombine, WanVideoVAELoader, PreviewImage, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, WanVideoModelLoader, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, WanVideoTeaCache, WanVideoVACEEncode, ImageResizeKJ, WanVideoTorchCompileSettings, ImageResizeKJ, GrowMaskWithBlur, InpaintPreprocessor, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, VHS_LoadVideo, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoSampler, INTConstant, WanVideoVACEModelSelect, INTConstant, INTConstant, LoadImage, RH_Captioner, RH_Captioner, LoadWanVideoT5TextEncoder, LayerMask: ObjectDetectorFL2, WanVideoTextEncode, WanVideoDecode, VHS_VideoCombine, WanVideoVAELoader, PreviewImage, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, WanVideoTeaCache, ImageResizeKJ, WanVideoTorchCompileSettings, ImageResizeKJ, GrowMaskWithBlur, InpaintPreprocessor, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, VHS_LoadVideo, WanVideoBlockSwap, WanVideoSampler, INTConstant, INTConstant, INTConstant, LoadImage, WanVideoModelLoader, WanVideoVACEEncode, WanVideoLoraSelect, WanVideoVACEModelSelect, RH_Captioner, LoadWanVideoT5TextEncoder, LayerMask: ObjectDetectorFL2, WanVideoTextEncode, WanVideoDecode, VHS_VideoCombine, WanVideoVAELoader, PreviewImage, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoExperimentalArgs, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, WanVideoTeaCache, ImageResizeKJ, ImageResizeKJ, GrowMaskWithBlur, InpaintPreprocessor, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, VHS_LoadVideo, WanVideoBlockSwap, WanVideoSampler, INTConstant, INTConstant, INTConstant, LoadImage, WanVideoVACEEncode, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoTorchCompileSettings]
patterns: []
missing: []
---

# 平台全量/CausVid-3步720P参考编辑(Wan2.1&MoviiGen&Skyreels)_1923420902107566082.json

> 来源文件 `comfyui_library/workflows/平台全量/CausVid-3步720P参考编辑(Wan2.1&MoviiGen&Skyreels)_1923420902107566082.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（96 个）：
- `LoadWanVideoT5TextEncoder`
- `LayerMask: ObjectDetectorFL2`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `PreviewImage`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoTeaCache`
- `WanVideoVACEEncode`
- `ImageResizeKJ`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJ`
- `GrowMaskWithBlur`
- `InpaintPreprocessor`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `VHS_LoadVideo`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `INTConstant`
- `WanVideoVACEModelSelect`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `RH_Captioner`
- `RH_Captioner`
- `LoadWanVideoT5TextEncoder`
- `LayerMask: ObjectDetectorFL2`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `PreviewImage`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoTeaCache`
- `ImageResizeKJ`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJ`
- `GrowMaskWithBlur`
- `InpaintPreprocessor`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `VHS_LoadVideo`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoVACEEncode`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `RH_Captioner`
- `LoadWanVideoT5TextEncoder`
- `LayerMask: ObjectDetectorFL2`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `PreviewImage`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoTeaCache`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `GrowMaskWithBlur`
- `InpaintPreprocessor`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `VHS_LoadVideo`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `WanVideoVACEEncode`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`

## 知识

覆盖率 **97%**（93/96）

**有卡**：`LoadWanVideoT5TextEncoder`、`LayerMask: ObjectDetectorFL2`、`WanVideoTextEncode`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM V2`、`WanVideoTeaCache`、`WanVideoVACEEncode`、`ImageResizeKJ`、`WanVideoTorchCompileSettings`、`GrowMaskWithBlur`、`InpaintPreprocessor`、`LayerMask: LoadFlorence2Model`、`LayerMask: SAM2Ultra`、`VHS_LoadVideo`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoSampler`、`INTConstant`、`WanVideoVACEModelSelect`、`LoadImage`、`RH_Captioner`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect
