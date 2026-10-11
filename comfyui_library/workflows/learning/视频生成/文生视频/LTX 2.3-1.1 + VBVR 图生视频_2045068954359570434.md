---
key: 视频生成/文生视频/LTX 2.3-1.1 + VBVR 图生视频_2045068954359570434.json
name: LTX 2.3-1.1 + VBVR 图生视频_2045068954359570434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3-1.1 + VBVR 图生视频_2045068954359570434.json
hash: f5eef02c748d9362
coverage: 0.6
learned_at: 2026-10-11 19:49:35
nodes: [Note, LoraLoaderModelOnly, SaveVideo, CLIPTextEncode, VRAMReserver, LoadImage, CLIPTextEncode, LoraLoaderModelOnly, image_scale_pixel_v2, PrimitiveInt, PrimitiveFloat, LayerUtility: PurgeVRAM V2, Seed Everywhere, workflow>9958, CheckpointLoaderSimple]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, workflow>9958, Seed Everywhere]
parameters: {"checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors"}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>9958` 知识库中没有该节点类型的任何知识, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/LTX 2.3-1.1 + VBVR 图生视频_2045068954359570434.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3-1.1 + VBVR 图生视频_2045068954359570434.json`

## 结构

**生成流程**：Model → Condition → Process → Output → Other

**节点**（15 个）：
- `Note`
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `VRAMReserver`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `image_scale_pixel_v2`
- `PrimitiveInt`
- `PrimitiveFloat`
- `LayerUtility: PurgeVRAM V2`
- `Seed Everywhere`
- `workflow>9958`
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **60%**（9/15）

**有卡**：`LoraLoaderModelOnly`、`SaveVideo`、`CLIPTextEncode`、`VRAMReserver`、`LoadImage`、`image_scale_pixel_v2`、`CheckpointLoaderSimple`

**缺卡**（3）：`LayerUtility: PurgeVRAM V2`、`workflow>9958`、`Seed Everywhere`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveVideo、image_scale_pixel_v2、VRAMReserver、sd15-t2i-basic

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>9958` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
