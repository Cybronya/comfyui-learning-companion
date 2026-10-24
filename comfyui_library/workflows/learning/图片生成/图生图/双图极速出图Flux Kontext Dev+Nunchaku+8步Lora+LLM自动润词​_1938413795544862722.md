---
key: 图片生成/图生图/双图极速出图Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词​_1938413795544862722.json
name: 双图极速出图Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词​_1938413795544862722
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/双图极速出图Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词​_1938413795544862722.json
hash: 7b8ed5adfa5ed7e8
coverage: 1
learned_at: 2026-10-23 12:35:02
nodes: [FluxGuidance, ReferenceLatent, VAEEncode, LoadImage, LoadImage, FluxKontextImageScale, ImageStitch, VAELoader, KSampler, ConditioningZeroOut, RH_LLMAPI_NODE, Text Multiline, Int, Int, VAEDecode, CLIPTextEncode, EmptySD3LatentImage, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, SaveImage, DualCLIPLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1018968724453103, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/双图极速出图Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词​_1938413795544862722.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/双图极速出图Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词​_1938413795544862722.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `FluxGuidance`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `LoadImage`
- `LoadImage`
- `FluxKontextImageScale`
- `ImageStitch`
- `VAELoader`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `RH_LLMAPI_NODE`
- `Text Multiline`
- `Int`
- `Int`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `DualCLIPLoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1018968724453103`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`FluxGuidance`、`ReferenceLatent`、`VAEEncode`、`LoadImage`、`FluxKontextImageScale`、`ImageStitch`、`VAELoader`、`KSampler`、`ConditioningZeroOut`、`RH_LLMAPI_NODE`、`Text Multiline`、`Int`、`VAEDecode`、`CLIPTextEncode`、`EmptySD3LatentImage`、`NunchakuFluxLoraLoader`、`NunchakuFluxDiTLoader`、`SaveImage`、`DualCLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
