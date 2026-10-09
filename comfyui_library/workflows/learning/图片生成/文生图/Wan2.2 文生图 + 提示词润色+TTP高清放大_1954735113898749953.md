---
key: 图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1954735113898749953.json
name: Wan2.2 文生图 + 提示词润色+TTP高清放大_1954735113898749953.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1954735113898749953.json
hash: 54eff95eb0e29478
coverage: 0.578125
learned_at: 2026-10-07 23:18:23
nodes: [CLIPTextEncode, easy imageBatchToImageList, VAEEncode, CR Text Concatenate, CR Text, RH_Translator, ShowText|pysssss, RH_Prompter, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, VAELoader, CLIPTextEncode, KSamplerAdvanced, CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, CR Text, ImageUpscaleWithModel, LayerUtility: ImageScaleByAspectRatio V2, UpscaleModelLoader, ImageScaleBy, easy cleanGpuUsed, easy imageSize, easy cleanGpuUsed, easy imageSize, CLIPLoader, UNETLoader, VAELoader, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, TTP_Tile_image_size, TTP_Image_Tile_Batch, PreviewImage, PreviewImage, easy cleanGpuUsed, ImageListToImageBatch, KSampler, VAEDecode, easy cleanGpuUsed, easy int, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), Text Multiline, easy int, easy int, easy ifElse, ShowText|pysssss, Note, PreviewImage, Note, TTP_Image_Assy, SaveImage, MathExpression|pysssss, PrimitiveBoolean, KSamplerAdvanced, easy cleanGpuUsed, VAEDecode]
patterns: []
missing: [CR Text, CR Text, CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, Text Multiline, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy imageBatchToImageList, easy int, easy int, easy int, easy imageSize, easy imageSize]
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 3.5, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Wan2.2 文生图 + 提示词润色+TTP高清放大_1954735113898749953.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1954735113898749953.json`

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

覆盖率 **58%**（37/64）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`RH_Translator`、`RH_Prompter`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAELoader`、`KSamplerAdvanced`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`ImageScaleBy`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`ImageListToImageBatch`、`KSampler`、`VAEDecode`、`TTP_Image_Assy`、`SaveImage`、`PrimitiveBoolean`

**缺卡**（17）：`CR Text`、`CR Text`、`CR Text Concatenate`、`LayerUtility: ImageScaleByAspectRatio V2`、`MathExpression|pysssss`、`Text Multiline`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy imageBatchToImageList`、`easy int`、`easy int`、`easy int`、`easy imageSize`、`easy imageSize`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSize` 仅有 Resolution 的通用知识，没有该节点自己的说明
