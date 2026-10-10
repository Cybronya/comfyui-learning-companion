---
key: 图片生成/图生图/Qwen_Image_2.1图像编辑｜图生图实操经验版｜稳定可靠_2102313763641847810.json
name: Qwen_Image_2.1图像编辑｜图生图实操经验版｜稳定可靠_2102313763641847810
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1图像编辑｜图生图实操经验版｜稳定可靠_2102313763641847810.json
hash: 457637b1de16cdd1
coverage: 0.901639
learned_at: 2026-10-10 20:48:10
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, VAEDecode, KSampler, Reroute, EmptyLatentImage, easy ifElse, LoadImage, LoadImage, 图像缩放V2_孤海, LoadImage, UNETLoader, TextEncodeQwenImage21, DF_Text_Box, 布尔孤海, GoohaiUniversalSlider, SaveImage, ResolutionSelector, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note, GH_ImageVideoComparer]
patterns: [text_to_image]
missing: [图像缩放V2_孤海, 布尔孤海]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `图像缩放V2_孤海` 知识库中没有该节点类型的任何知识, 次要节点 `布尔孤海` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_Image_2.1图像编辑｜图生图实操经验版｜稳定可靠_2102313763641847810.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1图像编辑｜图生图实操经验版｜稳定可靠_2102313763641847810.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（61 个）：
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
- `SaveImage`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`
- `GH_ImageVideoComparer`

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

覆盖率 **90%**（55/61）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`VAEDecode`、`KSampler`、`EmptyLatentImage`、`LoadImage`、`UNETLoader`、`TextEncodeQwenImage21`、`DF_Text_Box`、`GoohaiUniversalSlider`、`SaveImage`、`ResolutionSelector`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`、`GH_ImageVideoComparer`

**缺卡**（2）：`图像缩放V2_孤海`、`布尔孤海`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `图像缩放V2_孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `布尔孤海` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
