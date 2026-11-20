---
key: 平台全量/超强扩图+高清修复Qwen Image InstanX  SeedVR2.5 + TTP 分块放大_2001838366314381314.json
name: 超强扩图+高清修复Qwen Image InstanX  SeedVR2.5 + TTP 分块放大_2001838366314381314
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/超强扩图+高清修复Qwen Image InstanX  SeedVR2.5 + TTP 分块放大_2001838366314381314.json
hash: 02f303855a85e047
coverage: 0.477273
learned_at: 2026-11-14 02:46:05
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAEEncode, ControlNetInpaintingAliMamaApply, LayerUtility: PurgeVRAM, ImageAndMaskPreview, MarkdownNote, Image Comparer (rgthree), ImpactInt, VAEDecode, PreviewImage, Note, HYPIRAdvancedRestoration, Note, ModelSamplingAuraFlow, Note, KSampler, ImpactInt, ImagePadForOutpaint, LoadImage, LoraLoaderModelOnly, UNETLoader, CLIPTextEncode, CLIPTextEncode, CLIPLoader, VAELoader, ControlNetLoader, LayerUtility: ImageScaleByAspectRatio V2, Anything Everywhere3, Note, PreviewImage, GetNode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 198760974095979, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/超强扩图+高清修复Qwen Image InstanX  SeedVR2.5 + TTP 分块放大_2001838366314381314.json

> 来源文件 `comfyui_library/workflows/平台全量/超强扩图+高清修复Qwen Image InstanX  SeedVR2.5 + TTP 分块放大_2001838366314381314.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `ControlNetInpaintingAliMamaApply`
- `LayerUtility: PurgeVRAM`
- `ImageAndMaskPreview`
- `MarkdownNote`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `VAEDecode` ★核心
- `PreviewImage`
- `Note`
- `HYPIRAdvancedRestoration`
- `Note`
- `ModelSamplingAuraFlow`
- `Note`
- `KSampler` ★核心
- `ImpactInt`
- `ImagePadForOutpaint`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ControlNetLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Anything Everywhere3`
- `Note`
- `PreviewImage`
- `GetNode`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `198760974095979`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **48%**（21/44）

**有卡**：`VAEEncode`、`ControlNetInpaintingAliMamaApply`、`LayerUtility: PurgeVRAM`、`ImageAndMaskPreview`、`ImpactInt`、`VAEDecode`、`HYPIRAdvancedRestoration`、`ModelSamplingAuraFlow`、`KSampler`、`ImagePadForOutpaint`、`LoadImage`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`ControlNetLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
