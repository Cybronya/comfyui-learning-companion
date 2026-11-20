---
key: 平台全量/Wan2.2-VACE-参考编辑_1950470144420175874.json
name: Wan2.2-VACE-参考编辑_1950470144420175874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-VACE-参考编辑_1950470144420175874.json
hash: 9a32dfb4aebf58a8
coverage: 0.975
learned_at: 2026-11-14 01:06:03
nodes: [LayerMask: ObjectDetectorFL2, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, LayerMask: LoadFlorence2Model, LayerMask: SAM2Ultra, CLIPLoader, CLIPTextEncode, CFGZeroStarAndInit, CLIPTextEncode, VAEDecode, TrimVideoLatent, KSamplerAdvanced, KSamplerAdvanced, easy int, easy int, WanVideoEnhanceAVideoKJ, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, WanVaceToVideo, VAELoader, VHS_VideoCombine, CLIPLoader, CLIPTextEncode, CFGZeroStarAndInit, CLIPTextEncode, VAEDecode, TrimVideoLatent, KSamplerAdvanced, easy int, easy int, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, CFGZeroStarAndInit, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVideoEnhanceAVideoKJ, WanVaceToVideo, VAELoader, UnetLoaderGGUF, UnetLoaderGGUF, easy seed, INTConstant, VHS_VideoCombine, Florence2ModelLoader, VHS_LoadVideo, ImageToMask, INTConstant, VHS_LoadVideo, LoadImage, InpaintPreprocessor, GrowMaskWithBlur, VHS_VideoCombine, ImageResizeKJ, ImageResizeKJ, Florence2Run, PreviewImage, String Literal, KSamplerAdvanced, WanVideoEnhanceAVideoKJ, VHS_LoadVideo, INTConstant, GrowMaskWithBlur, PreviewImage, INTConstant, VHS_VideoCombine, ImageResizeKJv2, InpaintPreprocessor, String Literal, easy seed, UnetLoaderGGUF, UnetLoaderGGUF, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "beta", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 平台全量/Wan2.2-VACE-参考编辑_1950470144420175874.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-VACE-参考编辑_1950470144420175874.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
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
- `VHS_VideoCombine`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `KSamplerAdvanced` ★核心
- `easy int`
- `easy int`
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
- `INTConstant`
- `VHS_VideoCombine`
- `Florence2ModelLoader`
- `VHS_LoadVideo`
- `ImageToMask`
- `INTConstant`
- `VHS_LoadVideo`
- `LoadImage`
- `InpaintPreprocessor`
- `GrowMaskWithBlur`
- `VHS_VideoCombine`
- `ImageResizeKJ`
- `ImageResizeKJ`
- `Florence2Run`
- `PreviewImage`
- `String Literal`
- `KSamplerAdvanced` ★核心
- `WanVideoEnhanceAVideoKJ`
- `VHS_LoadVideo`
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
- `LoadImage`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `beta`

## 知识

覆盖率 **98%**（78/80）

**有卡**：`LayerMask: ObjectDetectorFL2`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`LayerMask: LoadFlorence2Model`、`LayerMask: SAM2Ultra`、`CLIPLoader`、`CLIPTextEncode`、`CFGZeroStarAndInit`、`VAEDecode`、`TrimVideoLatent`、`KSamplerAdvanced`、`easy int`、`WanVideoEnhanceAVideoKJ`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`WanVaceToVideo`、`VAELoader`、`UnetLoaderGGUF`、`easy seed`、`INTConstant`、`Florence2ModelLoader`、`VHS_LoadVideo`、`ImageToMask`、`LoadImage`、`InpaintPreprocessor`、`GrowMaskWithBlur`、`ImageResizeKJ`、`Florence2Run`、`String Literal`、`ImageResizeKJv2`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、CFGZeroStarAndInit、easy seed
