---
key: 图片生成/文生图/Z-image+Qwen3.5+Rtx超分优化生成2k图_2045497337547595778.json
name: Z-image+Qwen3.5+Rtx超分优化生成2k图_2045497337547595778
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image+Qwen3.5+Rtx超分优化生成2k图_2045497337547595778.json
hash: 6cfc89261c142100
coverage: 0.941176
learned_at: 2026-10-21 02:56:13
nodes: [ShowText, CLIPTextEncode, ConditioningZeroOut, MarkdownNote, UNETLoader, ModelSamplingAuraFlow, VAELoader, SaveImage, EmptySD3LatentImage, VAEDecode, RTXVideoSuperResolution, CLIPLoader, llama_cpp_model_loader, KSampler, llama_cpp_instruct_adv, LoraLoaderModelOnly, Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 83771091090635, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image+Qwen3.5+Rtx超分优化生成2k图_2045497337547595778.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image+Qwen3.5+Rtx超分优化生成2k图_2045497337547595778.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `ShowText`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `MarkdownNote`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `VAELoader`
- `SaveImage`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `RTXVideoSuperResolution`
- `CLIPLoader`
- `llama_cpp_model_loader`
- `KSampler` ★核心
- `llama_cpp_instruct_adv`
- `LoraLoaderModelOnly` ★核心
- `Text`

## 关键参数

- `seed` = `83771091090635`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`ShowText`、`CLIPTextEncode`、`ConditioningZeroOut`、`UNETLoader`、`ModelSamplingAuraFlow`、`VAELoader`、`SaveImage`、`EmptySD3LatentImage`、`VAEDecode`、`RTXVideoSuperResolution`、`CLIPLoader`、`llama_cpp_model_loader`、`KSampler`、`llama_cpp_instruct_adv`、`LoraLoaderModelOnly`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
