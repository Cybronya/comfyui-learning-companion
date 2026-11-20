---
key: 平台全量/2D转3D 潮玩盲盒对象一致性生图_Kontext1.0_1975106133272735746.json
name: 2D转3D 潮玩盲盒对象一致性生图_Kontext1.0_1975106133272735746
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/2D转3D 潮玩盲盒对象一致性生图_Kontext1.0_1975106133272735746.json
hash: 1d381924dfbdc620
coverage: 0.882353
learned_at: 2026-11-14 00:11:40
nodes: [ConditioningZeroOut, SaveImage, FluxGuidance, VAEDecode, VAEEncode, VAELoader, ReferenceLatent, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, DualCLIPLoader, LoadImage, FluxKontextImageScale, MarkdownNote, Image Comparer (rgthree), KSampler, CLIPTextEncode, RH_Translator]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 941742210770503, "steps": 20}
---

# 平台全量/2D转3D 潮玩盲盒对象一致性生图_Kontext1.0_1975106133272735746.json

> 来源文件 `comfyui_library/workflows/平台全量/2D转3D 潮玩盲盒对象一致性生图_Kontext1.0_1975106133272735746.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `ConditioningZeroOut`
- `SaveImage`
- `FluxGuidance`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `ReferenceLatent`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxDiTLoader`
- `DualCLIPLoader`
- `LoadImage`
- `FluxKontextImageScale`
- `MarkdownNote`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `RH_Translator`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `941742210770503`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`ConditioningZeroOut`、`SaveImage`、`FluxGuidance`、`VAEDecode`、`VAEEncode`、`VAELoader`、`ReferenceLatent`、`NunchakuFluxLoraLoader`、`NunchakuFluxDiTLoader`、`DualCLIPLoader`、`LoadImage`、`FluxKontextImageScale`、`KSampler`、`CLIPTextEncode`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent
