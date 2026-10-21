---
key: 图片生成/文生图/Z-image-trubo-Engineer v6提示词扩展+Dopsd最高质量文生图V1_2064643788697591810.json
name: Z-image-trubo-Engineer v6提示词扩展+Dopsd最高质量文生图V1_2064643788697591810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-trubo-Engineer v6提示词扩展+Dopsd最高质量文生图V1_2064643788697591810.json
hash: 94e22ea599bc9d47
coverage: 0.866667
learned_at: 2026-10-19 23:21:59
nodes: [VAEDecode, CLIPTextEncode, KSampler, LoraLoaderModelOnly, EmptySD3LatentImage, QwenImageEngineer, VAELoader, UNETLoader, ConditioningZeroOut, CR Prompt Text, PreviewAny, PreviewAny, SaveImage, ClipLoaderGGUF, QwenImageEngineer]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 42, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image-trubo-Engineer v6提示词扩展+Dopsd最高质量文生图V1_2064643788697591810.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-trubo-Engineer v6提示词扩展+Dopsd最高质量文生图V1_2064643788697591810.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptySD3LatentImage`
- `QwenImageEngineer`
- `VAELoader`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `CR Prompt Text`
- `PreviewAny`
- `PreviewAny`
- `SaveImage`
- `ClipLoaderGGUF`
- `QwenImageEngineer`

## 关键参数

- `seed` = `42`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`KSampler`、`LoraLoaderModelOnly`、`EmptySD3LatentImage`、`QwenImageEngineer`、`VAELoader`、`UNETLoader`、`ConditioningZeroOut`、`CR Prompt Text`、`SaveImage`、`ClipLoaderGGUF`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、UNETLoader、CLIPLoaderGGUF

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
