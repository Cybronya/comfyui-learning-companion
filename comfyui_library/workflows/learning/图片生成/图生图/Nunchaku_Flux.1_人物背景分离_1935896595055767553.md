---
key: 图片生成/图生图/Nunchaku_Flux.1_人物背景分离_1935896595055767553.json
name: Nunchaku_Flux.1_人物背景分离_1935896595055767553
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Nunchaku_Flux.1_人物背景分离_1935896595055767553.json
hash: 8f8f7d8fc5060cbe
coverage: 0.761905
learned_at: 2026-10-23 11:10:05
nodes: [NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuTextEncoderLoaderV2, VAELoader, FluxGuidance, KSampler, VAEDecode, PreviewImage, easy int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, CLIPTextEncode, RMBG, PreviewImage, PreviewImage, Note, InpaintModelConditioning, CLIPTextEncode, Fast Groups Bypasser (rgthree), SaveImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 628434167504561, "steps": 20}
---

# 图片生成/图生图/Nunchaku_Flux.1_人物背景分离_1935896595055767553.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Nunchaku_Flux.1_人物背景分离_1935896595055767553.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuTextEncoderLoaderV2`
- `VAELoader`
- `FluxGuidance`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `RMBG`
- `PreviewImage`
- `PreviewImage`
- `Note`
- `InpaintModelConditioning`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `SaveImage`

## 关键参数

- `seed` = `628434167504561`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`NunchakuFluxDiTLoader`、`NunchakuFluxLoraLoader`、`NunchakuTextEncoderLoaderV2`、`VAELoader`、`FluxGuidance`、`KSampler`、`VAEDecode`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CLIPTextEncode`、`RMBG`、`InpaintModelConditioning`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、FluxGuidance、NunchakuTextEncoderLoaderV2、NunchakuFluxLoraLoader
