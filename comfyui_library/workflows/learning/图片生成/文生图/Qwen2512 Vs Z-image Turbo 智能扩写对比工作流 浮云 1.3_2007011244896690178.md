---
key: 图片生成/文生图/Qwen2512 Vs Z-image Turbo 智能扩写对比工作流 浮云 1.3_2007011244896690178.json
name: Qwen2512 Vs Z-image Turbo 智能扩写对比工作流 浮云 1.3_2007011244896690178
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2512 Vs Z-image Turbo 智能扩写对比工作流 浮云 1.3_2007011244896690178.json
hash: 337871801537cf31
coverage: 0.902439
learned_at: 2026-10-19 22:00:52
nodes: [CLIPTextEncode, CLIPLoader, VAELoader, CFGNorm, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, ModelSamplingAuraFlow, easy showAnything, KSampler, ModelSamplingAuraFlow, CFGNorm, LoraLoaderModelOnly, CLIPLoader, ConditioningZeroOut, CLIPTextEncode, VAELoader, KSampler, VAEDecode, VAEDecode, RH_LLMAPI_NODE, UnetLoaderGGUF, UNETLoader, PreviewImage, AddLabel, EmptySD3LatentImage, EmptyLatentImage, ImageConcatMulti, UNETLoader, VAEDecode, CR Prompt Text, KSampler, AddLabel, easy showAnything, EmptyLatentImage, AddLabel, SaveImage, SaveImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 304528444692195, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen2512 Vs Z-image Turbo 智能扩写对比工作流 浮云 1.3_2007011244896690178.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2512 Vs Z-image Turbo 智能扩写对比工作流 浮云 1.3_2007011244896690178.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGNorm`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `easy showAnything`
- `KSampler` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `RH_LLMAPI_NODE`
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `PreviewImage`
- `AddLabel`
- `EmptySD3LatentImage`
- `EmptyLatentImage` ★核心
- `ImageConcatMulti`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CR Prompt Text`
- `KSampler` ★核心
- `AddLabel`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `AddLabel`
- `SaveImage`
- `SaveImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `304528444692195`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（37/41）

**有卡**：`CLIPTextEncode`、`CLIPLoader`、`VAELoader`、`CFGNorm`、`LoraLoaderModelOnly`、`UNETLoader`、`ModelSamplingAuraFlow`、`KSampler`、`ConditioningZeroOut`、`VAEDecode`、`RH_LLMAPI_NODE`、`UnetLoaderGGUF`、`AddLabel`、`EmptySD3LatentImage`、`EmptyLatentImage`、`ImageConcatMulti`、`CR Prompt Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
