---
key: 图片生成/图生图/图生图AIGC Image 2.5九图工作流，高质量图像到图像处理方案_2107238746419716097.json
name: 图生图AIGC Image 2.5九图工作流，高质量图像到图像处理方案_2107238746419716097
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图生图AIGC Image 2.5九图工作流，高质量图像到图像处理方案_2107238746419716097.json
hash: 166b9be8e3dabdca
coverage: 0.825
learned_at: 2026-10-06 21:43:53
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Prompt Text, RH_RhartImageG25SunburstImageToImage, SaveImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [RH_RhartImageG25SunburstImageToImage, CR Prompt Text, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `RH_RhartImageG25SunburstImageToImage` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/图生图AIGC Image 2.5九图工作流，高质量图像到图像处理方案_2107238746419716097.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图生图AIGC Image 2.5九图工作流，高质量图像到图像处理方案_2107238746419716097.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（40 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `RH_RhartImageG25SunburstImageToImage`
- `SaveImage`
- `LoadImage`
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

覆盖率 **82%**（33/40）

**有卡**：`LoadImage`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`VAELoader`

**缺卡**（3）：`RH_RhartImageG25SunburstImageToImage`、`CR Prompt Text`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `RH_RhartImageG25SunburstImageToImage` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
