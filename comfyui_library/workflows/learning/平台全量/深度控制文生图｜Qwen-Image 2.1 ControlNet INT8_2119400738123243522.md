---
key: 平台全量/深度控制文生图｜Qwen-Image 2.1 ControlNet INT8_2119400738123243522.json
name: 深度控制文生图｜Qwen-Image 2.1 ControlNet INT8_2119400738123243522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/深度控制文生图｜Qwen-Image 2.1 ControlNet INT8_2119400738123243522.json
hash: 2f508381f44a8f9d
coverage: 1
learned_at: 2026-11-14 02:20:15
nodes: [UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, SaveImage, QwenImage21Cache, BasicScheduler, ModelPatchLoader, ZImageFunControlnet, EmptyLatentImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 768, "width": 768}
---

# 平台全量/深度控制文生图｜Qwen-Image 2.1 ControlNet INT8_2119400738123243522.json

> 来源文件 `comfyui_library/workflows/平台全量/深度控制文生图｜Qwen-Image 2.1 ControlNet INT8_2119400738123243522.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `QwenImage21Cache`
- `BasicScheduler`
- `ModelPatchLoader`
- `ZImageFunControlnet`
- `EmptyLatentImage` ★核心
- `LoadImage`

## 关键参数

- `width` = `768`
- `height` = `768`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`QwenImage21Cache`、`BasicScheduler`、`ModelPatchLoader`、`ZImageFunControlnet`、`EmptyLatentImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、QwenImage21Cache、UNETLoader
