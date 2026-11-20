---
key: 平台全量/QwenImage2.1-换头&换脸_2119621158348869633.json
name: QwenImage2.1-换头&换脸_2119621158348869633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/QwenImage2.1-换头&换脸_2119621158348869633.json
hash: f03b06f8d5df30a1
coverage: 0.8125
learned_at: 2026-11-14 00:53:22
nodes: [VAEDecode, KSampler, QwenImage21Cache, TextGenerateLTX2Prompt, TextEncodeQwenImage21, UNETLoader, BatchImagesNode, CLIPLoader, CLIPLoader, VAELoader, SaveImage, LoadImage, LoadImage, JjkText, Image Comparer (rgthree), MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 392812574211115, "steps": 50}
---

# 平台全量/QwenImage2.1-换头&换脸_2119621158348869633.json

> 来源文件 `comfyui_library/workflows/平台全量/QwenImage2.1-换头&换脸_2119621158348869633.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `JjkText`
- `Image Comparer (rgthree)`
- `MarkdownNote`

## 关键参数

- `seed` = `392812574211115`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`UNETLoader`、`BatchImagesNode`、`CLIPLoader`、`VAELoader`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
