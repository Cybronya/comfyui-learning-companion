---
key: comfyui-workflow-templates-json/hidream_i1_dev.json
name: hidream_i1_dev
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/hidream_i1_dev.json
hash: 39f47cb27b7baacc
official: true
coverage: 0.833333
learned_at: 2026-10-07 21:35:29
nodes: [VAELoader, QuadrupleCLIPLoader, UNETLoader, EmptySD3LatentImage, CLIPTextEncode, VAEDecode, KSampler, SaveImage, MarkdownNote, CLIPTextEncode, ModelSamplingSD3, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "normal", "seed": 426270906276990, "steps": 28}
---

# comfyui-workflow-templates-json/hidream_i1_dev.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/hidream_i1_dev.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `VAELoader`
- `QuadrupleCLIPLoader`
- `UNETLoader` ★核心
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `MarkdownNote`

## 关键参数

- `seed` = `426270906276990`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`VAELoader`、`QuadrupleCLIPLoader`、`UNETLoader`、`EmptySD3LatentImage`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`SaveImage`、`ModelSamplingSD3`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、QuadrupleCLIPLoader、SaveImage、EmptySD3LatentImage
