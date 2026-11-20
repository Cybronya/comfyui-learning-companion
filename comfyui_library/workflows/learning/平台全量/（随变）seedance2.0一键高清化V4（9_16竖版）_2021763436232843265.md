---
key: 平台全量/（随变）seedance2.0一键高清化V4（9_16竖版）_2021763436232843265.json
name: （随变）seedance2.0一键高清化V4（9_16竖版）_2021763436232843265
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/（随变）seedance2.0一键高清化V4（9_16竖版）_2021763436232843265.json
hash: 225695b86f321d6b
coverage: 1
learned_at: 2026-11-14 02:54:14
nodes: [CreateVideo, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, GetVideoComponents, GetVideoComponents, ImageFromBatch+, FlashVSR_SM_Model, FlashVSR_SM_KSampler, ImageConcanate, VHS_VideoCombine, CreateVideo, SaveVideo, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1608761770}
---

# 平台全量/（随变）seedance2.0一键高清化V4（9_16竖版）_2021763436232843265.json

> 来源文件 `comfyui_library/workflows/平台全量/（随变）seedance2.0一键高清化V4（9_16竖版）_2021763436232843265.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（14 个）：
- `CreateVideo`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `GetVideoComponents`
- `GetVideoComponents`
- `ImageFromBatch+`
- `FlashVSR_SM_Model`
- `FlashVSR_SM_KSampler` ★核心
- `ImageConcanate`
- `VHS_VideoCombine`
- `CreateVideo`
- `SaveVideo`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `1608761770`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`CreateVideo`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetVideoComponents`、`ImageFromBatch+`、`FlashVSR_SM_Model`、`FlashVSR_SM_KSampler`、`ImageConcanate`、`VHS_VideoCombine`、`SaveVideo`、`VHS_LoadVideo`

**用到的条目**：FlashVSR_SM_KSampler、SaveVideo、CreateVideo、FlashVSR_SM_Model、GetVideoComponents、ImageConcanate、ImageFromBatch+、JWInteger
