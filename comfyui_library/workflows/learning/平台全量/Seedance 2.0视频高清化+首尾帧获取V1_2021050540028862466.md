---
key: 平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2021050540028862466.json
name: Seedance 2.0视频高清化+首尾帧获取V1_2021050540028862466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2021050540028862466.json
hash: 45fe2cd27caea4e5
coverage: 1
learned_at: 2026-11-14 01:00:16
nodes: [CreateVideo, SaveVideo, GetVideoComponents, FlashVSR_SM_Model, GetVideoComponents, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, ImageConcanate, FlashVSR_SM_KSampler, GetImageSizeAndCount, JWInteger, VHS_VideoCombine, ImageFromBatch+, ImageFromBatch+, SaveImage, SaveImage, LoadVideo]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1277587980}
---

# 平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2021050540028862466.json

> 来源文件 `comfyui_library/workflows/平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2021050540028862466.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（18 个）：
- `CreateVideo`
- `SaveVideo`
- `GetVideoComponents`
- `FlashVSR_SM_Model`
- `GetVideoComponents`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `ImageConcanate`
- `FlashVSR_SM_KSampler` ★核心
- `GetImageSizeAndCount`
- `JWInteger`
- `VHS_VideoCombine`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `SaveImage`
- `SaveImage`
- `LoadVideo`

## 关键参数

- `seed` = `1280`
- `steps` = `1277587980`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`CreateVideo`、`SaveVideo`、`GetVideoComponents`、`FlashVSR_SM_Model`、`ImageFromBatch+`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`ImageConcanate`、`FlashVSR_SM_KSampler`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`SaveImage`、`LoadVideo`

**用到的条目**：FlashVSR_SM_KSampler、GetImageSizeAndCount、SaveImage、SaveVideo、CreateVideo、FlashVSR_SM_Model、GetVideoComponents、ImageConcanate
