---
key: 图片生成/文生图/qwen-image（0.2）_2038786485712850946.json
name: qwen-image（0.2）_2038786485712850946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image（0.2）_2038786485712850946.json
hash: 7a679e86d3aa58fe
coverage: 1
learned_at: 2026-10-21 02:57:33
nodes: [VAEDecode, VAELoader, KSampler, CLIPLoader, EmptyLatentImage, ConditioningZeroOut, UNETLoader, CLIPTextEncode, SaveImage, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 761454328905493, "steps": 20, "width": 1080}
---

# 图片生成/文生图/qwen-image（0.2）_2038786485712850946.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image（0.2）_2038786485712850946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（10 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `761454328905493`
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

**有卡**：`VAEDecode`、`VAELoader`、`KSampler`、`CLIPLoader`、`EmptyLatentImage`、`ConditioningZeroOut`、`UNETLoader`、`CLIPTextEncode`、`SaveImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
