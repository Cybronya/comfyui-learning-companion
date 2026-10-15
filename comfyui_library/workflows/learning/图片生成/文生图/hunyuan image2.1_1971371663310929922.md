---
key: 图片生成/文生图/hunyuan image2.1_1971371663310929922.json
name: hunyuan image2.1_1971371663310929922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/hunyuan image2.1_1971371663310929922.json
hash: 77f36881e8cd5b84
coverage: 1
learned_at: 2026-10-10 20:59:21
nodes: [CLIPTextEncode, DualCLIPLoader, UNETLoader, ModelSamplingSD3, VAEDecode, SaveImage, VAELoader, EmptyHunyuanImageLatent, KSampler, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 210500120531898, "steps": 20}
---

# 图片生成/文生图/hunyuan image2.1_1971371663310929922.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/hunyuan image2.1_1971371663310929922.json`

## 结构

**节点**（10 个）：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `UNETLoader`
- `ModelSamplingSD3`
- `VAEDecode`
- `SaveImage`
- `VAELoader`
- `EmptyHunyuanImageLatent`
- `KSampler`
- `CLIPTextEncode`

## 关键参数

- `cfg` = `3`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `seed` = `210500120531898`
- `steps` = `20`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`CLIPTextEncode`、`DualCLIPLoader`、`UNETLoader`、`ModelSamplingSD3`、`VAEDecode`、`SaveImage`、`VAELoader`、`EmptyHunyuanImageLatent`、`KSampler`
