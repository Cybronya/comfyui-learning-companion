---
key: 平台全量/【上新】(IPA)-Flux redux model example_1860177378197598210.json
name: 【上新】(IPA)-Flux redux model example_1860177378197598210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【上新】(IPA)-Flux redux model example_1860177378197598210.json
hash: 19b6b992b8057adc
coverage: 0.814815
learned_at: 2026-11-14 01:22:44
nodes: [Label (rgthree), Label (rgthree), KSamplerSelect, RandomNoise, FluxGuidance, CLIPVisionEncode, StyleModelLoader, Note, BasicScheduler, ShowText|pysssss, CLIPVisionLoader, DualCLIPLoader, VAELoader, SamplerCustomAdvanced, VAEDecode, SaveImage, PreviewImage, BasicGuider, Note, EmptySD3LatentImage, StyleModelApply, Note, CLIPTextEncode, LoadImage, RH_Captioner, ModelSamplingFlux, UNETLoader]
patterns: []
missing: []
---

# 平台全量/【上新】(IPA)-Flux redux model example_1860177378197598210.json

> 来源文件 `comfyui_library/workflows/平台全量/【上新】(IPA)-Flux redux model example_1860177378197598210.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `Label (rgthree)`
- `Label (rgthree)`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `FluxGuidance`
- `CLIPVisionEncode`
- `StyleModelLoader`
- `Note`
- `BasicScheduler`
- `ShowText|pysssss`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `BasicGuider`
- `Note`
- `EmptySD3LatentImage`
- `StyleModelApply`
- `Note`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `RH_Captioner`
- `ModelSamplingFlux`
- `UNETLoader` ★核心

## 知识

覆盖率 **81%**（22/27）

**有卡**：`Label (rgthree)`、`KSamplerSelect`、`RandomNoise`、`FluxGuidance`、`CLIPVisionEncode`、`StyleModelLoader`、`BasicScheduler`、`CLIPVisionLoader`、`DualCLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`BasicGuider`、`EmptySD3LatentImage`、`StyleModelApply`、`CLIPTextEncode`、`LoadImage`、`RH_Captioner`、`ModelSamplingFlux`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
