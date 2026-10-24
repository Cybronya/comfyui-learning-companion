---
key: 图片生成/图生图/Nunchaku Qwen Edit  2509 1-3 Images for Reference_2037090640076480513.json
name: Nunchaku Qwen Edit  2509 1-3 Images for Reference_2037090640076480513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku Qwen Edit  2509 1-3 Images for Reference_2037090640076480513.json
hash: f9dce248a4b3bf26
coverage: 0.857143
learned_at: 2026-10-23 11:09:54
nodes: [KSampler, VAEDecode, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, VAELoader, ImageScaleToTotalPixels, NunchakuQwenImageDiTLoader, TextEncodeQwenImageEditPlus, SaveImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, Label (rgthree), LoadImage, LoadImage, MarkdownNote, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), TextEncodeQwenImageEditPlus, LoadImage, EmptySD3LatentImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 789836564900043, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Nunchaku Qwen Edit  2509 1-3 Images for Reference_2037090640076480513.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku Qwen Edit  2509 1-3 Images for Reference_2037090640076480513.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `NunchakuQwenImageDiTLoader`
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `Label (rgthree)`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `EmptySD3LatentImage`

## 关键参数

- `seed` = `789836564900043`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`KSampler`、`VAEDecode`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`NunchakuQwenImageDiTLoader`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`Label (rgthree)`、`LoadImage`、`EmptySD3LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEditPlus、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
