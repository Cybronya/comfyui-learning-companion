---
key: 图片生成/文生图/Lumina Image 2.0 官方工作流_1894345126246809602.json
name: Lumina Image 2.0 官方工作流_1894345126246809602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Lumina Image 2.0 官方工作流_1894345126246809602.json
hash: c09789986a7a6cc4
coverage: 0.8
learned_at: 2026-10-07 03:17:59
nodes: [CheckpointLoaderSimple, VAEDecode, EmptySD3LatentImage, SaveImage, ModelSamplingAuraFlow, CLIPTextEncode, Note, Note, KSampler, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "checkpoint": "lumina_2.safetensors", "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 526750517779995, "steps": 25}
---

# 图片生成/文生图/Lumina Image 2.0 官方工作流_1894345126246809602.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Lumina Image 2.0 官方工作流_1894345126246809602.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `SaveImage`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `lumina_2.safetensors`
- `seed` = `526750517779995`
- `steps` = `25`
- `cfg` = `4`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（8/10）

**有卡**：`CheckpointLoaderSimple`、`VAEDecode`、`EmptySD3LatentImage`、`SaveImage`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、SaveImage、EmptySD3LatentImage、ModelSamplingAuraFlow、sd15-t2i-basic
