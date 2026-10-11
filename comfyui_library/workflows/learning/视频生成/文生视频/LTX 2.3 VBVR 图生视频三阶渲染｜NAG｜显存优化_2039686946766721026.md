---
key: 视频生成/文生视频/LTX 2.3 VBVR 图生视频三阶渲染｜NAG｜显存优化_2039686946766721026.json
name: LTX 2.3 VBVR 图生视频三阶渲染｜NAG｜显存优化_2039686946766721026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3 VBVR 图生视频三阶渲染｜NAG｜显存优化_2039686946766721026.json
hash: a28e02f72119fd79
coverage: 0.810811
learned_at: 2026-10-11 19:49:34
nodes: [LoadImage, image_scale_pixel_v2, CLIPTextEncode, CheckpointLoaderSimple, workflow>675, LoadImage, image_scale_pixel_v2, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, workflow>675, LoadImage, image_scale_pixel_v2, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple, workflow>675, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveVideo, SaveVideo, SaveVideo, CLIPTextEncode, image_scale_pixel_v2, PrimitiveFloat, PrimitiveInt, LoraLoaderModelOnly, SaveVideo, CLIPTextEncode, LoraLoaderModelOnly, CheckpointLoaderSimple, VRAMReserver, LoadImage, workflow>515, Note, CLIPTextEncode]
patterns: []
missing: [workflow>515, workflow>675, workflow>675, workflow>675]
parameters: {"checkpoint": "ltx-2.3-22b-distilled.safetensors"}
discoveries: [次要节点 `workflow>515` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>675` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>675` 知识库中没有该节点类型的任何知识, 次要节点 `workflow>675` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX 2.3 VBVR 图生视频三阶渲染｜NAG｜显存优化_2039686946766721026.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3 VBVR 图生视频三阶渲染｜NAG｜显存优化_2039686946766721026.json`

## 结构

**生成流程**：Model → Condition → Process → Output → Other

**节点**（37 个）：
- `LoadImage`
- `image_scale_pixel_v2`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `workflow>675`
- `LoadImage`
- `image_scale_pixel_v2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `workflow>675`
- `LoadImage`
- `image_scale_pixel_v2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `workflow>675`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `SaveVideo`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `image_scale_pixel_v2`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `VRAMReserver`
- `LoadImage`
- `workflow>515`
- `Note`
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `ltx-2.3-22b-distilled.safetensors`

## 知识

覆盖率 **81%**（30/37）

**有卡**：`LoadImage`、`image_scale_pixel_v2`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`SaveVideo`、`VRAMReserver`

**缺卡**（4）：`workflow>515`、`workflow>675`、`workflow>675`、`workflow>675`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、SaveVideo、image_scale_pixel_v2、VRAMReserver、sd15-t2i-basic

## 学习发现

- 次要节点 `workflow>515` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>675` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>675` 知识库中没有该节点类型的任何知识
- 次要节点 `workflow>675` 知识库中没有该节点类型的任何知识
