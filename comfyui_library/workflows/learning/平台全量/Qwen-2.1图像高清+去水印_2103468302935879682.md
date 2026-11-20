---
key: 平台全量/Qwen-2.1图像高清+去水印_2103468302935879682.json
name: Qwen-2.1图像高清+去水印_2103468302935879682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-2.1图像高清+去水印_2103468302935879682.json
hash: 5bfced34f7153fef
coverage: 0.8125
learned_at: 2026-11-14 00:51:00
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, Label (rgthree), VAELoader, LoadImage, ResolutionSelector, QwenImage21Cache, KSampler, CLIPLoader, UNETLoader, VAEDecode, SaveImage, EmptyLatentImage, TextEncodeQwenImage21, JWInteger]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 900346733462798, "steps": 25, "width": 1024}
---

# 平台全量/Qwen-2.1图像高清+去水印_2103468302935879682.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-2.1图像高清+去水印_2103468302935879682.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Label (rgthree)`
- `VAELoader`
- `LoadImage`
- `ResolutionSelector`
- `QwenImage21Cache`
- `KSampler` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `JWInteger`

## 关键参数

- `seed` = `900346733462798`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`Label (rgthree)`、`VAELoader`、`LoadImage`、`ResolutionSelector`、`QwenImage21Cache`、`KSampler`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`JWInteger`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
