---
key: 视频生成/图生视频/CausVid-3步720P多图参考(Wan2.1&MoviiGen&Skyreels)_1923698037238263809.json
name: CausVid-3步720P多图参考(Wan2.1&MoviiGen&Skyreels)_1923698037238263809.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/CausVid-3步720P多图参考(Wan2.1&MoviiGen&Skyreels)_1923698037238263809.json
hash: 284836d1854c1220
coverage: 0.901639
learned_at: 2026-10-15 22:29:49
nodes: [RH_Captioner, WanVideoDecode, LoadWanVideoT5TextEncoder, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, LayerMask: ObjectDetectorFL2, WanVideoTextEncode, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, LayerMask: ObjectDetectorFL2, GetImageSize, Image Blank, ImageCompositeMasked, PreviewImage, VHS_VideoCombine, PreviewImage, GetImageSize, Image Blank, ImageConcanate, WanVideoVAELoader, String Literal, LoadImage, WanVideoModelLoader, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, ImageCompositeMasked, PreviewImage, LoadImage, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoTorchCompileSettings, INTConstant, INTConstant, WanVideoVACEEncode, INTConstant, easy showAnything, ImageResizeKJ, WanVideoSampler, RH_Captioner, WanVideoDecode, LoadWanVideoT5TextEncoder, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, LayerMask: ObjectDetectorFL2, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, LayerMask: ObjectDetectorFL2, GetImageSize, Image Blank, ImageCompositeMasked, PreviewImage, VHS_VideoCombine, PreviewImage, GetImageSize, Image Blank, ImageConcanate, WanVideoVAELoader, String Literal, LoadImage, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, ImageCompositeMasked, PreviewImage, LoadImage, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoTorchCompileSettings, INTConstant, INTConstant, WanVideoVACEEncode, INTConstant, easy showAnything, ImageResizeKJ, WanVideoModelLoader, WanVideoTextEncode, WanVideoSampler, RH_Captioner, WanVideoDecode, LoadWanVideoT5TextEncoder, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, LayerMask: ObjectDetectorFL2, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, LayerMask: ObjectDetectorFL2, GetImageSize, Image Blank, ImageCompositeMasked, PreviewImage, VHS_VideoCombine, PreviewImage, GetImageSize, Image Blank, ImageConcanate, WanVideoVAELoader, LoadImage, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, ImageCompositeMasked, PreviewImage, LoadImage, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoBlockSwap, WanVideoTorchCompileSettings, INTConstant, INTConstant, WanVideoVACEEncode, INTConstant, easy showAnything, ImageResizeKJ, WanVideoTextEncode, WanVideoSampler, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/CausVid-3步720P多图参考(Wan2.1&MoviiGen&Skyreels)_1923698037238263809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1923698037238263809.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（122 个）：
- `RH_Captioner`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `LayerMask: ObjectDetectorFL2`
- `WanVideoTextEncode`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `LayerMask: ObjectDetectorFL2`
- `GetImageSize`
- `Image Blank`
- `ImageCompositeMasked`
- `PreviewImage`
- `VHS_VideoCombine`
- `PreviewImage`
- `GetImageSize`
- `Image Blank`
- `ImageConcanate`
- `WanVideoVAELoader`
- `String Literal`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `ImageCompositeMasked`
- `PreviewImage`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `INTConstant`
- `INTConstant`
- `WanVideoVACEEncode`
- `INTConstant`
- `easy showAnything`
- `ImageResizeKJ`
- `WanVideoSampler` ★核心
- `RH_Captioner`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `LayerMask: ObjectDetectorFL2`
- `GetImageSize`
- `Image Blank`
- `ImageCompositeMasked`
- `PreviewImage`
- `VHS_VideoCombine`
- `PreviewImage`
- `GetImageSize`
- `Image Blank`
- `ImageConcanate`
- `WanVideoVAELoader`
- `String Literal`
- `LoadImage`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `ImageCompositeMasked`
- `PreviewImage`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `INTConstant`
- `INTConstant`
- `WanVideoVACEEncode`
- `INTConstant`
- `easy showAnything`
- `ImageResizeKJ`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `RH_Captioner`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `LayerMask: ObjectDetectorFL2`
- `GetImageSize`
- `Image Blank`
- `ImageCompositeMasked`
- `PreviewImage`
- `VHS_VideoCombine`
- `PreviewImage`
- `GetImageSize`
- `Image Blank`
- `ImageConcanate`
- `WanVideoVAELoader`
- `LoadImage`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `ImageCompositeMasked`
- `PreviewImage`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `INTConstant`
- `INTConstant`
- `WanVideoVACEEncode`
- `INTConstant`
- `easy showAnything`
- `ImageResizeKJ`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`

## 知识

覆盖率 **90%**（110/122）

**有卡**：`RH_Captioner`、`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`LayerMask: LoadFlorence2Model`、`LayerMask: SAM2Ultra`、`LayerMask: ObjectDetectorFL2`、`WanVideoTextEncode`、`GetImageSize`、`Image Blank`、`ImageCompositeMasked`、`VHS_VideoCombine`、`ImageConcanate`、`WanVideoVAELoader`、`String Literal`、`LoadImage`、`WanVideoModelLoader`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`WanVideoLoraSelect`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`INTConstant`、`WanVideoVACEEncode`、`ImageResizeKJ`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
