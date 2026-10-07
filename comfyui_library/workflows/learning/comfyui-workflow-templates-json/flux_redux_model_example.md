---
key: comfyui-workflow-templates-json/flux_redux_model_example.json
name: flux_redux_model_example
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/flux_redux_model_example.json
hash: fb5e6fac9566ffc9
official: true
coverage: 0.758621
learned_at: 2026-10-07 21:35:27
nodes: [PrimitiveNode, EmptySD3LatentImage, BasicScheduler, StyleModelApply, StyleModelApply, UNETLoader, DualCLIPLoader, VAELoader, StyleModelLoader, CLIPVisionLoader, VAEDecode, MarkdownNote, CLIPVisionEncode, CLIPVisionEncode, Note, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, RandomNoise, ModelSamplingFlux, Note, MarkdownNote, PrimitiveNode, FluxGuidance, MarkdownNote, CLIPTextEncode, SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/flux_redux_model_example.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/flux_redux_model_example.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `PrimitiveNode`
- `EmptySD3LatentImage`
- `BasicScheduler`
- `StyleModelApply`
- `StyleModelApply`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `MarkdownNote`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `Note`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `ModelSamplingFlux`
- `Note`
- `MarkdownNote`
- `PrimitiveNode`
- `FluxGuidance`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **76%**（22/29）

**有卡**：`EmptySD3LatentImage`、`BasicScheduler`、`StyleModelApply`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`StyleModelLoader`、`CLIPVisionLoader`、`VAEDecode`、`CLIPVisionEncode`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`ModelSamplingFlux`、`FluxGuidance`、`CLIPTextEncode`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
