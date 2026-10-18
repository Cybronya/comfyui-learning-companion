---
key: 视频生成/图生视频/(最高性价比方案-支持真人)Seedance2.0图生视频+Flashvsr高清化（贞贞的AI工坊）_2043642349795942401.json
name: (最高性价比方案-支持真人)Seedance2.0图生视频+Flashvsr高清化（贞贞的AI工坊）_2043642349795942401.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/(最高性价比方案-支持真人)Seedance2.0图生视频+Flashvsr高清化（贞贞的AI工坊）_2043642349795942401.json
hash: d8b0afab870821a7
coverage: 1
learned_at: 2026-10-15 22:36:33
nodes: [CR Prompt Text, CreateVideo, FlashVSR_SM_KSampler, ImageConcanate, JWInteger, GetVideoComponents, FlashVSR_SM_Model, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch+, JWInteger, GetVideoComponents, VHS_VideoCombine, LoadImage, Comfly_Doubao_Seedance2_0, CR Prompt Text, SaveVideo, Comfly_api_set]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1041322429}
---

# 视频生成/图生视频/(最高性价比方案-支持真人)Seedance2.0图生视频+Flashvsr高清化（贞贞的AI工坊）_2043642349795942401.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2043642349795942401.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（17 个）：
- `CR Prompt Text`
- `CreateVideo`
- `FlashVSR_SM_KSampler` ★核心
- `ImageConcanate`
- `JWInteger`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch+`
- `JWInteger`
- `GetVideoComponents`
- `VHS_VideoCombine`
- `LoadImage`
- `Comfly_Doubao_Seedance2_0`
- `CR Prompt Text`
- `SaveVideo`
- `Comfly_api_set`

## 关键参数

- `seed` = `1280`
- `steps` = `1041322429`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`CR Prompt Text`、`CreateVideo`、`FlashVSR_SM_KSampler`、`ImageConcanate`、`JWInteger`、`GetVideoComponents`、`FlashVSR_SM_Model`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageFromBatch+`、`VHS_VideoCombine`、`LoadImage`、`Comfly_Doubao_Seedance2_0`、`SaveVideo`、`Comfly_api_set`

**用到的条目**：LoadImage、FlashVSR_SM_KSampler、Comfly_Doubao_Seedance2_0、CR Prompt Text、SaveVideo、CreateVideo、GetVideoComponents、ImageConcanate
