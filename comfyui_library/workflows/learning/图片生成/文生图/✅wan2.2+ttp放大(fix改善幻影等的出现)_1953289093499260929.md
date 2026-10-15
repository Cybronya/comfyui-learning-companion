---
key: 图片生成/文生图/✅wan2.2+ttp放大(fix改善幻影等的出现)_1953289093499260929.json
name: ✅wan2.2+ttp放大(fix改善幻影等的出现)_1953289093499260929
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/✅wan2.2+ttp放大(fix改善幻影等的出现)_1953289093499260929.json
hash: c2e55e254c428ec2
coverage: 0.731481
learned_at: 2026-10-15 22:28:00
nodes: [SetNode, SetNode, CLIPTextEncode, GetNode, GetNode, VAEDecodeTiled, easy imageListToImageBatch, TTP_CoordinateSplitter, SetNode, easy imageBatchToImageList, CLIPTextEncode, ImageUpscaleWithModel, ImageResizeKJ, TTP_Image_Tile_Batch, TTP_Image_Assy, ImageSmartSharpen+, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageScaleToTotalPixels, easy cleanGpuUsed, CLIPLoader, SetNode, SetNode, VAELoader, SaveImage, NAGGuider, SamplerCustomAdvanced, GetNode, GetNode, GetNode, VAEEncode, RandomNoise, KSamplerSelect, ShowText|pysssss, ShowText|pysssss, CR Text Concatenate, CR Text, SetNode, Manual XY Entry Info, Manual XY Entry Info, Manual XY Entry Info, SetNode, UpscaleModelLoader, SetNode, PreviewImage, TTP_condtobatch, TTP_condsetarea_merge, GetNode, GetNode, ConditioningAverage, GetNode, SetNode, CR Text Concatenate, LayerUtility: LoadJoyCaptionBeta1Model, GetNode, LayerUtility: JoyCaptionBeta1, Image Comparer (rgthree), UNETLoader, LayerUtility: JoyCaptionBeta1, CR Text, PathchSageAttentionKJ, ModelSamplingSD3, BasicScheduler, LoraLoaderModelOnly, PathchSageAttentionKJ, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, CLIPLoader, ModelSamplingSD3, VAEDecode, SaveImage, SaveImage, UNETLoader, VAEEncode, ImageResizeAndCropNode, CLIPTextEncode, KSampler, Text Concatenate, KSampler, EmptyLatentImage, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, JWInteger, JWInteger, Bjornulf_TextToStringAndSeed, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1, PMRF, easy imageChooser, LoadImage, Text Multiline, LazySwitch1way, TTP_Tile_image_size, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: JoyCaptionBeta1ExtraOptions, LoadImage, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "heun", "scheduler": "beta", "seed": 497163970725457, "steps": 10, "width": 512}
---

# 图片生成/文生图/✅wan2.2+ttp放大(fix改善幻影等的出现)_1953289093499260929.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/✅wan2.2+ttp放大(fix改善幻影等的出现)_1953289093499260929.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（108 个）：
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `easy imageListToImageBatch`
- `TTP_CoordinateSplitter`
- `SetNode`
- `easy imageBatchToImageList`
- `CLIPTextEncode` ★核心
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
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
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
- `UNETLoader` ★核心
- `LayerUtility: JoyCaptionBeta1`
- `CR Text`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `ImageResizeAndCropNode`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `Text Concatenate`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `497163970725457`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（79/108）

**有卡**：`CLIPTextEncode`、`VAEDecodeTiled`、`easy imageListToImageBatch`、`TTP_CoordinateSplitter`、`easy imageBatchToImageList`、`ImageUpscaleWithModel`、`ImageResizeKJ`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`ImageSmartSharpen+`、`ImageScaleToTotalPixels`、`easy cleanGpuUsed`、`CLIPLoader`、`VAELoader`、`SaveImage`、`NAGGuider`、`SamplerCustomAdvanced`、`VAEEncode`、`RandomNoise`、`KSamplerSelect`、`CR Text Concatenate`、`CR Text`、`Manual XY Entry Info`、`UpscaleModelLoader`、`TTP_condtobatch`、`TTP_condsetarea_merge`、`ConditioningAverage`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`BasicScheduler`、`LoraLoaderModelOnly`、`VAEDecode`、`ImageResizeAndCropNode`、`KSampler`、`Text Concatenate`、`EmptyLatentImage`、`JWInteger`、`Bjornulf_TextToStringAndSeed`、`PMRF`、`easy imageChooser`、`LoadImage`、`Text Multiline`、`LazySwitch1way`、`TTP_Tile_image_size`、`LayerUtility: JoyCaptionBeta1ExtraOptions`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage
