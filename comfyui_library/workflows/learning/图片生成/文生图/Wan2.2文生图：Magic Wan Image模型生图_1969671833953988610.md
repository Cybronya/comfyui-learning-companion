---
key: 图片生成/文生图/Wan2.2文生图：Magic Wan Image模型生图_1969671833953988610.json
name: Wan2.2文生图：Magic Wan Image模型生图_1969671833953988610.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图：Magic Wan Image模型生图_1969671833953988610.json
hash: 5af0b8fbcd83e336
coverage: 0.916667
learned_at: 2026-10-09 02:01:39
nodes: [ModelSamplingSD3, EmptyLatentImage, CLIPLoader, KSampler, VAEDecode, FluxResolutionNode, PrimitiveStringMultiline, CLIPTextEncode, CLIPTextEncode, VAELoader, UNETLoader, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": 1, "height": 1376, "sampler_name": "deis", "scheduler": "simple", "seed": 969272243003471, "steps": 30, "width": 768}
---

# 图片生成/文生图/Wan2.2文生图：Magic Wan Image模型生图_1969671833953988610.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1969671833953988610.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `ModelSamplingSD3`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxResolutionNode`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `768`
- `height` = `1376`
- `batch_size` = `1`
- `seed` = `969272243003471`
- `steps` = `30`
- `cfg` = `3`
- `sampler_name` = `deis`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`ModelSamplingSD3`、`EmptyLatentImage`、`CLIPLoader`、`KSampler`、`VAEDecode`、`FluxResolutionNode`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、FluxResolutionNode
