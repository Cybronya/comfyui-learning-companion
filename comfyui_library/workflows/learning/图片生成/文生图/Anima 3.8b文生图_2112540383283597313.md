---
key: 图片生成/文生图/Anima 3.8b文生图_2112540383283597313.json
name: Anima 3.8b文生图_2112540383283597313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Anima 3.8b文生图_2112540383283597313.json
hash: e7444bc147be98e5
coverage: 1
learned_at: 2026-10-21 02:51:19
nodes: [Anima38BV2Prompt, KSampler, SaveImage, VAELoader, CLIPLoader, Anima38BV2Loader, EmptySD3LatentImage, VAEDecode, Anima38BV2Prompt, Text, AnimaQwen35Loader]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "beta", "seed": 20261002, "steps": 40}
---

# 图片生成/文生图/Anima 3.8b文生图_2112540383283597313.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Anima 3.8b文生图_2112540383283597313.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `Anima38BV2Prompt`
- `KSampler` ★核心
- `SaveImage`
- `VAELoader`
- `CLIPLoader`
- `Anima38BV2Loader`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `Anima38BV2Prompt`
- `Text`
- `AnimaQwen35Loader`

## 关键参数

- `seed` = `20261002`
- `steps` = `40`
- `cfg` = `5`
- `sampler_name` = `res_multistep`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`Anima38BV2Prompt`、`KSampler`、`SaveImage`、`VAELoader`、`CLIPLoader`、`Anima38BV2Loader`、`EmptySD3LatentImage`、`VAEDecode`、`Text`、`AnimaQwen35Loader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、Anima38BV2Prompt、SaveImage、EmptySD3LatentImage、Text
