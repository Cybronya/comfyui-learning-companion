---
key: 平台全量/FLUX.1 Kontext 产品摄影_1941850709623205889.json
name: FLUX.1 Kontext 产品摄影_1941850709623205889
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.1 Kontext 产品摄影_1941850709623205889.json
hash: f073105e4da2b434
coverage: 0.770833
learned_at: 2026-11-14 00:25:01
nodes: [PreviewImage, CLIPTextEncode, ReferenceLatent, FluxGuidance, ConditioningZeroOut, VAEEncode, FluxKontextImageScale, CLIPTextEncode, SetNode, SaveImage, ImageConcanate, ConditioningZeroOut, FluxGuidance, VAEEncode, FluxKontextImageScale, ReferenceLatent, VAEEncode, ImagePadForOutpaint, LoadImage, NunchakuFluxDiTLoader, VAEDecode, VAEDecode, LoadImage, YC Color Match, ShowText|pysssss, GetNode, CompositorConfig3, easy imageRemBg, PreviewImage, KSampler, RH_Translator, KSampler, easy imageToBase64, ShowText|pysssss, TTP_text_mix, RH_Translator, ShowText|pysssss, Anything Everywhere3, VAELoader, DualCLIPLoader, SaveImage, ShowText|pysssss, Compositor3, ShowText|pysssss, easy imageToBase64, GLM_Vision_ImageToPrompt, GLM_Vision_ImageToPrompt, MarkdownNote]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 251906855908884, "steps": 20}
---

# 平台全量/FLUX.1 Kontext 产品摄影_1941850709623205889.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.1 Kontext 产品摄影_1941850709623205889.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SaveImage`
- `ImageConcanate`
- `ConditioningZeroOut`
- `FluxGuidance`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ImagePadForOutpaint`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `YC Color Match`
- `ShowText|pysssss`
- `GetNode`
- `CompositorConfig3`
- `easy imageRemBg`
- `PreviewImage`
- `KSampler` ★核心
- `RH_Translator`
- `KSampler` ★核心
- `easy imageToBase64`
- `ShowText|pysssss`
- `TTP_text_mix`
- `RH_Translator`
- `ShowText|pysssss`
- `Anything Everywhere3`
- `VAELoader`
- `DualCLIPLoader`
- `SaveImage`
- `ShowText|pysssss`
- `Compositor3`
- `ShowText|pysssss`
- `easy imageToBase64`
- `GLM_Vision_ImageToPrompt`
- `GLM_Vision_ImageToPrompt`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `251906855908884`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（37/48）

**有卡**：`CLIPTextEncode`、`ReferenceLatent`、`FluxGuidance`、`ConditioningZeroOut`、`VAEEncode`、`FluxKontextImageScale`、`SaveImage`、`ImageConcanate`、`ImagePadForOutpaint`、`LoadImage`、`NunchakuFluxDiTLoader`、`VAEDecode`、`YC Color Match`、`CompositorConfig3`、`easy imageRemBg`、`KSampler`、`RH_Translator`、`easy imageToBase64`、`TTP_text_mix`、`VAELoader`、`DualCLIPLoader`、`Compositor3`、`GLM_Vision_ImageToPrompt`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent
