---
key: 图片生成/文生图/✅wan2.2+ttp放大(fix改善幻影等的出现)_1953289093499260929.json
name: ✅wan2.2+ttp放大(fix改善幻影等的出现)_1953289093499260929
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/✅wan2.2+ttp放大(fix改善幻影等的出现)_1953289093499260929.json
hash: c2e55e254c428ec2
coverage: 0.537037
learned_at: 2026-10-10 20:59:28
nodes: [SetNode, SetNode, CLIPTextEncode, GetNode, GetNode, VAEDecodeTiled, easy imageListToImageBatch, TTP_CoordinateSplitter, SetNode, easy imageBatchToImageList, CLIPTextEncode, ImageUpscaleWithModel, ImageResizeKJ, TTP_Image_Tile_Batch, TTP_Image_Assy, ImageSmartSharpen+, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageScaleToTotalPixels, easy cleanGpuUsed, CLIPLoader, SetNode, SetNode, VAELoader, SaveImage, NAGGuider, SamplerCustomAdvanced, GetNode, GetNode, GetNode, VAEEncode, RandomNoise, KSamplerSelect, ShowText|pysssss, ShowText|pysssss, CR Text Concatenate, CR Text, SetNode, Manual XY Entry Info, Manual XY Entry Info, Manual XY Entry Info, SetNode, UpscaleModelLoader, SetNode, PreviewImage, TTP_condtobatch, TTP_condsetarea_merge, GetNode, GetNode, ConditioningAverage, GetNode, SetNode, CR Text Concatenate, LayerUtility: LoadJoyCaptionBeta1Model, GetNode, LayerUtility: JoyCaptionBeta1, Image Comparer (rgthree), UNETLoader, LayerUtility: JoyCaptionBeta1, CR Text, PathchSageAttentionKJ, ModelSamplingSD3, BasicScheduler, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, CLIPLoader, ModelSamplingSD3, VAEDecode, SaveImage, SaveImage, UNETLoader, VAEEncode, ImageResizeAndCropNode, CLIPTextEncode, KSampler, Text Concatenate, KSampler, EmptyLatentImage, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, JWInteger, JWInteger, Bjornulf_TextToStringAndSeed, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1, PMRF, easy imageChooser, LoadImage, Text Multiline, LazySwitch1way, TTP_Tile_image_size, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: JoyCaptionBeta1ExtraOptions, LoadImage, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode]
patterns: [text_to_image, image_to_image]
missing: [CR Text, CR Text, CR Text Concatenate, CR Text Concatenate, ImageSmartSharpen+, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: LoadJoyCaptionBeta1Model, Manual XY Entry Info, Manual XY Entry Info, Manual XY Entry Info, Text Concatenate, Text Multiline, easy cleanGpuUsed, easy imageBatchToImageList, easy imageChooser, easy imageListToImageBatch]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "heun", "scheduler": "beta", "seed": 497163970725457, "steps": 10, "width": 512}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `ImageSmartSharpen+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识, 次要节点 `Manual XY Entry Info` 知识库中没有该节点类型的任何知识, 次要节点 `Manual XY Entry Info` 知识库中没有该节点类型的任何知识, 次要节点 `Manual XY Entry Info` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageBatchToImageList` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageChooser` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/✅wan2.2+ttp放大(fix改善幻影等的出现)_1953289093499260929.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/✅wan2.2+ttp放大(fix改善幻影等的出现)_1953289093499260929.json`

## 结构

**节点**（108 个）：
- `SetNode`
- `SetNode`
- `CLIPTextEncode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled`
- `easy imageListToImageBatch`
- `TTP_CoordinateSplitter`
- `SetNode`
- `easy imageBatchToImageList`
- `CLIPTextEncode`
- `ImageUpscaleWithModel`
- `ImageResizeKJ`
- `TTP_Image_Tile_Batch`
- `TTP_Image_Assy`
- `ImageSmartSharpen+`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SaveImage`
- `NAGGuider`
- `SamplerCustomAdvanced`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncode`
- `RandomNoise`
- `KSamplerSelect`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `CR Text Concatenate`
- `CR Text`
- `SetNode`
- `Manual XY Entry Info`
- `Manual XY Entry Info`
- `Manual XY Entry Info`
- `SetNode`
- `UpscaleModelLoader`
- `SetNode`
- `PreviewImage`
- `TTP_condtobatch`
- `TTP_condsetarea_merge`
- `GetNode`
- `GetNode`
- `ConditioningAverage`
- `GetNode`
- `SetNode`
- `CR Text Concatenate`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `GetNode`
- `LayerUtility: JoyCaptionBeta1`
- `Image Comparer (rgthree)`
- `UNETLoader`
- `LayerUtility: JoyCaptionBeta1`
- `CR Text`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `BasicScheduler`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader`
- `CLIPLoader`
- `ModelSamplingSD3`
- `VAEDecode`
- `SaveImage`
- `SaveImage`
- `UNETLoader`
- `VAEEncode`
- `ImageResizeAndCropNode`
- `CLIPTextEncode`
- `KSampler`
- `Text Concatenate`
- `KSampler`
- `EmptyLatentImage`
- `VAELoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `JWInteger`
- `JWInteger`
- `Bjornulf_TextToStringAndSeed`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1`
- `PMRF`
- `easy imageChooser`
- `LoadImage`
- `Text Multiline`
- `LazySwitch1way`
- `TTP_Tile_image_size`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LoadImage`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `CLIPTextEncode`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `512`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `seed` = `497163970725457`
- `steps` = `10`
- `width` = `512`

## 知识

覆盖率 **54%**（58/108）

**有卡**：`SetNode`、`CLIPTextEncode`、`GetNode`、`VAEDecodeTiled`、`easy imageListToImageBatch`、`TTP_CoordinateSplitter`、`easy imageBatchToImageList`、`ImageUpscaleWithModel`、`ImageResizeKJ`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`ImageSmartSharpen+`、`ImageScaleToTotalPixels`、`easy cleanGpuUsed`、`CLIPLoader`、`VAELoader`、`SaveImage`、`NAGGuider`、`SamplerCustomAdvanced`、`VAEEncode`、`RandomNoise`、`KSamplerSelect`、`ShowText|pysssss`、`CR Text Concatenate`、`CR Text`、`Manual XY Entry Info`、`UpscaleModelLoader`、`PreviewImage`、`TTP_condtobatch`、`TTP_condsetarea_merge`、`ConditioningAverage`

**缺卡**（21）：`CR Text`、`CR Text`、`CR Text Concatenate`、`CR Text Concatenate`、`ImageSmartSharpen+`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: LoadJoyCaptionBeta1Model`、`Manual XY Entry Info`、`Manual XY Entry Info`、`Manual XY Entry Info`、`Text Concatenate`、`Text Multiline`、`easy cleanGpuUsed`、`easy imageBatchToImageList`、`easy imageChooser`、`easy imageListToImageBatch`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
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
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
