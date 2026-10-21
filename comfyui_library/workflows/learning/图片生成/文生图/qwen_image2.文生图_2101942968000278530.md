---
key: 图片生成/文生图/qwen_image2.文生图_2101942968000278530.json
name: qwen_image2.文生图_2101942968000278530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen_image2.文生图_2101942968000278530.json
hash: bdac0f38dc180770
coverage: 0.9
learned_at: 2026-10-20 01:51:59
nodes: [VAEDecode, SaveImage, KSampler, CLIPLoader, UNETLoader, VAELoader, JjkText, ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 560093227128075, "steps": 25, "width": 1024}
---

# 图片生成/文生图/qwen_image2.文生图_2101942968000278530.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen_image2.文生图_2101942968000278530.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（10 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `JjkText`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `560093227128075`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`VAEDecode`、`SaveImage`、`KSampler`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
