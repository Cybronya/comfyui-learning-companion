---
key: 图片生成/文生图/z_image_turbo_basic_文生图_v14.0_yaowanli_2079045413621026817.json
name: z_image_turbo_basic_文生图_v14.0_yaowanli_2079045413621026817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z_image_turbo_basic_文生图_v14.0_yaowanli_2079045413621026817.json
hash: f14ff4f99e905bde
coverage: 1
learned_at: 2026-10-20 00:20:49
nodes: [UNETLoader, CLIPLoader, ModelSamplingAuraFlow, EmptySD3LatentImage, VAELoader, VAEDecode, KSampler, CLIPTextEncode, CLIPTextEncode, SaveImage, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 390598731116719, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/z_image_turbo_basic_文生图_v14.0_yaowanli_2079045413621026817.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z_image_turbo_basic_文生图_v14.0_yaowanli_2079045413621026817.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `390598731116719`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`UNETLoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`VAELoader`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`SaveImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
