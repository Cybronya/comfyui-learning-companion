---
key: 图片生成/图生图/FLUX.小红书网红生成机_1891789004021379074.json
name: FLUX.小红书网红生成机_1891789004021379074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.小红书网红生成机_1891789004021379074.json
hash: 6a409827936fa0ee
coverage: 0.909091
learned_at: 2026-10-23 10:54:18
nodes: [TextInput_, easy promptConcat, BasicScheduler, ModelSamplingFlux, Reroute, SaveImage, VAELoader, VAEDecode, DualCLIPLoader, RandomNoise, FluxGuidance, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, LoraLoaderModelOnly, UNETLoader, LoadImage, RH_Captioner, CLIPTextEncode, CR SDXL Aspect Ratio, ShowText|pysssss, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.小红书网红生成机_1891789004021379074.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.小红书网红生成机_1891789004021379074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（22 个）：
- `TextInput_`
- `easy promptConcat`
- `BasicScheduler`
- `ModelSamplingFlux`
- `Reroute`
- `SaveImage`
- `VAELoader`
- `VAEDecode` ★核心
- `DualCLIPLoader`
- `RandomNoise`
- `FluxGuidance`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `RH_Captioner`
- `CLIPTextEncode` ★核心
- `CR SDXL Aspect Ratio`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **91%**（20/22）

**有卡**：`TextInput_`、`easy promptConcat`、`BasicScheduler`、`ModelSamplingFlux`、`SaveImage`、`VAELoader`、`VAEDecode`、`DualCLIPLoader`、`RandomNoise`、`FluxGuidance`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`、`RH_Captioner`、`CLIPTextEncode`、`CR SDXL Aspect Ratio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect
