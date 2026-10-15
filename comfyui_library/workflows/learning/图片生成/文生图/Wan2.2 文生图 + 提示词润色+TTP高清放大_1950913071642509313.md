---
key: 图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1950913071642509313.json
name: Wan2.2 文生图 + 提示词润色+TTP高清放大_1950913071642509313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1950913071642509313.json
hash: 788704092bbd4b40
coverage: 0.84375
learned_at: 2026-10-15 22:27:35
nodes: [CLIPTextEncode, easy imageBatchToImageList, VAEEncode, CR Text Concatenate, CR Text, RH_Translator, ShowText|pysssss, RH_Prompter, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, VAELoader, CLIPTextEncode, KSamplerAdvanced, CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, CR Text, ImageUpscaleWithModel, LayerUtility: ImageScaleByAspectRatio V2, UpscaleModelLoader, ImageScaleBy, easy cleanGpuUsed, easy imageSize, easy cleanGpuUsed, easy imageSize, CLIPLoader, UNETLoader, VAELoader, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, TTP_Tile_image_size, TTP_Image_Tile_Batch, PreviewImage, PreviewImage, easy cleanGpuUsed, ImageListToImageBatch, KSampler, VAEDecode, easy cleanGpuUsed, easy int, easy cleanGpuUsed, VAEDecode, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), easy int, easy int, PrimitiveBoolean, easy ifElse, ShowText|pysssss, Note, PreviewImage, Note, TTP_Image_Assy, SaveImage, MathExpression|pysssss, Text Multiline]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "heun", "scheduler": "beta", "seed": 676961355349973, "steps": 10}
---

# 图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1950913071642509313.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1950913071642509313.json`

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
- `KSamplerAdvanced` ★核心
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
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `easy int`
- `easy int`
- `PrimitiveBoolean`
- `easy ifElse`
- `ShowText|pysssss`
- `Note`
- `PreviewImage`
- `Note`
- `TTP_Image_Assy`
- `SaveImage`
- `MathExpression|pysssss`
- `Text Multiline`

## 关键参数

- `seed` = `676961355349973`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **84%**（54/64）

**有卡**：`CLIPTextEncode`、`easy imageBatchToImageList`、`VAEEncode`、`CR Text Concatenate`、`CR Text`、`RH_Translator`、`RH_Prompter`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAELoader`、`KSamplerAdvanced`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`ImageUpscaleWithModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`UpscaleModelLoader`、`ImageScaleBy`、`easy cleanGpuUsed`、`easy imageSize`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImageListToImageBatch`、`KSampler`、`VAEDecode`、`easy int`、`PrimitiveBoolean`、`TTP_Image_Assy`、`SaveImage`、`MathExpression|pysssss`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced
