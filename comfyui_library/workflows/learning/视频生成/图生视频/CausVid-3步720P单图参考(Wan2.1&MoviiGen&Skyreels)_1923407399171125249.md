---
key: 视频生成/图生视频/CausVid-3步720P单图参考(Wan2.1&MoviiGen&Skyreels)_1923407399171125249.json
name: CausVid-3步720P单图参考(Wan2.1&MoviiGen&Skyreels)_1923407399171125249.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1923407399171125249.json
hash: 457a731ec95b66e2
coverage: 0.894495
learned_at: 2026-10-15 22:29:48
nodes: [WanVideoDecode, LoadWanVideoT5TextEncoder, WanVideoTextEncode, GetImageSize, Image Blank, WanVideoVAELoader, PreviewImage, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, LayerMask: SAM2Ultra, LayerUtility: PurgeVRAM, ImageCompositeMasked, easy ifElse, ImageResizeKJ, PreviewImage, WanVideoDecode, LoadWanVideoT5TextEncoder, GetImageSize, Image Blank, WanVideoVAELoader, VHS_VideoCombine, PreviewImage, WanVideoVACEEncode, WanVideoModelLoader, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, LayerMask: SAM2Ultra, ImageResizeKJ, easy ifElse, PreviewImage, LoadImage, WanVideoSampler, WanVideoSampler, WanVideoLoraSelect, WanVideoVACEModelSelect, INTConstant, INTConstant, WanVideoBlockSwap, LayerMask: ObjectDetectorFL2, LayerMask: LoadFlorence2Model, ImageCompositeMasked, LayerUtility: PurgeVRAM, INTConstant, WanVideoBlockSwap, INTConstant, WanVideoModelLoader, INTConstant, INTConstant, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVACEEncode, LoadImage, String Literal, VHS_VideoCombine, WanVideoDecode, LoadWanVideoT5TextEncoder, GetImageSize, Image Blank, WanVideoVAELoader, PreviewImage, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, LayerMask: SAM2Ultra, LayerUtility: PurgeVRAM, ImageCompositeMasked, easy ifElse, ImageResizeKJ, PreviewImage, WanVideoBlockSwap, INTConstant, INTConstant, INTConstant, WanVideoLoraSelect, WanVideoVACEModelSelect, VHS_VideoCombine, WanVideoTextEncode, String Literal, WanVideoSampler, LoadImage, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoTextEncode, GetImageSize, Image Blank, WanVideoVAELoader, PreviewImage, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, LayerMask: SAM2Ultra, LayerUtility: PurgeVRAM, easy ifElse, PreviewImage, WanVideoBlockSwap, INTConstant, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVACEEncode, VHS_VideoCombine, easy showAnything, WanVideoModelLoader, ImageResizeKJ, INTConstant, INTConstant, ImageCompositeMasked, WanVideoDecode, LoadImage, WanVideoVACEEncode, WanVideoTextEncode, WanVideoEnhanceAVideo, LoadWanVideoT5TextEncoder, WanVideoTextEncode, GetImageSize, Image Blank, WanVideoVAELoader, PreviewImage, LayerMask: LoadFlorence2Model, LayerMask: ObjectDetectorFL2, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, LayerMask: SAM2Ultra, LayerUtility: PurgeVRAM, easy ifElse, PreviewImage, WanVideoBlockSwap, INTConstant, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoVACEEncode, VHS_VideoCombine, easy showAnything, WanVideoModelLoader, ImageResizeKJ, INTConstant, INTConstant, ImageCompositeMasked, WanVideoDecode, LoadImage, WanVideoSampler, RH_Captioner, RH_Captioner, WanVideoSampler, WanVideoEnhanceAVideo, WanVideoDecode, LoadWanVideoT5TextEncoder, GetImageSize, Image Blank, WanVideoVAELoader, VHS_VideoCombine, PreviewImage, WanVideoVACEEncode, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, LayerMask: SAM2Ultra, ImageResizeKJ, easy ifElse, PreviewImage, LoadImage, WanVideoSampler, WanVideoLoraSelect, WanVideoVACEModelSelect, INTConstant, INTConstant, WanVideoBlockSwap, LayerMask: ObjectDetectorFL2, LayerMask: LoadFlorence2Model, ImageCompositeMasked, LayerUtility: PurgeVRAM, INTConstant, WanVideoTextEncode, String Literal, WanVideoDecode, LoadWanVideoT5TextEncoder, GetImageSize, Image Blank, WanVideoVAELoader, VHS_VideoCombine, PreviewImage, WanVideoVACEEncode, WanVideoEnhanceAVideo, WanVideoTeaCache, WanVideoSLG, WanVideoExperimentalArgs, LayerMask: SAM2Ultra, ImageResizeKJ, easy ifElse, PreviewImage, LoadImage, WanVideoSampler, WanVideoLoraSelect, WanVideoVACEModelSelect, INTConstant, INTConstant, WanVideoBlockSwap, LayerMask: ObjectDetectorFL2, LayerMask: LoadFlorence2Model, ImageCompositeMasked, LayerUtility: PurgeVRAM, INTConstant, WanVideoTextEncode, String Literal, WanVideoModelLoader, WanVideoModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/CausVid-3步720P单图参考(Wan2.1&MoviiGen&Skyreels)_1923407399171125249.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1923407399171125249.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（218 个）：
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `GetImageSize`
- `Image Blank`
- `WanVideoVAELoader`
- `PreviewImage`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `LayerMask: SAM2Ultra`
- `LayerUtility: PurgeVRAM`
- `ImageCompositeMasked`
- `easy ifElse`
- `ImageResizeKJ`
- `PreviewImage`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `GetImageSize`
- `Image Blank`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoVACEEncode`
- `WanVideoModelLoader`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `LayerMask: SAM2Ultra`
- `ImageResizeKJ`
- `easy ifElse`
- `PreviewImage`
- `LoadImage`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `INTConstant`
- `INTConstant`
- `WanVideoBlockSwap`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: LoadFlorence2Model`
- `ImageCompositeMasked`
- `LayerUtility: PurgeVRAM`
- `INTConstant`
- `WanVideoBlockSwap`
- `INTConstant`
- `WanVideoModelLoader`
- `INTConstant`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEEncode`
- `LoadImage`
- `String Literal`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `GetImageSize`
- `Image Blank`
- `WanVideoVAELoader`
- `PreviewImage`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `LayerMask: SAM2Ultra`
- `LayerUtility: PurgeVRAM`
- `ImageCompositeMasked`
- `easy ifElse`
- `ImageResizeKJ`
- `PreviewImage`
- `WanVideoBlockSwap`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `String Literal`
- `WanVideoSampler` ★核心
- `LoadImage`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `GetImageSize`
- `Image Blank`
- `WanVideoVAELoader`
- `PreviewImage`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `LayerMask: SAM2Ultra`
- `LayerUtility: PurgeVRAM`
- `easy ifElse`
- `PreviewImage`
- `WanVideoBlockSwap`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEEncode`
- `VHS_VideoCombine`
- `easy showAnything`
- `WanVideoModelLoader`
- `ImageResizeKJ`
- `INTConstant`
- `INTConstant`
- `ImageCompositeMasked`
- `WanVideoDecode`
- `LoadImage`
- `WanVideoVACEEncode`
- `WanVideoTextEncode`
- `WanVideoEnhanceAVideo`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `GetImageSize`
- `Image Blank`
- `WanVideoVAELoader`
- `PreviewImage`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: ObjectDetectorFL2`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `LayerMask: SAM2Ultra`
- `LayerUtility: PurgeVRAM`
- `easy ifElse`
- `PreviewImage`
- `WanVideoBlockSwap`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoVACEEncode`
- `VHS_VideoCombine`
- `easy showAnything`
- `WanVideoModelLoader`
- `ImageResizeKJ`
- `INTConstant`
- `INTConstant`
- `ImageCompositeMasked`
- `WanVideoDecode`
- `LoadImage`
- `WanVideoSampler` ★核心
- `RH_Captioner`
- `RH_Captioner`
- `WanVideoSampler` ★核心
- `WanVideoEnhanceAVideo`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `GetImageSize`
- `Image Blank`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoVACEEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `LayerMask: SAM2Ultra`
- `ImageResizeKJ`
- `easy ifElse`
- `PreviewImage`
- `LoadImage`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `INTConstant`
- `INTConstant`
- `WanVideoBlockSwap`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: LoadFlorence2Model`
- `ImageCompositeMasked`
- `LayerUtility: PurgeVRAM`
- `INTConstant`
- `WanVideoTextEncode`
- `String Literal`
- `WanVideoDecode`
- `LoadWanVideoT5TextEncoder`
- `GetImageSize`
- `Image Blank`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoVACEEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `WanVideoExperimentalArgs`
- `LayerMask: SAM2Ultra`
- `ImageResizeKJ`
- `easy ifElse`
- `PreviewImage`
- `LoadImage`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `INTConstant`
- `INTConstant`
- `WanVideoBlockSwap`
- `LayerMask: ObjectDetectorFL2`
- `LayerMask: LoadFlorence2Model`
- `ImageCompositeMasked`
- `LayerUtility: PurgeVRAM`
- `INTConstant`
- `WanVideoTextEncode`
- `String Literal`
- `WanVideoModelLoader`
- `WanVideoModelLoader`

## 知识

覆盖率 **89%**（195/218）

**有卡**：`WanVideoDecode`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`GetImageSize`、`Image Blank`、`WanVideoVAELoader`、`LayerMask: LoadFlorence2Model`、`LayerMask: ObjectDetectorFL2`、`WanVideoEnhanceAVideo`、`WanVideoTeaCache`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`LayerMask: SAM2Ultra`、`LayerUtility: PurgeVRAM`、`ImageCompositeMasked`、`ImageResizeKJ`、`VHS_VideoCombine`、`WanVideoVACEEncode`、`WanVideoModelLoader`、`LoadImage`、`WanVideoSampler`、`WanVideoLoraSelect`、`WanVideoVACEModelSelect`、`INTConstant`、`WanVideoBlockSwap`、`String Literal`、`RH_Captioner`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelect
