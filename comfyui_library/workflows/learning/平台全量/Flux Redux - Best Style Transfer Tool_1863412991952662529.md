---
key: 平台全量/Flux Redux - Best Style Transfer Tool_1863412991952662529.json
name: Flux Redux - Best Style Transfer Tool_1863412991952662529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Redux - Best Style Transfer Tool_1863412991952662529.json
hash: 5096d0c4063790b9
coverage: 0.730769
learned_at: 2026-11-14 00:28:03
nodes: [SamplerCustomAdvanced, KSamplerSelect, RandomNoise, EmptySD3LatentImage, PrimitiveNode, Note, Note, CLIPVisionEncode, BasicGuider, StyleModelApply, CLIPVisionLoader, StyleModelLoader, VAELoader, VAEDecode, Note, PrimitiveNode, Note, BasicScheduler, UNETLoader, DualCLIPLoader, LoraLoader, FluxGuidance, LoadImage, SaveImage, PreviewImage, CLIPTextEncode]
patterns: [lora]
missing: []
parameters: {"lora_name": "flux_realism_lora.safetensors", "strength_clip": 1, "strength_model": 0.75}
---

# 平台全量/Flux Redux - Best Style Transfer Tool_1863412991952662529.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Redux - Best Style Transfer Tool_1863412991952662529.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `EmptySD3LatentImage`
- `PrimitiveNode`
- `Note`
- `Note`
- `CLIPVisionEncode`
- `BasicGuider`
- `StyleModelApply`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `Note`
- `PrimitiveNode`
- `Note`
- `BasicScheduler`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoader` ★核心
- `FluxGuidance`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：lora

## 关键参数

- `lora_name` = `flux_realism_lora.safetensors`
- `strength_model` = `0.75`
- `strength_clip` = `1`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`EmptySD3LatentImage`、`CLIPVisionEncode`、`BasicGuider`、`StyleModelApply`、`CLIPVisionLoader`、`StyleModelLoader`、`VAELoader`、`VAEDecode`、`BasicScheduler`、`UNETLoader`、`DualCLIPLoader`、`LoraLoader`、`FluxGuidance`、`LoadImage`、`SaveImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
