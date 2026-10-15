---
key: 图片生成/文生图/WAN2.2文生图_1953166220825718786.json
name: WAN2.2文生图_1953166220825718786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAN2.2文生图_1953166220825718786.json
hash: a03d2f3d5b1aeaf7
coverage: 0.941176
learned_at: 2026-10-10 20:59:13
nodes: [CLIPLoader, VAELoader, UNETLoader, UNETLoader, EmptySD3LatentImage, LoadImage, KSampler, LoadImage, KSampler, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, VAEDecode, RH_LLMAPI_NODE, PreviewImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "heun", "scheduler": "simple", "seed": 678250135486522, "steps": 20}
---

# 图片生成/文生图/WAN2.2文生图_1953166220825718786.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WAN2.2文生图_1953166220825718786.json`

## 结构

**节点**（17 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader`
- `UNETLoader`
- `EmptySD3LatentImage`
- `LoadImage`
- `KSampler`
- `LoadImage`
- `KSampler`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `VAEDecode`
- `RH_LLMAPI_NODE`
- `PreviewImage`
- `SaveImage`

## 关键参数

- `cfg` = `1`
- `denoise` = `0.30000000000000004`
- `sampler_name` = `heun`
- `scheduler` = `simple`
- `seed` = `678250135486522`
- `steps` = `20`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`EmptySD3LatentImage`、`LoadImage`、`KSampler`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAEDecode`、`RH_LLMAPI_NODE`、`PreviewImage`
