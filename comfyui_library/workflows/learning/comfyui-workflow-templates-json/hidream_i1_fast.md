---
key: comfyui-workflow-templates-json/hidream_i1_fast.json
name: hidream_i1_fast
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/hidream_i1_fast.json
hash: c2a6a09ef218fa2c
official: true
coverage: 0.833333
learned_at: 2026-10-10 22:47:19
nodes: [VAELoader, QuadrupleCLIPLoader, UNETLoader, ModelSamplingSD3, CLIPTextEncode, EmptySD3LatentImage, KSampler, MarkdownNote, VAEDecode, SaveImage, CLIPTextEncode, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "normal", "seed": 833271177511441, "steps": 16}
---

# comfyui-workflow-templates-json/hidream_i1_fast.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/hidream_i1_fast.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `VAELoader`
- `QuadrupleCLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `MarkdownNote`

## 关键参数

- `seed` = `833271177511441`
- `steps` = `16`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`VAELoader`、`QuadrupleCLIPLoader`、`UNETLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`EmptySD3LatentImage`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、QuadrupleCLIPLoader、SaveImage、EmptySD3LatentImage
