---
key: 图片生成/图生图/M_ACE_Plus_LoRA_subject_refence主体一致性生成_1956725732975022081.json
name: M_ACE_Plus_LoRA_subject_refence主体一致性生成_1956725732975022081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/M_ACE_Plus_LoRA_subject_refence主体一致性生成_1956725732975022081.json
hash: 1b03d937bc83779b
coverage: 0.909091
learned_at: 2026-10-23 11:09:15
nodes: [DifferentialDiffusion, UNETLoader, FluxGuidance, CLIPTextEncode, VAEDecode, LoraLoaderModelOnly, VAELoader, DualCLIPLoader, ImageGenResolutionFromImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, LoadImage, ImageCrop, SaveImage, Note Plus (mtb), LoadImageFromUrl, PreviewImage, PreviewImage, InpaintModelConditioning, ImagePadForOutpaint, RMBG]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 130441935105520, "steps": 28}
---

# 图片生成/图生图/M_ACE_Plus_LoRA_subject_refence主体一致性生成_1956725732975022081.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/M_ACE_Plus_LoRA_subject_refence主体一致性生成_1956725732975022081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `DifferentialDiffusion`
- `UNETLoader` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `ImageGenResolutionFromImage`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageCrop`
- `SaveImage`
- `Note Plus (mtb)`
- `LoadImageFromUrl`
- `PreviewImage`
- `PreviewImage`
- `InpaintModelConditioning`
- `ImagePadForOutpaint`
- `RMBG`

## 关键参数

- `seed` = `130441935105520`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **91%**（20/22）

**有卡**：`DifferentialDiffusion`、`UNETLoader`、`FluxGuidance`、`CLIPTextEncode`、`VAEDecode`、`LoraLoaderModelOnly`、`VAELoader`、`DualCLIPLoader`、`ImageGenResolutionFromImage`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`ImageCrop`、`SaveImage`、`Note Plus (mtb)`、`LoadImageFromUrl`、`InpaintModelConditioning`、`ImagePadForOutpaint`、`RMBG`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
