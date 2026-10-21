---
key: 图片生成/文生图/FLUX.1 LoRA模型工作流搭建_2014635794983555074.json
name: FLUX.1 LoRA模型工作流搭建_2014635794983555074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.1 LoRA模型工作流搭建_2014635794983555074.json
hash: 83433c39ea29aaba
coverage: 1
learned_at: 2026-10-19 22:14:57
nodes: [UNETLoader, LoraLoaderModelOnly, CLIPTextEncodeFlux, KSampler, DualCLIPLoader, VAELoader, EmptySD3LatentImage, ConditioningZeroOut, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 177986991850977, "steps": 20}
---

# 图片生成/文生图/FLUX.1 LoRA模型工作流搭建_2014635794983555074.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.1 LoRA模型工作流搭建_2014635794983555074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output

**节点**（10 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncodeFlux` ★核心
- `KSampler` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `EmptySD3LatentImage`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `177986991850977`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncodeFlux`、`KSampler`、`DualCLIPLoader`、`VAELoader`、`EmptySD3LatentImage`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、ConditioningZeroOut、CLIPTextEncodeFlux、DualCLIPLoader
