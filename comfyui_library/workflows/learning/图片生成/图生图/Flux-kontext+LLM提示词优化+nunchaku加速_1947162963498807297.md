---
key: 图片生成/图生图/Flux-kontext+LLM提示词优化+nunchaku加速_1947162963498807297.json
name: Flux-kontext+LLM提示词优化+nunchaku加速_1947162963498807297
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux-kontext+LLM提示词优化+nunchaku加速_1947162963498807297.json
hash: fd384da9a4cf4bd0
coverage: 0.882353
learned_at: 2026-10-23 10:58:34
nodes: [CLIPTextEncode, ConditioningZeroOut, RH_LLMAPI_NODE, ReferenceLatent, VAEEncode, FluxKontextImageScale, FluxGuidance, NunchakuFluxDiTLoader, DualCLIPLoader, VAELoader, Image Comparer (rgthree), KSampler, LoadImage, easy showAnything, CR Text, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 914249129352611, "steps": 20}
---

# 图片生成/图生图/Flux-kontext+LLM提示词优化+nunchaku加速_1947162963498807297.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux-kontext+LLM提示词优化+nunchaku加速_1947162963498807297.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `RH_LLMAPI_NODE`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `FluxGuidance`
- `NunchakuFluxDiTLoader`
- `DualCLIPLoader`
- `VAELoader`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `LoadImage`
- `easy showAnything`
- `CR Text`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `914249129352611`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`CLIPTextEncode`、`ConditioningZeroOut`、`RH_LLMAPI_NODE`、`ReferenceLatent`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`NunchakuFluxDiTLoader`、`DualCLIPLoader`、`VAELoader`、`KSampler`、`LoadImage`、`CR Text`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent
