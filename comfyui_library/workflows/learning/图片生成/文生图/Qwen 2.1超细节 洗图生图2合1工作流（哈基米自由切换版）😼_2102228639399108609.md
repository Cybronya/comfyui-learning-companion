---
key: 图片生成/文生图/Qwen 2.1超细节 洗图生图2合1工作流（哈基米自由切换版）😼_2102228639399108609.json
name: Qwen 2.1超细节 洗图生图2合1工作流（哈基米自由切换版）😼_2102228639399108609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen 2.1超细节 洗图生图2合1工作流（哈基米自由切换版）😼_2102228639399108609.json
hash: 09fa693971edcbb2
coverage: 0.758621
learned_at: 2026-10-20 01:50:49
nodes: [TextEncodeQwenImage21, EmptyLatentImage, KSampler, TextGenerateLTX2Prompt, easy showAnything, ResolutionSelector, EmptyImage, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, MarkdownNote, Switch any [Crystools], Label (rgthree), MarkdownNote, MarkdownNote, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadImage, VAEDecode, SaveImage, Text Multiline, CLIPLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, easy seed, Label (rgthree), ShowText|pysssss, RH_LLMAPI_Pro_Node]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 905, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen 2.1超细节 洗图生图2合1工作流（哈基米自由切换版）😼_2102228639399108609.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen 2.1超细节 洗图生图2合1工作流（哈基米自由切换版）😼_2102228639399108609.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `ResolutionSelector`
- `EmptyImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `MarkdownNote`
- `Switch any [Crystools]`
- `Label (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Text Multiline`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `easy seed`
- `Label (rgthree)`
- `ShowText|pysssss`
- `RH_LLMAPI_Pro_Node`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `905`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（22/29）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`TextGenerateLTX2Prompt`、`ResolutionSelector`、`EmptyImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`INTConstant`、`Switch any [Crystools]`、`Label (rgthree)`、`LoadImage`、`VAEDecode`、`SaveImage`、`Text Multiline`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`easy seed`、`RH_LLMAPI_Pro_Node`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
