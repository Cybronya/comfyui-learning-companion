---
key: 图片生成/图生图/Qwen Image 2.1 turbo光影迁移 图生图处理生成工具_2113004334173741057.json
name: Qwen Image 2.1 turbo光影迁移 图生图处理生成工具_2113004334173741057
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 turbo光影迁移 图生图处理生成工具_2113004334173741057.json
hash: 1d32dfbf0fc1dc6a
coverage: 0.869565
learned_at: 2026-10-26 22:02:57
nodes: [ResolutionSelector, EmptyLatentImage, ComfySwitchNode, CLIPLoader, VAELoader, SaveImage, SamplerCustom, KSamplerSelect, ManualSigmas, UNETLoader, PrimitiveBoolean, TextEncodeQwenImage21, LoraLoaderModelOnly, VAEDecode, LoadImage, LoadImage, Image Comparer (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 turbo光影迁移 图生图处理生成工具_2113004334173741057.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 turbo光影迁移 图生图处理生成工具_2113004334173741057.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（46 个）：
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `UNETLoader` ★核心
- `PrimitiveBoolean`
- `TextEncodeQwenImage21`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
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

覆盖率 **87%**（40/46）

**有卡**：`ResolutionSelector`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`SaveImage`、`SamplerCustom`、`KSamplerSelect`、`ManualSigmas`、`UNETLoader`、`PrimitiveBoolean`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`VAEDecode`、`LoadImage`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
