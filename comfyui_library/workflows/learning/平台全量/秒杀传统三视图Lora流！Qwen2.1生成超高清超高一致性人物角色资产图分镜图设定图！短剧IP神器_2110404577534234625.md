---
key: 平台全量/秒杀传统三视图Lora流！Qwen2.1生成超高清超高一致性人物角色资产图分镜图设定图！短剧IP神器_2110404577534234625.json
name: 秒杀传统三视图Lora流！Qwen2.1生成超高清超高一致性人物角色资产图分镜图设定图！短剧IP神器_2110404577534234625
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/秒杀传统三视图Lora流！Qwen2.1生成超高清超高一致性人物角色资产图分镜图设定图！短剧IP神器_2110404577534234625.json
hash: e7355d243b7420bb
coverage: 0.924731
learned_at: 2026-11-14 02:27:22
nodes: [QwenImage21SageAttentionT8, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerMask: PersonMaskUltra V2, LayerUtility: CropByMask V2, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, SaveImage, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2, LayerUtility: CropByMask V2, CLIPLoader, VAELoader, UNETLoader, VAELoader, LoraLoaderModelOnly, CLIPTextEncode, PathchSageAttentionKJ, MathExpression|pysssss, VAEEncodeTiled, SeedVR2Conditioning, KSampler, VAEDecodeTiled, TTP_Tile_image_size, ShunjingAIShade, TTP_Image_Tile_Batch, easy imageBatchToImageList, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, ReferenceLatent, ConditioningZeroOut, KSampler, ShunjingAIShade, easy imageListToImageBatch, TTP_Image_Assy, MathExpression|pysssss, LayerUtility: ImageScaleByAspectRatio V2, easy compare, UNETLoader, ManualSigmas, SeedNode, SamplerCustom, VAEDecode, VAEDecode, SamplerCustom, KSamplerSelect, SamplerCustom, VAEDecode, CLIPLoader, ImageConcatMulti, LayerUtility: ImageScaleRestore V2, SeedVR2Preprocess, UNETLoader, VAEDecode, LoadImage, 长边短边, easy imageRemBg, LayerUtility: PurgeVRAM V2, LoadImage, LoadImage, LoadImage, SimpleMath+, PrimitiveInt, SimpleMath+, RHHiddenNodes, SamplerCustom, VAEDecode, GetImageSize, ImageConcatMulti, ComfySwitchNode, ManualSigmas, ImageConcatMulti, GetImageSize, 图像缩放V2_孤海, PreviewImage, TextEncodeQwenImage21, ComfySwitchNode, EmptyLatentImage, TextEncodeQwenImage21, ComfySwitchNode, EmptyLatentImage, TextEncodeQwenImage21, ComfySwitchNode, TextEncodeQwenImage21, ComfySwitchNode, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "simple", "seed": 953847905181517, "steps": 1, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/秒杀传统三视图Lora流！Qwen2.1生成超高清超高一致性人物角色资产图分镜图设定图！短剧IP神器_2110404577534234625.json

> 来源文件 `comfyui_library/workflows/平台全量/秒杀传统三视图Lora流！Qwen2.1生成超高清超高一致性人物角色资产图分镜图设定图！短剧IP神器_2110404577534234625.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
- `QwenImage21SageAttentionT8`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
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
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleRestore V2`
- `SeedVR2Preprocess`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LoadImage`
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
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `GetImageSize`
- `ImageConcatMulti`
- `ComfySwitchNode`
- `ManualSigmas`
- `ImageConcatMulti`
- `GetImageSize`
- `图像缩放V2_孤海`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`

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

覆盖率 **92%**（86/93）

**有卡**：`QwenImage21SageAttentionT8`、`VAELoader`、`LoraLoaderModelOnly`、`LayerMask: PersonMaskUltra V2`、`LayerUtility: CropByMask V2`、`SaveImage`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`MathExpression|pysssss`、`VAEEncodeTiled`、`SeedVR2Conditioning`、`KSampler`、`VAEDecodeTiled`、`TTP_Tile_image_size`、`ShunjingAIShade`、`TTP_Image_Tile_Batch`、`easy imageBatchToImageList`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`easy imageListToImageBatch`、`TTP_Image_Assy`、`easy compare`、`ManualSigmas`、`SeedNode`、`SamplerCustom`、`VAEDecode`、`KSamplerSelect`、`ImageConcatMulti`、`LayerUtility: ImageScaleRestore V2`、`SeedVR2Preprocess`、`LoadImage`、`长边短边`、`easy imageRemBg`、`LayerUtility: PurgeVRAM V2`、`SimpleMath+`、`RHHiddenNodes`、`GetImageSize`、`图像缩放V2_孤海`、`TextEncodeQwenImage21`、`EmptyLatentImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
