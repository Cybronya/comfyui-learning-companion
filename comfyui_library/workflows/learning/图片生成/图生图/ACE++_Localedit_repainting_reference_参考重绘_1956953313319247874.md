---
key: 图片生成/图生图/ACE++_Localedit_repainting_reference_参考重绘_1956953313319247874.json
name: ACE++_Localedit_repainting_reference_参考重绘_1956953313319247874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ACE++_Localedit_repainting_reference_参考重绘_1956953313319247874.json
hash: 04e57f7c062a533e
coverage: 0.916667
learned_at: 2026-10-23 10:50:16
nodes: [DifferentialDiffusion, ACEPlusLoraProcessor, GrowMaskWithBlur, LoadImage, LoadImage, CLIPTextEncode, CLIPTextEncode, KSampler, SaveImage, MaskPreview+, PreviewImage, MaskPreview+, Note Plus (mtb), LoadImageFromUrl, RMBG, PreviewImage, VAELoader, DualCLIPLoader, ACEPlusLoraConditioning, UNETLoader, LoraLoaderModelOnly, ImageCrop, VAEDecode, FluxGuidance]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 750560967347752, "steps": 28}
---

# 图片生成/图生图/ACE++_Localedit_repainting_reference_参考重绘_1956953313319247874.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ACE++_Localedit_repainting_reference_参考重绘_1956953313319247874.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `DifferentialDiffusion`
- `ACEPlusLoraProcessor`
- `GrowMaskWithBlur`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `MaskPreview+`
- `PreviewImage`
- `MaskPreview+`
- `Note Plus (mtb)`
- `LoadImageFromUrl`
- `RMBG`
- `PreviewImage`
- `VAELoader`
- `DualCLIPLoader`
- `ACEPlusLoraConditioning`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageCrop`
- `VAEDecode` ★核心
- `FluxGuidance`

## 关键参数

- `seed` = `750560967347752`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`DifferentialDiffusion`、`ACEPlusLoraProcessor`、`GrowMaskWithBlur`、`LoadImage`、`CLIPTextEncode`、`KSampler`、`SaveImage`、`MaskPreview+`、`Note Plus (mtb)`、`LoadImageFromUrl`、`RMBG`、`VAELoader`、`DualCLIPLoader`、`ACEPlusLoraConditioning`、`UNETLoader`、`LoraLoaderModelOnly`、`ImageCrop`、`VAEDecode`、`FluxGuidance`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
