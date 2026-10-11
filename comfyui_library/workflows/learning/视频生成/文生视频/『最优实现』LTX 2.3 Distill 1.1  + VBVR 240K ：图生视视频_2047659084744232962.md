---
key: 视频生成/文生视频/『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：图生视视频_2047659084744232962.json
name: 『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：图生视视频_2047659084744232962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/『最优实现』LTX 2.3 Distill 1.1  + VBVR 240K ：图生视视频_2047659084744232962.json
hash: 3a5b13854958298a
coverage: 0.642857
learned_at: 2026-10-11 19:49:45
nodes: [CLIPTextEncode, image_scale_pixel_v2, PrimitiveFloat, LayerUtility: PurgeVRAM V2, workflow>9958, CheckpointLoaderSimple, SaveVideo, VRAMReserver, LoraLoaderModelOnly, LoraLoaderModelOnly, Seed Everywhere, LoadImage, PrimitiveInt, CLIPTextEncode]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, workflow>9958, Seed Everywhere]
parameters: {"checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors"}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>9958` 知识库中没有该节点类型的任何知识, 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **64%**（9/14）

**有卡**：`CLIPTextEncode`、`image_scale_pixel_v2`、`CheckpointLoaderSimple`、`SaveVideo`、`VRAMReserver`、`LoraLoaderModelOnly`、`LoadImage`

**缺卡**（3）：`LayerUtility: PurgeVRAM V2`、`workflow>9958`、`Seed Everywhere`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveVideo、image_scale_pixel_v2、VRAMReserver、sd15-t2i-basic

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>9958` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed Everywhere` 仅有 KSampler 的通用知识，没有该节点自己的说明
