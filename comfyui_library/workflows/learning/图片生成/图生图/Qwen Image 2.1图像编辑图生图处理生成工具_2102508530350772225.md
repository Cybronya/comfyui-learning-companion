---
key: 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102508530350772225.json
name: Qwen Image 2.1图像编辑图生图处理生成工具_2102508530350772225
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102508530350772225.json
hash: 19828c9645b77c31
coverage: 0.836735
learned_at: 2026-10-10 20:48:06
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, VAEDecode, KSampler, Reroute, EmptyLatentImage, easy ifElse, LoadImage, LoadImage, 图像缩放V2_孤海, LoadImage, UNETLoader, TextEncodeQwenImage21, DF_Text_Box, 布尔孤海, GoohaiUniversalSlider, GH_ImageVideoComparer, SaveImage, ResolutionSelector, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [图像缩放V2_孤海, 布尔孤海]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `图像缩放V2_孤海` 知识库中没有该节点类型的任何知识, 次要节点 `布尔孤海` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102508530350772225.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图像编辑图生图处理生成工具_2102508530350772225.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（49 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Reroute`
- `EmptyLatentImage` ★核心
- `easy ifElse`
- `LoadImage`
- `LoadImage`
- `图像缩放V2_孤海`
- `LoadImage`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `DF_Text_Box`
- `布尔孤海`
- `GoohaiUniversalSlider`
- `GH_ImageVideoComparer`
- `SaveImage`
- `ResolutionSelector`
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

覆盖率 **84%**（41/49）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`VAEDecode`、`KSampler`、`EmptyLatentImage`、`LoadImage`、`UNETLoader`、`TextEncodeQwenImage21`、`DF_Text_Box`、`GoohaiUniversalSlider`、`GH_ImageVideoComparer`、`SaveImage`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（2）：`图像缩放V2_孤海`、`布尔孤海`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `图像缩放V2_孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `布尔孤海` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
