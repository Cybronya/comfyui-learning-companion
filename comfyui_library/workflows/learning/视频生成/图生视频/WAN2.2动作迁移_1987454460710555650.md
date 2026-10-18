---
key: 视频生成/图生视频/WAN2.2动作迁移_1987454460710555650.json
name: WAN2.2动作迁移_1987454460710555650.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2动作迁移_1987454460710555650.json
hash: e8994fbc999a325d
coverage: 0.951613
learned_at: 2026-10-15 22:32:58
nodes: [SaveVideoRGBA, easy int, easy int, GetImageSize, TorchCompileModelWanVideoV2, PathchSageAttentionKJ, easy int, easy ifElse, ModelSamplingSD3, easy ifElse, easy positive, CLIPVisionEncode, SimpleMath+, easy compare, easy lengthAnything, easy batchAnything, SimpleMath+, easy promptReplace, VAEDecode, TrimVideoLatent, easy int, OnnxDetectionModelLoader, easy whileLoopStart, easy int, WanAnimateToVideo, SimpleMath+, easy convertAnything, SimpleMath+, SimpleMathDual+, VHS_VideoInfo, easy compare, easy whileLoopEnd, ModelPatchTorchSettings, Any Switch (rgthree), easy int, easy int, PoseAndFaceDetection, DrawViTPose, ImageResizeKJv2, wanBlockSwap, ImageResizeKJv2, RHHiddenNodes, CLIPLoader, LoraLoaderModelOnly, SimpleMath+, easy int, GetImageRangeFromBatch, KSampler, ImageConcatMulti, CLIPTextEncode, CLIPTextEncode, VHS_LoadVideo, easy int, LoadImage, VHS_VideoCombine, easy boolean, easy int, SimpleMath+, SaveVideoRGBA, SaveVideoRGBA, ImageConcatMulti, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "linear_quadratic", "seed": 57924536850887, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/WAN2.2动作迁移_1987454460710555650.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1987454460710555650.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `SaveVideoRGBA`
- `easy int`
- `easy int`
- `GetImageSize`
- `TorchCompileModelWanVideoV2`
- `PathchSageAttentionKJ`
- `easy int`
- `easy ifElse`
- `ModelSamplingSD3`
- `easy ifElse`
- `easy positive`
- `CLIPVisionEncode`
- `SimpleMath+`
- `easy compare`
- `easy lengthAnything`
- `easy batchAnything`
- `SimpleMath+`
- `easy promptReplace`
- `VAEDecode` ★核心
- `TrimVideoLatent`
- `easy int`
- `OnnxDetectionModelLoader`
- `easy whileLoopStart`
- `easy int`
- `WanAnimateToVideo`
- `SimpleMath+`
- `easy convertAnything`
- `SimpleMath+`
- `SimpleMathDual+`
- `VHS_VideoInfo`
- `easy compare`
- `easy whileLoopEnd`
- `ModelPatchTorchSettings`
- `Any Switch (rgthree)`
- `easy int`
- `easy int`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `ImageResizeKJv2`
- `wanBlockSwap`
- `ImageResizeKJv2`
- `RHHiddenNodes`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SimpleMath+`
- `easy int`
- `GetImageRangeFromBatch`
- `KSampler` ★核心
- `ImageConcatMulti`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VHS_LoadVideo`
- `easy int`
- `LoadImage`
- `VHS_VideoCombine`
- `easy boolean`
- `easy int`
- `SimpleMath+`
- `SaveVideoRGBA`
- `SaveVideoRGBA`
- `ImageConcatMulti`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `57924536850887`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `linear_quadratic`
- `denoise` = `1`

## 知识

覆盖率 **95%**（59/62）

**有卡**：`SaveVideoRGBA`、`easy int`、`GetImageSize`、`TorchCompileModelWanVideoV2`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`easy positive`、`CLIPVisionEncode`、`SimpleMath+`、`easy compare`、`easy lengthAnything`、`easy batchAnything`、`easy promptReplace`、`VAEDecode`、`TrimVideoLatent`、`OnnxDetectionModelLoader`、`easy whileLoopStart`、`WanAnimateToVideo`、`easy convertAnything`、`SimpleMathDual+`、`VHS_VideoInfo`、`easy whileLoopEnd`、`ModelPatchTorchSettings`、`PoseAndFaceDetection`、`DrawViTPose`、`ImageResizeKJv2`、`wanBlockSwap`、`RHHiddenNodes`、`CLIPLoader`、`LoraLoaderModelOnly`、`GetImageRangeFromBatch`、`KSampler`、`ImageConcatMulti`、`CLIPTextEncode`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoCombine`、`easy boolean`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode、TrimVideoLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
