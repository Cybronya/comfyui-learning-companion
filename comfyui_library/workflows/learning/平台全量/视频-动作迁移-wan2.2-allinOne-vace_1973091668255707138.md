---
key: 平台全量/视频-动作迁移-wan2.2-allinOne-vace_1973091668255707138.json
name: 视频-动作迁移-wan2.2-allinOne-vace_1973091668255707138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-动作迁移-wan2.2-allinOne-vace_1973091668255707138.json
hash: 580e4489a76bc78a
coverage: 0.641304
learned_at: 2026-11-14 02:34:08
nodes: [PreviewImage, PreviewImage, ImageFromBatch+, VHS_VideoInfoLoaded, SetNode, Reroute, VHS_VideoCombine, ImageConcanate, GetImageSizeAndCount, easy showAnything, GetImageSizeAndCount, SetNode, Reroute, GetImageSizeAndCount, SetNode, Florence2Run, GetNode, easy showAnything, GetNode, GetImageSizeAndCount, PreviewImage, GetNode, ShowText|pysssss, PreviewImage, SetNode, GetImageSizeAndCount, SetNode, CLIPTextEncode, CLIPTextEncode, PathchSageAttentionKJ, ModelSamplingSD3, TrimVideoLatent, WanVaceToVideo, GetNode, GetImageSizeAndCount, GetNode, GetImageSizeAndCount, GetNode, WanVideoVACEStartToEndFrame, VHS_VideoCombine, GetNode, GetImageSizeAndCount, INTConstant, GetImageSizeAndCount, ImageFromBatch, PreviewImage, VAEDecodeTiled, ImageFromBatch+, VHS_VideoCombine, PreviewImage, GetNode, GetNode, GetImageSizeAndCount, easy seed, GetImageSizeAndCount, StringFunction|pysssss, ImageFromBatch+, GetImageSizeAndCount, KSampler, LayerUtility: ImageScaleByAspectRatio V2, easy anythingIndexSwitch, PreviewImage, SetNode, ImageResizeKJ, GetNode, ImageFromBatch, ImageResizeKJ, SetNode, GetNode, ImageFromBatch, Florence2ModelLoader, SetNode, ImageResizeKJ, VHS_VideoCombine, CR Upscale Image, GetImageSizeAndCount, SetNode, easy int, easy positive, CM_IntToFloat, LoadImage, ImageFromBatch, easy int, GetImageSizeAndCount, AIO_Preprocessor, CheckpointLoaderSimple, VHS_LoadVideo, INTConstant, GetImageSizeAndCount, GetImageSizeAndCount, SetNode, easy int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v4.safetensors", "denoise": 1, "sampler_name": "ipndm", "scheduler": "sgm_uniform", "seed": 7567358653673, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/视频-动作迁移-wan2.2-allinOne-vace_1973091668255707138.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-动作迁移-wan2.2-allinOne-vace_1973091668255707138.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `PreviewImage`
- `PreviewImage`
- `ImageFromBatch+`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `Reroute`
- `VHS_VideoCombine`
- `ImageConcanate`
- `GetImageSizeAndCount`
- `easy showAnything`
- `GetImageSizeAndCount`
- `SetNode`
- `Reroute`
- `GetImageSizeAndCount`
- `SetNode`
- `Florence2Run`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `GetNode`
- `ShowText|pysssss`
- `PreviewImage`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `WanVaceToVideo`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoVACEStartToEndFrame`
- `VHS_VideoCombine`
- `GetNode`
- `GetImageSizeAndCount`
- `INTConstant`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `PreviewImage`
- `VAEDecodeTiled` ★核心
- `ImageFromBatch+`
- `VHS_VideoCombine`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `easy seed`
- `GetImageSizeAndCount`
- `StringFunction|pysssss`
- `ImageFromBatch+`
- `GetImageSizeAndCount`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy anythingIndexSwitch`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJ`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJ`
- `SetNode`
- `GetNode`
- `ImageFromBatch`
- `Florence2ModelLoader`
- `SetNode`
- `ImageResizeKJ`
- `VHS_VideoCombine`
- `CR Upscale Image`
- `GetImageSizeAndCount`
- `SetNode`
- `easy int`
- `easy positive`
- `CM_IntToFloat`
- `LoadImage`
- `ImageFromBatch`
- `easy int`
- `GetImageSizeAndCount`
- `AIO_Preprocessor`
- `CheckpointLoaderSimple` ★核心
- `VHS_LoadVideo`
- `INTConstant`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `SetNode`
- `easy int`

## 关键参数

- `seed` = `7567358653673`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `ipndm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v4.safetensors`

## 知识

覆盖率 **64%**（59/92）

**有卡**：`ImageFromBatch+`、`VHS_VideoInfoLoaded`、`VHS_VideoCombine`、`ImageConcanate`、`GetImageSizeAndCount`、`Florence2Run`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`TrimVideoLatent`、`WanVaceToVideo`、`WanVideoVACEStartToEndFrame`、`INTConstant`、`ImageFromBatch`、`VAEDecodeTiled`、`easy seed`、`StringFunction|pysssss`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy anythingIndexSwitch`、`ImageResizeKJ`、`Florence2ModelLoader`、`CR Upscale Image`、`easy int`、`easy positive`、`CM_IntToFloat`、`LoadImage`、`AIO_Preprocessor`、`CheckpointLoaderSimple`、`VHS_LoadVideo`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、easy seed、TrimVideoLatent、VAEDecodeTiled

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
