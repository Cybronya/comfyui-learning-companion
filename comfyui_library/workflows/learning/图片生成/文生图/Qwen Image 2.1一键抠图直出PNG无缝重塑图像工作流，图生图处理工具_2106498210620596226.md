---
key: 图片生成/文生图/Qwen Image 2.1一键抠图直出PNG无缝重塑图像工作流，图生图处理工具_2106498210620596226.json
name: Qwen Image 2.1一键抠图直出PNG无缝重塑图像工作流，图生图处理工具_2106498210620596226
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1一键抠图直出PNG无缝重塑图像工作流，图生图处理工具_2106498210620596226.json
hash: 742ae8f3a77629ca
coverage: 0.846154
learned_at: 2026-10-06 21:48:04
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, VAEDecode, SaveImage, SaveImageAdvanced, KSampler, UNETLoader, LoadImage, TextEncodeQwenImage21, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [SaveImageAdvanced, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1一键抠图直出PNG无缝重塑图像工作流，图生图处理工具_2106498210620596226.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1一键抠图直出PNG无缝重塑图像工作流，图生图处理工具_2106498210620596226.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（39 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `UNETLoader` ★核心
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

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（33/39）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`VAEDecode`、`SaveImage`、`KSampler`、`UNETLoader`、`LoadImage`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`CLIPTextEncode`

**缺卡**（2）：`SaveImageAdvanced`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
