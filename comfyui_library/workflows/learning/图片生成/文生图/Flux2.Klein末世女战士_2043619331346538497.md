---
key: 图片生成/文生图/Flux2.Klein末世女战士_2043619331346538497.json
name: Flux2.Klein末世女战士_2043619331346538497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux2.Klein末世女战士_2043619331346538497.json
hash: c0ca636476d0ce5a
coverage: 0.861538
learned_at: 2026-10-21 02:52:14
nodes: [KSamplerSelect, SamplerCustomAdvanced, EmptyFlux2LatentImage, CLIPTextEncode, PrimitiveInt, PrimitiveInt, CLIPLoader, VAELoader, CLIPTextEncode, KSamplerSelect, SamplerCustomAdvanced, EmptyFlux2LatentImage, PrimitiveInt, PrimitiveInt, UNETLoader, VAELoader, CFGGuider, ConditioningZeroOut, CLIPTextEncode, Flux2Scheduler, KSamplerSelect, EmptyFlux2LatentImage, PrimitiveInt, PrimitiveInt, ConditioningZeroOut, CLIPTextEncode, UNETLoader, CLIPLoader, SamplerCustomAdvanced, CFGGuider, Flux2Scheduler, VAEDecode, VAEDecode, VAEDecode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, VAEDecode, RandomNoise, RandomNoise, RandomNoise, Flux2Scheduler, CFGGuider, CFGNorm, SaveImage, CLIPLoader, PrimitiveStringMultiline, VAELoader, UNETLoader, SaveImage, SaveImage, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, AddLabel, MarkdownNote, AddLabel, AddLabel, AddLabel, ImageConcatMulti, SaveImage, SaveImage, PrimitiveStringMultiline]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 0, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Flux2.Klein末世女战士_2043619331346538497.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux2.Klein末世女战士_2043619331346538497.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `VAELoader`
- `CFGGuider`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `RandomNoise`
- `RandomNoise`
- `RandomNoise`
- `Flux2Scheduler`
- `CFGGuider`
- `CFGNorm`
- `SaveImage`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `VAELoader`
- `UNETLoader` ★核心
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `AddLabel`
- `MarkdownNote`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `SaveImage`
- `SaveImage`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `0`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（56/65）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`CFGGuider`、`ConditioningZeroOut`、`Flux2Scheduler`、`VAEDecode`、`EmptySD3LatentImage`、`KSampler`、`ModelSamplingAuraFlow`、`RandomNoise`、`CFGNorm`、`SaveImage`、`AddLabel`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、CFGGuider

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
