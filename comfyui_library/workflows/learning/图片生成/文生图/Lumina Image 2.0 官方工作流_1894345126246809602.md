---
key: 图片生成/文生图/Lumina Image 2.0 官方工作流_1894345126246809602.json
name: Lumina Image 2.0 官方工作流_1894345126246809602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Lumina Image 2.0 官方工作流_1894345126246809602.json
hash: c09789986a7a6cc4
coverage: 0.8
learned_at: 2026-10-10 20:58:46
nodes: [CheckpointLoaderSimple, VAEDecode, EmptySD3LatentImage, SaveImage, ModelSamplingAuraFlow, CLIPTextEncode, Note, Note, KSampler, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 4, "checkpoint": "lumina_2.safetensors", "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 526750517779995, "steps": 25}
---

# 图片生成/文生图/Lumina Image 2.0 官方工作流_1894345126246809602.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Lumina Image 2.0 官方工作流_1894345126246809602.json`

## 结构

**节点**（10 个）：
- `CheckpointLoaderSimple`
- `VAEDecode`
- `EmptySD3LatentImage`
- `SaveImage`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode`
- `Note`
- `Note`
- `KSampler`
- `CLIPTextEncode`

## 关键参数

- `cfg` = `4`
- `checkpoint` = `lumina_2.safetensors`
- `denoise` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `seed` = `526750517779995`
- `steps` = `25`

## 知识

覆盖率 **80%**（8/10）

**有卡**：`CheckpointLoaderSimple`、`VAEDecode`、`EmptySD3LatentImage`、`SaveImage`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`Note`
