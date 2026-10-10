---
key: Wan2.2文生图工作流——comfyui官方版_1951146831617175554.json
name: Wan2.2文生图工作流——comfyui官方版_1951146831617175554
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2文生图工作流——comfyui官方版_1951146831617175554.json
hash: e730d131e1ae5311
coverage: 1
learned_at: 2026-10-10 20:59:14
nodes: [LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, VAELoader, KSampler, ModelSamplingSD3, UNETLoader, CLIPLoader, CLIPTextEncode, CLIPTextEncode, KSampler, VAEDecode, VAEDecode, EmptyHunyuanLatentVideo, LoraLoaderModelOnly, SaveImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "beta", "seed": 68775626476827, "steps": 10}
---

# Wan2.2文生图工作流——comfyui官方版_1951146831617175554.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2文生图工作流——comfyui官方版_1951146831617175554.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `VAELoader`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImage`

## 关键参数

- `seed` = `68775626476827`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingSD3`、`VAELoader`、`KSampler`、`CLIPLoader`、`CLIPTextEncode`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo
