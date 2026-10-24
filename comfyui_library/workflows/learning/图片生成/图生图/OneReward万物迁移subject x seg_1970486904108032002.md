---
key: 图片生成/图生图/OneReward万物迁移subject x seg_1970486904108032002.json
name: OneReward万物迁移subject x seg_1970486904108032002
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/OneReward万物迁移subject x seg_1970486904108032002.json
hash: f164e279b4bdb451
coverage: 0.935484
learned_at: 2026-10-23 11:10:34
nodes: [CLIPVisionLoader, StyleModelApply, CLIPVisionEncode, Note Plus (mtb), StyleModelLoader, VAEDecode, FluxGuidance, DifferentialDiffusion, ImageCrop, DualCLIPLoader, MaskPreview+, CLIPTextEncode, ACEPlusLoraConditioning, LoraLoaderModelOnly, VAELoader, UNETLoader, ACEPlusLoraProcessor, PreviewImage, RMBG, CLIPTextEncode, KSampler, PreviewImage, SaveImage, MaskPreview+, GrowMaskWithBlur, LoadImage, GroundingDinoSAM2Segment (segment anything2), SAM2ModelLoader (segment anything2), GroundingDinoModelLoader (segment anything2), LoadImage, LoadImageFromUrl]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 1027755670856327, "steps": 28}
---

# 图片生成/图生图/OneReward万物迁移subject x seg_1970486904108032002.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/OneReward万物迁移subject x seg_1970486904108032002.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `CLIPVisionLoader`
- `StyleModelApply`
- `CLIPVisionEncode`
- `Note Plus (mtb)`
- `StyleModelLoader`
- `VAEDecode` ★核心
- `FluxGuidance`
- `DifferentialDiffusion`
- `ImageCrop`
- `DualCLIPLoader`
- `MaskPreview+`
- `CLIPTextEncode` ★核心
- `ACEPlusLoraConditioning`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `ACEPlusLoraProcessor`
- `PreviewImage`
- `RMBG`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `SaveImage`
- `MaskPreview+`
- `GrowMaskWithBlur`
- `LoadImage`
- `GroundingDinoSAM2Segment (segment anything2)`
- `SAM2ModelLoader (segment anything2)`
- `GroundingDinoModelLoader (segment anything2)`
- `LoadImage`
- `LoadImageFromUrl`

## 关键参数

- `seed` = `1027755670856327`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`CLIPVisionLoader`、`StyleModelApply`、`CLIPVisionEncode`、`Note Plus (mtb)`、`StyleModelLoader`、`VAEDecode`、`FluxGuidance`、`DifferentialDiffusion`、`ImageCrop`、`DualCLIPLoader`、`MaskPreview+`、`CLIPTextEncode`、`ACEPlusLoraConditioning`、`LoraLoaderModelOnly`、`VAELoader`、`UNETLoader`、`ACEPlusLoraProcessor`、`RMBG`、`KSampler`、`SaveImage`、`GrowMaskWithBlur`、`LoadImage`、`GroundingDinoSAM2Segment (segment anything2)`、`SAM2ModelLoader (segment anything2)`、`GroundingDinoModelLoader (segment anything2)`、`LoadImageFromUrl`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
