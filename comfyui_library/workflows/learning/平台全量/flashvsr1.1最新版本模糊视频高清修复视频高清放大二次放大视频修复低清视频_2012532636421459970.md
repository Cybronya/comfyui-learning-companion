---
key: 平台全量/flashvsr1.1最新版本模糊视频高清修复视频高清放大二次放大视频修复低清视频_2012532636421459970.json
name: flashvsr1.1最新版本模糊视频高清修复视频高清放大二次放大视频修复低清视频_2012532636421459970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/flashvsr1.1最新版本模糊视频高清修复视频高清放大二次放大视频修复低清视频_2012532636421459970.json
hash: 8c3994f3c2bfaa4d
coverage: 1
learned_at: 2026-11-14 01:10:30
nodes: [FlashVSR_SM_Model, LayerUtility: ImageScaleByAspectRatio V2, FlashVSR_SM_KSampler, VHS_VideoCombine, VHS_VideoInfoLoaded, ShowAnything|Mie, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 1, "scheduler": 3.5, "seed": 1280, "steps": 1173738585}
---

# 平台全量/flashvsr1.1最新版本模糊视频高清修复视频高清放大二次放大视频修复低清视频_2012532636421459970.json

> 来源文件 `comfyui_library/workflows/平台全量/flashvsr1.1最新版本模糊视频高清修复视频高清放大二次放大视频修复低清视频_2012532636421459970.json`

## 结构

**生成流程**：Sampling → Process → Other

**节点**（7 个）：
- `FlashVSR_SM_Model`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FlashVSR_SM_KSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `ShowAnything|Mie`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `1173738585`
- `cfg` = `randomize`
- `sampler_name` = `1`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`FlashVSR_SM_Model`、`LayerUtility: ImageScaleByAspectRatio V2`、`FlashVSR_SM_KSampler`、`VHS_VideoCombine`、`VHS_VideoInfoLoaded`、`ShowAnything|Mie`、`VHS_LoadVideo`

**用到的条目**：FlashVSR_SM_KSampler、FlashVSR_SM_Model、LayerUtility: ImageScaleByAspectRatio V2、ShowAnything|Mie、VHS_LoadVideo、VHS_VideoCombine、VHS_VideoInfoLoaded、KSampler
