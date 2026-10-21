---
key: 图片生成/文生图/Z-image文生图GGUF.json_2057397174631223298.json
name: Z-image文生图GGUF.json_2057397174631223298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image文生图GGUF.json_2057397174631223298.json
hash: 5981f47011939937
coverage: 1
learned_at: 2026-10-19 22:45:52
nodes: [SaveImage, VAELoader, ConditioningZeroOut, VAEDecode, CLIPTextEncode, EmptySD3LatentImage, ModelSamplingAuraFlow, KSampler, CLIPLoaderGGUF, UNETLoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 681512537629269, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image文生图GGUF.json_2057397174631223298.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image文生图GGUF.json_2057397174631223298.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `SaveImage`
- `VAELoader`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `CLIPLoaderGGUF`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `681512537629269`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`SaveImage`、`VAELoader`、`ConditioningZeroOut`、`VAEDecode`、`CLIPTextEncode`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`KSampler`、`CLIPLoaderGGUF`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、UNETLoader、CLIPLoaderGGUF、ClipLoaderGGUF

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
