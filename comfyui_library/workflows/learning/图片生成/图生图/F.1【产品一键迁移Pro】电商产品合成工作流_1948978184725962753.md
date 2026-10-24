---
key: 图片生成/图生图/F.1【产品一键迁移Pro】电商产品合成工作流_1948978184725962753.json
name: F.1【产品一键迁移Pro】电商产品合成工作流_1948978184725962753
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1【产品一键迁移Pro】电商产品合成工作流_1948978184725962753.json
hash: f5a697f1d02a8489
coverage: 0.888889
learned_at: 2026-10-23 10:52:37
nodes: [ConditioningZeroOut, easy imageRemBg, VAEEncode, FluxKontextImageScale, DualCLIPLoader, VAELoader, ReferenceLatent, FluxGuidance, NunchakuFluxDiTLoader, Note, VAEDecode, SaveImage, PreviewImage, FastCanvasTool, PreviewImage, LoadImage, LoadImage, ImageCrop+, KSampler, easy imageConcat, easy imageConcat, UNETLoader, NunchakuFluxLoraLoader, CLIPTextEncode, SaveImage, LoraLoaderModelOnly, FastCanvas]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1036967478227981, "steps": 20}
---

# 图片生成/图生图/F.1【产品一键迁移Pro】电商产品合成工作流_1948978184725962753.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1【产品一键迁移Pro】电商产品合成工作流_1948978184725962753.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `ConditioningZeroOut`
- `easy imageRemBg`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `DualCLIPLoader`
- `VAELoader`
- `ReferenceLatent`
- `FluxGuidance`
- `NunchakuFluxDiTLoader`
- `Note`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `FastCanvasTool`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `ImageCrop+`
- `KSampler` ★核心
- `easy imageConcat`
- `easy imageConcat`
- `UNETLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `FastCanvas`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1036967478227981`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`ConditioningZeroOut`、`easy imageRemBg`、`VAEEncode`、`FluxKontextImageScale`、`DualCLIPLoader`、`VAELoader`、`ReferenceLatent`、`FluxGuidance`、`NunchakuFluxDiTLoader`、`VAEDecode`、`SaveImage`、`FastCanvasTool`、`LoadImage`、`ImageCrop+`、`KSampler`、`easy imageConcat`、`UNETLoader`、`NunchakuFluxLoraLoader`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`FastCanvas`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
