---
key: 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-3图首尾帧_1982052292696391681.json
name: MEGA-v10-WAN2.2-AllInOne-3图首尾帧_1982052292696391681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-3图首尾帧_1982052292696391681.json
hash: 63718508126b67e1
coverage: 0.962963
learned_at: 2026-10-15 22:45:23
nodes: [ImageResizeKJ, ImageResizeKJ, INTConstant, INTConstant, ImageResizeKJ, GetImageRangeFromBatch, LoadImage, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, PrimitiveInt, VAEDecode, WanVideoVACEStartToEndFrame, GetImageSizeAndCount, WanVaceToVideo, ImageBatchMulti, MaskBatchMulti, LoadImage, String Literal, VHS_VideoCombine, WanVideoVACEStartToEndFrame, LoadImage, LoadImage, KSampler, CheckpointLoaderSimple, CLIPLoader, AV_VAELoader]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v11.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 6456545463455, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-3图首尾帧_1982052292696391681.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-3图首尾帧_1982052292696391681.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（27 个）：
- `ImageResizeKJ`
- `ImageResizeKJ`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJ`
- `GetImageRangeFromBatch`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PrimitiveInt`
- `VAEDecode` ★核心
- `WanVideoVACEStartToEndFrame`
- `GetImageSizeAndCount`
- `WanVaceToVideo`
- `ImageBatchMulti`
- `MaskBatchMulti`
- `LoadImage`
- `String Literal`
- `VHS_VideoCombine`
- `WanVideoVACEStartToEndFrame`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPLoader`
- `AV_VAELoader`

## 关键参数

- `seed` = `6456545463455`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v11.safetensors`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`ImageResizeKJ`、`INTConstant`、`GetImageRangeFromBatch`、`LoadImage`、`CLIPTextEncode`、`ModelSamplingSD3`、`VAEDecode`、`WanVideoVACEStartToEndFrame`、`GetImageSizeAndCount`、`WanVaceToVideo`、`ImageBatchMulti`、`MaskBatchMulti`、`String Literal`、`VHS_VideoCombine`、`KSampler`、`CheckpointLoaderSimple`、`CLIPLoader`、`AV_VAELoader`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、AV_VAELoader、GetImageSizeAndCount

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
