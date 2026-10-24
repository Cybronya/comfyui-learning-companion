---
key: 图片生成/图生图/kontext nunchaku 单图编辑极速版 LLM智能提示词扩写 -StarAi_1939659944482217985.json
name: kontext nunchaku 单图编辑极速版 LLM智能提示词扩写 -StarAi_1939659944482217985
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/kontext nunchaku 单图编辑极速版 LLM智能提示词扩写 -StarAi_1939659944482217985.json
hash: a4dc8c878db00e5f
coverage: 0.941176
learned_at: 2026-10-23 11:38:46
nodes: [ReferenceLatent, Note Plus (mtb), DualCLIPLoader, VAEEncode, FluxKontextImageScale, VAEDecode, FluxGuidance, ConditioningZeroOut, KSampler, RH_LLMAPI_NODE, CLIPTextEncode, VAELoader, NunchakuFluxDiTLoader, LoadImage, Text, SaveImage, MarkdownNote]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 929350105213565, "steps": 20}
---

# 图片生成/图生图/kontext nunchaku 单图编辑极速版 LLM智能提示词扩写 -StarAi_1939659944482217985.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/kontext nunchaku 单图编辑极速版 LLM智能提示词扩写 -StarAi_1939659944482217985.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `ReferenceLatent`
- `Note Plus (mtb)`
- `DualCLIPLoader`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `VAEDecode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `RH_LLMAPI_NODE`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `NunchakuFluxDiTLoader`
- `LoadImage`
- `Text`
- `SaveImage`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `929350105213565`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`ReferenceLatent`、`Note Plus (mtb)`、`DualCLIPLoader`、`VAEEncode`、`FluxKontextImageScale`、`VAEDecode`、`FluxGuidance`、`ConditioningZeroOut`、`KSampler`、`RH_LLMAPI_NODE`、`CLIPTextEncode`、`VAELoader`、`NunchakuFluxDiTLoader`、`LoadImage`、`Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent
