---
key: 平台全量/6图编辑QwenImage2.1_turbo专用工作流_高效改图方案_2117903041503522817.json
name: 6图编辑QwenImage2.1_turbo专用工作流_高效改图方案_2117903041503522817
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/6图编辑QwenImage2.1_turbo专用工作流_高效改图方案_2117903041503522817.json
hash: ac3c1ce19e557577
coverage: 0.92
learned_at: 2026-11-14 00:13:51
nodes: [VAELoader, TextEncodeQwenImage21, QwenImage21Cache, RandomNoise, KSamplerSelect, VAEDecode, SaveImage, BasicGuider, SamplerCustomAdvanced, ManualSigmas, ComfySwitchNode, UNETLoader, CLIPLoader, ResolutionSelector, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, PrimitiveBoolean, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, LoadImage, EmptyLatentImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 1024, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/6图编辑QwenImage2.1_turbo专用工作流_高效改图方案_2117903041503522817.json

> 来源文件 `comfyui_library/workflows/平台全量/6图编辑QwenImage2.1_turbo专用工作流_高效改图方案_2117903041503522817.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（50 个）：
- `VAELoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ResolutionSelector`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **92%**（46/50）

**有卡**：`VAELoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`RandomNoise`、`KSamplerSelect`、`VAEDecode`、`SaveImage`、`BasicGuider`、`SamplerCustomAdvanced`、`ManualSigmas`、`UNETLoader`、`CLIPLoader`、`ResolutionSelector`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`LoadImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
