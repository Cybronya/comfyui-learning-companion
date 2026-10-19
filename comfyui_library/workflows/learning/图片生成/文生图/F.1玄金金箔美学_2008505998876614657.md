---
key: 图片生成/文生图/F.1玄金金箔美学_2008505998876614657.json
name: F.1玄金金箔美学_2008505998876614657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/F.1玄金金箔美学_2008505998876614657.json
hash: d9fea9d3946398aa
coverage: 1
learned_at: 2026-10-19 22:00:29
nodes: [VAELoader, DualCLIPLoader, CLIPTextEncode, EmptySD3LatentImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ConditioningZeroOut, VAEDecode, SaveImage, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 403741177012914, "steps": 12}
---

# 图片生成/文生图/F.1玄金金箔美学_2008505998876614657.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/F.1玄金金箔美学_2008505998876614657.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output

**节点**（11 个）：
- `VAELoader`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心

## 关键参数

- `seed` = `403741177012914`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`VAELoader`、`DualCLIPLoader`、`CLIPTextEncode`、`EmptySD3LatentImage`、`UNETLoader`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、UNETLoader、SaveImage
