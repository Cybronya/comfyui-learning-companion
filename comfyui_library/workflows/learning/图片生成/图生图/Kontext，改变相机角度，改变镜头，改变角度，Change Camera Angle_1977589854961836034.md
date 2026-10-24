---
key: 图片生成/图生图/Kontext，改变相机角度，改变镜头，改变角度，Change Camera Angle_1977589854961836034.json
name: Kontext，改变相机角度，改变镜头，改变角度，Change Camera Angle_1977589854961836034
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Kontext，改变相机角度，改变镜头，改变角度，Change Camera Angle_1977589854961836034.json
hash: fab6985c4bf79771
coverage: 0.909091
learned_at: 2026-10-23 11:07:31
nodes: [DualCLIPLoader, FluxKontextImageScale, VAELoader, FluxGuidance, VAEEncode, RH_Translator, ttN concat, LoadImage, SaveImage, TeaCache, LoraLoaderModelOnly, ConditioningZeroOut, VAEDecode, MuyeTextEditOutput, PreviewImage, CLIPTextEncode, easy showAnything, ReferenceLatent, RepeatLatentBatch, KSampler, UNETLoader, Note _O]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 65896122251859, "steps": 20}
---

# 图片生成/图生图/Kontext，改变相机角度，改变镜头，改变角度，Change Camera Angle_1977589854961836034.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Kontext，改变相机角度，改变镜头，改变角度，Change Camera Angle_1977589854961836034.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `DualCLIPLoader`
- `FluxKontextImageScale`
- `VAELoader`
- `FluxGuidance`
- `VAEEncode` ★核心
- `RH_Translator`
- `ttN concat`
- `LoadImage`
- `SaveImage`
- `TeaCache`
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `MuyeTextEditOutput`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `Note _O`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `65896122251859`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`DualCLIPLoader`、`FluxKontextImageScale`、`VAELoader`、`FluxGuidance`、`VAEEncode`、`RH_Translator`、`ttN concat`、`LoadImage`、`SaveImage`、`TeaCache`、`LoraLoaderModelOnly`、`ConditioningZeroOut`、`VAEDecode`、`MuyeTextEditOutput`、`CLIPTextEncode`、`ReferenceLatent`、`RepeatLatentBatch`、`KSampler`、`UNETLoader`、`Note _O`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、SaveImage
