---
key: 视频生成/文生视频/Wan2.2-VACE-文生视频_2072999663609094144.json
name: Wan2.2-VACE-文生视频_2072999663609094144
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-VACE-文生视频_2072999663609094144.json
hash: e161eee6db05d3b2
coverage: 0.983673
learned_at: 2026-10-15 22:47:13
nodes: [CLIPTextEncode, CFGZeroStarAndInit, CLIPTextEncode, VAEDecode, TrimVideoLatent, KSamplerAdvanced, KSamplerAdvanced, easy int, WanVideoEnhanceAVideoKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, easy seed, easy int, INTConstant, VHS_VideoCombine, String Literal, WanVaceToVideo, CLIPLoader, VAELoader, CLIPLoader, CLIPTextEncode, CFGZeroStarAndInit, CLIPTextEncode, ImageResizeKJ, INTConstant, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, VAEDecode, TrimVideoLatent, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, easy int, easy int, WanVideoEnhanceAVideoKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, WanVaceToVideo, VAELoader, UnetLoaderGGUF, UnetLoaderGGUF, INTConstant, CLIPLoader, CLIPTextEncode, CFGZeroStarAndInit, CLIPTextEncode, ImageResizeKJ, INTConstant, GetImageSizeAndCount, WanVideoVACEStartToEndFrame, VAEDecode, TrimVideoLatent, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, easy int, easy int, WanVideoEnhanceAVideoKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, VAELoader, UnetLoaderGGUF, UnetLoaderGGUF, INTConstant, WanVaceToVideo, String Literal, String Literal, easy seed, LoadImage, LoadImage, CLIPLoader, CLIPTextEncode, CFGZeroStarAndInit, CLIPTextEncode, ImageResizeKJ, INTConstant, GetImageSizeAndCount, ImageResizeKJ, WanVideoVACEStartToEndFrame, VAEDecode, TrimVideoLatent, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, easy int, easy int, WanVideoEnhanceAVideoKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, WanVaceToVideo, String Literal, VAELoader, UnetLoaderGGUF, UnetLoaderGGUF, INTConstant, LoadImage, LoadImage, CLIPLoader, CLIPTextEncode, CFGZeroStarAndInit, CLIPTextEncode, VAEDecode, TrimVideoLatent, KSamplerAdvanced, KSamplerAdvanced, easy int, easy int, WanVideoEnhanceAVideoKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, WanVaceToVideo, VAELoader, UnetLoaderGGUF, UnetLoaderGGUF, easy seed, MaskToImage, VHS_VideoCombine, INTConstant, String Literal, INTConstant, ImagePadKJ, GetImageSize+, ImageResizeKJ, JWImageExtractFromBatch, VHS_VideoCombine, VHS_LoadVideo, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, LayerMask: ObjectDetectorFL2, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, LayerMask: ObjectDetectorFL2, GetImageSize, Image Blank, ImageCompositeMasked, PreviewImage, PreviewImage, GetImageSize, Image Blank, ImageCompositeMasked, PreviewImage, ImageConcanate, INTConstant, CLIPLoader, CLIPTextEncode, CFGZeroStarAndInit, CLIPTextEncode, VAEDecode, TrimVideoLatent, KSamplerAdvanced, KSamplerAdvanced, easy int, WanVideoEnhanceAVideoKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, VAELoader, UnetLoaderGGUF, UnetLoaderGGUF, easy seed, easy int, WanVaceToVideo, INTConstant, ImageResizeKJ, LoadImage, LoadImage, String Literal, LoadImage, LayerMask: ObjectDetectorFL2, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, CLIPLoader, CLIPTextEncode, CFGZeroStarAndInit, CLIPTextEncode, VAEDecode, TrimVideoLatent, KSamplerAdvanced, KSamplerAdvanced, easy int, easy int, WanVideoEnhanceAVideoKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, WanVaceToVideo, VAELoader, INTConstant, GrowMaskWithBlur, PreviewImage, INTConstant, VHS_VideoCombine, ImageResizeKJv2, InpaintPreprocessor, String Literal, easy seed, UnetLoaderGGUF, UnetLoaderGGUF, VHS_VideoCombine, VHS_LoadVideo, VHS_VideoCombine, UnetLoaderGGUF, UnetLoaderGGUF]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/Wan2.2-VACE-文生视频_2072999663609094144.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-VACE-文生视频_2072999663609094144.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（245 个）：
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy int`
- `WanVideoEnhanceAVideoKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `WanVideoEnhanceAVideoKJ`
- `easy seed`
- `easy int`
- `INTConstant`
- `VHS_VideoCombine`
- `String Literal`
- `WanVaceToVideo`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `INTConstant`
- `GetImageSizeAndCount`
- `WanVideoVACEStartToEndFrame`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy int`
- `easy int`
- `WanVideoEnhanceAVideoKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `WanVideoEnhanceAVideoKJ`
- `WanVaceToVideo`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `INTConstant`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `INTConstant`
- `GetImageSizeAndCount`
- `WanVideoVACEStartToEndFrame`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy int`
- `easy int`
- `WanVideoEnhanceAVideoKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `WanVideoEnhanceAVideoKJ`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `INTConstant`
- `WanVaceToVideo`
- `String Literal`
- `String Literal`
- `easy seed`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `INTConstant`
- `GetImageSizeAndCount`
- `ImageResizeKJ`
- `WanVideoVACEStartToEndFrame`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy int`
- `easy int`
- `WanVideoEnhanceAVideoKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `WanVideoEnhanceAVideoKJ`
- `WanVaceToVideo`
- `String Literal`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `INTConstant`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy int`
- `easy int`
- `WanVideoEnhanceAVideoKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `WanVideoEnhanceAVideoKJ`
- `WanVaceToVideo`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `easy seed`
- `MaskToImage`
- `VHS_VideoCombine`
- `INTConstant`
- `String Literal`
- `INTConstant`
- `ImagePadKJ`
- `GetImageSize+`
- `ImageResizeKJ`
- `JWImageExtractFromBatch`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
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
- `PreviewImage`
- `GetImageSize`
- `Image Blank`
- `ImageCompositeMasked`
- `PreviewImage`
- `ImageConcanate`
- `INTConstant`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy int`
- `WanVideoEnhanceAVideoKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `WanVideoEnhanceAVideoKJ`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `easy seed`
- `easy int`
- `WanVaceToVideo`
- `INTConstant`
- `ImageResizeKJ`
- `LoadImage`
- `LoadImage`
- `String Literal`
- `LoadImage`
- `LayerMask: ObjectDetectorFL2`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `LayerMask: LoadFlorence2Model`
- `LayerMask: SAM2Ultra`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy int`
- `easy int`
- `WanVideoEnhanceAVideoKJ`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CFGZeroStarAndInit`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `WanVideoEnhanceAVideoKJ`
- `WanVaceToVideo`
- `VAELoader`
- `INTConstant`
- `GrowMaskWithBlur`
- `PreviewImage`
- `INTConstant`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `InpaintPreprocessor`
- `String Literal`
- `easy seed`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `beta`

## 知识

覆盖率 **98%**（241/245）

**有卡**：`CLIPTextEncode`、`CFGZeroStarAndInit`、`VAEDecode`、`TrimVideoLatent`、`KSamplerAdvanced`、`easy int`、`WanVideoEnhanceAVideoKJ`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`easy seed`、`INTConstant`、`VHS_VideoCombine`、`String Literal`、`WanVaceToVideo`、`CLIPLoader`、`VAELoader`、`ImageResizeKJ`、`GetImageSizeAndCount`、`WanVideoVACEStartToEndFrame`、`UnetLoaderGGUF`、`LoadImage`、`MaskToImage`、`ImagePadKJ`、`GetImageSize+`、`JWImageExtractFromBatch`、`VHS_LoadVideo`、`LayerMask: LoadFlorence2Model`、`LayerMask: SAM2Ultra`、`LayerMask: ObjectDetectorFL2`、`GetImageSize`、`Image Blank`、`ImageCompositeMasked`、`ImageConcanate`、`LayerUtility: PurgeVRAM V2`、`GrowMaskWithBlur`、`ImageResizeKJv2`、`InpaintPreprocessor`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerAdvanced、CFGZeroStarAndInit
