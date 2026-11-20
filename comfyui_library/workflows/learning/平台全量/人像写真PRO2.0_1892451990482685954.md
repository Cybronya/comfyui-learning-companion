---
key: 平台全量/人像写真PRO2.0_1892451990482685954.json
name: 人像写真PRO2.0_1892451990482685954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/人像写真PRO2.0_1892451990482685954.json
hash: 78e1fe2cc1989f23
coverage: 0.827586
learned_at: 2026-11-14 01:36:02
nodes: [FluxForwardOverrider, ApplyTeaCachePatch, ApplyTeaCachePatchAdvanced, BasicScheduler, BasicGuider, ImageConcanate, LmcqDeepLoader, PulidFluxInsightFaceLoader, PulidFluxEvaClipLoader, PulidFluxModelLoader, ApplyPulidFlux, VAEDecode, KSamplerSelect, FluxGuidance, CLIPTextEncode, RandomNoise, SamplerCustomAdvanced, ShowText|pysssss, LoadImage, PreviewImage, SaveImage, UNETLoader, VAELoader, DualCLIPLoader, ShowText|pysssss, Anything Everywhere3, Note, EmptySD3LatentImage, LmcqDeepGen]
patterns: []
missing: []
---

# 平台全量/人像写真PRO2.0_1892451990482685954.json

> 来源文件 `comfyui_library/workflows/平台全量/人像写真PRO2.0_1892451990482685954.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `FluxForwardOverrider`
- `ApplyTeaCachePatch`
- `ApplyTeaCachePatchAdvanced`
- `BasicScheduler`
- `BasicGuider`
- `ImageConcanate`
- `LmcqDeepLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxEvaClipLoader`
- `PulidFluxModelLoader`
- `ApplyPulidFlux`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `ShowText|pysssss`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `ShowText|pysssss`
- `Anything Everywhere3`
- `Note`
- `EmptySD3LatentImage`
- `LmcqDeepGen`

## 知识

覆盖率 **83%**（24/29）

**有卡**：`FluxForwardOverrider`、`ApplyTeaCachePatch`、`ApplyTeaCachePatchAdvanced`、`BasicScheduler`、`BasicGuider`、`ImageConcanate`、`LmcqDeepLoader`、`PulidFluxInsightFaceLoader`、`PulidFluxEvaClipLoader`、`PulidFluxModelLoader`、`ApplyPulidFlux`、`VAEDecode`、`KSamplerSelect`、`FluxGuidance`、`CLIPTextEncode`、`RandomNoise`、`SamplerCustomAdvanced`、`LoadImage`、`SaveImage`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`EmptySD3LatentImage`、`LmcqDeepGen`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
