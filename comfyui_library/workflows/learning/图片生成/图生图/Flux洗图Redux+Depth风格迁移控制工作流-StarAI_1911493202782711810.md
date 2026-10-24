---
key: 图片生成/图生图/Flux洗图Redux+Depth风格迁移控制工作流-StarAI_1911493202782711810.json
name: Flux洗图Redux+Depth风格迁移控制工作流-StarAI_1911493202782711810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux洗图Redux+Depth风格迁移控制工作流-StarAI_1911493202782711810.json
hash: 312b64e99b1d419b
coverage: 0.925926
learned_at: 2026-10-23 11:02:14
nodes: [Florence2Run, Florence2ModelLoader, easy showAnything, StyleModelApply, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, Text Concatenate (JPS), CR Prompt Text, CR Latent Batch Size, InstructPixToPixConditioning, VAEDecode, LoadImage, PreviewImage, CLIPVisionEncode, StyleModelLoader, CLIPVisionLoader, AIO_Preprocessor, VAELoader, DualCLIPLoader, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, SaveImage, LoadImage, Note Plus (mtb)]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 344325017125160, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux洗图Redux+Depth风格迁移控制工作流-StarAI_1911493202782711810.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux洗图Redux+Depth风格迁移控制工作流-StarAI_1911493202782711810.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（27 个）：
- `Florence2Run`
- `Florence2ModelLoader`
- `easy showAnything`
- `StyleModelApply`
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `Text Concatenate (JPS)`
- `CR Prompt Text`
- `CR Latent Batch Size`
- `InstructPixToPixConditioning`
- `VAEDecode` ★核心
- `LoadImage`
- `PreviewImage`
- `CLIPVisionEncode`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `AIO_Preprocessor`
- `VAELoader`
- `DualCLIPLoader`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `Note Plus (mtb)`

## 关键参数

- `seed` = `344325017125160`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`Florence2Run`、`Florence2ModelLoader`、`StyleModelApply`、`ConditioningZeroOut`、`FluxGuidance`、`CLIPTextEncode`、`Text Concatenate (JPS)`、`CR Prompt Text`、`CR Latent Batch Size`、`InstructPixToPixConditioning`、`VAEDecode`、`LoadImage`、`CLIPVisionEncode`、`StyleModelLoader`、`CLIPVisionLoader`、`AIO_Preprocessor`、`VAELoader`、`DualCLIPLoader`、`KSampler`、`LoraLoaderModelOnly`、`UNETLoader`、`SaveImage`、`Note Plus (mtb)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
