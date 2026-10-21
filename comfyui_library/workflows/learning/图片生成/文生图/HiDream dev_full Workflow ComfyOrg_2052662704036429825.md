---
key: 图片生成/文生图/HiDream dev_full Workflow ComfyOrg_2052662704036429825.json
name: HiDream dev_full Workflow ComfyOrg_2052662704036429825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/HiDream dev_full Workflow ComfyOrg_2052662704036429825.json
hash: 9299668ff5203ff8
coverage: 0.846154
learned_at: 2026-10-21 02:52:38
nodes: [CLIPTextEncode, ModelSamplingSD3, VAEDecode, VAELoader, QuadrupleCLIPLoader, EmptySD3LatentImage, SaveImage, MarkdownNote, KSampler, UNETLoader, UNETLoader, Note, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "lcm", "scheduler": "simple", "seed": 743518407693938, "steps": 28}
---

# 图片生成/文生图/HiDream dev_full Workflow ComfyOrg_2052662704036429825.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/HiDream dev_full Workflow ComfyOrg_2052662704036429825.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `VAELoader`
- `QuadrupleCLIPLoader`
- `EmptySD3LatentImage`
- `SaveImage`
- `MarkdownNote`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Note`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `743518407693938`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`VAEDecode`、`VAELoader`、`QuadrupleCLIPLoader`、`EmptySD3LatentImage`、`SaveImage`、`KSampler`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、QuadrupleCLIPLoader、SaveImage、EmptySD3LatentImage
