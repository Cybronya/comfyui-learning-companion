---
key: 图片生成/图生图/Qwen Image 2.1多合一文生图图生图处理工具_2102471938563207170.json
name: Qwen Image 2.1多合一文生图图生图处理工具_2102471938563207170
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多合一文生图图生图处理工具_2102471938563207170.json
hash: ecc78a1df1a14ff4
coverage: 0.684783
learned_at: 2026-10-10 20:48:06
nodes: [ResolutionSelector, LoadImage, ResolutionSelector, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SeedVR2VideoUpscaler, LoadImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SaveImage, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, TextInput_, EmptyLatentImage, QwenImage21Cache, TextEncodeQwenImage21, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, TextGenerateLTX2Prompt, SetNode, SetNode, GetNode, GetNode, TextGenerateLTX2Prompt, easy seed, LoraLoaderModelOnly, UNETLoader, CLIPLoader, CLIPLoader, Anything Everywhere3, easy showAnything, LoadImage, TextInput_, KSampler, SaveImage, SaveImageAdvanced, VAEDecode, SaveImageAdvanced, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [easy seed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1多合一文生图图生图处理工具_2102471938563207170.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1多合一文生图图生图处理工具_2102471938563207170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（92 个）：
- `ResolutionSelector`
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SeedVR2VideoUpscaler`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SaveImage`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TextInput_`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `TextGenerateLTX2Prompt`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `easy seed`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `Anything Everywhere3`
- `easy showAnything`
- `LoadImage`
- `TextInput_`
- `KSampler` ★核心
- `SaveImage`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `孤海注释`
- `孤海注释`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **68%**（63/92）

**有卡**：`ResolutionSelector`、`LoadImage`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SaveImage`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`TextInput_`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`LoraLoaderModelOnly`、`UNETLoader`、`SaveImageAdvanced`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（1）：`easy seed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
