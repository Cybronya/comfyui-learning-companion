---
key: 视频生成/文生视频/『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：图生视视频_2047659084744232962.json
name: 『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：图生视视频_2047659084744232962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：图生视视频_2047659084744232962.json
hash: 3a5b13854958298a
coverage: 0.857143
learned_at: 2026-10-15 22:47:38
nodes: [CLIPTextEncode, image_scale_pixel_v2, PrimitiveFloat, LayerUtility: PurgeVRAM V2, workflow>9958, CheckpointLoaderSimple, SaveVideo, VRAMReserver, LoraLoaderModelOnly, LoraLoaderModelOnly, Seed Everywhere, LoadImage, PrimitiveInt, CLIPTextEncode]
patterns: []
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors"}
---

# 视频生成/文生视频/『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：图生视视频_2047659084744232962.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：图生视视频_2047659084744232962.json`

## 结构

**生成流程**：Model → Condition → Process → Output → Other

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `image_scale_pixel_v2`
- `PrimitiveFloat`
- `LayerUtility: PurgeVRAM V2`
- `workflow>9958`
- `CheckpointLoaderSimple` ★核心
- `SaveVideo`
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Seed Everywhere`
- `LoadImage`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`CLIPTextEncode`、`image_scale_pixel_v2`、`LayerUtility: PurgeVRAM V2`、`workflow>9958`、`CheckpointLoaderSimple`、`SaveVideo`、`VRAMReserver`、`LoraLoaderModelOnly`、`Seed Everywhere`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Seed Everywhere、SaveVideo、image_scale_pixel_v2、VRAMReserver
