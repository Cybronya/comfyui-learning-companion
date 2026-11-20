---
key: 平台全量/增强版Qwen-image最强扩图 扩图Qwen+Image+InstanX_加速版_双节棍版本_1999309377121157122.json
name: 增强版Qwen-image最强扩图 扩图Qwen+Image+InstanX_加速版_双节棍版本_1999309377121157122
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/增强版Qwen-image最强扩图 扩图Qwen+Image+InstanX_加速版_双节棍版本_1999309377121157122.json
hash: ae85d117d36b46d2
coverage: 0.785714
learned_at: 2026-11-14 01:57:05
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, VAEEncode, LoraLoaderModelOnly, ControlNetLoader, LayerUtility: PurgeVRAM, UNETLoader, ImageAndMaskPreview, PreviewImage, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, ModelSamplingAuraFlow, ImageConcanate, KSampler, Note, VAEEncode, ControlNetInpaintingAliMamaApply, LoadImage, Note, NunchakuQwenImageDiTLoader, SaveImage, PreviewImage, ImagePadForOutpaint, SaveImage, VAEDecode, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 649734048173395, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/增强版Qwen-image最强扩图 扩图Qwen+Image+InstanX_加速版_双节棍版本_1999309377121157122.json

> 来源文件 `comfyui_library/workflows/平台全量/增强版Qwen-image最强扩图 扩图Qwen+Image+InstanX_加速版_双节棍版本_1999309377121157122.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ControlNetLoader`
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `ImageAndMaskPreview`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `ModelSamplingAuraFlow`
- `ImageConcanate`
- `KSampler` ★核心
- `Note`
- `VAEEncode` ★核心
- `ControlNetInpaintingAliMamaApply`
- `LoadImage`
- `Note`
- `NunchakuQwenImageDiTLoader`
- `SaveImage`
- `PreviewImage`
- `ImagePadForOutpaint`
- `SaveImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `649734048173395`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（22/28）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`VAEEncode`、`LoraLoaderModelOnly`、`ControlNetLoader`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`ImageAndMaskPreview`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingAuraFlow`、`ImageConcanate`、`KSampler`、`ControlNetInpaintingAliMamaApply`、`LoadImage`、`NunchakuQwenImageDiTLoader`、`SaveImage`、`ImagePadForOutpaint`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
