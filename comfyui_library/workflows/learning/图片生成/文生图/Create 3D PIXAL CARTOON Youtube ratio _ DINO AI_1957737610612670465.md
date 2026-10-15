---
key: 图片生成/文生图/Create 3D PIXAL CARTOON Youtube ratio _ DINO AI_1957737610612670465.json
name: Create 3D PIXAL CARTOON Youtube ratio _ DINO AI_1957737610612670465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Create 3D PIXAL CARTOON Youtube ratio _ DINO AI_1957737610612670465.json
hash: 374c8e96e0511083
coverage: 1
learned_at: 2026-10-15 22:26:14
nodes: [VAEDecode, VAELoader, SamplerCustomAdvanced, KSamplerSelect, BasicScheduler, BasicGuider, RandomNoise, FluxGuidance, LoraLoaderModelOnly, DualCLIPLoader, UNETLoader, ModelSamplingFlux, SaveImage, CLIPTextEncode, CR SDXL Aspect Ratio]
patterns: []
missing: []
---

# 图片生成/文生图/Create 3D PIXAL CARTOON Youtube ratio _ DINO AI_1957737610612670465.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Create 3D PIXAL CARTOON Youtube ratio _ DINO AI_1957737610612670465.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `RandomNoise`
- `FluxGuidance`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingFlux`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CR SDXL Aspect Ratio`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`VAEDecode`、`VAELoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`FluxGuidance`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`UNETLoader`、`ModelSamplingFlux`、`SaveImage`、`CLIPTextEncode`、`CR SDXL Aspect Ratio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
