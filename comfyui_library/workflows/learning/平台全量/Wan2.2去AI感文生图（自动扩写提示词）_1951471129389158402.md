---
key: 平台全量/Wan2.2去AI感文生图（自动扩写提示词）_1951471129389158402.json
name: Wan2.2去AI感文生图（自动扩写提示词）_1951471129389158402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2去AI感文生图（自动扩写提示词）_1951471129389158402.json
hash: 441b55e7355f24f8
coverage: 0.863636
learned_at: 2026-11-14 01:06:20
nodes: [LoraLoader, LoraLoader, LoraLoader, CR Text Concatenate, UNETLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, SaveImage, CLIPLoader, VAELoader, CR Text, RH_LLMAPI_NODE, easy showAnything, KSampler, ImpactSwitch, CFGZeroStarAndInit, CLIPTextEncode, VAEDecode, ImpactInt, ImpactInt, MarkdownNote, CR Text]
patterns: [lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Wan2.1_T2V_14B_FusionX_LoRA.safetensors", "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 860958430634636, "steps": 8, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.2去AI感文生图（自动扩写提示词）_1951471129389158402.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2去AI感文生图（自动扩写提示词）_1951471129389158402.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `CR Text Concatenate`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `CR Text`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `KSampler` ★核心
- `ImpactSwitch`
- `CFGZeroStarAndInit`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ImpactInt`
- `ImpactInt`
- `MarkdownNote`
- `CR Text`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `Wan2.1_T2V_14B_FusionX_LoRA.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `860958430634636`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`LoraLoader`、`CR Text Concatenate`、`UNETLoader`、`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`SaveImage`、`CLIPLoader`、`VAELoader`、`CR Text`、`RH_LLMAPI_NODE`、`KSampler`、`CFGZeroStarAndInit`、`VAEDecode`、`ImpactInt`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、UNETLoader、CFGZeroStarAndInit、EmptyHunyuanLatentVideo

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
