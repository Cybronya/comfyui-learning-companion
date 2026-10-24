---
key: 图片生成/图生图/Nunchaku qwen image edit 4步图像编辑模型 极速版-StarAI_1965839255085953026.json
name: Nunchaku qwen image edit 4步图像编辑模型 极速版-StarAI_1965839255085953026
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku qwen image edit 4步图像编辑模型 极速版-StarAI_1965839255085953026.json
hash: 79b257ce5245f809
coverage: 0.794118
learned_at: 2026-10-23 11:09:56
nodes: [easy cleanGpuUsed, NunchakuQwenImageDiTLoader, NunchakuQwenImageDiTLoader, NunchakuQwenImageDiTLoader, easy cleanGpuUsed, ImpactSwitch, ImpactSwitch, Int, ImpactSwitch, Int, CLIPLoader, VAELoader, CR Text, CFGNorm, SaveImage, SaveImage, Int, LoadImage, Image Comparer (rgthree), ModelSamplingAuraFlow, VAEEncode, ImageScaleToMegapixels, VAEDecode, KSampler, TextEncodeQwenImageEdit, TextEncodeQwenImageEdit, SaveImage, PreviewImage, SaveImage, Int, easy float, easy float, MarkdownNote, MarkdownNote]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 363389578502135, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Nunchaku qwen image edit 4步图像编辑模型 极速版-StarAI_1965839255085953026.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku qwen image edit 4步图像编辑模型 极速版-StarAI_1965839255085953026.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `easy cleanGpuUsed`
- `NunchakuQwenImageDiTLoader`
- `NunchakuQwenImageDiTLoader`
- `NunchakuQwenImageDiTLoader`
- `easy cleanGpuUsed`
- `ImpactSwitch`
- `ImpactSwitch`
- `Int`
- `ImpactSwitch`
- `Int`
- `CLIPLoader`
- `VAELoader`
- `CR Text`
- `CFGNorm`
- `SaveImage`
- `SaveImage`
- `Int`
- `LoadImage`
- `Image Comparer (rgthree)`
- `ModelSamplingAuraFlow`
- `VAEEncode` ★核心
- `ImageScaleToMegapixels`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEdit`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `Int`
- `easy float`
- `easy float`
- `MarkdownNote`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `363389578502135`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（27/34）

**有卡**：`easy cleanGpuUsed`、`NunchakuQwenImageDiTLoader`、`Int`、`CLIPLoader`、`VAELoader`、`CR Text`、`CFGNorm`、`SaveImage`、`LoadImage`、`ModelSamplingAuraFlow`、`VAEEncode`、`ImageScaleToMegapixels`、`VAEDecode`、`KSampler`、`TextEncodeQwenImageEdit`、`easy float`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEdit、VAEEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
