---
key: 图片生成/图生图/Qwen image 2.1多参考生图 短剧分镜8步加速处理工具_2113027948751183873.json
name: Qwen image 2.1多参考生图 短剧分镜8步加速处理工具_2113027948751183873
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1多参考生图 短剧分镜8步加速处理工具_2113027948751183873.json
hash: 8a7ced56413585e7
coverage: 0.918367
learned_at: 2026-10-26 22:03:14
nodes: [RandomNoise, QwenImage21Cache, CLIPLoader, EmptyLatentImage, CFGGuider, KSamplerSelect, BasicScheduler, ExtendIntermediateSigmas, UNETLoader, VAEDecode, SamplerCustomAdvanced, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, LoadImage, LoraLoaderModelOnly, LoadImage, TextEncodeQwenImage21, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1多参考生图 短剧分镜8步加速处理工具_2113027948751183873.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1多参考生图 短剧分镜8步加速处理工具_2113027948751183873.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（49 个）：
- `RandomNoise`
- `QwenImage21Cache`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ExtendIntermediateSigmas`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `TextEncodeQwenImage21`
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **92%**（45/49）

**有卡**：`RandomNoise`、`QwenImage21Cache`、`CLIPLoader`、`EmptyLatentImage`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`ExtendIntermediateSigmas`、`UNETLoader`、`VAEDecode`、`SamplerCustomAdvanced`、`SaveImage`、`LoraLoaderModelOnly`、`VAELoader`、`LoadImage`、`TextEncodeQwenImage21`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
