---
key: 视频生成/图生视频/wan2.2图生视频-扣子api调用_1964008268450418690.json
name: wan2.2图生视频-扣子api调用_1964008268450418690.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2图生视频-扣子api调用_1964008268450418690.json
hash: df7a3621fe124d19
coverage: 0.894737
learned_at: 2026-10-15 22:31:34
nodes: [WanImageToVideo, CLIPVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, ModelSamplingSD3, CheckpointLoaderSimple, PreviewImage, KSampler, CLIPTextEncode, CLIPVisionLoader, VHS_VideoCombine, VAEDecodeTiled, PrimitiveInt, RIFE VFI, UpscaleModelLoader, ImageUpscaleWithModel, LoadImage, RH_Translator, Textbox]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 814845875102001, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/wan2.2图生视频-扣子api调用_1964008268450418690.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1964008268450418690.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `WanImageToVideo`
- `CLIPVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `VHS_VideoCombine`
- `VAEDecodeTiled` ★核心
- `PrimitiveInt`
- `RIFE VFI`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `LoadImage`
- `RH_Translator`
- `Textbox`

## 关键参数

- `checkpoint` = `wan2.2-i2v-rapid-aio-v10.safetensors`
- `seed` = `814845875102001`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`WanImageToVideo`、`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`ModelSamplingSD3`、`CheckpointLoaderSimple`、`KSampler`、`CLIPVisionLoader`、`VHS_VideoCombine`、`VAEDecodeTiled`、`RIFE VFI`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`LoadImage`、`RH_Translator`、`Textbox`

**用到的条目**：KSampler、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEDecodeTiled、CLIPVisionEncode、ImageUpscaleWithModel、UpscaleModelLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
