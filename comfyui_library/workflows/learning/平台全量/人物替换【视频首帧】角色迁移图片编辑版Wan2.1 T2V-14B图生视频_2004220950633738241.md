---
key: 平台全量/人物替换【视频首帧】角色迁移图片编辑版Wan2.1 T2V-14B图生视频_2004220950633738241.json
name: 人物替换【视频首帧】角色迁移图片编辑版Wan2.1 T2V-14B图生视频_2004220950633738241
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/人物替换【视频首帧】角色迁移图片编辑版Wan2.1 T2V-14B图生视频_2004220950633738241.json
hash: be238d0aea15aaa4
coverage: 0.513514
learned_at: 2026-11-14 01:37:59
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ToBinaryMask, WanVideoEnhanceAVideo, StringLength, easy int, easy compare, PreviewAny, easy cleanGpuUsed, easy ifElse, PrimitiveStringMultiline, ToBinaryMask, easy ifElse, MaskToImage, easy cleanGpuUsed, PreviewImage, Mask Fill Holes, Any Switch (rgthree), easy cleanGpuUsed, easy isMaskEmpty, Mask Fill Holes, easy ifElse, WanVideoExperimentalArgs, WanVideoSLG, INPAINT_MaskedFill, MediaPipe-FaceMeshPreprocessor, DWPreprocessor, DWPreprocessor, Note, PreviewAny, RMBG, LayerUtility: CropByMask V2, PrimitiveInt, WanVideoTextEncode, ImageResizeKJv2, ImageCompositeMasked, RepeatImageBatch, easy isMaskEmpty, GetImageSizeAndCount, ImageResizeKJv2, Any Switch (rgthree), ImageResizeKJv2, RepeatImageBatch, RepeatImageBatch, ImageToMask, Any Switch (rgthree), WanVideoVACEEncode, Any Switch (rgthree), WanVideoAddStandInLatent, PreviewImage, ClothesSegment, WanVideoEncode, ApplyFaceProcessor, FaceProcessorLoader, Fast Groups Muter (rgthree), Qwen2.5VL, PreviewAny, easy seed, easy int, VHS_LoadVideo, ImageFromBatch, WanVideoDecode, ImageConcanate, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), PreviewImage, WanVideoSampler, Fast Groups Muter (rgthree), PreviewImage, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, Anything Everywhere3, LoadImage, LoadImage, GetNode, PreviewImage, Image Comparer (rgthree), SetNode, GetImageRangeFromBatch, SaveImage]
patterns: []
missing: []
---

# 平台全量/人物替换【视频首帧】角色迁移图片编辑版Wan2.1 T2V-14B图生视频_2004220950633738241.json

> 来源文件 `comfyui_library/workflows/平台全量/人物替换【视频首帧】角色迁移图片编辑版Wan2.1 T2V-14B图生视频_2004220950633738241.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（111 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ToBinaryMask`
- `WanVideoEnhanceAVideo`
- `StringLength`
- `easy int`
- `easy compare`
- `PreviewAny`
- `easy cleanGpuUsed`
- `easy ifElse`
- `PrimitiveStringMultiline`
- `ToBinaryMask`
- `easy ifElse`
- `MaskToImage`
- `easy cleanGpuUsed`
- `PreviewImage`
- `Mask Fill Holes`
- `Any Switch (rgthree)`
- `easy cleanGpuUsed`
- `easy isMaskEmpty`
- `Mask Fill Holes`
- `easy ifElse`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `INPAINT_MaskedFill`
- `MediaPipe-FaceMeshPreprocessor`
- `DWPreprocessor`
- `DWPreprocessor`
- `Note`
- `PreviewAny`
- `RMBG`
- `LayerUtility: CropByMask V2`
- `PrimitiveInt`
- `WanVideoTextEncode`
- `ImageResizeKJv2`
- `ImageCompositeMasked`
- `RepeatImageBatch`
- `easy isMaskEmpty`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `Any Switch (rgthree)`
- `ImageResizeKJv2`
- `RepeatImageBatch`
- `RepeatImageBatch`
- `ImageToMask`
- `Any Switch (rgthree)`
- `WanVideoVACEEncode`
- `Any Switch (rgthree)`
- `WanVideoAddStandInLatent`
- `PreviewImage`
- `ClothesSegment`
- `WanVideoEncode`
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `Fast Groups Muter (rgthree)`
- `Qwen2.5VL`
- `PreviewAny`
- `easy seed`
- `easy int`
- `VHS_LoadVideo`
- `ImageFromBatch`
- `WanVideoDecode`
- `ImageConcanate`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `Fast Groups Muter (rgthree)`
- `PreviewImage`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `Anything Everywhere3`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SetNode`
- `GetImageRangeFromBatch`
- `SaveImage`

## 知识

覆盖率 **51%**（57/111）

**有卡**：`ToBinaryMask`、`WanVideoEnhanceAVideo`、`StringLength`、`easy int`、`easy compare`、`easy cleanGpuUsed`、`MaskToImage`、`Mask Fill Holes`、`easy isMaskEmpty`、`WanVideoExperimentalArgs`、`WanVideoSLG`、`INPAINT_MaskedFill`、`MediaPipe-FaceMeshPreprocessor`、`DWPreprocessor`、`RMBG`、`LayerUtility: CropByMask V2`、`WanVideoTextEncode`、`ImageResizeKJv2`、`ImageCompositeMasked`、`RepeatImageBatch`、`GetImageSizeAndCount`、`ImageToMask`、`WanVideoVACEEncode`、`WanVideoAddStandInLatent`、`ClothesSegment`、`WanVideoEncode`、`ApplyFaceProcessor`、`FaceProcessorLoader`、`Qwen2.5VL`、`easy seed`、`VHS_LoadVideo`、`ImageFromBatch`、`WanVideoDecode`、`ImageConcanate`、`WanVideoSampler`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`WanVideoVACEModelSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`LoadImage`、`GetImageRangeFromBatch`、`SaveImage`

**用到的条目**：LoadImage、easy seed、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoAddStandInLatent、WanVideoDecode、WanVideoEncode、WanVideoTextEncode
