---
key: 图片生成/图生图/FLUX+模特姿势动作控制（大牌运动模特）V1.13_1914983446777688066.json
name: FLUX+模特姿势动作控制（大牌运动模特）V1.13_1914983446777688066
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX+模特姿势动作控制（大牌运动模特）V1.13_1914983446777688066.json
hash: 73d9a93dda5840c1
coverage: 0.954545
learned_at: 2026-10-23 10:53:42
nodes: [DepthAnythingV2Preprocessor, ConditioningZeroOut, AIO_Preprocessor, ControlNetApplySD3, VAELoader, FluxGuidance, easy imageSize, DWPreprocessor, LoadImage, UNETLoader, LoraLoader, LoraLoader, DualCLIPLoader, VAEDecode, SaveImage, PreviewImage, ControlNetLoader, LP-TranslateToEN, ETN_Translate, CLIPTextEncode, KSampler, EmptyLatentImage]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "controlnet_strength": 0.8000000000000002, "denoise": 1, "height": 512, "lora_name": "人像_艺术摄影-1.0-FLUX_S1.0.safetensors", "sampler_name": "deis", "scheduler": "beta", "seed": 63923576527075, "steps": 20, "strength_clip": 1, "strength_model": 0.4, "width": 1024}
---

# 图片生成/图生图/FLUX+模特姿势动作控制（大牌运动模特）V1.13_1914983446777688066.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX+模特姿势动作控制（大牌运动模特）V1.13_1914983446777688066.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `DepthAnythingV2Preprocessor`
- `ConditioningZeroOut`
- `AIO_Preprocessor`
- `ControlNetApplySD3` ★核心
- `VAELoader`
- `FluxGuidance`
- `easy imageSize`
- `DWPreprocessor`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `ControlNetLoader`
- `LP-TranslateToEN`
- `ETN_Translate`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image、lora

## 关键参数

- `controlnet_strength` = `0.8000000000000002`
- `lora_name` = `人像_艺术摄影-1.0-FLUX_S1.0.safetensors`
- `strength_model` = `0.4`
- `strength_clip` = `1`
- `seed` = `63923576527075`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1024`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`DepthAnythingV2Preprocessor`、`ConditioningZeroOut`、`AIO_Preprocessor`、`ControlNetApplySD3`、`VAELoader`、`FluxGuidance`、`easy imageSize`、`DWPreprocessor`、`LoadImage`、`UNETLoader`、`LoraLoader`、`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`ControlNetLoader`、`LP-TranslateToEN`、`ETN_Translate`、`CLIPTextEncode`、`KSampler`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
