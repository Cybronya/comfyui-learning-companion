---
key: 平台全量/Flux GGUF - simple workflow for low vram machines_1892109645031366657.json
name: Flux GGUF - simple workflow for low vram machines_1892109645031366657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux GGUF - simple workflow for low vram machines_1892109645031366657.json
hash: 8e5d4ec522e4cc8e
coverage: 0.652174
learned_at: 2026-11-14 00:27:40
nodes: [UnetLoaderGGUF, Note, RandomNoise, BasicScheduler, SaveImage, Reroute, Reroute, Reroute, KSamplerSelect, Reroute, SamplerCustomAdvanced, CLIPTextEncode, BasicGuider, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, VAEDecodeTiled_TiledDiffusion, Reroute, Note, DPRandomGenerator, EmptyLatentImage, Reroute, DualCLIPLoader, VAELoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1152, "width": 896}
---

# 平台全量/Flux GGUF - simple workflow for low vram machines_1892109645031366657.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux GGUF - simple workflow for low vram machines_1892109645031366657.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `UnetLoaderGGUF` ★核心
- `Note`
- `RandomNoise`
- `BasicScheduler`
- `SaveImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `KSamplerSelect` ★核心
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecodeTiled_TiledDiffusion` ★核心
- `Reroute`
- `Note`
- `DPRandomGenerator`
- `EmptyLatentImage` ★核心
- `Reroute`
- `DualCLIPLoader`
- `VAELoader`

## 关键参数

- `width` = `896`
- `height` = `1152`
- `batch_size` = `1`

## 知识

覆盖率 **65%**（15/23）

**有卡**：`UnetLoaderGGUF`、`RandomNoise`、`BasicScheduler`、`SaveImage`、`KSamplerSelect`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`BasicGuider`、`LoraLoaderModelOnly`、`LayerUtility: PurgeVRAM`、`VAEDecodeTiled_TiledDiffusion`、`DPRandomGenerator`、`EmptyLatentImage`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、EmptyLatentImage、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeTiled_TiledDiffusion、SaveImage
