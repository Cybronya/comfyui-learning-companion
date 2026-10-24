---
key: 图片生成/图生图/Wan2.2+Vace图像局部修复，8g显卡运行GGUF图像裁切放大修复，放大可见像素，修复效果更好_1957280670374621186.json
name: Wan2.2+Vace图像局部修复，8g显卡运行GGUF图像裁切放大修复，放大可见像素，修复效果更好_1957280670374621186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2+Vace图像局部修复，8g显卡运行GGUF图像裁切放大修复，放大可见像素，修复效果更好_1957280670374621186.json
hash: f6a2bc112bdc0b8e
coverage: 1
learned_at: 2026-10-23 11:28:04
nodes: [CLIPTextEncode, ApplySageAttention, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ApplySageAttention, ModelSamplingSD3, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, InpaintModelConditioning, KSampler, LayerUtility: PurgeVRAM V2, KSampler, LayerUtility: PurgeVRAM V2, VAEDecode, VAELoader, CLIPTextEncode, CLIPLoader, LayerUtility: PurgeVRAM V2, DeepTranslatorTextNode, InpaintCrop, InpaintStitch, SaveImage, MaskPreview+, LoadImage, UnetLoaderGGUF, UnetLoaderGGUF, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.25, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 778870544138817, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2+Vace图像局部修复，8g显卡运行GGUF图像裁切放大修复，放大可见像素，修复效果更好_1957280670374621186.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2+Vace图像局部修复，8g显卡运行GGUF图像裁切放大修复，放大可见像素，修复效果更好_1957280670374621186.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（29 个）：
- `CLIPTextEncode` ★核心
- `ApplySageAttention`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `ApplySageAttention`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `LayerUtility: PurgeVRAM V2`
- `DeepTranslatorTextNode`
- `InpaintCrop`
- `InpaintStitch`
- `SaveImage`
- `MaskPreview+`
- `LoadImage`
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `778870544138817`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.25`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`CLIPTextEncode`、`ApplySageAttention`、`ModelSamplingSD3`、`LayerUtility: PurgeVRAM V2`、`InpaintModelConditioning`、`KSampler`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`DeepTranslatorTextNode`、`InpaintCrop`、`InpaintStitch`、`SaveImage`、`MaskPreview+`、`LoadImage`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、InpaintModelConditioning

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
