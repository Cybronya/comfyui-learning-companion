---
key: 图片生成/文生图/【寄语秋歌】Qwen-image-2.1文生图工作流_2103274633997934594.json
name: 【寄语秋歌】Qwen-image-2.1文生图工作流_2103274633997934594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【寄语秋歌】Qwen-image-2.1文生图工作流_2103274633997934594.json
hash: 93df85ed31d049d0
coverage: 0.6
learned_at: 2026-10-07 02:34:07
nodes: [ResolutionSelector, EmptyLatentImage, KSampler, TextEncodeQwenImage21, ResizeImageMaskNode, VAEEncodeTiled, VAELoader, SeedVR2Preprocess, SeedVR2Conditioning, Note, KSampler, Note, VAEDecodeTiled, SeedVR2PostProcessing, PreviewImage, SetNode, MarkdownNote, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, Fast Groups Bypasser (rgthree), UNETLoader, VAEDecode, SaveImage, GetNode, Label (rgthree), Label (rgthree), Label (rgthree), Note]
patterns: []
missing: [Label (rgthree), Label (rgthree), Label (rgthree)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 102000888227243, "steps": 1, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/【寄语秋歌】Qwen-image-2.1文生图工作流_2103274633997934594.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【寄语秋歌】Qwen-image-2.1文生图工作流_2103274633997934594.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（30 个）：
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `ResizeImageMaskNode`
- `VAEEncodeTiled` ★核心
- `VAELoader`
- `SeedVR2Preprocess`
- `SeedVR2Conditioning`
- `Note`
- `KSampler` ★核心
- `Note`
- `VAEDecodeTiled` ★核心
- `SeedVR2PostProcessing`
- `PreviewImage`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Note`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `102000888227243`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **60%**（18/30）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImage21`、`ResizeImageMaskNode`、`VAEEncodeTiled`、`VAELoader`、`SeedVR2Preprocess`、`SeedVR2Conditioning`、`VAEDecodeTiled`、`SeedVR2PostProcessing`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`SaveImage`

**缺卡**（3）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
