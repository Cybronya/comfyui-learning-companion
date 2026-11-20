---
key: 平台全量/真实好用！seedance2.0 视频高清放大 最强视频编辑王者！_2021795658616807426.json
name: 真实好用！seedance2.0 视频高清放大 最强视频编辑王者！_2021795658616807426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/真实好用！seedance2.0 视频高清放大 最强视频编辑王者！_2021795658616807426.json
hash: 06ecb2e84793fe20
coverage: 1
learned_at: 2026-11-14 02:26:49
nodes: [FlashVSR_SM_Model, FlashVSR_SM_KSampler, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, VHS_VideoInfo, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 768, "steps": 1501089514}
---

# 平台全量/真实好用！seedance2.0 视频高清放大 最强视频编辑王者！_2021795658616807426.json

> 来源文件 `comfyui_library/workflows/平台全量/真实好用！seedance2.0 视频高清放大 最强视频编辑王者！_2021795658616807426.json`

## 结构

**生成流程**：Sampling → Process → Other

**节点**（7 个）：
- `FlashVSR_SM_Model`
- `FlashVSR_SM_KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `768`
- `steps` = `1501089514`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`FlashVSR_SM_Model`、`FlashVSR_SM_KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`VHS_VideoInfo`、`VHS_VideoCombine`

**用到的条目**：FlashVSR_SM_KSampler、FlashVSR_SM_Model、LayerUtility: ImageScaleByAspectRatio V2、VHS_LoadVideo、VHS_VideoCombine、VHS_VideoInfo、KSampler、image_to_image_controlnet_face_detailer_lora
