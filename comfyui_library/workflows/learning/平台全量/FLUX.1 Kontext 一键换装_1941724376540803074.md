---
key: 平台全量/FLUX.1 Kontext 一键换装_1941724376540803074.json
name: FLUX.1 Kontext 一键换装_1941724376540803074
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.1 Kontext 一键换装_1941724376540803074.json
hash: e3ab01b8d18373eb
coverage: 0.805556
learned_at: 2026-11-14 00:25:01
nodes: [PreviewImage, ImagePadForOutpaint, FL_SaveWebPImage(SaveImage), PreviewImage, VAEDecode, ReferenceLatent, FluxGuidance, CLIPTextEncode, DeepTranslatorTextNode, FluxKontextImageScale, TTP_text_mix, easy imageToBase64, easy imageToBase64, ShowText|pysssss, ShowText|pysssss, Anything Everywhere3, VAELoader, DualCLIPLoader, TeaCache, PathchSageAttentionKJ, LoadImage, LoadImage, PreviewImage, ConditioningZeroOut, ImageConcanate, FluxKontextImageScale, VAEEncode, VAEEncode, KSampler, UNETLoader, Primitive string [Crystools], GLM_Vision_ImageToPrompt, GLM_Vision_ImageToPrompt, ImageConcanate, SaveImage, MarkdownNote]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 404819789577410, "steps": 20}
---

# 平台全量/FLUX.1 Kontext 一键换装_1941724376540803074.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.1 Kontext 一键换装_1941724376540803074.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `PreviewImage`
- `ImagePadForOutpaint`
- `FL_SaveWebPImage(SaveImage)`
- `PreviewImage`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `DeepTranslatorTextNode`
- `FluxKontextImageScale`
- `TTP_text_mix`
- `easy imageToBase64`
- `easy imageToBase64`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `Anything Everywhere3`
- `VAELoader`
- `DualCLIPLoader`
- `TeaCache`
- `PathchSageAttentionKJ`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `ConditioningZeroOut`
- `ImageConcanate`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `Primitive string [Crystools]`
- `GLM_Vision_ImageToPrompt`
- `GLM_Vision_ImageToPrompt`
- `ImageConcanate`
- `SaveImage`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `404819789577410`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（29/36）

**有卡**：`ImagePadForOutpaint`、`FL_SaveWebPImage(SaveImage)`、`VAEDecode`、`ReferenceLatent`、`FluxGuidance`、`CLIPTextEncode`、`DeepTranslatorTextNode`、`FluxKontextImageScale`、`TTP_text_mix`、`easy imageToBase64`、`VAELoader`、`DualCLIPLoader`、`TeaCache`、`PathchSageAttentionKJ`、`LoadImage`、`ConditioningZeroOut`、`ImageConcanate`、`VAEEncode`、`KSampler`、`UNETLoader`、`Primitive string [Crystools]`、`GLM_Vision_ImageToPrompt`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
