---
key: 图片生成/图生图/Wan2.2真实图生图洗图工作流lora去除AI油腻味，_1958429494354853889.json
name: Wan2.2真实图生图洗图工作流lora去除AI油腻味，_1958429494354853889
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2真实图生图洗图工作流lora去除AI油腻味，_1958429494354853889.json
hash: 73f9e8a034d92971
coverage: 0.967742
learned_at: 2026-10-23 11:28:24
nodes: [ApplySageAttention, KSampler, LayerUtility: PurgeVRAM, CLIPLoader, LayerUtility: PurgeVRAM, VAEEncode, LayerUtility: PurgeVRAM, CLIPTextEncode, LoadImage, DeepTranslatorTextNode, VAELoader, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, VAEDecode, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, ApplySageAttention, ModelSamplingSD3, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, ModelSamplingSD3, CLIPTextEncode, KSampler, ImageScale, SaveImage, Image Comparer (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 727406298615693, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2真实图生图洗图工作流lora去除AI油腻味，_1958429494354853889.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2真实图生图洗图工作流lora去除AI油腻味，_1958429494354853889.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `ApplySageAttention`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPLoader`
- `LayerUtility: PurgeVRAM`
- `VAEEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `DeepTranslatorTextNode`
- `VAELoader`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `ApplySageAttention`
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ImageScale`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `727406298615693`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **97%**（30/31）

**有卡**：`ApplySageAttention`、`KSampler`、`LayerUtility: PurgeVRAM`、`CLIPLoader`、`VAEEncode`、`CLIPTextEncode`、`LoadImage`、`DeepTranslatorTextNode`、`VAELoader`、`LoraLoaderModelOnly`、`VAEDecode`、`ModelSamplingSD3`、`ImageScale`、`SaveImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
