---
key: 平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2021474178897022977.json
name: Seedance 2.0视频高清化+首尾帧获取V1_2021474178897022977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2021474178897022977.json
hash: f2c0f82b6092b30b
coverage: 1
learned_at: 2026-11-14 01:00:16
nodes: [FlashVSR_SM_Model, ImageFromBatch+, SaveImage, SaveImage, ImageFromBatch+, LoadVideo, GetVideoComponents, ImageFromBatch+, GetVideoComponents, LayerUtility: ImageScaleByAspectRatio V2, JWInteger, JWInteger, ImageConcanate, FlashVSR_SM_KSampler, CreateVideo, SaveVideo, GetImageSizeAndCount, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": "randomize", "denoise": 11, "sampler_name": 2, "scheduler": 3.5, "seed": 1280, "steps": 1757820508}
---

# 平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2021474178897022977.json

> 来源文件 `comfyui_library/workflows/平台全量/Seedance 2.0视频高清化+首尾帧获取V1_2021474178897022977.json`

## 结构

**生成流程**：Sampling → Process → Output → Other

**节点**（18 个）：
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
- `SaveImage`
- `SaveImage`
- `ImageFromBatch+`
- `LoadVideo`
- `GetVideoComponents`
- `ImageFromBatch+`
- `GetVideoComponents`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `JWInteger`
- `JWInteger`
- `ImageConcanate`
- `FlashVSR_SM_KSampler` ★核心
- `CreateVideo`
- `SaveVideo`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `1280`
- `steps` = `1757820508`
- `cfg` = `randomize`
- `sampler_name` = `2`
- `scheduler` = `3.5`
- `denoise` = `11`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`FlashVSR_SM_Model`、`ImageFromBatch+`、`SaveImage`、`LoadVideo`、`GetVideoComponents`、`LayerUtility: ImageScaleByAspectRatio V2`、`JWInteger`、`ImageConcanate`、`FlashVSR_SM_KSampler`、`CreateVideo`、`SaveVideo`、`GetImageSizeAndCount`、`VHS_VideoCombine`

**用到的条目**：FlashVSR_SM_KSampler、GetImageSizeAndCount、SaveImage、SaveVideo、CreateVideo、FlashVSR_SM_Model、GetVideoComponents、ImageConcanate
