---
key: 图片生成/图生图/Qwen Image 2.1 双参考图换装编辑｜本地 GGUF 提示词增强_2101976709301096450.json
name: Qwen Image 2.1 双参考图换装编辑｜本地 GGUF 提示词增强_2101976709301096450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 双参考图换装编辑｜本地 GGUF 提示词增强_2101976709301096450.json
hash: e36a63af354bf5fb
coverage: 0.823529
learned_at: 2026-10-21 00:42:10
nodes: [VAELoader, UNETLoader, CLIPLoader, QwenImage21Cache, EmptyLatentImage, SaveImage, KSampler, VAEDecode, TextEncodeQwenImage21, LoadImage, LoadImage, ResolutionSelector, PreviewImage, LoadImage, LoadImage, JjkText, ComfySwitchNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 231146640399843, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 双参考图换装编辑｜本地 GGUF 提示词增强_2101976709301096450.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 双参考图换装编辑｜本地 GGUF 提示词增强_2101976709301096450.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `JjkText`
- `ComfySwitchNode`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `231146640399843`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`VAELoader`、`UNETLoader`、`CLIPLoader`、`QwenImage21Cache`、`EmptyLatentImage`、`SaveImage`、`KSampler`、`VAEDecode`、`TextEncodeQwenImage21`、`LoadImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
