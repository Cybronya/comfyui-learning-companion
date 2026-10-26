---
key: 图片生成/图生图/“一张图能变多少姿势？”不！Qwen2.1出的一整套人像写真！小红书宫格图组图故事板短剧分镜随心发！_2114635915229483009.json
name: “一张图能变多少姿势？”不！Qwen2.1出的一整套人像写真！小红书宫格图组图故事板短剧分镜随心发！_2114635915229483009
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/“一张图能变多少姿势？”不！Qwen2.1出的一整套人像写真！小红书宫格图组图故事板短剧分镜随心发！_2114635915229483009.json
hash: efd1d482a4c49863
coverage: 0.873418
learned_at: 2026-10-26 22:04:25
nodes: [ComfySwitchNode, CLIPLoader, ComfySwitchNode, HfImageToRGB, LoraLoaderModelOnly, llama_cpp_parameters, LoraLoaderModelOnly, TextEncodeQwenImage21, LoraLoaderModelOnly, EmptyLatentImage, QwenImage21Cache, SaveImage, CR Text Concatenate, LoraLoaderModelOnly, PrimitiveInt, PrimitiveInt, llama_cpp_model_loader, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, VAELoader, VAEDecode, LayerColor: Brightness & Contrast, TextEncodeQwenImage21, easy imageSwitch, llama_cpp_instruct_adv, easy showAnything, easy promptLine, DapaoBatchImageGrid, LayerUtility: PurgeVRAM V2, 长边短边, easy compare, PrimitiveInt, CLIPLoader, VAELoader, UNETLoader, VAELoader, LoraLoaderModelOnly, PathchSageAttentionKJ, MathExpression|pysssss, VAEEncodeTiled, KSampler, VAEDecodeTiled, TTP_Tile_image_size, ShunjingAIShade, TTP_Image_Tile_Batch, easy imageBatchToImageList, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, ReferenceLatent, ConditioningZeroOut, KSampler, ShunjingAIShade, easy imageListToImageBatch, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2Preprocess, VAEDecode, SeedVR2Conditioning, LayerUtility: ImageScaleRestore V2, UNETLoader, LoadImage, TTP_Image_Assy, 图像缩放V2_孤海, RHHiddenNodes, PrimitiveStringMultiline, RHHiddenNodes, RHHiddenNodes, LoadImage, VAEDecode, PreviewImage, KSampler, SaveImage, KSampler, UNETLoader, SimpleMath+, PrimitiveInt, SimpleMath+, PrimitiveInt, EmptyLatentImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "deis_2m", "scheduler": "simple", "seed": 823835124586781, "steps": 40, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/“一张图能变多少姿势？”不！Qwen2.1出的一整套人像写真！小红书宫格图组图故事板短剧分镜随心发！_2114635915229483009.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/“一张图能变多少姿势？”不！Qwen2.1出的一整套人像写真！小红书宫格图组图故事板短剧分镜随心发！_2114635915229483009.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（79 个）：
- `ComfySwitchNode`
- `CLIPLoader`
- `ComfySwitchNode`
- `HfImageToRGB`
- `LoraLoaderModelOnly` ★核心
- `llama_cpp_parameters`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `SaveImage`
- `CR Text Concatenate`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `llama_cpp_model_loader`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `VAELoader`
- `VAEDecode` ★核心
- `LayerColor: Brightness & Contrast`
- `TextEncodeQwenImage21`
- `easy imageSwitch`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `easy promptLine`
- `DapaoBatchImageGrid`
- `LayerUtility: PurgeVRAM V2`
- `长边短边`
- `easy compare`
- `PrimitiveInt`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `MathExpression|pysssss`
- `VAEEncodeTiled` ★核心
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `TTP_Tile_image_size`
- `ShunjingAIShade`
- `TTP_Image_Tile_Batch`
- `easy imageBatchToImageList`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ShunjingAIShade`
- `easy imageListToImageBatch`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeedVR2Preprocess`
- `VAEDecode` ★核心
- `SeedVR2Conditioning`
- `LayerUtility: ImageScaleRestore V2`
- `UNETLoader` ★核心
- `LoadImage`
- `TTP_Image_Assy`
- `图像缩放V2_孤海`
- `RHHiddenNodes`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `LoadImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `SaveImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `SimpleMath+`
- `PrimitiveInt`
- `SimpleMath+`
- `PrimitiveInt`
- `EmptyLatentImage` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `823835124586781`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `deis_2m`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（69/79）

**有卡**：`CLIPLoader`、`HfImageToRGB`、`LoraLoaderModelOnly`、`llama_cpp_parameters`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`QwenImage21Cache`、`SaveImage`、`CR Text Concatenate`、`llama_cpp_model_loader`、`LayerMask: PersonMaskUltra V2`、`LayerUtility: CropByMask V2`、`VAELoader`、`VAEDecode`、`LayerColor: Brightness & Contrast`、`easy imageSwitch`、`llama_cpp_instruct_adv`、`easy promptLine`、`DapaoBatchImageGrid`、`LayerUtility: PurgeVRAM V2`、`长边短边`、`easy compare`、`UNETLoader`、`PathchSageAttentionKJ`、`MathExpression|pysssss`、`VAEEncodeTiled`、`KSampler`、`VAEDecodeTiled`、`TTP_Tile_image_size`、`ShunjingAIShade`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`easy imageListToImageBatch`、`SeedVR2Preprocess`、`SeedVR2Conditioning`、`LayerUtility: ImageScaleRestore V2`、`LoadImage`、`TTP_Image_Assy`、`图像缩放V2_孤海`、`RHHiddenNodes`、`SimpleMath+`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
