---
key: 图片生成/文生图/✅Qwen-imag+wan2.2ttp放大(fix改善幻影等的出现)_1954937738723147777.json
name: ✅Qwen-imag+wan2.2ttp放大(fix改善幻影等的出现)_1954937738723147777
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/✅Qwen-imag+wan2.2ttp放大(fix改善幻影等的出现)_1954937738723147777.json
hash: 17e1d1d55ddb2ac8
coverage: 0.654206
learned_at: 2026-10-15 22:28:00
nodes: [SetNode, SetNode, GetNode, CLIPTextEncode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, VAEEncode, SetNode, TTP_condsetarea_merge, UNETLoader, CR Text, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, Manual XY Entry Info, CLIPTextEncode, VAELoader, LayerUtility: JoyCaptionBeta1, GetNode, LayerUtility: JoyCaptionBeta1, SetNode, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, GetNode, ShowText|pysssss, CR Text Concatenate, CR Text Concatenate, SetNode, ShowText|pysssss, GetNode, GetNode, GetNode, UpscaleModelLoader, Manual XY Entry Info, TTP_Tile_image_size, easy imageBatchToImageList, ImageSmartSharpen+, TTP_Image_Tile_Batch, TTP_CoordinateSplitter, TTP_condtobatch, GetNode, TTP_Image_Assy, easy imageListToImageBatch, Manual XY Entry Info, BasicScheduler, GetNode, KSamplerSelect, RandomNoise, NAGGuider, GetNode, ConditioningAverage, SetNode, easy imageChooser, ImageResizeAndCropNode, ImageUpscaleWithModel, ImageScaleBy, ImageResizeKJ, PreviewImage, easy cleanGpuUsed, Fast Groups Bypasser (rgthree), SamplerCustomAdvanced, VAEDecodeTiled, SetNode, GetNode, GetNode, Fast Groups Muter (rgthree), LazySwitch1way, easy imageChooser, LoadImage, SaveImage, Image Comparer (rgthree), LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions, ImageResizeAndCropNode, PrimitiveStringMultiline, Text Concatenate, LayerUtility: JoyCaptionBeta1, CLIPTextEncode, VAELoader, CLIPTextEncode, SetNode, GetNode, PrimitiveInt, PrimitiveInt, LoadImage, KSampler, VAEDecode, SetNode, CLIPTextEncode, CLIPLoader, PMRF, EmptySD3LatentImage, ModelSamplingAuraFlow, LoraLoader, LoraLoader, UNETLoader, CLIPLoader, LoraLoader, Text Multiline, easy imageChooser]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Qwen-Image_EmotionalPhotography_v1.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 697799697150739, "steps": 8, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/✅Qwen-imag+wan2.2ttp放大(fix改善幻影等的出现)_1954937738723147777.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/✅Qwen-imag+wan2.2ttp放大(fix改善幻影等的出现)_1954937738723147777.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `SetNode`
- `TTP_condsetarea_merge`
- `UNETLoader` ★核心
- `CR Text`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `SetNode`
- `Manual XY Entry Info`
- `CLIPTextEncode` ★核心
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
- `KSamplerSelect` ★核心
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
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeTiled` ★核心
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
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `PMRF`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoader` ★核心
- `Text Multiline`
- `easy imageChooser`

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `697799697150739`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `Qwen-Image_EmotionalPhotography_v1.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`

## 知识

覆盖率 **65%**（70/107）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`TTP_condsetarea_merge`、`UNETLoader`、`CR Text`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`Manual XY Entry Info`、`VAELoader`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: LoadJoyCaptionBeta1Model`、`CR Text Concatenate`、`UpscaleModelLoader`、`TTP_Tile_image_size`、`easy imageBatchToImageList`、`ImageSmartSharpen+`、`TTP_Image_Tile_Batch`、`TTP_CoordinateSplitter`、`TTP_condtobatch`、`TTP_Image_Assy`、`easy imageListToImageBatch`、`BasicScheduler`、`KSamplerSelect`、`RandomNoise`、`NAGGuider`、`ConditioningAverage`、`easy imageChooser`、`ImageResizeAndCropNode`、`ImageUpscaleWithModel`、`ImageScaleBy`、`ImageResizeKJ`、`easy cleanGpuUsed`、`SamplerCustomAdvanced`、`VAEDecodeTiled`、`LazySwitch1way`、`LoadImage`、`SaveImage`、`Text Concatenate`、`KSampler`、`VAEDecode`、`CLIPLoader`、`PMRF`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`LoraLoader`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
