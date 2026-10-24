---
key: 图片生成/图生图/单图Qwen2.1八步加速出全套写真，小红书宫格图组图分镜_2111971265673261058.json
name: 单图Qwen2.1八步加速出全套写真，小红书宫格图组图分镜_2111971265673261058
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/单图Qwen2.1八步加速出全套写真，小红书宫格图组图分镜_2111971265673261058.json
hash: 290ab0e42ccb1d92
coverage: 0.882883
learned_at: 2026-10-23 12:32:05
nodes: [CLIPLoader, llama_cpp_parameters, CR Text Concatenate, PrimitiveInt, TextEncodeQwenImage21, PrimitiveStringMultiline, CLIPLoader, KSamplerSelect, VAELoader, CLIPLoader, VAELoader, UNETLoader, VAELoader, LoraLoaderModelOnly, CLIPTextEncode, PathchSageAttentionKJ, MathExpression|pysssss, VAEEncodeTiled, KSampler, VAEDecodeTiled, TTP_Tile_image_size, ShunjingAIShade, TTP_Image_Tile_Batch, easy imageBatchToImageList, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, ReferenceLatent, ConditioningZeroOut, KSampler, ShunjingAIShade, easy imageListToImageBatch, TTP_Image_Assy, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, SeedVR2Preprocess, UNETLoader, VAEDecode, SeedVR2Conditioning, 长边短边, easy compare, PrimitiveInt, LoadImage, EmptyLatentImage, ComfySwitchNode, LayerUtility: ImageScaleRestore V2, LayerUtility: CropByMask V2, LayerMask: PersonMaskUltra V2, HfImageToRGB, SamplerCustom, ComfySwitchNode, RHHiddenNodes, llama_cpp_instruct_adv, 图像缩放V2_孤海, VAEDecode, PrimitiveInt, ManualSigmas, llama_cpp_model_loader, easy showAnything, VAEDecode, TextEncodeQwenImage21, SamplerCustom, LayerColor: Brightness & Contrast, LayerUtility: PurgeVRAM V2, easy promptLine, LoadImage, DapaoBatchImageGrid, EmptyLatentImage, UNETLoader, QwenImage21SageAttentionT8, LoraLoaderModelOnly, LoraLoaderModelOnly, RHHiddenNodes, VAELoader, RHHiddenNodes, PrimitiveInt, PrimitiveInt, SimpleMath+, SimpleMath+, LoraLoaderModelOnly, SaveImage, SaveImage, easy imageSwitch, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/单图Qwen2.1八步加速出全套写真，小红书宫格图组图分镜_2111971265673261058.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/单图Qwen2.1八步加速出全套写真，小红书宫格图组图分镜_2111971265673261058.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（111 个）：
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

覆盖率 **88%**（98/111）

**有卡**：`CLIPLoader`、`llama_cpp_parameters`、`CR Text Concatenate`、`TextEncodeQwenImage21`、`KSamplerSelect`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`MathExpression|pysssss`、`VAEEncodeTiled`、`KSampler`、`VAEDecodeTiled`、`TTP_Tile_image_size`、`ShunjingAIShade`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`SeedVR2Preprocess`、`VAEDecode`、`SeedVR2Conditioning`、`长边短边`、`easy compare`、`LoadImage`、`EmptyLatentImage`、`LayerUtility: ImageScaleRestore V2`、`LayerUtility: CropByMask V2`、`LayerMask: PersonMaskUltra V2`、`HfImageToRGB`、`SamplerCustom`、`RHHiddenNodes`、`llama_cpp_instruct_adv`、`图像缩放V2_孤海`、`ManualSigmas`、`llama_cpp_model_loader`、`LayerColor: Brightness & Contrast`、`LayerUtility: PurgeVRAM V2`、`easy promptLine`、`DapaoBatchImageGrid`、`QwenImage21SageAttentionT8`、`SimpleMath+`、`SaveImage`、`easy imageSwitch`、`solarL_SaveImagesToZip`

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
