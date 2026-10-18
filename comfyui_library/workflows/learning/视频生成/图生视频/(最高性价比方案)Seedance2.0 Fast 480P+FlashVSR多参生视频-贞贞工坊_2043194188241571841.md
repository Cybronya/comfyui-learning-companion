---
key: 视频生成/图生视频/(最高性价比方案)Seedance2.0 Fast 480P+FlashVSR多参生视频-贞贞工坊_2043194188241571841.json
name: (最高性价比方案)Seedance2.0 Fast 480P+FlashVSR多参生视频-贞贞工坊_2043194188241571841.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(最高性价比方案)Seedance2.0 Fast 480P+FlashVSR多参生视频-贞贞工坊_2043194188241571841.json
hash: ba48f23be484439b
coverage: 1
learned_at: 2026-10-15 22:36:31
nodes: [LoadAudio, LoadImage, CR Prompt Text, CR Prompt Text, CreateVideo, FlashVSR_SM_KSampler, ImageConcanate, JWInteger, GetVideoComponents, FlashVSR_SM_Model, GetVideoComponents, LayerUtility: ImageScaleByAspectRatio V2, SaveVideo, ImageFromBatch+, VHS_VideoCombine, Comfly_Doubao_Seedance2_0, JWInteger, Comfly_api_set, LoadImage]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1987845430}
---

# 视频生成/图生视频/(最高性价比方案)Seedance2.0 Fast 480P+FlashVSR多参生视频-贞贞工坊_2043194188241571841.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043194188241571841.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（19 个）：
- `LoadAudio`
- `LoadImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `CreateVideo`
- `FlashVSR_SM_KSampler` ★核心
- `ImageConcanate`
- `JWInteger`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `GetVideoComponents`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveVideo`
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `Comfly_Doubao_Seedance2_0`
- `JWInteger`
- `Comfly_api_set`
- `LoadImage`

## 关键参数

- `seed` = `1280`
- `steps` = `1987845430`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`LoadAudio`、`LoadImage`、`CR Prompt Text`、`CreateVideo`、`FlashVSR_SM_KSampler`、`ImageConcanate`、`JWInteger`、`GetVideoComponents`、`FlashVSR_SM_Model`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveVideo`、`ImageFromBatch+`、`VHS_VideoCombine`、`Comfly_Doubao_Seedance2_0`、`Comfly_api_set`

**用到的条目**：LoadImage、FlashVSR_SM_KSampler、Comfly_Doubao_Seedance2_0、CR Prompt Text、SaveVideo、CreateVideo、GetVideoComponents、ImageConcanate
