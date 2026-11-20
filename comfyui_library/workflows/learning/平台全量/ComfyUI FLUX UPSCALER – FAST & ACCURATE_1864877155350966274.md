---
key: 平台全量/ComfyUI FLUX UPSCALER – FAST & ACCURATE_1864877155350966274.json
name: ComfyUI FLUX UPSCALER – FAST & ACCURATE_1864877155350966274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ComfyUI FLUX UPSCALER – FAST & ACCURATE_1864877155350966274.json
hash: c9cca499351196b1
coverage: 0.814815
learned_at: 2026-11-14 00:22:17
nodes: [UNETLoader, DualCLIPLoader, VAELoader, LoadImage, LoraLoader, Anything Everywhere, WD14Tagger|pysssss, Anything Everywhere, CLIPTextEncode, ControlNetLoader, CLIPTextEncode, ImageScaleToMegapixels, ControlNetApplySD3, GetImageSize, Anything Everywhere, FluxGuidance, ModelSamplingFlux, RandomNoise, BasicGuider, KSamplerSelect, BasicScheduler, VAEEncode, SamplerCustomAdvanced, VAEDecode, SaveImage, Image Comparer (rgthree), PreviewImage]
patterns: [lora]
missing: []
parameters: {"controlnet_strength": 1, "lora_name": "flux_realism_lora.safetensors", "strength_clip": 1, "strength_model": 0.9500000000000001}
---

# 平台全量/ComfyUI FLUX UPSCALER – FAST & ACCURATE_1864877155350966274.json

> 来源文件 `comfyui_library/workflows/平台全量/ComfyUI FLUX UPSCALER – FAST & ACCURATE_1864877155350966274.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoraLoader` ★核心
- `Anything Everywhere`
- `WD14Tagger|pysssss`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `ImageScaleToMegapixels`
- `ControlNetApplySD3` ★核心
- `GetImageSize`
- `Anything Everywhere`
- `FluxGuidance`
- `ModelSamplingFlux`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `flux_realism_lora.safetensors`
- `strength_model` = `0.9500000000000001`
- `strength_clip` = `1`
- `controlnet_strength` = `1`

## 知识

覆盖率 **81%**（22/27）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LoadImage`、`LoraLoader`、`WD14Tagger|pysssss`、`CLIPTextEncode`、`ControlNetLoader`、`ImageScaleToMegapixels`、`ControlNetApplySD3`、`GetImageSize`、`FluxGuidance`、`ModelSamplingFlux`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`VAEEncode`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplySD3、ControlNetLoader、FluxGuidance
