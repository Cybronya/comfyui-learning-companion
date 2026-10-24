---
key: 图片生成/图生图/ACE++_Localedit_repainting_ref_redux_参考+Redux重绘_1956959999537680386.json
name: ACE++_Localedit_repainting_ref_redux_参考+Redux重绘_1956959999537680386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ACE++_Localedit_repainting_ref_redux_参考+Redux重绘_1956959999537680386.json
hash: 7d6b540dc8aa9bf1
coverage: 0.928571
learned_at: 2026-10-23 10:50:15
nodes: [CLIPVisionLoader, StyleModelApply, CLIPVisionEncode, ACEPlusLoraProcessor, GrowMaskWithBlur, LoadImage, PreviewImage, MaskPreview+, PreviewImage, ImageCrop, SaveImage, MaskPreview+, KSampler, LoadImage, Note Plus (mtb), StyleModelLoader, DualCLIPLoader, VAELoader, ACEPlusLoraConditioning, CLIPTextEncode, UNETLoader, DifferentialDiffusion, LoraLoaderModelOnly, CLIPTextEncode, VAEDecode, FluxGuidance, RMBG, LoadImageFromUrl]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 397934584397535, "steps": 28}
---

# 图片生成/图生图/ACE++_Localedit_repainting_ref_redux_参考+Redux重绘_1956959999537680386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ACE++_Localedit_repainting_ref_redux_参考+Redux重绘_1956959999537680386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `CLIPVisionLoader`
- `StyleModelApply`
- `CLIPVisionEncode`
- `ACEPlusLoraProcessor`
- `GrowMaskWithBlur`
- `LoadImage`
- `PreviewImage`
- `MaskPreview+`
- `PreviewImage`
- `ImageCrop`
- `SaveImage`
- `MaskPreview+`
- `KSampler` ★核心
- `LoadImage`
- `Note Plus (mtb)`
- `StyleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `ACEPlusLoraConditioning`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `DifferentialDiffusion`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `FluxGuidance`
- `RMBG`
- `LoadImageFromUrl`

## 关键参数

- `seed` = `397934584397535`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`CLIPVisionLoader`、`StyleModelApply`、`CLIPVisionEncode`、`ACEPlusLoraProcessor`、`GrowMaskWithBlur`、`LoadImage`、`MaskPreview+`、`ImageCrop`、`SaveImage`、`KSampler`、`Note Plus (mtb)`、`StyleModelLoader`、`DualCLIPLoader`、`VAELoader`、`ACEPlusLoraConditioning`、`CLIPTextEncode`、`UNETLoader`、`DifferentialDiffusion`、`LoraLoaderModelOnly`、`VAEDecode`、`FluxGuidance`、`RMBG`、`LoadImageFromUrl`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
