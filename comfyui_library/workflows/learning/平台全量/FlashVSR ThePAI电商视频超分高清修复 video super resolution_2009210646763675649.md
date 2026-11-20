---
key: 平台全量/FlashVSR ThePAI电商视频超分高清修复 video super resolution_2009210646763675649.json
name: FlashVSR ThePAI电商视频超分高清修复 video super resolution_2009210646763675649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FlashVSR ThePAI电商视频超分高清修复 video super resolution_2009210646763675649.json
hash: 21ee5030f62084d7
coverage: 0.782609
learned_at: 2026-11-14 00:26:55
nodes: [FlashVSR_SM_KSampler, VHS_VideoCombine, ImageConcatMulti, Reroute (rgthree), VHS_VideoCombine, VHS_VideoInfo, FlashVSR_SM_Model, JWInteger, Reroute, Note, ImageScaleToTotalPixels, MarkdownNote, VHS_LoadVideo, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, ImageConcatMulti, VHS_VideoInfo, Fast Groups Bypasser (rgthree), JWInteger, VHS_VideoCombine, VHS_LoadVideo, FlashVSRNode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 961592704}
---

# 平台全量/FlashVSR ThePAI电商视频超分高清修复 video super resolution_2009210646763675649.json

> 来源文件 `comfyui_library/workflows/平台全量/FlashVSR ThePAI电商视频超分高清修复 video super resolution_2009210646763675649.json`

## 结构

**生成流程**：Sampling → Process → Other

**节点**（23 个）：
- `FlashVSR_SM_KSampler` ★核心
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `Reroute (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `FlashVSR_SM_Model`
- `JWInteger`
- `Reroute`
- `Note`
- `ImageScaleToTotalPixels`
- `MarkdownNote`
- `VHS_LoadVideo`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `ImageConcatMulti`
- `VHS_VideoInfo`
- `Fast Groups Bypasser (rgthree)`
- `JWInteger`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `FlashVSRNode`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1280`
- `steps` = `961592704`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`FlashVSR_SM_KSampler`、`VHS_VideoCombine`、`ImageConcatMulti`、`VHS_VideoInfo`、`FlashVSR_SM_Model`、`JWInteger`、`ImageScaleToTotalPixels`、`VHS_LoadVideo`、`LayerUtility: PurgeVRAM V2`、`FlashVSRNode`

**用到的条目**：FlashVSR_SM_KSampler、FlashVSR_SM_Model、FlashVSRNode、ImageConcatMulti、ImageScaleToTotalPixels、JWInteger、LayerUtility: PurgeVRAM V2、VHS_LoadVideo
