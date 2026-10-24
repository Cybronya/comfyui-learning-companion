---
key: 图片生成/图生图/Qwen2.1人像写真姿势套图，小红书宫格图组图分镜随心发_2111188924164042754.json
name: Qwen2.1人像写真姿势套图，小红书宫格图组图分镜随心发_2111188924164042754
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1人像写真姿势套图，小红书宫格图组图分镜随心发_2111188924164042754.json
hash: d4a1f1c15a7b3edc
coverage: 0.866071
learned_at: 2026-10-23 11:19:07
nodes: [CLIPLoader, llama_cpp_parameters, llama_cpp_model_loader, CR Text Concatenate, PrimitiveInt, PrimitiveInt, PrimitiveInt, TextEncodeQwenImage21, PrimitiveStringMultiline, CLIPLoader, QwenImage21SageAttentionT8, VAELoader, easy promptLine, LoraLoaderModelOnly, UNETLoader, LayerUtility: PurgeVRAM V2, ManualSigmas, KSamplerSelect, VAELoader, CLIPLoader, VAELoader, UNETLoader, VAELoader, LoraLoaderModelOnly, CLIPTextEncode, PathchSageAttentionKJ, MathExpression|pysssss, VAEEncodeTiled, KSampler, VAEDecodeTiled, TTP_Tile_image_size, ShunjingAIShade, TTP_Image_Tile_Batch, easy imageBatchToImageList, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, ReferenceLatent, ConditioningZeroOut, KSampler, ShunjingAIShade, easy imageListToImageBatch, TTP_Image_Assy, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2Preprocess, UNETLoader, VAEDecode, SeedVR2Conditioning, 长边短边, easy compare, PrimitiveInt, LoadImage, EmptyLatentImage, ComfySwitchNode, LayerUtility: ImageScaleRestore V2, LayerUtility: CropByMask V2, LayerMask: PersonMaskUltra V2, LoadImage, SamplerCustom, LoraLoaderModelOnly, HfImageToRGB, EmptyLatentImage, VAEDecode, easy imageSwitch, 图像缩放V2_孤海, PrimitiveInt, PrimitiveInt, PrimitiveInt, DapaoBatchImageGrid, easy showAnything, VAEDecode, LayerColor: Brightness & Contrast, SamplerCustom, TextEncodeQwenImage21, ComfySwitchNode, LoraLoaderModelOnly, SaveImage, SaveImage, LoraLoaderModelOnly, llama_cpp_instruct_adv, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen2.1人像写真姿势套图，小红书宫格图组图分镜随心发_2111188924164042754.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1人像写真姿势套图，小红书宫格图组图分镜随心发_2111188924164042754.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（112 个）：
- `CLIPLoader`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `CR Text Concatenate`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `TextEncodeQwenImage21`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `VAELoader`
- `easy promptLine`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM V2`
- `ManualSigmas`
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
- `LoadImage`
- `SamplerCustom` ★核心
- `LoraLoaderModelOnly` ★核心
- `HfImageToRGB`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `easy imageSwitch`
- `图像缩放V2_孤海`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `DapaoBatchImageGrid`
- `easy showAnything`
- `VAEDecode` ★核心
- `LayerColor: Brightness & Contrast`
- `SamplerCustom` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `llama_cpp_instruct_adv`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（97/112）

**有卡**：`CLIPLoader`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`CR Text Concatenate`、`TextEncodeQwenImage21`、`QwenImage21SageAttentionT8`、`VAELoader`、`easy promptLine`、`LoraLoaderModelOnly`、`UNETLoader`、`LayerUtility: PurgeVRAM V2`、`ManualSigmas`、`KSamplerSelect`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`MathExpression|pysssss`、`VAEEncodeTiled`、`KSampler`、`VAEDecodeTiled`、`TTP_Tile_image_size`、`ShunjingAIShade`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`SeedVR2Preprocess`、`VAEDecode`、`SeedVR2Conditioning`、`长边短边`、`easy compare`、`LoadImage`、`EmptyLatentImage`、`LayerUtility: ImageScaleRestore V2`、`LayerUtility: CropByMask V2`、`LayerMask: PersonMaskUltra V2`、`SamplerCustom`、`HfImageToRGB`、`easy imageSwitch`、`图像缩放V2_孤海`、`DapaoBatchImageGrid`、`LayerColor: Brightness & Contrast`、`SaveImage`、`llama_cpp_instruct_adv`、`RHHiddenNodes`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
