---
key: 平台全量/Seedance2.0 Flashvsr 480P高清放大到1080P_2084198101111361537.json
name: Seedance2.0 Flashvsr 480P高清放大到1080P_2084198101111361537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Seedance2.0 Flashvsr 480P高清放大到1080P_2084198101111361537.json
hash: ed53dddbf6d8453d
coverage: 1
learned_at: 2026-11-14 01:00:20
nodes: [CreateVideo, JWInteger, GetVideoComponents, FlashVSR_SM_Model, GetVideoComponents, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, SaveVideo, FlashVSR_SM_KSampler, LoadVideo]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1520721912}
---

# 平台全量/Seedance2.0 Flashvsr 480P高清放大到1080P_2084198101111361537.json

> 来源文件 `comfyui_library/workflows/平台全量/Seedance2.0 Flashvsr 480P高清放大到1080P_2084198101111361537.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（11 个）：
- `CreateVideo`
- `JWInteger`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `GetVideoComponents`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `SaveVideo`
- `FlashVSR_SM_KSampler` ★核心
- `LoadVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `1520721912`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`CreateVideo`、`JWInteger`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveVideo`、`FlashVSR_SM_KSampler`、`LoadVideo`

**用到的条目**：FlashVSR_SM_KSampler、SaveVideo、CreateVideo、FlashVSR_SM_Model、GetVideoComponents、ImageFromBatch+、JWInteger、LayerUtility: ImageScaleByAspectRatio V2
