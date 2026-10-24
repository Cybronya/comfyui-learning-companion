---
key: 图片生成/图生图/【Supermate】Hunyuan_video_1.5AIO_V1扩图洗图工作流_1993499865617465346.json
name: 【Supermate】Hunyuan_video_1.5AIO_V1扩图洗图工作流_1993499865617465346
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【Supermate】Hunyuan_video_1.5AIO_V1扩图洗图工作流_1993499865617465346.json
hash: d3bfa6efac68e6cc
coverage: 0.944444
learned_at: 2026-10-23 11:49:02
nodes: [Label (rgthree), Image Comparer (rgthree), SaveImage, ImageStitch, ImageScaleToTotalPixels, ImagePadForOutpaint, VAEEncode, ConditioningZeroOut, CFGNorm, ModelSamplingAuraFlow, VAEDecode, SaveImage, KSampler, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, CheckpointLoaderSimple]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "checkpoint": "HV15-Rapid-AIO-v1.safetensors", "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta", "seed": 64555507052260, "steps": 10}
---

# 图片生成/图生图/【Supermate】Hunyuan_video_1.5AIO_V1扩图洗图工作流_1993499865617465346.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【Supermate】Hunyuan_video_1.5AIO_V1扩图洗图工作流_1993499865617465346.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `Label (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `ImageStitch`
- `ImageScaleToTotalPixels`
- `ImagePadForOutpaint`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `64555507052260`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `HV15-Rapid-AIO-v1.safetensors`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`Label (rgthree)`、`SaveImage`、`ImageStitch`、`ImageScaleToTotalPixels`、`ImagePadForOutpaint`、`VAEEncode`、`ConditioningZeroOut`、`CFGNorm`、`ModelSamplingAuraFlow`、`VAEDecode`、`KSampler`、`TextEncodeQwenImageEditPlus`、`LoraLoaderModelOnly`、`LoadImage`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、ConditioningZeroOut、LoadImage、CFGNorm、TextEncodeQwenImageEditPlus
