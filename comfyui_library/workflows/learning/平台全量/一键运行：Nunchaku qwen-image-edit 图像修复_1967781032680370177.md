---
key: 平台全量/一键运行：Nunchaku qwen-image-edit 图像修复_1967781032680370177.json
name: 一键运行：Nunchaku qwen-image-edit 图像修复_1967781032680370177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键运行：Nunchaku qwen-image-edit 图像修复_1967781032680370177.json
hash: ac7c58dec651e01b
coverage: 0.866667
learned_at: 2026-11-14 01:30:08
nodes: [NunchakuQwenImageDiTLoader, KSampler (Efficient), Seed Everywhere, TextEncodeQwenImageEdit, TextEncodeQwenImageEdit, PreviewImage, Prompts Everywhere, LoadImage, ModelSamplingAuraFlow, CLIPLoader, VAEEncode, VAELoader, Note, SaveImage, LayerFilter: HDREffects]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 863198421841779, "steps": 8}
---

# 平台全量/一键运行：Nunchaku qwen-image-edit 图像修复_1967781032680370177.json

> 来源文件 `comfyui_library/workflows/平台全量/一键运行：Nunchaku qwen-image-edit 图像修复_1967781032680370177.json`

## 结构

**生成流程**：Model → Encode → Sampling → Output → Other

**节点**（15 个）：
- `NunchakuQwenImageDiTLoader`
- `KSampler (Efficient)` ★核心
- `Seed Everywhere`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEdit`
- `PreviewImage`
- `Prompts Everywhere`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAEEncode` ★核心
- `VAELoader`
- `Note`
- `SaveImage`
- `LayerFilter: HDREffects`

## 关键参数

- `seed` = `863198421841779`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`NunchakuQwenImageDiTLoader`、`KSampler (Efficient)`、`Seed Everywhere`、`TextEncodeQwenImageEdit`、`Prompts Everywhere`、`LoadImage`、`ModelSamplingAuraFlow`、`CLIPLoader`、`VAEEncode`、`VAELoader`、`SaveImage`、`LayerFilter: HDREffects`

**用到的条目**：VAELoader、CLIPLoader、LoadImage、KSampler (Efficient)、Seed Everywhere、TextEncodeQwenImageEdit、VAEEncode、Prompts Everywhere
