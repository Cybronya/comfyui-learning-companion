---
key: sd3.5_large 生成双人合照_1848787187654594562.json
name: sd3.5_large 生成双人合照_1848787187654594562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/sd3.5_large 生成双人合照_1848787187654594562.json
hash: e671c8dc0c5e5c9b
coverage: 0.8125
learned_at: 2026-10-10 20:59:26
nodes: [VAEDecode, SaveImage, EmptySD3LatentImage, Note, CLIPLoader, DualCLIPLoader, Note, TripleCLIPLoader, CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, KSampler, SeargePromptText, RH_Prompter, ShowText|pysssss, SeargePromptText]
patterns: []
missing: []
parameters: {"cfg": 5.45, "checkpoint": "sd3.5_large.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 534920178543917, "steps": 25}
---

# sd3.5_large 生成双人合照_1848787187654594562.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/sd3.5_large 生成双人合照_1848787187654594562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `EmptySD3LatentImage`
- `Note`
- `CLIPLoader`
- `DualCLIPLoader`
- `Note`
- `TripleCLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SeargePromptText`
- `RH_Prompter`
- `ShowText|pysssss`
- `SeargePromptText`

## 关键参数

- `checkpoint` = `sd3.5_large.safetensors`
- `seed` = `534920178543917`
- `steps` = `25`
- `cfg` = `5.45`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`VAEDecode`、`SaveImage`、`EmptySD3LatentImage`、`CLIPLoader`、`DualCLIPLoader`、`TripleCLIPLoader`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`KSampler`、`SeargePromptText`、`RH_Prompter`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、DualCLIPLoader、RH_Prompter、SeargePromptText
