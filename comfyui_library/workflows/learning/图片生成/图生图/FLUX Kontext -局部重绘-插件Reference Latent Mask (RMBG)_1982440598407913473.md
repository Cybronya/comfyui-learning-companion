---
key: 图片生成/图生图/FLUX Kontext -局部重绘-插件Reference Latent Mask (RMBG)_1982440598407913473.json
name: FLUX Kontext -局部重绘-插件Reference Latent Mask (RMBG)_1982440598407913473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX Kontext -局部重绘-插件Reference Latent Mask (RMBG)_1982440598407913473.json
hash: 3a37bc53891000ee
coverage: 0.904762
learned_at: 2026-10-23 10:53:23
nodes: [UNETLoader, PathchSageAttentionKJ, DualCLIPLoader, VAELoader, Anything Everywhere3, AILab_ImagePreview, KSampler, VAEDecode, CLIPTextEncode, LayerMask: MaskInvert, VAEEncode, AILab_ReferenceLatentMask, FluxGuidance, ConditioningZeroOut, AILab_ImagePreview, FluxKontextImageScale, AILab_LoadImageSimple, MarkdownNote, AILab_MaskOverlay, RBGImageStitchPlus, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 100, "steps": 25}
---

# 图片生成/图生图/FLUX Kontext -局部重绘-插件Reference Latent Mask (RMBG)_1982440598407913473.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX Kontext -局部重绘-插件Reference Latent Mask (RMBG)_1982440598407913473.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `DualCLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `AILab_ImagePreview`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LayerMask: MaskInvert`
- `VAEEncode` ★核心
- `AILab_ReferenceLatentMask`
- `FluxGuidance`
- `ConditioningZeroOut`
- `AILab_ImagePreview`
- `FluxKontextImageScale`
- `AILab_LoadImageSimple`
- `MarkdownNote`
- `AILab_MaskOverlay`
- `RBGImageStitchPlus`
- `SaveImage`

## 关键参数

- `seed` = `100`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`UNETLoader`、`PathchSageAttentionKJ`、`DualCLIPLoader`、`VAELoader`、`AILab_ImagePreview`、`KSampler`、`VAEDecode`、`CLIPTextEncode`、`LayerMask: MaskInvert`、`VAEEncode`、`AILab_ReferenceLatentMask`、`FluxGuidance`、`ConditioningZeroOut`、`FluxKontextImageScale`、`AILab_LoadImageSimple`、`AILab_MaskOverlay`、`RBGImageStitchPlus`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、FluxGuidance、VAEEncode
