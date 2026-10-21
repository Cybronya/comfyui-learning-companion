---
key: 图片生成/文生图/【Supermate】Z-image-Base和Flux2 Klein天生一对工作流_2016511237093330945.json
name: 【Supermate】Z-image-Base和Flux2 Klein天生一对工作流_2016511237093330945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【Supermate】Z-image-Base和Flux2 Klein天生一对工作流_2016511237093330945.json
hash: 8796d7b8f1d61679
coverage: 0.958333
learned_at: 2026-10-19 22:15:48
nodes: [ModelSamplingAuraFlow, Label (rgthree), EmptySD3LatentImage, VAEDecode, ImageResize+, KSampler, ConditioningZeroOut, VAEDecode, easy cleanGpuUsed, VAEDecode, ModelSamplingAuraFlow, EmptySD3LatentImage, CLIPTextEncode, ReferenceLatent, VAEEncode, easy cleanGpuUsed, KSampler, SaveImage, VAELoader, CLIPLoader, VAELoader, CLIPLoader, CLIPTextEncode, CLIPLoader, SaveImage, CLIPTextEncode, ImageResize+, easy cleanGpuUsed, ConditioningZeroOut, CLIPLoader, easy cleanGpuUsed, KSampler, VAEDecode, SaveImage, ReferenceLatent, VAEEncode, UNETLoader, UNETLoader, UNETLoader, UNETLoader, VAELoader, VAELoader, Image Comparer (rgthree), KSampler, CLIPTextEncode, CLIPTextEncode, Fast Groups Bypasser (rgthree), CLIPTextEncode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 548249873467021, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/【Supermate】Z-image-Base和Flux2 Klein天生一对工作流_2016511237093330945.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【Supermate】Z-image-Base和Flux2 Klein天生一对工作流_2016511237093330945.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `ModelSamplingAuraFlow`
- `Label (rgthree)`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `ImageResize+`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `SaveImage`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ImageResize+`
- `easy cleanGpuUsed`
- `ConditioningZeroOut`
- `CLIPLoader`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `548249873467021`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **96%**（46/48）

**有卡**：`ModelSamplingAuraFlow`、`Label (rgthree)`、`EmptySD3LatentImage`、`VAEDecode`、`ImageResize+`、`KSampler`、`ConditioningZeroOut`、`easy cleanGpuUsed`、`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`SaveImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader、ReferenceLatent

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
