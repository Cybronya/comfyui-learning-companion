---
key: 图片生成/文生图/图图的蕾米埃尔·丹工作流_Tutu's Remielle Dan workflow_2069063026359234561.json
name: 图图的蕾米埃尔·丹工作流_Tutu's Remielle Dan workflow_2069063026359234561
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图图的蕾米埃尔·丹工作流_Tutu's Remielle Dan workflow_2069063026359234561.json
hash: 32ab9cedcf4e35dc
coverage: 0.909091
learned_at: 2026-10-19 23:23:00
nodes: [CLIPLoader, VAELoader, CLIPTextEncode, VAEDecode, KSampler, EmptyLatentImage, SaveImage, Note, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1520, "sampler_name": "er_sde", "scheduler": "simple", "seed": 486903739302064, "steps": 45, "width": 1024}
---

# 图片生成/文生图/图图的蕾米埃尔·丹工作流_Tutu's Remielle Dan workflow_2069063026359234561.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图图的蕾米埃尔·丹工作流_Tutu's Remielle Dan workflow_2069063026359234561.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `Note`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `486903739302064`
- `steps` = `45`
- `cfg` = `4`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1520`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`EmptyLatentImage`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader
