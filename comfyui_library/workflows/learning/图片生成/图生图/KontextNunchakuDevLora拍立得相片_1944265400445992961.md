---
key: 图片生成/图生图/KontextNunchakuDevLora拍立得相片_1944265400445992961.json
name: KontextNunchakuDevLora拍立得相片_1944265400445992961
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLora拍立得相片_1944265400445992961.json
hash: 03bbc366b574bef4
coverage: 1
learned_at: 2026-10-23 11:06:38
nodes: [VAEDecode, SaveImage, DualCLIPLoader, SDXLPromptStyler, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, KSampler, ReferenceLatent, ModelSamplingFlux, NunchakuFluxDiTLoader, FluxKontextImageScale, VAELoader, VAEEncode, JoinStringMulti, ArtistsImage_Zho, LoadImage, LoraLoaderModelOnly, RH_Translator]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 1118687469627057, "steps": 20}
---

# 图片生成/图生图/KontextNunchakuDevLora拍立得相片_1944265400445992961.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLora拍立得相片_1944265400445992961.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `DualCLIPLoader`
- `SDXLPromptStyler`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `ReferenceLatent`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `FluxKontextImageScale`
- `VAELoader`
- `VAEEncode` ★核心
- `JoinStringMulti`
- `ArtistsImage_Zho`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `RH_Translator`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1118687469627057`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`VAEDecode`、`SaveImage`、`DualCLIPLoader`、`SDXLPromptStyler`、`FluxGuidance`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`KSampler`、`ReferenceLatent`、`ModelSamplingFlux`、`NunchakuFluxDiTLoader`、`FluxKontextImageScale`、`VAELoader`、`VAEEncode`、`JoinStringMulti`、`ArtistsImage_Zho`、`LoadImage`、`LoraLoaderModelOnly`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
