---
key: 数字人/数字人/Wan2.2_S2V_音频加图像生成视频_接力_2062002837080592385.json
name: Wan2.2_S2V_音频加图像生成视频_接力_2062002837080592385
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2_S2V_音频加图像生成视频_接力_2062002837080592385.json
hash: c366766643aab09f
coverage: 0.712121
learned_at: 2026-10-26 01:57:58
nodes: [UNETLoader, CLIPLoader, VAELoader, AudioEncoderLoader, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, PrimitiveInt, SimpleMath+, AudioEncoderEncode, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, WanSoundImageToVideo, WanSoundImageToVideoExtend, PrimitiveFloat, KSamplerSelect, BasicScheduler, CFGGuider, RandomNoise, SamplerCustomAdvanced, VAEDecode, PrimitiveFloat, CreateVideo, SaveVideo, ImageFromBatch, SaveImage, CheckpointLoaderSimple, ImageScale, CLIPTextEncode, CLIPTextEncode, PrimitiveFloat, PrimitiveInt, VAEEncode, KSampler, VAEDecode, UpscaleModelLoader, ImageUpscaleWithModel, ImageScale, SaveImage, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, SimpleMath+, SimpleMath+, easy showAnything, easy showAnything, GetImageSizeAndCount, SimpleMath+, easy showAnything, easy cleanGpuUsed, easy cleanGpuUsed, PrimitiveInt, SimpleMath+, ImageFromBatch, SimpleMath+, SimpleMath+, ImageScale, LoadImage, VHS_LoadAudioUpload, Note, SimpleMath+]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 5.5, "checkpoint": "sd_xl_base_1.0.safetensors", "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 0, "steps": 25}
---

# 数字人/数字人/Wan2.2_S2V_音频加图像生成视频_接力_2062002837080592385.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2_S2V_音频加图像生成视频_接力_2062002837080592385.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `AudioEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `SimpleMath+`
- `AudioEncoderEncode`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `WanSoundImageToVideo`
- `WanSoundImageToVideoExtend`
- `PrimitiveFloat`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `PrimitiveFloat`
- `CreateVideo`
- `SaveVideo`
- `ImageFromBatch`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `ImageScale`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `PrimitiveInt`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScale`
- `SaveImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `SimpleMath+`
- `SimpleMath+`
- `easy showAnything`
- `easy showAnything`
- `GetImageSizeAndCount`
- `SimpleMath+`
- `easy showAnything`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `PrimitiveInt`
- `SimpleMath+`
- `ImageFromBatch`
- `SimpleMath+`
- `SimpleMath+`
- `ImageScale`
- `LoadImage`
- `VHS_LoadAudioUpload`
- `Note`
- `SimpleMath+`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `sd_xl_base_1.0.safetensors`
- `seed` = `0`
- `steps` = `25`
- `cfg` = `5.5`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **71%**（47/66）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`AudioEncoderLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPTextEncode`、`SimpleMath+`、`AudioEncoderEncode`、`WanSoundImageToVideo`、`WanSoundImageToVideoExtend`、`KSamplerSelect`、`BasicScheduler`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`ImageFromBatch`、`SaveImage`、`CheckpointLoaderSimple`、`ImageScale`、`VAEEncode`、`KSampler`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`LoadImage`、`VHS_LoadAudioUpload`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader
