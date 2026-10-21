---
key: 图片生成/图生图/Qwen image 2.1图像编辑(8)4步加速版_2104743245573083137.json
name: Qwen image 2.1图像编辑(8)4步加速版_2104743245573083137
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图像编辑(8)4步加速版_2104743245573083137.json
hash: 46d36bf4d7c61938
coverage: 0.411765
learned_at: 2026-10-21 00:42:57
nodes: [MarkdownNote, GetNode, GetNode, GetNode, CLIPLoader, SetNode, SetNode, SetNode, GetNode, 孤海注释, ComfySwitchNode, MarkdownNote, SetNode, SetNode, 孤海注释, VAEEncode, GetNode, ImageScaleToTotalPixels, GetNode, GetNode, TextEncodeQwenImage21, GetNode, SaveImageAdvanced, KSampler, VAELoader, SetNode, StringReplace, UNETLoader, QwenImage21Cache, LoadImage, JjkText, VAEDecode, SaveImage, ExecutionBlocker]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1032855041201176, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1图像编辑(8)4步加速版_2104743245573083137.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1图像编辑(8)4步加速版_2104743245573083137.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `孤海注释`
- `ComfySwitchNode`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `孤海注释`
- `VAEEncode` ★核心
- `GetNode`
- `ImageScaleToTotalPixels`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `VAELoader`
- `SetNode`
- `StringReplace`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `JjkText`
- `VAEDecode` ★核心
- `SaveImage`
- `ExecutionBlocker`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1032855041201176`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **41%**（14/34）

**有卡**：`CLIPLoader`、`VAEEncode`、`ImageScaleToTotalPixels`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`KSampler`、`VAELoader`、`StringReplace`、`UNETLoader`、`QwenImage21Cache`、`LoadImage`、`VAEDecode`、`SaveImage`、`ExecutionBlocker`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
