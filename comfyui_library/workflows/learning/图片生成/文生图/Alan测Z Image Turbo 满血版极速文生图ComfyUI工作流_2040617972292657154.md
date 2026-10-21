---
key: 图片生成/文生图/Alan测Z Image Turbo 满血版极速文生图ComfyUI工作流_2040617972292657154.json
name: Alan测Z Image Turbo 满血版极速文生图ComfyUI工作流_2040617972292657154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Alan测Z Image Turbo 满血版极速文生图ComfyUI工作流_2040617972292657154.json
hash: 7430e604ac803f8b
coverage: 0.928571
learned_at: 2026-10-21 02:51:18
nodes: [SamplerCustomAdvanced, KSamplerSelect, VAELoader, Anything Everywhere3, BasicScheduler, LatentPixelScale, RandomNoise, BasicGuider, KSamplerAdvanced, UpscaleModelLoader, Float, PrimitiveInt, VAEDecode, SaveImage, ConditioningZeroOut, CLIPTextEncode, LoraLoader, CLIPLoader, UNETLoader, VAEDecode, Int, Int, KSamplerAdvanced, CLIPTextEncode, EmptyLatentImage, Int, SaveImage, Text Multiline]
patterns: [lora]
missing: []
parameters: {"batch_size": 4, "cfg": 10, "denoise": "ddim_uniform", "height": 1280, "lora_name": null, "sampler_name": 1, "scheduler": "dpmpp_3m_sde", "seed": "enable", "steps": "randomize", "strength_clip": 1, "strength_model": 1, "width": 720}
---

# 图片生成/文生图/Alan测Z Image Turbo 满血版极速文生图ComfyUI工作流_2040617972292657154.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Alan测Z Image Turbo 满血版极速文生图ComfyUI工作流_2040617972292657154.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（28 个）：
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `VAELoader`
- `Anything Everywhere3`
- `BasicScheduler`
- `LatentPixelScale`
- `RandomNoise`
- `BasicGuider`
- `KSamplerAdvanced` ★核心
- `UpscaleModelLoader`
- `Float`
- `PrimitiveInt`
- `VAEDecode` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `Int`
- `Int`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `Int`
- `SaveImage`
- `Text Multiline`

**识别到的模式**：lora

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `dpmpp_3m_sde`
- `denoise` = `ddim_uniform`
- `lora_name` = `None`
- `strength_model` = `1`
- `strength_clip` = `1`
- `width` = `720`
- `height` = `1280`
- `batch_size` = `4`

## 知识

覆盖率 **93%**（26/28）

**有卡**：`SamplerCustomAdvanced`、`KSamplerSelect`、`VAELoader`、`BasicScheduler`、`LatentPixelScale`、`RandomNoise`、`BasicGuider`、`KSamplerAdvanced`、`UpscaleModelLoader`、`Float`、`VAEDecode`、`SaveImage`、`ConditioningZeroOut`、`CLIPTextEncode`、`LoraLoader`、`CLIPLoader`、`UNETLoader`、`Int`、`EmptyLatentImage`、`Text Multiline`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader、KSamplerAdvanced
