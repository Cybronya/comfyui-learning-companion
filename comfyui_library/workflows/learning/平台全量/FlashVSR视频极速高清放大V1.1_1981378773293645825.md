---
key: 平台全量/FlashVSR视频极速高清放大V1.1_1981378773293645825.json
name: FlashVSR视频极速高清放大V1.1_1981378773293645825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FlashVSR视频极速高清放大V1.1_1981378773293645825.json
hash: 846405cf9b73507b
coverage: 1
learned_at: 2026-11-14 00:27:07
nodes: [CreateVideo, ImageFromBatch+, FlashVSR_SM_KSampler, GetVideoComponents, LoadVideo, GetVideoComponents, JWInteger, VHS_VideoCombine, SaveVideo, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, FlashVSR_SM_Model]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1903554175}
---

# 平台全量/FlashVSR视频极速高清放大V1.1_1981378773293645825.json

> 来源文件 `comfyui_library/workflows/平台全量/FlashVSR视频极速高清放大V1.1_1981378773293645825.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（12 个）：
- `CreateVideo`
- `ImageFromBatch+`
- `FlashVSR_SM_KSampler` ★核心
- `GetVideoComponents`
- `LoadVideo`
- `GetVideoComponents`
- `JWInteger`
- `VHS_VideoCombine`
- `SaveVideo`
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FlashVSR_SM_Model`

## 关键参数

- `seed` = `1280`
- `steps` = `1903554175`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`CreateVideo`、`ImageFromBatch+`、`FlashVSR_SM_KSampler`、`GetVideoComponents`、`LoadVideo`、`JWInteger`、`VHS_VideoCombine`、`SaveVideo`、`ImageConcanate`、`LayerUtility: ImageScaleByAspectRatio V2`、`FlashVSR_SM_Model`

**用到的条目**：FlashVSR_SM_KSampler、SaveVideo、CreateVideo、FlashVSR_SM_Model、GetVideoComponents、ImageConcanate、ImageFromBatch+、JWInteger
