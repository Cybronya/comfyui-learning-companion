---
key: 图片生成/图生图/双节棍4步_千问图像编辑-快速编辑_Qwen+Image+EDIT+nunchaku+Lightni_1966242828240195585.json
name: 双节棍4步_千问图像编辑-快速编辑_Qwen+Image+EDIT+nunchaku+Lightni_1966242828240195585
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/双节棍4步_千问图像编辑-快速编辑_Qwen+Image+EDIT+nunchaku+Lightni_1966242828240195585.json
hash: 1e213cb67c505b22
coverage: 0.842105
learned_at: 2026-10-23 12:35:26
nodes: [TextEncodeQwenImageEdit, SaveImage, PreviewImage, VAEDecode, CFGNorm, ModelSamplingAuraFlow, ImageScaleToMegapixels, ImageConcanate, SaveImage, VAEEncode, CLIPLoader, VAELoader, TextEncodeQwenImageEdit, MarkdownNote, MarkdownNote, LoadImage, KSampler, LoraLoaderModelOnly, NunchakuQwenImageDiTLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 580887945124865, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/双节棍4步_千问图像编辑-快速编辑_Qwen+Image+EDIT+nunchaku+Lightni_1966242828240195585.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/双节棍4步_千问图像编辑-快速编辑_Qwen+Image+EDIT+nunchaku+Lightni_1966242828240195585.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `TextEncodeQwenImageEdit`
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `ImageScaleToMegapixels`
- `ImageConcanate`
- `SaveImage`
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEdit`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `NunchakuQwenImageDiTLoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `580887945124865`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`TextEncodeQwenImageEdit`、`SaveImage`、`VAEDecode`、`CFGNorm`、`ModelSamplingAuraFlow`、`ImageScaleToMegapixels`、`ImageConcanate`、`VAEEncode`、`CLIPLoader`、`VAELoader`、`LoadImage`、`KSampler`、`LoraLoaderModelOnly`、`NunchakuQwenImageDiTLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEdit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
