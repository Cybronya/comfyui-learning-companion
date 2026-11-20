---
key: 平台全量/视频转白膜模式sam3.1使用_2114748488465608705.json
name: 视频转白膜模式sam3.1使用_2114748488465608705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频转白膜模式sam3.1使用_2114748488465608705.json
hash: bba2439f37a0a6ee
coverage: 1
learned_at: 2026-11-14 02:41:43
nodes: [VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, SAM3_VideoTrack, CheckpointLoaderSimple, CLIPTextEncode, SAM3DBody_Predict, SAM3DBody_Loader, SAM3DBody_Render, SCAIL2ColoredMask, ImageCompositeMasked, ImageToMask, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_Multiplex_fp16.safetensors"}
---

# 平台全量/视频转白膜模式sam3.1使用_2114748488465608705.json

> 来源文件 `comfyui_library/workflows/平台全量/视频转白膜模式sam3.1使用_2114748488465608705.json`

## 结构

**生成流程**：Model → Condition → Process → Other

**节点**（12 个）：
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SAM3_VideoTrack`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `SAM3DBody_Predict`
- `SAM3DBody_Loader`
- `SAM3DBody_Render`
- `SCAIL2ColoredMask`
- `ImageCompositeMasked`
- `ImageToMask`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `sam3.1_Multiplex_fp16.safetensors`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`SAM3_VideoTrack`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`SAM3DBody_Predict`、`SAM3DBody_Loader`、`SAM3DBody_Render`、`SCAIL2ColoredMask`、`ImageCompositeMasked`、`ImageToMask`、`VHS_VideoCombine`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、ImageCompositeMasked、ImageToMask、LayerUtility: ImageScaleByAspectRatio V2、SAM3_VideoTrack、SAM3DBody_Loader、SAM3DBody_Predict
