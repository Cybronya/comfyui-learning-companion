---
key: 图片生成/图生图/Qwen Image 2.1纠正背景透视溶图工作流，图生图背景融合处理工具_2107200687548493825.json
name: Qwen Image 2.1纠正背景透视溶图工作流，图生图背景融合处理工具_2107200687548493825
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1纠正背景透视溶图工作流，图生图背景融合处理工具_2107200687548493825.json
hash: 21e407c6cb338b87
coverage: 0.795918
learned_at: 2026-10-07 02:41:26
nodes: [CLIPLoader, VAELoader, UNETLoader, TextEncodeQwenImage21, KSamplerAdvanced, KSamplerAdvanced, VAEDecode, Image Comparer (rgthree), LoadImage, 图像缩放V2_孤海, UC_ImagePad, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Prompt Text, FluxGuidance, InvertMask (segment anything), MaskToImage, Cut By Mask, SaveImageAdvanced, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [Cut By Mask, InvertMask (segment anything), UC_ImagePad, 图像缩放V2_孤海, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Cut By Mask` 知识库中没有该节点类型的任何知识, 次要节点 `InvertMask (segment anything)` 知识库中没有该节点类型的任何知识, 次要节点 `UC_ImagePad` 知识库中没有该节点类型的任何知识, 次要节点 `图像缩放V2_孤海` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1纠正背景透视溶图工作流，图生图背景融合处理工具_2107200687548493825.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1纠正背景透视溶图工作流，图生图背景融合处理工具_2107200687548493825.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（49 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `图像缩放V2_孤海`
- `UC_ImagePad`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `FluxGuidance`
- `InvertMask (segment anything)`
- `MaskToImage`
- `Cut By Mask`
- `SaveImageAdvanced`
- `SaveImage`
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

覆盖率 **80%**（39/49）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`TextEncodeQwenImage21`、`KSamplerAdvanced`、`VAEDecode`、`LoadImage`、`LoraLoaderModelOnly`、`FluxGuidance`、`MaskToImage`、`SaveImageAdvanced`、`SaveImage`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（5）：`Cut By Mask`、`InvertMask (segment anything)`、`UC_ImagePad`、`图像缩放V2_孤海`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Cut By Mask` 知识库中没有该节点类型的任何知识
- 次要节点 `InvertMask (segment anything)` 知识库中没有该节点类型的任何知识
- 次要节点 `UC_ImagePad` 知识库中没有该节点类型的任何知识
- 次要节点 `图像缩放V2_孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
