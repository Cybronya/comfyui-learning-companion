---
key: 平台全量/seedance2.0 视频高清放大_2021176268426842114.json
name: seedance2.0 视频高清放大_2021176268426842114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/seedance2.0 视频高清放大_2021176268426842114.json
hash: abeeb1bacf6c26d9
coverage: 1
learned_at: 2026-11-14 01:17:38
nodes: [LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, FlashVSR_SM_KSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoInfo, LoadImage, LoadImage, FlashVSR_SM_Model]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 768, "steps": 1409698427}
---

# 平台全量/seedance2.0 视频高清放大_2021176268426842114.json

> 来源文件 `comfyui_library/workflows/平台全量/seedance2.0 视频高清放大_2021176268426842114.json`

## 结构

**生成流程**：Sampling → Process → Other

**节点**（9 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `FlashVSR_SM_KSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `LoadImage`
- `LoadImage`
- `FlashVSR_SM_Model`

## 关键参数

- `seed` = `768`
- `steps` = `1409698427`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`FlashVSR_SM_KSampler`、`VHS_VideoCombine`、`VHS_VideoInfo`、`LoadImage`、`FlashVSR_SM_Model`

**用到的条目**：LoadImage、FlashVSR_SM_KSampler、FlashVSR_SM_Model、LayerUtility: ImageScaleByAspectRatio V2、VHS_LoadVideo、VHS_VideoCombine、VHS_VideoInfo、KSampler
