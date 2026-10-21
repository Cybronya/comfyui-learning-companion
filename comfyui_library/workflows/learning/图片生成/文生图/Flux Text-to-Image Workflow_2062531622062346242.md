---
key: 图片生成/文生图/Flux Text-to-Image Workflow_2062531622062346242.json
name: Flux Text-to-Image Workflow_2062531622062346242
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux Text-to-Image Workflow_2062531622062346242.json
hash: e94a75c104968aa9
coverage: 0.947368
learned_at: 2026-10-19 23:02:21
nodes: [KSamplerSelect, RandomNoise, BasicScheduler, VAELoader, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, UNETLoader, BasicGuider, CLIPTextEncode, CLIPTextEncode, DualCLIPLoader, VAEDecode, SaveImage, SamplerCustomAdvanced, PreviewImage, EmptyLatentImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 720, "width": 1280}
---

# 图片生成/文生图/Flux Text-to-Image Workflow_2062531622062346242.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux Text-to-Image Workflow_2062531622062346242.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `BasicScheduler`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `BasicGuider`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`KSamplerSelect`、`RandomNoise`、`BasicScheduler`、`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`BasicGuider`、`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`SamplerCustomAdvanced`、`EmptyLatentImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、EmptyLatentImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、SaveImage
