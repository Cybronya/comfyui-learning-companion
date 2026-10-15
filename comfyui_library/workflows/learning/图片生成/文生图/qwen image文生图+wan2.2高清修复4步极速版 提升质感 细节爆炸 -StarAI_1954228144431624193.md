---
key: 图片生成/文生图/qwen image文生图+wan2.2高清修复4步极速版 提升质感 细节爆炸 -StarAI_1954228144431624193.json
name: qwen image文生图+wan2.2高清修复4步极速版 提升质感 细节爆炸 -StarAI_1954228144431624193
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image文生图+wan2.2高清修复4步极速版 提升质感 细节爆炸 -StarAI_1954228144431624193.json
hash: 0a3c4381ca24ca37
coverage: 0.772152
learned_at: 2026-10-10 20:59:24
nodes: [easy textSwitch, easy int, easy int, EmptySD3LatentImage, VAELoader, CLIPLoader, PathchSageAttentionKJ, SaveImage, SaveImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, VAEDecode, CR Text Concatenate, RH_Prompter, RHHiddenNodes, CLIPTextEncode, CLIPTextEncode, Textbox, easy showAnything, Note, RH_Captioner, CLIPLoader, Textbox, CLIPLoader, ModelSamplingAuraFlow, LatentUpscaleBy, ImpactSwitch, TTP_Tile_image_size, TTP_Image_Tile_Batch, easy imageBatchToImageList, VAEEncode, VAELoader, UNETLoader, LoraLoaderModelOnly, ModelSamplingAuraFlow, KSampler, KSampler, LoraLoaderModelOnly, UNETLoader, ClownsharKSampler_Beta, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixels, UpscaleModelLoader, ImageUpscaleWithModel, TTP_Image_Assy, VAEDecodeTiled, ImageListToBatch+, SaveImage, ImageScaleToTotalPixels, UpscaleModelLoader, easy imageBatchToImageList, VAELoader, CLIPTextEncode, PathchSageAttentionKJ, LoadImage, ImageUpscaleWithModel, VAEEncode, KSampler, VAEDecodeTiled, ImageListToBatch+, TTP_Image_Tile_Batch, TTP_Tile_image_size, ImageScaleToTotalPixels, SaveImage, Image Comparer (rgthree), TTP_Image_Assy, Image Comparer (rgthree), Text, ShowText, CLIPTextEncode, VAEDecode, Note Plus (mtb), Fast Groups Bypasser (rgthree), MarkdownNote, easy int]
patterns: [image_to_image]
missing: [CR Text Concatenate, ImageListToBatch+, ImageListToBatch+, LayerUtility: ImageScaleByAspectRatio V2, Note Plus (mtb), easy imageBatchToImageList, easy imageBatchToImageList, easy int, easy int, easy int, easy textSwitch]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "simple", "seed": 55735268734307, "steps": 4}
discoveries: [次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `ImageListToBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageListToBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen image文生图+wan2.2高清修复4步极速版 提升质感 细节爆炸 -StarAI_1954228144431624193.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image文生图+wan2.2高清修复4步极速版 提升质感 细节爆炸 -StarAI_1954228144431624193.json`

## 结构

**节点**（79 个）：
- `easy textSwitch`
- `easy int`
- `easy int`
- `EmptySD3LatentImage`
- `VAELoader`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `SaveImage`
- `SaveImage`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `VAEDecode`
- `CR Text Concatenate`
- `RH_Prompter`
- `RHHiddenNodes`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `Textbox`
- `easy showAnything`
- `Note`
- `RH_Captioner`
- `CLIPLoader`
- `Textbox`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `LatentUpscaleBy`
- `ImpactSwitch`
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `VAEEncode`
- `VAELoader`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `KSampler`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `ClownsharKSampler_Beta`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixels`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `TTP_Image_Assy`
- `VAEDecodeTiled`
- `ImageListToBatch+`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `UpscaleModelLoader`
- `easy imageBatchToImageList`
- `VAELoader`
- `CLIPTextEncode`
- `PathchSageAttentionKJ`
- `LoadImage`
- `ImageUpscaleWithModel`
- `VAEEncode`
- `KSampler`
- `VAEDecodeTiled`
- `ImageListToBatch+`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `Image Comparer (rgthree)`
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `Text`
- `ShowText`
- `CLIPTextEncode`
- `VAEDecode`
- `Note Plus (mtb)`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `easy int`

**识别到的模式**：image_to_image

## 关键参数

- `cfg` = `1`
- `denoise` = `0.30000000000000004`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `55735268734307`
- `steps` = `4`

## 知识

覆盖率 **77%**（61/79）

**有卡**：`easy textSwitch`、`easy int`、`EmptySD3LatentImage`、`VAELoader`、`CLIPLoader`、`PathchSageAttentionKJ`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEDecode`、`CR Text Concatenate`、`RH_Prompter`、`RHHiddenNodes`、`Textbox`、`easy showAnything`、`Note`、`RH_Captioner`、`ModelSamplingAuraFlow`、`LatentUpscaleBy`、`ImpactSwitch`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`VAEEncode`、`KSampler`、`ClownsharKSampler_Beta`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleToTotalPixels`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`TTP_Image_Assy`、`VAEDecodeTiled`、`ImageListToBatch+`、`LoadImage`

**缺卡**（11）：`CR Text Concatenate`、`ImageListToBatch+`、`ImageListToBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`Note Plus (mtb)`、`easy imageBatchToImageList`、`easy imageBatchToImageList`、`easy int`、`easy int`、`easy int`、`easy textSwitch`

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageListToBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageListToBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy textSwitch` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
