---
key: 图片生成/文生图/qwen-image（0.2）_2038498159269253121.json
name: qwen-image（0.2）_2038498159269253121
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image（0.2）_2038498159269253121.json
hash: 68dd266dc37d78f2
coverage: 1
learned_at: 2026-10-21 02:57:33
nodes: [SaveImage, VAEDecode, VAELoader, KSampler, LoraLoaderModelOnly, UNETLoader, CLIPLoader, CLIPTextEncode, EmptyLatentImage, ConditioningZeroOut]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 135796245069966, "steps": 20, "width": 1080}
---

# 图片生成/文生图/qwen-image（0.2）_2038498159269253121.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image（0.2）_2038498159269253121.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（10 个）：
- `SaveImage`
- `VAEDecode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `135796245069966`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`SaveImage`、`VAEDecode`、`VAELoader`、`KSampler`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`ConditioningZeroOut`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
