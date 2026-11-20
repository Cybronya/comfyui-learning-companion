---
key: 平台全量/F.1 复古风格头像_1889917217784602625.json
name: F.1 复古风格头像_1889917217784602625
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/F.1 复古风格头像_1889917217784602625.json
hash: 2bf75e33ab480662
coverage: 0.961538
learned_at: 2026-11-14 00:24:01
nodes: [ModelSamplingFlux, KSamplerSelect, RandomNoise, BasicGuider, PulidEvaClipLoader, PulidInsightFaceLoader, VAEDecode, VAEEncode, BasicScheduler, SamplerCustomAdvanced, Note, FluxGuidance, StyleModelApplySimple, ApplyPulidFlux, PulidFluxModelLoader, UNETLoader, CLIPVisionLoader, StyleModelLoader, CLIPVisionEncode, DualCLIPLoader, VAELoader, CR SDXL Aspect Ratio, LoadImage, LoraLoaderModelOnly, CLIPTextEncode, SaveImage]
patterns: []
missing: []
---

# 平台全量/F.1 复古风格头像_1889917217784602625.json

> 来源文件 `comfyui_library/workflows/平台全量/F.1 复古风格头像_1889917217784602625.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（26 个）：
- `ModelSamplingFlux`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `BasicGuider`
- `PulidEvaClipLoader`
- `PulidInsightFaceLoader`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `Note`
- `FluxGuidance`
- `StyleModelApplySimple`
- `ApplyPulidFlux`
- `PulidFluxModelLoader`
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `StyleModelLoader`
- `CLIPVisionEncode`
- `DualCLIPLoader`
- `VAELoader`
- `CR SDXL Aspect Ratio`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`ModelSamplingFlux`、`KSamplerSelect`、`RandomNoise`、`BasicGuider`、`PulidEvaClipLoader`、`PulidInsightFaceLoader`、`VAEDecode`、`VAEEncode`、`BasicScheduler`、`SamplerCustomAdvanced`、`FluxGuidance`、`StyleModelApplySimple`、`ApplyPulidFlux`、`PulidFluxModelLoader`、`UNETLoader`、`CLIPVisionLoader`、`StyleModelLoader`、`CLIPVisionEncode`、`DualCLIPLoader`、`VAELoader`、`CR SDXL Aspect Ratio`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect
