---
key: 图片生成/图生图/秒杀传统三视图Lora流，Qwen2.1角色资产图制作，短剧IP神器_2114187385666891778.json
name: 秒杀传统三视图Lora流，Qwen2.1角色资产图制作，短剧IP神器_2114187385666891778
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/秒杀传统三视图Lora流，Qwen2.1角色资产图制作，短剧IP神器_2114187385666891778.json
hash: 164255506161fdcb
coverage: 0.927711
learned_at: 2026-10-26 22:06:44
nodes: [QwenImage21SageAttentionT8, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLatentImage, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, SaveImage, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2, CLIPLoader, VAELoader, UNETLoader, VAELoader, LoraLoaderModelOnly, CLIPTextEncode, PathchSageAttentionKJ, MathExpression|pysssss, VAEEncodeTiled, SeedVR2Conditioning, KSampler, VAEDecodeTiled, TTP_Tile_image_size, ShunjingAIShade, TTP_Image_Tile_Batch, easy imageBatchToImageList, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, ReferenceLatent, ConditioningZeroOut, KSampler, ShunjingAIShade, easy imageListToImageBatch, TTP_Image_Assy, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, easy compare, UNETLoader, ManualSigmas, SeedNode, SamplerCustom, VAEDecode, ComfySwitchNode, ComfySwitchNode, VAEDecode, SamplerCustom, KSamplerSelect, ComfySwitchNode, SamplerCustom, VAEDecode, CLIPLoader, ImageConcatMulti, LayerUtility: ImageScaleRestore V2, SeedVR2Preprocess, UNETLoader, VAEDecode, PreviewImage, TextEncodeQwenImage21, TextEncodeQwenImage21, LoadImage, easy imageSwitch, 长边短边, easy imageRemBg, LayerUtility: PurgeVRAM V2, LoadImage, LoadImage, LoadImage, SimpleMath+, PrimitiveInt, SimpleMath+, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, TextEncodeQwenImage21, EmptyImage, PreviewImage]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "simple", "seed": 953847905181517, "steps": 1, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/秒杀传统三视图Lora流，Qwen2.1角色资产图制作，短剧IP神器_2114187385666891778.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/秒杀传统三视图Lora流，Qwen2.1角色资产图制作，短剧IP神器_2114187385666891778.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `QwenImage21SageAttentionT8`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropByMask V2`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: PersonMaskUltra V2`
- `SaveImage`
- `LayerUtility: CropByMask V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: CropByMask V2`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `MathExpression|pysssss`
- `VAEEncodeTiled` ★核心
- `SeedVR2Conditioning`
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
- `easy compare`
- `UNETLoader` ★核心
- `ManualSigmas`
- `SeedNode`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `ComfySwitchNode`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleRestore V2`
- `SeedVR2Preprocess`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `LoadImage`
- `easy imageSwitch`
- `长边短边`
- `easy imageRemBg`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SimpleMath+`
- `PrimitiveInt`
- `SimpleMath+`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `TextEncodeQwenImage21`
- `EmptyImage`
- `PreviewImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `953847905181517`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（77/83）

**有卡**：`QwenImage21SageAttentionT8`、`VAELoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`LayerMask: PersonMaskUltra V2`、`LayerUtility: CropByMask V2`、`SaveImage`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`MathExpression|pysssss`、`VAEEncodeTiled`、`SeedVR2Conditioning`、`KSampler`、`VAEDecodeTiled`、`TTP_Tile_image_size`、`ShunjingAIShade`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`easy compare`、`ManualSigmas`、`SeedNode`、`SamplerCustom`、`VAEDecode`、`KSamplerSelect`、`ImageConcatMulti`、`LayerUtility: ImageScaleRestore V2`、`SeedVR2Preprocess`、`TextEncodeQwenImage21`、`LoadImage`、`easy imageSwitch`、`长边短边`、`easy imageRemBg`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`、`RHHiddenNodes`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
