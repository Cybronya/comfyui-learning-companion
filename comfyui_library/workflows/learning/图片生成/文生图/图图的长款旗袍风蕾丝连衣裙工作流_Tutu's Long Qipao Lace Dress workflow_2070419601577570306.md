---
key: 图片生成/文生图/图图的长款旗袍风蕾丝连衣裙工作流_Tutu's Long Qipao Lace Dress workflow_2070419601577570306.json
name: 图图的长款旗袍风蕾丝连衣裙工作流_Tutu's Long Qipao Lace Dress workflow_2070419601577570306
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图图的长款旗袍风蕾丝连衣裙工作流_Tutu's Long Qipao Lace Dress workflow_2070419601577570306.json
hash: 60de3e5646f0dcb3
coverage: 0.909091
learned_at: 2026-10-19 23:43:12
nodes: [EmptyLatentImage, ConditioningZeroOut, VAELoader, VAEDecode, UNETLoader, Note, CLIPLoader, CLIPTextEncode, KSampler, SaveImage, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "ddim", "scheduler": "sgm_uniform", "seed": 125378883435496, "steps": 10, "width": 1080}
---

# 图片生成/文生图/图图的长款旗袍风蕾丝连衣裙工作流_Tutu's Long Qipao Lace Dress workflow_2070419601577570306.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图图的长款旗袍风蕾丝连衣裙工作流_Tutu's Long Qipao Lace Dress workflow_2070419601577570306.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `Note`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `125378883435496`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `ddim`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`EmptyLatentImage`、`ConditioningZeroOut`、`VAELoader`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`KSampler`、`SaveImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
