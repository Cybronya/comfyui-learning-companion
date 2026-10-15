---
key: 图片生成/反推提示词/千问image2.1图像编辑 全自动提示词（优化）_2103398363587764226.json
name: 千问image2.1图像编辑 全自动提示词（优化）_2103398363587764226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/千问image2.1图像编辑 全自动提示词（优化）_2103398363587764226.json
hash: 53cae23ad9dba930
coverage: 0.372881
learned_at: 2026-10-15 22:25:03
nodes: [CLIPLoader, GetNode, SetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, QwenImage21Cache, Seed (rgthree), EmptyLatentImage, GetNode, SetNode, VAELoader, UNETLoader, SetNode, GetNode, 忽略多组孤海, QwenPERewriteT8, ShowText|pysssss, Note, GetNode, GetNode, SetNode, SaveImageAdvanced, VAEDecode, SaveImage, KSampler, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, TextEncodeQwenImage21, SetNode, SetNode, SetNode, SetNode, LoadImage, 忽略多组孤海, ComfySwitchNode, ResolutionSelector, Note, SetNode, Note, Text Multiline, Image Comparer (rgthree), LoadImage, LoadImage, Note, XinbaoImageStandardizer]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 153481661071141, "steps": 25, "width": 1024}
---

# 图片生成/反推提示词/千问image2.1图像编辑 全自动提示词（优化）_2103398363587764226.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/千问image2.1图像编辑 全自动提示词（优化）_2103398363587764226.json`

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
- `QwenPERewriteT8`
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
- `ResolutionSelector`
- `Note`
- `SetNode`
- `Note`
- `Text Multiline`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `Note`
- `XinbaoImageStandardizer`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `153481661071141`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **37%**（22/59）

**有卡**：`CLIPLoader`、`LoadImage`、`QwenImage21Cache`、`Seed (rgthree)`、`EmptyLatentImage`、`VAELoader`、`UNETLoader`、`忽略多组孤海`、`QwenPERewriteT8`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`、`KSampler`、`TextEncodeQwenImage21`、`ResolutionSelector`、`Text Multiline`、`XinbaoImageStandardizer`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
