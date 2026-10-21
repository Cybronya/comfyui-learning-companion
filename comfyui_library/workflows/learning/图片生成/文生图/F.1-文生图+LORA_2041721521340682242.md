---
key: 图片生成/文生图/F.1-文生图+LORA_2041721521340682242.json
name: F.1-文生图+LORA_2041721521340682242
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1-文生图+LORA_2041721521340682242.json
hash: 92b48968b8530724
coverage: 1
learned_at: 2026-10-21 02:51:44
nodes: [RandomNoise, KSamplerSelect, BasicGuider, VAELoader, VAEDecode, DualCLIPLoader, CLIPTextEncode, BasicScheduler, UNETLoader, LoraLoaderModelOnly, EmptyLatentImage, SaveImage, SamplerCustomAdvanced]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1536, "width": 1024}
---

# 图片生成/文生图/F.1-文生图+LORA_2041721521340682242.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1-文生图+LORA_2041721521340682242.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `VAELoader`
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `SamplerCustomAdvanced` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`RandomNoise`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`VAEDecode`、`DualCLIPLoader`、`CLIPTextEncode`、`BasicScheduler`、`UNETLoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`SaveImage`、`SamplerCustomAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
