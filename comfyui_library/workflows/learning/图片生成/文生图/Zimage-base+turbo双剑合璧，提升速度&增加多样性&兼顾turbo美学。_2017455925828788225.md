---
key: 图片生成/文生图/Zimage-base+turbo双剑合璧，提升速度&增加多样性&兼顾turbo美学。_2017455925828788225.json
name: Zimage-base+turbo双剑合璧，提升速度&增加多样性&兼顾turbo美学。_2017455925828788225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Zimage-base+turbo双剑合璧，提升速度&增加多样性&兼顾turbo美学。_2017455925828788225.json
hash: ae1e91b919f8a891
coverage: 0.761905
learned_at: 2026-10-19 22:15:38
nodes: [ModelSamplingAuraFlow, CLIPLoader, VAEDecode, ConditioningZeroOut, CLIPTextEncode, CLIPTextEncode, UNETLoader, KSampler, UNETLoader, KSampler, VAELoader, EmptySD3LatentImage, VAEDecode, LoraLoaderModelOnly, Note, Note, StringConcatenate, PrimitiveStringMultiline, Note, PreviewImage, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 460215711258301, "steps": 20}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Zimage-base+turbo双剑合璧，提升速度&增加多样性&兼顾turbo美学。_2017455925828788225.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Zimage-base+turbo双剑合璧，提升速度&增加多样性&兼顾turbo美学。_2017455925828788225.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAELoader`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `Note`
- `PreviewImage`
- `SaveImage`

## 关键参数

- `seed` = `460215711258301`
- `steps` = `20`
- `cfg` = `4`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`ModelSamplingAuraFlow`、`CLIPLoader`、`VAEDecode`、`ConditioningZeroOut`、`CLIPTextEncode`、`UNETLoader`、`KSampler`、`VAELoader`、`EmptySD3LatentImage`、`LoraLoaderModelOnly`、`StringConcatenate`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
