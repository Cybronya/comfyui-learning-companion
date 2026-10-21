---
key: 图片生成/文生图/Moss-image(文生图+可选提示词增强）MOSS-Image-SFT 8步极速生图_2112344170261213186.json
name: Moss-image(文生图+可选提示词增强）MOSS-Image-SFT 8步极速生图_2112344170261213186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Moss-image(文生图+可选提示词增强）MOSS-Image-SFT 8步极速生图_2112344170261213186.json
hash: 2a85fb93bc917a8f
coverage: 0.452055
learned_at: 2026-10-21 02:53:51
nodes: [SetNode, UNETLoader, SetNode, CLIPLoader, SetNode, VAELoader, SetNode, GetNode, VAEDecode, MarkdownNote, CLIPTextEncode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, EmptyFlux2LatentImage, GetNode, SetNode, GetNode, KSampler, GetNode, LoraLoaderModelOnly, ResolutionSelector, SetNode, SkipLayerGuidanceDiTSimple, PrimitiveInt, PrimitiveInt, PrimitiveInt, easy anythingIndexSwitch, easy anythingIndexSwitch, PrimitiveFloat, PrimitiveFloat, PrimitiveFloat, GetNode, VAELoader, SeedVR2Conditioning, KSampler, UNETLoader, Note, VAEEncodeTiled, SeedVR2Preprocess, GetNode, SetNode, ImageColorMatch+, PreviewImage, DF_Integer, Note, easy int, SimpleMath+, Note, VAEDecodeTiled, LayerUtility: ImageScaleByAspectRatio V2, ImageCASharpening+, Image Comparer (rgthree), easy anythingIndexSwitch, GetNode, 忽略多组孤海, SetNode, GetNode, PreviewAny, PrimitiveStringMultiline, TextGenerate, Any Switch (rgthree), 忽略多组孤海, CLIPTextEncode, easy int, MarkdownNote, JjkText, easy seed, SaveImage, MarkdownNote]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "linear_quadratic", "seed": 959948902156063, "steps": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Moss-image(文生图+可选提示词增强）MOSS-Image-SFT 8步极速生图_2112344170261213186.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Moss-image(文生图+可选提示词增强）MOSS-Image-SFT 8步极速生图_2112344170261213186.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `VAEDecode` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyFlux2LatentImage`
- `GetNode`
- `SetNode`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `ResolutionSelector`
- `SetNode`
- `SkipLayerGuidanceDiTSimple`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy anythingIndexSwitch`
- `easy anythingIndexSwitch`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `GetNode`
- `VAELoader`
- `SeedVR2Conditioning`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `Note`
- `VAEEncodeTiled` ★核心
- `SeedVR2Preprocess`
- `GetNode`
- `SetNode`
- `ImageColorMatch+`
- `PreviewImage`
- `DF_Integer`
- `Note`
- `easy int`
- `SimpleMath+`
- `Note`
- `VAEDecodeTiled` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageCASharpening+`
- `Image Comparer (rgthree)`
- `easy anythingIndexSwitch`
- `GetNode`
- `忽略多组孤海`
- `SetNode`
- `GetNode`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `Any Switch (rgthree)`
- `忽略多组孤海`
- `CLIPTextEncode` ★核心
- `easy int`
- `MarkdownNote`
- `JjkText`
- `easy seed`
- `SaveImage`
- `MarkdownNote`

## 关键参数

- `seed` = `959948902156063`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `linear_quadratic`
- `denoise` = `1`

## 知识

覆盖率 **45%**（33/73）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`CLIPTextEncode`、`EmptyFlux2LatentImage`、`KSampler`、`LoraLoaderModelOnly`、`ResolutionSelector`、`SkipLayerGuidanceDiTSimple`、`easy anythingIndexSwitch`、`SeedVR2Conditioning`、`VAEEncodeTiled`、`SeedVR2Preprocess`、`ImageColorMatch+`、`DF_Integer`、`easy int`、`SimpleMath+`、`VAEDecodeTiled`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCASharpening+`、`忽略多组孤海`、`TextGenerate`、`easy seed`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ResolutionSelector

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
