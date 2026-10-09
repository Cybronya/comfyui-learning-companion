---
key: 图片生成/图生图/Qwen image 2.1超细节多图像编辑工作流_2102274071047270401.json
name: Qwen image 2.1超细节多图像编辑工作流_2102274071047270401.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1超细节多图像编辑工作流_2102274071047270401.json
hash: adb4ed772a06e9da
coverage: 0.709677
learned_at: 2026-10-09 22:27:10
nodes: [EmptyLatentImage, easy seed, ResolutionSelector, EmptyImage, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, Label (rgthree), MarkdownNote, Label (rgthree), QwenImage21Cache, MarkdownNote, MarkdownNote, Image Comparer (rgthree), UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, Text Multiline, TextEncodeQwenImage21, KSampler, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAEDecode, SaveImage]
patterns: []
missing: [Label (rgthree), Label (rgthree), LayerUtility: ImageScaleByAspectRatio V2, Text Multiline, easy seed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 25, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen image 2.1超细节多图像编辑工作流_2102274071047270401.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102274071047270401.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `EmptyLatentImage` ★核心
- `easy seed`
- `ResolutionSelector`
- `EmptyImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `Label (rgthree)`
- `MarkdownNote`
- `Label (rgthree)`
- `QwenImage21Cache`
- `MarkdownNote`
- `MarkdownNote`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `Text Multiline`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `999`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（22/31）

**有卡**：`EmptyLatentImage`、`ResolutionSelector`、`EmptyImage`、`INTConstant`、`QwenImage21Cache`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`LoadImage`、`VAEDecode`、`SaveImage`

**缺卡**（5）：`Label (rgthree)`、`Label (rgthree)`、`LayerUtility: ImageScaleByAspectRatio V2`、`Text Multiline`、`easy seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
