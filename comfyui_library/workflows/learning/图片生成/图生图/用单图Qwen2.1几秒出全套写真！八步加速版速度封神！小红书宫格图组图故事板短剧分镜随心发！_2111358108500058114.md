---
key: 图片生成/图生图/用单图Qwen2.1几秒出全套写真！八步加速版速度封神！小红书宫格图组图故事板短剧分镜随心发！_2111358108500058114.json
name: 用单图Qwen2.1几秒出全套写真！八步加速版速度封神！小红书宫格图组图故事板短剧分镜随心发！_2111358108500058114
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/用单图Qwen2.1几秒出全套写真！八步加速版速度封神！小红书宫格图组图故事板短剧分镜随心发！_2111358108500058114.json
hash: 8a7d2471e1b1b611
coverage: 0.890244
learned_at: 2026-10-23 13:15:36
nodes: [CLIPLoader, llama_cpp_parameters, CR Text Concatenate, PrimitiveInt, TextEncodeQwenImage21, PrimitiveStringMultiline, CLIPLoader, KSamplerSelect, VAELoader, CLIPLoader, VAELoader, UNETLoader, VAELoader, LoraLoaderModelOnly, CLIPTextEncode, PathchSageAttentionKJ, MathExpression|pysssss, VAEEncodeTiled, KSampler, VAEDecodeTiled, TTP_Tile_image_size, ShunjingAIShade, TTP_Image_Tile_Batch, easy imageBatchToImageList, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, ReferenceLatent, ConditioningZeroOut, KSampler, ShunjingAIShade, easy imageListToImageBatch, TTP_Image_Assy, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2Preprocess, UNETLoader, VAEDecode, SeedVR2Conditioning, 长边短边, easy compare, PrimitiveInt, LoadImage, EmptyLatentImage, ComfySwitchNode, LayerUtility: ImageScaleRestore V2, LayerUtility: CropByMask V2, LayerMask: PersonMaskUltra V2, HfImageToRGB, SamplerCustom, ComfySwitchNode, RHHiddenNodes, llama_cpp_instruct_adv, 图像缩放V2_孤海, VAEDecode, PrimitiveInt, ManualSigmas, llama_cpp_model_loader, easy showAnything, VAEDecode, TextEncodeQwenImage21, SamplerCustom, LayerColor: Brightness & Contrast, LayerUtility: PurgeVRAM V2, easy promptLine, LoadImage, DapaoBatchImageGrid, EmptyLatentImage, UNETLoader, QwenImage21SageAttentionT8, LoraLoaderModelOnly, LoraLoaderModelOnly, RHHiddenNodes, VAELoader, RHHiddenNodes, PrimitiveInt, PrimitiveInt, SimpleMath+, SimpleMath+, LoraLoaderModelOnly, SaveImage, SaveImage, easy imageSwitch]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "simple", "seed": 953847905181517, "steps": 1, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/用单图Qwen2.1几秒出全套写真！八步加速版速度封神！小红书宫格图组图故事板短剧分镜随心发！_2111358108500058114.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/用单图Qwen2.1几秒出全套写真！八步加速版速度封神！小红书宫格图组图故事板短剧分镜随心发！_2111358108500058114.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `CLIPLoader`
- `llama_cpp_parameters`
- `CR Text Concatenate`
- `PrimitiveInt`
- `TextEncodeQwenImage21`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
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
- `TTP_Image_Assy`
- `MathExpression|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SeedVR2Preprocess`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SeedVR2Conditioning`
- `长边短边`
- `easy compare`
- `PrimitiveInt`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: CropByMask V2`
- `LayerMask: PersonMaskUltra V2`
- `HfImageToRGB`
- `SamplerCustom` ★核心
- `ComfySwitchNode`
- `RHHiddenNodes`
- `llama_cpp_instruct_adv`
- `图像缩放V2_孤海`
- `VAEDecode` ★核心
- `PrimitiveInt`
- `ManualSigmas`
- `llama_cpp_model_loader`
- `easy showAnything`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `SamplerCustom` ★核心
- `LayerColor: Brightness & Contrast`
- `LayerUtility: PurgeVRAM V2`
- `easy promptLine`
- `LoadImage`
- `DapaoBatchImageGrid`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `QwenImage21SageAttentionT8`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RHHiddenNodes`
- `VAELoader`
- `RHHiddenNodes`
- `PrimitiveInt`
- `PrimitiveInt`
- `SimpleMath+`
- `SimpleMath+`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImage`
- `easy imageSwitch`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `953847905181517`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（73/82）

**有卡**：`CLIPLoader`、`llama_cpp_parameters`、`CR Text Concatenate`、`TextEncodeQwenImage21`、`KSamplerSelect`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`MathExpression|pysssss`、`VAEEncodeTiled`、`KSampler`、`VAEDecodeTiled`、`TTP_Tile_image_size`、`ShunjingAIShade`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`SeedVR2Preprocess`、`VAEDecode`、`SeedVR2Conditioning`、`长边短边`、`easy compare`、`LoadImage`、`EmptyLatentImage`、`LayerUtility: ImageScaleRestore V2`、`LayerUtility: CropByMask V2`、`LayerMask: PersonMaskUltra V2`、`HfImageToRGB`、`SamplerCustom`、`RHHiddenNodes`、`llama_cpp_instruct_adv`、`图像缩放V2_孤海`、`ManualSigmas`、`llama_cpp_model_loader`、`LayerColor: Brightness & Contrast`、`LayerUtility: PurgeVRAM V2`、`easy promptLine`、`DapaoBatchImageGrid`、`QwenImage21SageAttentionT8`、`SimpleMath+`、`SaveImage`、`easy imageSwitch`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
