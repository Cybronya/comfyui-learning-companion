---
key: 视频生成/文生视频/Wan2.2Rapid-AIO-T2V&I2V合集_2002401911326273537.json
name: Wan2.2Rapid-AIO-T2V&I2V合集_2002401911326273537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2Rapid-AIO-T2V&I2V合集_2002401911326273537.json
hash: e86ab9187e7a8347
coverage: 0.782609
learned_at: 2026-10-15 22:47:13
nodes: [ModelSamplingSD3, CLIPTextEncode, RIFE VFI, VHS_VideoCombine, CLIPTextEncode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VHS_VideoCombine, ModelSamplingSD3, WanVideoVACEStartToEndFrame, VHS_VideoCombine, Fast Groups Bypasser (rgthree), KSampler, ImageResizeKJv2, KSampler, CLIPTextEncode, LoadImage, RIFE VFI, PrimitiveInt, WanVaceToVideo, WanVaceToVideo, easy showAnything, Qwen3_VQA, LoadImage, ImageResizeKJv2, PrimitiveInt, Note, VAEDecode, easy clearCacheAll, VAEDecode, INTConstant, INTConstant, INTConstant, INTConstant, easy clearCacheAll, CheckpointLoaderSimple, easy clearCacheAll, easy showAnything, MuyeTextEditOutput, CheckpointLoaderSimple, CLIPTextEncode, RH_LLMAPI_NODE, Text Multiline, VHS_VideoCombine]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-nsfw-v10.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 8848, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2Rapid-AIO-T2V&I2V合集_2002401911326273537.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2Rapid-AIO-T2V&I2V合集_2002401911326273537.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（46 个）：
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `RIFE VFI`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `WanVideoVACEStartToEndFrame`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
- `ImageResizeKJv2`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `RIFE VFI`
- `PrimitiveInt`
- `WanVaceToVideo`
- `WanVaceToVideo`
- `easy showAnything`
- `Qwen3_VQA`
- `LoadImage`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `Note`
- `VAEDecode` ★核心
- `easy clearCacheAll`
- `VAEDecode` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `easy clearCacheAll`
- `CheckpointLoaderSimple` ★核心
- `easy clearCacheAll`
- `easy showAnything`
- `MuyeTextEditOutput`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_NODE`
- `Text Multiline`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `8848`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-nsfw-v10.safetensors`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`ModelSamplingSD3`、`CLIPTextEncode`、`RIFE VFI`、`VHS_VideoCombine`、`WanVideoVACEStartToEndFrame`、`KSampler`、`ImageResizeKJv2`、`LoadImage`、`WanVaceToVideo`、`Qwen3_VQA`、`VAEDecode`、`easy clearCacheAll`、`INTConstant`、`CheckpointLoaderSimple`、`MuyeTextEditOutput`、`RH_LLMAPI_NODE`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ImageResizeKJv2、MuyeTextEditOutput、INTConstant

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
