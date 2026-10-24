---
key: 图片生成/图生图/Qwen-史上最强动漫转写实真人-Anything to Real Characters_1991953881183703042.json
name: Qwen-史上最强动漫转写实真人-Anything to Real Characters_1991953881183703042
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-史上最强动漫转写实真人-Anything to Real Characters_1991953881183703042.json
hash: b2034c8a71fae27b
coverage: 0.692308
learned_at: 2026-10-23 11:18:57
nodes: [GetNode, MarkdownNote, GetNode, GetNode, SetNode, SetNode, TextEncodeQwenImageEdit, LoadImage, GetNode, GetNode, SetNode, VAEEncode, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, LoadImage, CFGNorm, ModelSamplingAuraFlow, CLIPLoader, UNETLoader, VAELoader, Note, DF_Integer, DF_Integer, SeedVR2BlockSwap, SaveImage, ImageResize+, TTP_Image_Assy, ImageColorMatchAdobe+, VAEDecode, KSampler, TTP_Image_Tile_Batch, ImpactMinMax, SimpleMath+, DF_Get_image_size, SeedVR2, Fast Groups Muter (rgthree), ImageScaleToTotalPixels, SetNode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2m", "scheduler": "sgm_uniform", "seed": 201350275970278, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-史上最强动漫转写实真人-Anything to Real Characters_1991953881183703042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-史上最强动漫转写实真人-Anything to Real Characters_1991953881183703042.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `GetNode`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `TextEncodeQwenImageEdit`
- `LoadImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `Note`
- `DF_Integer`
- `DF_Integer`
- `SeedVR2BlockSwap`
- `SaveImage`
- `ImageResize+`
- `TTP_Image_Assy`
- `ImageColorMatchAdobe+`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TTP_Image_Tile_Batch`
- `ImpactMinMax`
- `SimpleMath+`
- `DF_Get_image_size`
- `SeedVR2`
- `Fast Groups Muter (rgthree)`
- `ImageScaleToTotalPixels`
- `SetNode`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `201350275970278`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **69%**（27/39）

**有卡**：`TextEncodeQwenImageEdit`、`LoadImage`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`LoraLoaderModelOnly`、`CFGNorm`、`ModelSamplingAuraFlow`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`DF_Integer`、`SeedVR2BlockSwap`、`SaveImage`、`ImageResize+`、`TTP_Image_Assy`、`ImageColorMatchAdobe+`、`VAEDecode`、`KSampler`、`TTP_Image_Tile_Batch`、`ImpactMinMax`、`SimpleMath+`、`DF_Get_image_size`、`SeedVR2`、`ImageScaleToTotalPixels`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
