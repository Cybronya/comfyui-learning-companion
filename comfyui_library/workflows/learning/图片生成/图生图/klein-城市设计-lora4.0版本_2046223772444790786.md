---
key: 图片生成/图生图/klein-城市设计-lora4.0版本_2046223772444790786.json
name: klein-城市设计-lora4.0版本_2046223772444790786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/klein-城市设计-lora4.0版本_2046223772444790786.json
hash: 6a8803f0a8e2de81
coverage: 0.733333
learned_at: 2026-10-23 11:38:17
nodes: [KSamplerSelect, CFGGuider, Reroute, Reroute, RandomNoise, EmptyFlux2LatentImage, Reroute, CLIPLoader, UNETLoader, CLIPTextEncode, SamplerCustomAdvanced, Flux2Scheduler, Reroute, SaveImage, VAELoader, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, ReferenceLatent, ReferenceLatent, Reroute, Reroute, Reroute, Reroute, LoraLoaderModelOnly, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, CLIPTextEncode, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/klein-城市设计-lora4.0版本_2046223772444790786.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/klein-城市设计-lora4.0版本_2046223772444790786.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `KSamplerSelect` ★核心
- `CFGGuider`
- `Reroute`
- `Reroute`
- `RandomNoise`
- `EmptyFlux2LatentImage`
- `Reroute`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `Reroute`
- `SaveImage`
- `VAELoader`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 知识

覆盖率 **73%**（22/30）

**有卡**：`KSamplerSelect`、`CFGGuider`、`RandomNoise`、`EmptyFlux2LatentImage`、`CLIPLoader`、`UNETLoader`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`SaveImage`、`VAELoader`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEEncode`、`ReferenceLatent`、`LoraLoaderModelOnly`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider
