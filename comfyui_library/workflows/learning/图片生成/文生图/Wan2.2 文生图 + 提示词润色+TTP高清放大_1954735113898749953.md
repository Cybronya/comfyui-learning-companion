---
key: 图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1954735113898749953.json
name: Wan2.2 文生图 + 提示词润色+TTP高清放大_1954735113898749953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1954735113898749953.json
hash: 54eff95eb0e29478
coverage: 0.84375
learned_at: 2026-10-15 22:27:35
nodes: [CLIPTextEncode, easy imageBatchToImageList, VAEEncode, CR Text Concatenate, CR Text, RH_Translator, ShowText|pysssss, RH_Prompter, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, VAELoader, CLIPTextEncode, KSamplerAdvanced, CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, CR Text, ImageUpscaleWithModel, LayerUtility: ImageScaleByAspectRatio V2, UpscaleModelLoader, ImageScaleBy, easy cleanGpuUsed, easy imageSize, easy cleanGpuUsed, easy imageSize, CLIPLoader, UNETLoader, VAELoader, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, TTP_Tile_image_size, TTP_Image_Tile_Batch, PreviewImage, PreviewImage, easy cleanGpuUsed, ImageListToImageBatch, KSampler, VAEDecode, easy cleanGpuUsed, easy int, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), Text Multiline, easy int, easy int, easy ifElse, ShowText|pysssss, Note, PreviewImage, Note, TTP_Image_Assy, SaveImage, MathExpression|pysssss, PrimitiveBoolean, KSamplerAdvanced, easy cleanGpuUsed, VAEDecode]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1954735113898749953.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1954735113898749953.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `CLIPTextEncode` ★核心
- `easy imageBatchToImageList`
- `VAEEncode` ★核心
- `CR Text Concatenate`
- `CR Text`
- `RH_Translator`
- `ShowText|pysssss`
- `RH_Prompter`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `CR Text`
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UpscaleModelLoader`
- `ImageScaleBy`
- `easy cleanGpuUsed`
- `easy imageSize`
- `easy cleanGpuUsed`
- `easy imageSize`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `PreviewImage`
- `PreviewImage`
- `easy cleanGpuUsed`
- `ImageListToImageBatch`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `easy int`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `Text Multiline`
- `easy int`
- `easy int`
- `easy ifElse`
- `ShowText|pysssss`
- `Note`
- `PreviewImage`
- `Note`
- `TTP_Image_Assy`
- `SaveImage`
- `MathExpression|pysssss`
- `PrimitiveBoolean`
- `KSamplerAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（54/64）

**有卡**：`CLIPTextEncode`、`easy imageBatchToImageList`、`VAEEncode`、`CR Text Concatenate`、`CR Text`、`RH_Translator`、`RH_Prompter`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAELoader`、`KSamplerAdvanced`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`ImageUpscaleWithModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`UpscaleModelLoader`、`ImageScaleBy`、`easy cleanGpuUsed`、`easy imageSize`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImageListToImageBatch`、`KSampler`、`VAEDecode`、`easy int`、`Text Multiline`、`TTP_Image_Assy`、`SaveImage`、`MathExpression|pysssss`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced
