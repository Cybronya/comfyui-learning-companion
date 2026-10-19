---
key: 图片生成/文生图/Z-Image：BEYOND REALITY⚡️超越真实⚡️V3.0_2007353437893169153.json
name: Z-Image：BEYOND REALITY⚡️超越真实⚡️V3.0_2007353437893169153
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image：BEYOND REALITY⚡️超越真实⚡️V3.0_2007353437893169153.json
hash: 06c5a74ea641dace
coverage: 0.883721
learned_at: 2026-10-19 22:01:02
nodes: [Reroute, CLIPTextEncode, CFGNorm, EmptyLatentImage, CLIPTextEncode, EmptyLatentImage, CLIPTextEncode, EmptyLatentImage, SaveImage, SaveImage, CLIPTextEncode, CLIPTextEncode, Reroute, CLIPTextEncode, CLIPLoader, VAELoader, Reroute, MuyeSizeSelector, Reroute, Reroute, ProcessString, CFGNorm, CFGNorm, UNETLoader, UNETLoader, UNETLoader, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, VAEDecode, VAEDecode, ImageConcatMulti, AddLabel, AddLabel, VAEDecode, AddLabel, easy promptLine, easy promptLine, KSampler, KSampler, KSampler, SaveImage, SaveImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1600, "sampler_name": "euler", "scheduler": "simple", "seed": 763095163055431, "steps": 10, "width": 1200}
---

# 图片生成/文生图/Z-Image：BEYOND REALITY⚡️超越真实⚡️V3.0_2007353437893169153.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image：BEYOND REALITY⚡️超越真实⚡️V3.0_2007353437893169153.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `Reroute`
- `CLIPTextEncode` ★核心
- `CFGNorm`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `MuyeSizeSelector`
- `Reroute`
- `Reroute`
- `ProcessString`
- `CFGNorm`
- `CFGNorm`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `AddLabel`
- `AddLabel`
- `VAEDecode` ★核心
- `AddLabel`
- `easy promptLine`
- `easy promptLine`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1200`
- `height` = `1600`
- `batch_size` = `1`
- `seed` = `763095163055431`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（38/43）

**有卡**：`CLIPTextEncode`、`CFGNorm`、`EmptyLatentImage`、`SaveImage`、`CLIPLoader`、`VAELoader`、`MuyeSizeSelector`、`ProcessString`、`UNETLoader`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`ImageConcatMulti`、`AddLabel`、`easy promptLine`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、CFGNorm
