---
key: 图片生成/图生图/qwen image2.1 电商主图编辑，提示词自动优化版_2105708075872247810.json
name: qwen image2.1 电商主图编辑，提示词自动优化版_2105708075872247810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image2.1 电商主图编辑，提示词自动优化版_2105708075872247810.json
hash: e20ce2239f7a5f4d
coverage: 0.372881
learned_at: 2026-10-21 00:46:03
nodes: [CLIPLoader, GetNode, SetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, QwenImage21Cache, Seed (rgthree), EmptyLatentImage, GetNode, SetNode, VAELoader, UNETLoader, SetNode, GetNode, 忽略多组孤海, ShowText|pysssss, Note, GetNode, GetNode, SetNode, SaveImageAdvanced, VAEDecode, SaveImage, KSampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, SetNode, SetNode, SetNode, SetNode, LoadImage, 忽略多组孤海, ComfySwitchNode, Note, SetNode, Image Comparer (rgthree), LoadImage, LoadImage, Note, XinbaoImageStandardizer, MarkdownNote, ResolutionSelector, QwenPERewriteT8, Text Multiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 16461585333262, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen image2.1 电商主图编辑，提示词自动优化版_2105708075872247810.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image2.1 电商主图编辑，提示词自动优化版_2105708075872247810.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `CLIPLoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `QwenImage21Cache`
- `Seed (rgthree)`
- `EmptyLatentImage` ★核心
- `GetNode`
- `SetNode`
- `VAELoader`
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `忽略多组孤海`
- `ShowText|pysssss`
- `Note`
- `GetNode`
- `GetNode`
- `SetNode`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `忽略多组孤海`
- `ComfySwitchNode`
- `Note`
- `SetNode`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `Note`
- `XinbaoImageStandardizer`
- `MarkdownNote`
- `ResolutionSelector`
- `QwenPERewriteT8`
- `Text Multiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `16461585333262`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **37%**（22/59）

**有卡**：`CLIPLoader`、`LoadImage`、`QwenImage21Cache`、`Seed (rgthree)`、`EmptyLatentImage`、`VAELoader`、`UNETLoader`、`忽略多组孤海`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`、`KSampler`、`TextEncodeQwenImage21`、`XinbaoImageStandardizer`、`ResolutionSelector`、`QwenPERewriteT8`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
