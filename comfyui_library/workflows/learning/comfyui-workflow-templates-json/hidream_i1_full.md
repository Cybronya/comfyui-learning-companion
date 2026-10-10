---
key: comfyui-workflow-templates-json/hidream_i1_full.json
name: hidream_i1_full
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/hidream_i1_full.json
hash: 0992df685679cf0a
official: true
coverage: 0.833333
learned_at: 2026-10-10 22:47:20
nodes: [VAEDecode, CLIPTextEncode, EmptySD3LatentImage, CLIPTextEncode, KSampler, ModelSamplingSD3, QuadrupleCLIPLoader, VAELoader, UNETLoader, MarkdownNote, SaveImage, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 647719102242276, "steps": 50}
---

# comfyui-workflow-templates-json/hidream_i1_full.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/hidream_i1_full.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `ModelSamplingSD3`
- `QuadrupleCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `MarkdownNote`
- `SaveImage`
- `MarkdownNote`

## 关键参数

- `seed` = `647719102242276`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **83%**（10/12）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`EmptySD3LatentImage`、`KSampler`、`ModelSamplingSD3`、`QuadrupleCLIPLoader`、`VAELoader`、`UNETLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、QuadrupleCLIPLoader、SaveImage、EmptySD3LatentImage
