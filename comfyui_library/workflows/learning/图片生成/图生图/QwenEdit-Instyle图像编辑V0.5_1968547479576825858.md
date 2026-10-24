---
key: 图片生成/图生图/QwenEdit-Instyle图像编辑V0.5_1968547479576825858.json
name: QwenEdit-Instyle图像编辑V0.5_1968547479576825858
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenEdit-Instyle图像编辑V0.5_1968547479576825858.json
hash: f539ecf18314aa91
coverage: 0.875
learned_at: 2026-10-23 11:20:14
nodes: [ConditioningZeroOut, PreviewImage, KSampler, SaveImage, VAEDecode, VAEEncode, LoraLoaderModelOnly, FluxKontextImageScale, TextEncodeQwenImageEdit_lrzjason, VAELoader, VAEEncode, LoadImage, ConditioningZeroOut, PreviewImage, LoraLoaderModelOnly, KSampler, SaveImage, VAEDecode, ImageConcanate, VAEEncode, LoraLoaderModelOnly, TextEncodeQwenImageEdit_lrzjason, LoraLoaderModelOnly, CLIPLoader, UNETLoader, LoraLoaderModelOnly, SaveImage, Image Comparer (rgthree), CR Prompt Text, ImageConcanate, SaveImage, Image Comparer (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 1091359629774734, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QwenEdit-Instyle图像编辑V0.5_1968547479576825858.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenEdit-Instyle图像编辑V0.5_1968547479576825858.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `ConditioningZeroOut`
- `PreviewImage`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxKontextImageScale`
- `TextEncodeQwenImageEdit_lrzjason`
- `VAELoader`
- `VAEEncode` ★核心
- `LoadImage`
- `ConditioningZeroOut`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `ImageConcanate`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEdit_lrzjason`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `CR Prompt Text`
- `ImageConcanate`
- `SaveImage`
- `Image Comparer (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1091359629774734`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`ConditioningZeroOut`、`KSampler`、`SaveImage`、`VAEDecode`、`VAEEncode`、`LoraLoaderModelOnly`、`FluxKontextImageScale`、`TextEncodeQwenImageEdit_lrzjason`、`VAELoader`、`LoadImage`、`ImageConcanate`、`CLIPLoader`、`UNETLoader`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
