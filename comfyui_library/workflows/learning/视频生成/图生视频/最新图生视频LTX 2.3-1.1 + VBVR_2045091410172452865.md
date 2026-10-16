---
key: 视频生成/图生视频/最新图生视频LTX 2.3-1.1 + VBVR_2045091410172452865.json
name: 最新图生视频LTX 2.3-1.1 + VBVR_2045091410172452865.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2045091410172452865.json
hash: 4dc401cb94b4f060
coverage: 0.8
learned_at: 2026-10-15 22:36:45
nodes: [Note, LoraLoaderModelOnly, CLIPTextEncode, VRAMReserver, LoraLoaderModelOnly, image_scale_pixel_v2, PrimitiveInt, LayerUtility: PurgeVRAM V2, Seed Everywhere, workflow>9958, CheckpointLoaderSimple, PrimitiveFloat, CLIPTextEncode, LoadImage, SaveVideo]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors"}
---

# 视频生成/图生视频/最新图生视频LTX 2.3-1.1 + VBVR_2045091410172452865.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2045091410172452865.json`

## 结构

**生成流程**：Model → Condition → Process → Output → Other

**节点**（15 个）：
- `Note`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `image_scale_pixel_v2`
- `PrimitiveInt`
- `LayerUtility: PurgeVRAM V2`
- `Seed Everywhere`
- `workflow>9958`
- `CheckpointLoaderSimple` ★核心
- `PrimitiveFloat`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `SaveVideo`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`LoraLoaderModelOnly`、`CLIPTextEncode`、`VRAMReserver`、`image_scale_pixel_v2`、`LayerUtility: PurgeVRAM V2`、`Seed Everywhere`、`workflow>9958`、`CheckpointLoaderSimple`、`LoadImage`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Seed Everywhere、SaveVideo、image_scale_pixel_v2、VRAMReserver
