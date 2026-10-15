---
key: 视频生成/文生视频/B妮B妳_视频流_Wan2.2-AllinOne_N_S_F_W_(破审方法)_2007048031564210178.json
name: B妮B妳_视频流_Wan2.2-AllinOne_N_S_F_W_(破审方法)_2007048031564210178
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/B妮B妳_视频流_Wan2.2-AllinOne_N_S_F_W_(破审方法)_2007048031564210178.json
hash: 7b33bdb3cd4f6347
coverage: 0.872727
learned_at: 2026-10-15 22:44:05
nodes: [CLIPVisionLoader, WanVideoVAELoader, LayerUtility: PurgeVRAM, WanVideoDecode, CLIPTextEncode, Note, PreviewImage, KSampler, CLIPVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, CheckpointLoaderSimple, VHS_VideoCombine, PreviewBridge, CR Load Image List, VHS_VideoCombine, SaveLatent, Reroute, Mute / Bypass Repeater (rgthree), WanImageToVideo, Note, CLIPTextEncode, VHS_VideoCombine, LayerUtility: PurgeVRAM, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PreviewBridge, CLIPVisionLoader, CLIPVisionEncode, LoadImage, WanImageToVideo, EmptyLatentImage, LayerUtility: ImageScaleByAspectRatio V2, CheckpointLoaderSimple, LoadLatent, VHS_VideoCombine, CheckpointLoaderSimple, LoadLatent, VAEDecode, PreviewImage, VHS_VideoCombine, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Note, Note, LoadImage, CLIPTextEncode, CLIPTextEncode, ModelSamplingSD3, LayerUtility: PurgeVRAM, Mute / Bypass Repeater (rgthree), HAIGC_SaveImagesToZip, VAEDecode, VAEDecode, KSampler, Mute / Bypass Repeater (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "wan2.2-i2v-rapid-aio-v10-nsfw.safetensors", "denoise": 1, "height": 832, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 192054346835137, "steps": 4, "width": 480}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/B妮B妳_视频流_Wan2.2-AllinOne_N_S_F_W_(破审方法)_2007048031564210178.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/B妮B妳_视频流_Wan2.2-AllinOne_N_S_F_W_(破审方法)_2007048031564210178.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `CLIPTextEncode` ★核心
- `Note`
- `PreviewImage`
- `KSampler` ★核心
- `CLIPVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CheckpointLoaderSimple` ★核心
- `VHS_VideoCombine`
- `PreviewBridge`
- `CR Load Image List`
- `VHS_VideoCombine`
- `SaveLatent`
- `Reroute`
- `Mute / Bypass Repeater (rgthree)`
- `WanImageToVideo`
- `Note`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PreviewBridge`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `LoadImage`
- `WanImageToVideo`
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CheckpointLoaderSimple` ★核心
- `LoadLatent`
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `LoadLatent`
- `VAEDecode` ★核心
- `PreviewImage`
- `VHS_VideoCombine`
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `Note`
- `Note`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `LayerUtility: PurgeVRAM`
- `Mute / Bypass Repeater (rgthree)`
- `HAIGC_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Mute / Bypass Repeater (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `192054346835137`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-i2v-rapid-aio-v10-nsfw.safetensors`
- `width` = `480`
- `height` = `832`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（48/55）

**有卡**：`CLIPVisionLoader`、`WanVideoVAELoader`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`CLIPTextEncode`、`KSampler`、`CLIPVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CheckpointLoaderSimple`、`VHS_VideoCombine`、`PreviewBridge`、`CR Load Image List`、`SaveLatent`、`Mute / Bypass Repeater (rgthree)`、`WanImageToVideo`、`ModelSamplingSD3`、`LoadImage`、`EmptyLatentImage`、`LoadLatent`、`VAEDecode`、`HAIGC_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage、SaveLatent、CLIPVisionEncode

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
