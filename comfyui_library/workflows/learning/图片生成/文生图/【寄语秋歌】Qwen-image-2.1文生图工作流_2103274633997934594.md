---
key: 图片生成/文生图/【寄语秋歌】Qwen-image-2.1文生图工作流_2103274633997934594.json
name: 【寄语秋歌】Qwen-image-2.1文生图工作流_2103274633997934594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【寄语秋歌】Qwen-image-2.1文生图工作流_2103274633997934594.json
hash: 93df85ed31d049d0
coverage: 0.6
learned_at: 2026-10-10 20:59:30
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

**节点**（30 个）：
- `ResolutionSelector`
- `EmptyLatentImage`
- `KSampler`
- `TextEncodeQwenImage21`
- `ResizeImageMaskNode`
- `VAEEncodeTiled`
- `VAELoader`
- `SeedVR2Preprocess`
- `SeedVR2Conditioning`
- `Note`
- `KSampler`
- `Note`
- `VAEDecodeTiled`
- `SeedVR2PostProcessing`
- `PreviewImage`
- `SetNode`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `SaveImage`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Note`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `102000888227243`
- `steps` = `1`
- `width` = `1024`

## 知识

覆盖率 **60%**（18/30）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImage21`、`ResizeImageMaskNode`、`VAEEncodeTiled`、`VAELoader`、`SeedVR2Preprocess`、`SeedVR2Conditioning`、`Note`、`VAEDecodeTiled`、`SeedVR2PostProcessing`、`PreviewImage`、`SetNode`、`MarkdownNote`

**缺卡**（3）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
