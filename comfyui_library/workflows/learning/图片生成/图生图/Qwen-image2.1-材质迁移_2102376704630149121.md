---
key: 图片生成/图生图/Qwen-image2.1-材质迁移_2102376704630149121.json
name: Qwen-image2.1-材质迁移_2102376704630149121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-材质迁移_2102376704630149121.json
hash: 3cacec5573ee7cd4
coverage: 0.818182
learned_at: 2026-10-10 20:48:09
nodes: [PreviewImage, UNETLoader, CLIPLoader, VAELoader, KSampler, SaveImage, VAEDecode, TextEncodeQwenImage21, Image Comparer (rgthree), LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 794579175216495, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-材质迁移_2102376704630149121.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-材质迁移_2102376704630149121.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（11 个）：
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `794579175216495`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImage21`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、SaveImage
