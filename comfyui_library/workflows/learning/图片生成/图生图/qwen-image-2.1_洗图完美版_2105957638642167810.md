---
key: 图片生成/图生图/qwen-image-2.1_洗图完美版_2105957638642167810.json
name: qwen-image-2.1_洗图完美版_2105957638642167810.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1_洗图完美版_2105957638642167810.json
hash: e0057a02c63a7e97
coverage: 0.540541
learned_at: 2026-10-09 22:09:17
nodes: [JoinStrings, easy showAnything, MarkdownNote, ConditioningZeroOut, SaveImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, ImageScaleBy, LayerUtility: PurgeVRAM, SeedVR2VideoUpscaler, LayerUtility: ImageReelComposit, ShowText|pysssss, Fast Groups Bypasser (rgthree), LayerUtility: ImageReel, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), LayerUtility: PurgeVRAM, SaveImage, MarkdownNote, LoraLoaderModelOnly, KSampler, VAELoader, UNETLoader, CLIPTextEncode, LayerUtility: PurgeVRAM, ImpactInt, CLIPLoader, MarkdownNote, TextInput_, Qwen3_VQA, LoadImage, VAEDecode, VAEEncode, PreviewImage, easy imageConcat, PreviewImage, PrimitiveNode]
patterns: [image_to_image]
missing: [LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, easy imageConcat]
parameters: {"cfg": 1, "denoise": 0.7000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 118035628489200, "steps": 40}
discoveries: [次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/qwen-image-2.1_洗图完美版_2105957638642167810.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2105957638642167810.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `JoinStrings`
- `easy showAnything`
- `MarkdownNote`
- `ConditioningZeroOut`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `ImageScaleBy`
- `LayerUtility: PurgeVRAM`
- `SeedVR2VideoUpscaler`
- `LayerUtility: ImageReelComposit`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `ImpactInt`
- `CLIPLoader`
- `MarkdownNote`
- `TextInput_`
- `Qwen3_VQA`
- `LoadImage`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `PreviewImage`
- `easy imageConcat`
- `PreviewImage`
- `PrimitiveNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `118035628489200`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.7000000000000002`

## 知识

覆盖率 **54%**（20/37）

**有卡**：`JoinStrings`、`ConditioningZeroOut`、`SaveImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`ImageScaleBy`、`SeedVR2VideoUpscaler`、`LoraLoaderModelOnly`、`KSampler`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`ImpactInt`、`CLIPLoader`、`TextInput_`、`Qwen3_VQA`、`LoadImage`、`VAEDecode`、`VAEEncode`

**缺卡**（7）：`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`easy imageConcat`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 学习发现

- 次要节点 `LayerUtility: ImageReel` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageReelComposit` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageConcat` 知识库中没有该节点类型的任何知识
