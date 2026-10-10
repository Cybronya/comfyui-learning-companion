---
key: F.1 在线生图-文生图_1873981103047315457.json
name: F.1 在线生图-文生图_1873981103047315457
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1 在线生图-文生图_1873981103047315457.json
hash: 1c71f57ad6333e1b
coverage: 0.884615
learned_at: 2026-10-10 20:58:30
nodes: [SaveImage, SaveImage, SaveImage, EmptyLatentImage, Anything Everywhere3, UNETLoader, SaveImage, CLIPTextEncode, KSampler, ConditioningZeroOut, VAEDecode, KSampler, ConditioningZeroOut, KSampler, ConditioningZeroOut, KSampler, ConditioningZeroOut, VAEDecode, VAEDecode, VAEDecode, FluxGuidance, VAELoader, Anything Everywhere3, DualCLIPLoader, JjkText, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 851368470472983, "steps": 20, "width": 1024}
---

# F.1 在线生图-文生图_1873981103047315457.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1 在线生图-文生图_1873981103047315457.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `Anything Everywhere3`
- `UNETLoader` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `FluxGuidance`
- `VAELoader`
- `Anything Everywhere3`
- `DualCLIPLoader`
- `JjkText`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `851368470472983`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（23/26）

**有卡**：`SaveImage`、`EmptyLatentImage`、`UNETLoader`、`CLIPTextEncode`、`KSampler`、`ConditioningZeroOut`、`VAEDecode`、`FluxGuidance`、`VAELoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
