---
key: 视频生成/图生视频/LTX 2.3蒸馏1.1 + VBVR 逻辑优化-图生视频_2046866167066791938.json
name: LTX 2.3蒸馏1.1 + VBVR 逻辑优化-图生视频_2046866167066791938.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX 2.3蒸馏1.1 + VBVR 逻辑优化-图生视频_2046866167066791938.json
hash: 1179ef0e8d335e00
coverage: 0.8
learned_at: 2026-10-15 22:37:01
nodes: [LoraLoaderModelOnly, SaveVideo, CLIPTextEncode, VRAMReserver, LoraLoaderModelOnly, image_scale_pixel_v2, PrimitiveInt, PrimitiveFloat, LayerUtility: PurgeVRAM V2, CheckpointLoaderSimple, Seed Everywhere, workflow>9958, LoadImage, CLIPTextEncode, Note]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-distilled.safetensors"}
---

# 视频生成/图生视频/LTX 2.3蒸馏1.1 + VBVR 逻辑优化-图生视频_2046866167066791938.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046866167066791938.json`

## 结构

**生成流程**：Model → Condition → Process → Output → Other

**节点**（15 个）：
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `image_scale_pixel_v2`
- `PrimitiveInt`
- `PrimitiveFloat`
- `LayerUtility: PurgeVRAM V2`
- `CheckpointLoaderSimple` ★核心
- `Seed Everywhere`
- `workflow>9958`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Note`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled.safetensors`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`LoraLoaderModelOnly`、`SaveVideo`、`CLIPTextEncode`、`VRAMReserver`、`image_scale_pixel_v2`、`LayerUtility: PurgeVRAM V2`、`CheckpointLoaderSimple`、`Seed Everywhere`、`workflow>9958`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Seed Everywhere、SaveVideo、image_scale_pixel_v2、VRAMReserver
