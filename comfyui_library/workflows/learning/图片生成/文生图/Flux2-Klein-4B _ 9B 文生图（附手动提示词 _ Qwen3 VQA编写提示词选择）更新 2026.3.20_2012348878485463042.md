---
key: 图片生成/文生图/Flux2-Klein-4B _ 9B 文生图（附手动提示词 _ Qwen3 VQA编写提示词选择）更新 2026.3.20_2012348878485463042.json
name: Flux2-Klein-4B _ 9B 文生图（附手动提示词 _ Qwen3 VQA编写提示词选择）更新 2026.3.20_2012348878485463042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux2-Klein-4B _ 9B 文生图（附手动提示词 _ Qwen3 VQA编写提示词选择）更新 2026.3.20_2012348878485463042.json
hash: c9ebb67dcc5b0ba9
coverage: 0.744681
learned_at: 2026-10-19 22:15:05
nodes: [easy int, easy int, CLIPLoader, CLIPLoader, JjkText, easy anythingIndexSwitch, Qwen3_VQA_Plus, PreviewAny, CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, PrimitiveNode, Note, UNETLoader, UNETLoader, VAELoader, easy anythingIndexSwitch, ConditioningZeroOut, easy int, LoraLoaderModelOnly, Note, Note, easy anythingIndexSwitch, PathchSageAttentionKJ, ModelPatchTorchSettings, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), EmptyFlux2LatentImage, CLIPTextEncode, ModelSamplingAuraFlow, easy cleanGpuUsed, ConditioningZeroOut, CLIPTextEncode, JjkText, Fast Groups Bypasser (rgthree), VAEDecode, SaveImage, VAEEncode, KSampler, KSampler, Note, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, VAEDecode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 393751833571792, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Flux2-Klein-4B _ 9B 文生图（附手动提示词 _ Qwen3 VQA编写提示词选择）更新 2026.3.20_2012348878485463042.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux2-Klein-4B _ 9B 文生图（附手动提示词 _ Qwen3 VQA编写提示词选择）更新 2026.3.20_2012348878485463042.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `easy int`
- `easy int`
- `CLIPLoader`
- `CLIPLoader`
- `JjkText`
- `easy anythingIndexSwitch`
- `Qwen3_VQA_Plus`
- `PreviewAny`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `Note`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `easy anythingIndexSwitch`
- `ConditioningZeroOut`
- `easy int`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `easy anythingIndexSwitch`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `easy cleanGpuUsed`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `JjkText`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `Note`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `VAEDecode` ★核心

## 关键参数

- `seed` = `393751833571792`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（35/47）

**有卡**：`easy int`、`CLIPLoader`、`easy anythingIndexSwitch`、`Qwen3_VQA_Plus`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`EmptyFlux2LatentImage`、`ModelSamplingAuraFlow`、`easy cleanGpuUsed`、`VAEDecode`、`SaveImage`、`VAEEncode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
