---
key: 平台全量/CHEN-F.1-Kontext-极限电商换装V2_1958766766275059713.json
name: CHEN-F.1-Kontext-极限电商换装V2_1958766766275059713
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/CHEN-F.1-Kontext-极限电商换装V2_1958766766275059713.json
hash: 3224d6c3420d9b81
coverage: 0.9375
learned_at: 2026-11-14 00:21:59
nodes: [ImagePadForOutpaint, FluxKontextImageScale, ImageStitch, Anything Everywhere3, VAEEncode, ReferenceLatent, ConditioningZeroOut, VAEDecode, PreviewImage, FluxGuidance, CLIPTextEncode, KSampler, VAELoader, LoadImage, LoadImage, LoraLoaderModelOnly, Switch image [Crystools], SaveImage, UNETLoader, CLIPTextEncode, ttN concat, VAEEncode, VAEDecode, KSampler, FluxGuidance, ReferenceLatent, FluxKontextImageScale, VAEEncode, ConditioningZeroOut, RH_Translator, DualCLIPLoader, TeaCache]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1028921289217942, "steps": 30}
---

# 平台全量/CHEN-F.1-Kontext-极限电商换装V2_1958766766275059713.json

> 来源文件 `comfyui_library/workflows/平台全量/CHEN-F.1-Kontext-极限电商换装V2_1958766766275059713.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `ImagePadForOutpaint`
- `FluxKontextImageScale`
- `ImageStitch`
- `Anything Everywhere3`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `PreviewImage`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Switch image [Crystools]`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ttN concat`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `FluxGuidance`
- `ReferenceLatent`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `RH_Translator`
- `DualCLIPLoader`
- `TeaCache`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1028921289217942`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`ImagePadForOutpaint`、`FluxKontextImageScale`、`ImageStitch`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`VAEDecode`、`FluxGuidance`、`CLIPTextEncode`、`KSampler`、`VAELoader`、`LoadImage`、`LoraLoaderModelOnly`、`Switch image [Crystools]`、`SaveImage`、`UNETLoader`、`ttN concat`、`RH_Translator`、`DualCLIPLoader`、`TeaCache`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
