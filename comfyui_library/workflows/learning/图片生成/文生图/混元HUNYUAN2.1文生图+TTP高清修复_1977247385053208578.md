---
key: 图片生成/文生图/混元HUNYUAN2.1文生图+TTP高清修复_1977247385053208578.json
name: 混元HUNYUAN2.1文生图+TTP高清修复_1977247385053208578.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/混元HUNYUAN2.1文生图+TTP高清修复_1977247385053208578.json
hash: 1775405b74b87242
coverage: 0.782609
learned_at: 2026-10-09 19:50:54
nodes: [UNETLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, VAEEncode, HunyuanRefinerLatent, LayerUtility: PurgeVRAM V2, VAEDecode, KSampler, Note, ImageScaleBy, UpscaleModelLoader, SaveImage, Note, UNETLoader, CLIPTextEncode, CLIPTextEncode, DualCLIPLoader, KSampler, VAEDecode, ImageCASharpening+, VAELoader, EmptyHunyuanImageLatent, FluxResolutionNode, SaveImage, Anything Everywhere3, UNETLoader, DualCLIPLoader, VAELoader, LoraLoaderModelOnly, CLIPTextEncode, ConditioningZeroOut, KSampler, VAEDecodeTiled, easy imageListToImageBatch, PreviewImage, Note, TTP_Image_Tile_Batch, TTP_Tile_image_size, ImageUpscaleWithModel, VAEEncodeTiled, easy imageBatchToImageList, TTP_Image_Assy, SaveImage, Image Comparer (rgthree), RH_Translator]
patterns: []
missing: [ImageCASharpening+, LayerUtility: PurgeVRAM V2, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "karras", "seed": 842656240405713, "steps": 2}
discoveries: [次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/混元HUNYUAN2.1文生图+TTP高清修复_1977247385053208578.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1977247385053208578.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `HunyuanRefinerLatent`
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Note`
- `ImageScaleBy`
- `UpscaleModelLoader`
- `SaveImage`
- `Note`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageCASharpening+`
- `VAELoader`
- `EmptyHunyuanImageLatent`
- `FluxResolutionNode`
- `SaveImage`
- `Anything Everywhere3`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `easy imageListToImageBatch`
- `PreviewImage`
- `Note`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `ImageUpscaleWithModel`
- `VAEEncodeTiled` ★核心
- `easy imageBatchToImageList`
- `TTP_Image_Assy`
- `SaveImage`
- `Image Comparer (rgthree)`
- `RH_Translator`

## 关键参数

- `seed` = `842656240405713`
- `steps` = `2`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `karras`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`VAEEncode`、`HunyuanRefinerLatent`、`VAEDecode`、`KSampler`、`ImageScaleBy`、`UpscaleModelLoader`、`SaveImage`、`DualCLIPLoader`、`EmptyHunyuanImageLatent`、`FluxResolutionNode`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`VAEDecodeTiled`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`ImageUpscaleWithModel`、`VAEEncodeTiled`、`TTP_Image_Assy`、`RH_Translator`

**缺卡**（4）：`ImageCASharpening+`、`LayerUtility: PurgeVRAM V2`、`easy imageBatchToImageList`、`easy imageListToImageBatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、VAEDecodeTiled

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ImageCASharpening+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
