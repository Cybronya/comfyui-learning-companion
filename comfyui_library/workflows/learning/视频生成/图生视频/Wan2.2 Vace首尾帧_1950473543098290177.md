---
key: 视频生成/图生视频/Wan2.2 Vace首尾帧_1950473543098290177.json
name: Wan2.2 Vace首尾帧_1950473543098290177.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Vace首尾帧_1950473543098290177.json
hash: 838a4eb677a01830
coverage: 0.948718
learned_at: 2026-10-15 22:30:55
nodes: [ImageBatch, ImageBatch, UnetLoaderGGUF, CLIPTextEncode, CLIPLoader, KSamplerAdvanced, UnetLoaderGGUF, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, ModelSamplingSD3, WanVaceToVideo, KSamplerAdvanced, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, TrimVideoLatent, VAEDecode, ImageFromBatch+, VHS_VideoCombine, MaskToImage, ImageBatch, ImageBatch, JWInteger, SolidMask, MaskToImage, RepeatImageBatch, SolidMask, PreviewImage, PreviewImage, CLIPTextEncode, MathExpression|pysssss, ImageToMask, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, LoadImage, LoadImage, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "lcm", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 Vace首尾帧_1950473543098290177.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950473543098290177.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `ImageBatch`
- `ImageBatch`
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `UnetLoaderGGUF` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `WanVaceToVideo`
- `KSamplerAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `MaskToImage`
- `ImageBatch`
- `ImageBatch`
- `JWInteger`
- `SolidMask`
- `MaskToImage`
- `RepeatImageBatch`
- `SolidMask`
- `PreviewImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `MathExpression|pysssss`
- `ImageToMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `VAELoader`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `lcm`
- `denoise` = `simple`

## 知识

覆盖率 **95%**（37/39）

**有卡**：`ImageBatch`、`UnetLoaderGGUF`、`CLIPTextEncode`、`CLIPLoader`、`KSamplerAdvanced`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`WanVaceToVideo`、`LayerUtility: PurgeVRAM`、`TrimVideoLatent`、`VAEDecode`、`ImageFromBatch+`、`VHS_VideoCombine`、`MaskToImage`、`JWInteger`、`SolidMask`、`RepeatImageBatch`、`MathExpression|pysssss`、`ImageToMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageResizeKJv2`、`LoadImage`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、KSamplerAdvanced
