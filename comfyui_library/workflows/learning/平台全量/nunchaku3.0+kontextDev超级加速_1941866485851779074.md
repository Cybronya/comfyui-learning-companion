---
key: 平台全量/nunchaku3.0+kontextDev超级加速_1941866485851779074.json
name: nunchaku3.0+kontextDev超级加速_1941866485851779074
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/nunchaku3.0+kontextDev超级加速_1941866485851779074.json
hash: 3f990ff7e8f5e7a4
coverage: 0.863636
learned_at: 2026-11-14 01:15:34
nodes: [VAELoader, DualCLIPLoader, NunchakuFluxDiTLoader, ImageStitch, FluxKontextImageScale, PreviewImage, ReferenceLatent, ConditioningZeroOut, KSampler, VAEDecode, FluxGuidance, EmptySD3LatentImage, Note, SaveImage, Note, LoadImage, CLIPTextEncode, LoadImage, ApplyFBCacheOnModel, LoraLoader, VAEEncode, easy anythingIndexSwitch]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "FLUX.1-Turbo-8step.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 83862369046991, "steps": 20, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
---

# 平台全量/nunchaku3.0+kontextDev超级加速_1941866485851779074.json

> 来源文件 `comfyui_library/workflows/平台全量/nunchaku3.0+kontextDev超级加速_1941866485851779074.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `VAELoader`
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `ImageStitch`
- `FluxKontextImageScale`
- `PreviewImage`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxGuidance`
- `EmptySD3LatentImage`
- `Note`
- `SaveImage`
- `Note`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ApplyFBCacheOnModel`
- `LoraLoader` ★核心
- `VAEEncode` ★核心
- `easy anythingIndexSwitch`

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `83862369046991`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `FLUX.1-Turbo-8step.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`VAELoader`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`ImageStitch`、`FluxKontextImageScale`、`ReferenceLatent`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`FluxGuidance`、`EmptySD3LatentImage`、`SaveImage`、`LoadImage`、`CLIPTextEncode`、`ApplyFBCacheOnModel`、`LoraLoader`、`VAEEncode`、`easy anythingIndexSwitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent
