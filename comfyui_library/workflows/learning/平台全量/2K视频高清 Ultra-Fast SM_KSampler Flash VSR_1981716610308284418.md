---
key: 平台全量/2K视频高清 Ultra-Fast SM_KSampler Flash VSR_1981716610308284418.json
name: 2K视频高清 Ultra-Fast SM_KSampler Flash VSR_1981716610308284418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/2K视频高清 Ultra-Fast SM_KSampler Flash VSR_1981716610308284418.json
hash: e2be619f077ffc4c
coverage: 1
learned_at: 2026-11-14 00:11:41
nodes: [FlashVSR_SM_KSampler, VHS_VideoCombine, FlashVSRNode, VHS_VideoCombine, VHS_VideoInfo, Int, VHS_LoadVideo, ImageConcatMulti, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, FlashVSR_SM_Model, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 689342368}
---

# 平台全量/2K视频高清 Ultra-Fast SM_KSampler Flash VSR_1981716610308284418.json

> 来源文件 `comfyui_library/workflows/平台全量/2K视频高清 Ultra-Fast SM_KSampler Flash VSR_1981716610308284418.json`

## 结构

**生成流程**：Sampling → Process → Other

**节点**（13 个）：
- `FlashVSR_SM_KSampler` ★核心
- `VHS_VideoCombine`
- `FlashVSRNode`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `Int`
- `VHS_LoadVideo`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `FlashVSR_SM_Model`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 关键参数

- `seed` = `1280`
- `steps` = `689342368`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`FlashVSR_SM_KSampler`、`VHS_VideoCombine`、`FlashVSRNode`、`VHS_VideoInfo`、`Int`、`VHS_LoadVideo`、`ImageConcatMulti`、`LayerUtility: PurgeVRAM V2`、`FlashVSR_SM_Model`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：FlashVSR_SM_KSampler、FlashVSR_SM_Model、FlashVSRNode、ImageConcatMulti、Int、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM V2、VHS_LoadVideo
