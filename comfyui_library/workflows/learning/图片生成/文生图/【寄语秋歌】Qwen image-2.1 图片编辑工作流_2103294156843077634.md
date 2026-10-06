---
key: 图片生成/文生图/【寄语秋歌】Qwen image-2.1 图片编辑工作流_2103294156843077634.json
name: 【寄语秋歌】Qwen image-2.1 图片编辑工作流_2103294156843077634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【寄语秋歌】Qwen image-2.1 图片编辑工作流_2103294156843077634.json
hash: 3214665eed644a03
coverage: 0.621622
learned_at: 2026-10-07 02:34:03
nodes: [ResolutionSelector, LoadImage, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, LoadImage, LoadImage, SetNode, SetNode, SetNode, SetNode, GetNode, TextEncodeQwenImage21, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), ResizeImageMaskNode, VAEEncodeTiled, VAELoader, SeedVR2Preprocess, SeedVR2Conditioning, KSampler, Note, Note, VAEDecodeTiled, SeedVR2PostProcessing, PreviewImage, UNETLoader, CLIPLoader, VAELoader, UNETLoader, Fast Groups Bypasser (rgthree), LoadImage, VAEDecode, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 112174012753731, "steps": 1, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/【寄语秋歌】Qwen image-2.1 图片编辑工作流_2103294156843077634.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【寄语秋歌】Qwen image-2.1 图片编辑工作流_2103294156843077634.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（37 个）：
- `ResolutionSelector`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `ResizeImageMaskNode`
- `VAEEncodeTiled` ★核心
- `VAELoader`
- `SeedVR2Preprocess`
- `SeedVR2Conditioning`
- `KSampler` ★核心
- `Note`
- `Note`
- `VAEDecodeTiled` ★核心
- `SeedVR2PostProcessing`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `112174012753731`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **62%**（23/37）

**有卡**：`ResolutionSelector`、`LoadImage`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ResizeImageMaskNode`、`VAEEncodeTiled`、`VAELoader`、`SeedVR2Preprocess`、`SeedVR2Conditioning`、`VAEDecodeTiled`、`SeedVR2PostProcessing`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
