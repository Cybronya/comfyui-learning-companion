---
key: 平台全量/VSR放大高清 浮云3.9_2030932744414433282.json
name: VSR放大高清 浮云3.9_2030932744414433282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/VSR放大高清 浮云3.9_2030932744414433282.json
hash: f04e2724cb735f46
coverage: 1
learned_at: 2026-11-14 01:03:08
nodes: [JWInteger, GetVideoComponents, FlashVSR_SM_Model, ImageFromBatch+, JWInteger, GetVideoComponents, CreateVideo, GetVideoComponents, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, FlashVSR_SM_KSampler, LoadVideo]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 861493885}
---

# 平台全量/VSR放大高清 浮云3.9_2030932744414433282.json

> 来源文件 `comfyui_library/workflows/平台全量/VSR放大高清 浮云3.9_2030932744414433282.json`

## 结构

**生成流程**：Sampling → Process → Other

**节点**（12 个）：
- `JWInteger`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `JWInteger`
- `GetVideoComponents`
- `CreateVideo`
- `GetVideoComponents`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `FlashVSR_SM_KSampler` ★核心
- `LoadVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `861493885`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`JWInteger`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`CreateVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoCombine`、`FlashVSR_SM_KSampler`、`LoadVideo`

**用到的条目**：FlashVSR_SM_KSampler、CreateVideo、FlashVSR_SM_Model、GetVideoComponents、ImageFromBatch+、JWInteger、LayerUtility: ImageScaleByAspectRatio V2、LoadVideo
