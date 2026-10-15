---
key: 图片生成/文生图/✅Qwen-imag+wan2.2ttp放大(fix改善幻影等的出现)_1954937738723147777.json
name: ✅Qwen-imag+wan2.2ttp放大(fix改善幻影等的出现)_1954937738723147777
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/✅Qwen-imag+wan2.2ttp放大(fix改善幻影等的出现)_1954937738723147777.json
hash: 17e1d1d55ddb2ac8
coverage: 0.448598
learned_at: 2026-10-10 20:59:28
nodes: [SetNode, SetNode, GetNode, CLIPTextEncode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, VAEEncode, SetNode, TTP_condsetarea_merge, UNETLoader, CR Text, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, Manual XY Entry Info, CLIPTextEncode, VAELoader, LayerUtility: JoyCaptionBeta1, GetNode, LayerUtility: JoyCaptionBeta1, SetNode, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, GetNode, ShowText|pysssss, CR Text Concatenate, CR Text Concatenate, SetNode, ShowText|pysssss, GetNode, GetNode, GetNode, UpscaleModelLoader, Manual XY Entry Info, TTP_Tile_image_size, easy imageBatchToImageList, ImageSmartSharpen+, TTP_Image_Tile_Batch, TTP_CoordinateSplitter, TTP_condtobatch, GetNode, TTP_Image_Assy, easy imageListToImageBatch, Manual XY Entry Info, BasicScheduler, GetNode, KSamplerSelect, RandomNoise, NAGGuider, GetNode, ConditioningAverage, SetNode, easy imageChooser, ImageResizeAndCropNode, ImageUpscaleWithModel, ImageScaleBy, ImageResizeKJ, PreviewImage, easy cleanGpuUsed, Fast Groups Bypasser (rgthree), SamplerCustomAdvanced, VAEDecodeTiled, SetNode, GetNode, GetNode, Fast Groups Muter (rgthree), LazySwitch1way, easy imageChooser, LoadImage, SaveImage, Image Comparer (rgthree), LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions, ImageResizeAndCropNode, PrimitiveStringMultiline, Text Concatenate, LayerUtility: JoyCaptionBeta1, CLIPTextEncode, VAELoader, CLIPTextEncode, SetNode, GetNode, PrimitiveInt, PrimitiveInt, LoadImage, KSampler, VAEDecode, SetNode, CLIPTextEncode, CLIPLoader, PMRF, EmptySD3LatentImage, ModelSamplingAuraFlow, LoraLoader, LoraLoader, UNETLoader, CLIPLoader, LoraLoader, Text Multiline, easy imageChooser]
patterns: [image_to_image, lora]
missing: [CR Text, CR Text Concatenate, CR Text Concatenate, ImageSmartSharpen+, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: LoadJoyCaptionBeta1Model, Manual XY Entry Info, Manual XY Entry Info, Manual XY Entry Info, Text Concatenate, Text Multiline, easy cleanGpuUsed, easy imageBatchToImageList, easy imageChooser, easy imageChooser, easy imageChooser, easy imageListToImageBatch]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Qwen-Image_EmotionalPhotography_v1.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 697799697150739, "steps": 8, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识, 次要节点 `Manual XY Entry Info` 知识库中没有该节点类型的任何知识, 次要节点 `Manual XY Entry Info` 知识库中没有该节点类型的任何知识, 次要节点 `Manual XY Entry Info` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/✅Qwen-imag+wan2.2ttp放大(fix改善幻影等的出现)_1954937738723147777.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/✅Qwen-imag+wan2.2ttp放大(fix改善幻影等的出现)_1954937738723147777.json`

## 结构

**节点**（107 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEEncode`
- `SetNode`
- `TTP_condsetarea_merge`
- `UNETLoader`
- `CR Text`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `SetNode`
- `Manual XY Entry Info`
- `CLIPTextEncode`
- `VAELoader`
- `LayerUtility: JoyCaptionBeta1`
- `GetNode`
- `LayerUtility: JoyCaptionBeta1`
- `SetNode`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `GetNode`
- `ShowText|pysssss`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `SetNode`
- `ShowText|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `UpscaleModelLoader`
- `Manual XY Entry Info`
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`
- `ImageSmartSharpen+`
- `TTP_Image_Tile_Batch`
- `TTP_CoordinateSplitter`
- `TTP_condtobatch`
- `GetNode`
- `TTP_Image_Assy`
- `easy imageListToImageBatch`
- `Manual XY Entry Info`
- `BasicScheduler`
- `GetNode`
- `KSamplerSelect`
- `RandomNoise`
- `NAGGuider`
- `GetNode`
- `ConditioningAverage`
- `SetNode`
- `easy imageChooser`
- `ImageResizeAndCropNode`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `ImageResizeKJ`
- `PreviewImage`
- `easy cleanGpuUsed`
- `Fast Groups Bypasser (rgthree)`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `SetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Muter (rgthree)`
- `LazySwitch1way`
- `easy imageChooser`
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `ImageResizeAndCropNode`
- `PrimitiveStringMultiline`
- `Text Concatenate`
- `LayerUtility: JoyCaptionBeta1`
- `CLIPTextEncode`
- `VAELoader`
- `CLIPTextEncode`
- `SetNode`
- `GetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `KSampler`
- `VAEDecode`
- `SetNode`
- `CLIPTextEncode`
- `CLIPLoader`
- `PMRF`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `LoraLoader`
- `LoraLoader`
- `UNETLoader`
- `CLIPLoader`
- `LoraLoader`
- `Text Multiline`
- `easy imageChooser`

**识别到的模式**：image_to_image、lora

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `lora_name` = `Qwen-Image_EmotionalPhotography_v1.safetensors`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `697799697150739`
- `steps` = `8`
- `strength_clip` = `1.0000000000000002`
- `strength_model` = `1.0000000000000002`

## 知识

覆盖率 **45%**（48/107）

**有卡**：`SetNode`、`GetNode`、`CLIPTextEncode`、`VAEEncode`、`TTP_condsetarea_merge`、`UNETLoader`、`CR Text`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`Manual XY Entry Info`、`VAELoader`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: LoadJoyCaptionBeta1Model`、`ShowText|pysssss`、`CR Text Concatenate`、`UpscaleModelLoader`、`TTP_Tile_image_size`、`easy imageBatchToImageList`、`ImageSmartSharpen+`、`TTP_Image_Tile_Batch`、`TTP_CoordinateSplitter`、`TTP_condtobatch`

**缺卡**（22）：`CR Text`、`CR Text Concatenate`、`CR Text Concatenate`、`ImageSmartSharpen+`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: LoadJoyCaptionBeta1Model`、`Manual XY Entry Info`、`Manual XY Entry Info`、`Manual XY Entry Info`、`Text Concatenate`、`Text Multiline`、`easy cleanGpuUsed`、`easy imageBatchToImageList`、`easy imageChooser`、`easy imageChooser`、`easy imageChooser`、`easy imageListToImageBatch`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
- 次要节点 `Manual XY Entry Info` 知识库中没有该节点类型的任何知识
- 次要节点 `Manual XY Entry Info` 知识库中没有该节点类型的任何知识
- 次要节点 `Manual XY Entry Info` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
