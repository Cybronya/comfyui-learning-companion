---
key: 平台全量/seedance2.0 视频高清放大_2021767550123646978.json
name: seedance2.0 视频高清放大_2021767550123646978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/seedance2.0 视频高清放大_2021767550123646978.json
hash: 7638b975e8c2e408
coverage: 1
learned_at: 2026-11-14 01:17:40
nodes: [LayerUtility: ImageScaleByAspectRatio V2, FlashVSR_SM_KSampler, VHS_VideoCombine, FlashVSR_SM_Model, VHS_VideoInfo, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 768, "steps": 1244665281}
---

# 平台全量/seedance2.0 视频高清放大_2021767550123646978.json

> 来源文件 `comfyui_library/workflows/平台全量/seedance2.0 视频高清放大_2021767550123646978.json`

## 结构

**生成流程**：Sampling → Process → Other

**节点**（7 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FlashVSR_SM_KSampler` ★核心
- `VHS_VideoCombine`
- `FlashVSR_SM_Model`
- `VHS_VideoInfo`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `768`
- `steps` = `1244665281`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`FlashVSR_SM_KSampler`、`VHS_VideoCombine`、`FlashVSR_SM_Model`、`VHS_VideoInfo`、`VHS_LoadVideo`

**用到的条目**：FlashVSR_SM_KSampler、FlashVSR_SM_Model、LayerUtility: ImageScaleByAspectRatio V2、VHS_LoadVideo、VHS_VideoCombine、VHS_VideoInfo、KSampler、image_to_image_controlnet_face_detailer_lora
