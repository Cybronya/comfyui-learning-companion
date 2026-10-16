---
key: 视频生成/图生视频/Wan2.2 Vace首尾帧实验版V1_1950053355886436353.json
name: Wan2.2 Vace首尾帧实验版V1_1950053355886436353.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950053355886436353.json
hash: e56868bf4b961b66
coverage: 0.844444
learned_at: 2026-10-15 22:30:52
nodes: [CLIPTextEncode, ImageBatch, ImageBatch, ImageToMask, MaskToImage, LayerUtility: PurgeVRAM, TrimVideoLatent, LayerUtility: PurgeVRAM, PathchSageAttentionKJ, ModelSamplingSD3, MaskToImage, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, easy showAnything, easy showAnything, SolidMask, RepeatImageBatch, ImageBatch, SolidMask, easy showAnything, easy showAnything, MathExpression|pysssss, ImageBatch, PreviewImage, LoadImage, ModelSamplingSD3, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, JWInteger, WanVaceToVideo, UnetLoaderGGUF, UnetLoaderGGUF, CLIPTextEncode, CLIPLoader, VAELoader, KSamplerAdvanced, KSamplerAdvanced, VHS_VideoCombine, JWInteger, Note, VAEDecode, ImageFromBatch+]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 Vace首尾帧实验版V1_1950053355886436353.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950053355886436353.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPTextEncode` ★核心
- `ImageBatch`
- `ImageBatch`
- `ImageToMask`
- `MaskToImage`
- `LayerUtility: PurgeVRAM`
- `TrimVideoLatent`
- `LayerUtility: PurgeVRAM`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `MaskToImage`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `easy showAnything`
- `easy showAnything`
- `SolidMask`
- `RepeatImageBatch`
- `ImageBatch`
- `SolidMask`
- `easy showAnything`
- `easy showAnything`
- `MathExpression|pysssss`
- `ImageBatch`
- `PreviewImage`
- `LoadImage`
- `ModelSamplingSD3`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `JWInteger`
- `WanVaceToVideo`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_VideoCombine`
- `JWInteger`
- `Note`
- `VAEDecode` ★核心
- `ImageFromBatch+`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（38/45）

**有卡**：`CLIPTextEncode`、`ImageBatch`、`ImageToMask`、`MaskToImage`、`LayerUtility: PurgeVRAM`、`TrimVideoLatent`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`LoadImage`、`SolidMask`、`RepeatImageBatch`、`MathExpression|pysssss`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`WanVaceToVideo`、`UnetLoaderGGUF`、`CLIPLoader`、`VAELoader`、`KSamplerAdvanced`、`VHS_VideoCombine`、`VAEDecode`、`ImageFromBatch+`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
