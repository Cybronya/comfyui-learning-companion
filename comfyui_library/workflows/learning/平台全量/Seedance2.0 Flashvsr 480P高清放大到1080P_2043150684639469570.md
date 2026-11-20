---
key: 平台全量/Seedance2.0 Flashvsr 480P高清放大到1080P_2043150684639469570.json
name: Seedance2.0 Flashvsr 480P高清放大到1080P_2043150684639469570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Seedance2.0 Flashvsr 480P高清放大到1080P_2043150684639469570.json
hash: 2039de54619e2923
coverage: 1
learned_at: 2026-11-14 01:00:20
nodes: [CreateVideo, JWInteger, GetVideoComponents, FlashVSR_SM_Model, GetVideoComponents, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, LoadVideo, SaveVideo, FlashVSR_SM_KSampler]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 791730981}
---

# 平台全量/Seedance2.0 Flashvsr 480P高清放大到1080P_2043150684639469570.json

> 来源文件 `comfyui_library/workflows/平台全量/Seedance2.0 Flashvsr 480P高清放大到1080P_2043150684639469570.json`

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
- `LoadVideo`
- `SaveVideo`
- `FlashVSR_SM_KSampler` ★核心

## 关键参数

- `seed` = `1280`
- `steps` = `791730981`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`CreateVideo`、`JWInteger`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadVideo`、`SaveVideo`、`FlashVSR_SM_KSampler`

**用到的条目**：FlashVSR_SM_KSampler、SaveVideo、CreateVideo、FlashVSR_SM_Model、GetVideoComponents、ImageFromBatch+、JWInteger、LayerUtility: ImageScaleByAspectRatio V2
