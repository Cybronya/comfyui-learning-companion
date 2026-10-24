---
key: 图片生成/图生图/FLUX.1-dev洗图工作流，一键生成相似图（防侵权）_2039928937966473218.json
name: FLUX.1-dev洗图工作流，一键生成相似图（防侵权）_2039928937966473218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.1-dev洗图工作流，一键生成相似图（防侵权）_2039928937966473218.json
hash: 79936894743f8ff7
coverage: 0.913043
learned_at: 2026-10-23 10:54:01
nodes: [BasicGuider, VAEEncode, VAEDecode, Image Comparer (rgthree), SaveImage, LoadImage, DualCLIPLoader, VAELoader, Florence2Run, ShowText|pysssss, CLIPTextEncode, StyleModelApply, KSamplerSelect, CLIPVisionEncode, StyleModelLoader, CLIPVisionLoader, RHHiddenNodes, BasicScheduler, RandomNoise, SamplerCustomAdvanced, Florence2ModelLoader, LayerUtility: ImageScaleByAspectRatio V2, FluxGuidance]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.1-dev洗图工作流，一键生成相似图（防侵权）_2039928937966473218.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.1-dev洗图工作流，一键生成相似图（防侵权）_2039928937966473218.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `BasicGuider`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `DualCLIPLoader`
- `VAELoader`
- `Florence2Run`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `StyleModelApply`
- `KSamplerSelect` ★核心
- `CLIPVisionEncode`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `RHHiddenNodes`
- `BasicScheduler`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `Florence2ModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FluxGuidance`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`BasicGuider`、`VAEEncode`、`VAEDecode`、`SaveImage`、`LoadImage`、`DualCLIPLoader`、`VAELoader`、`Florence2Run`、`CLIPTextEncode`、`StyleModelApply`、`KSamplerSelect`、`CLIPVisionEncode`、`StyleModelLoader`、`CLIPVisionLoader`、`RHHiddenNodes`、`BasicScheduler`、`RandomNoise`、`SamplerCustomAdvanced`、`Florence2ModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`FluxGuidance`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced、VAEEncode
