---
key: Qwen Image 2.1图像编辑加二次采样放大，去提示词增强精简版图生图方案_2103533493711106050.json
name: Qwen Image 2.1图像编辑加二次采样放大，去提示词增强精简版图生图方案_2103533493711106050
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图像编辑加二次采样放大，去提示词增强精简版图生图方案_2103533493711106050.json
hash: f0dd6cc8c536085d
coverage: 0.736842
learned_at: 2026-10-10 20:58:52
nodes: [GetNode, QwenImage21Cache, GetImageSizeAndCount, easy cleanGpuUsed, easy clearCacheAll, ComfyMathExpression, GetNode, GetNode, GetNode, TextEncodeQwenImage21, EmptyLatentImage, PathchSageAttentionKJ, QwenImage21Cache, KSampler, GetNode, GetNode, UNETLoader, CLIPLoader, VAELoader, GetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, KSampler, GetNode, ComfyMathExpression, TextEncodeQwenImage21, PathchSageAttentionKJ, SetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, EmptyLatentImage, VAEDecode, ResolutionSelector, Textbox, CLIPLoader, PreviewImage, VAEDecode, SaveImage, PrimitiveFloat, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [easy cleanGpuUsed, easy clearCacheAll]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen Image 2.1图像编辑加二次采样放大，去提示词增强精简版图生图方案_2103533493711106050.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图像编辑加二次采样放大，去提示词增强精简版图生图方案_2103533493711106050.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
- `GetNode`
- `QwenImage21Cache`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `GetNode`
- `ComfyMathExpression`
- `TextEncodeQwenImage21`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ResolutionSelector`
- `Textbox`
- `CLIPLoader`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PrimitiveFloat`
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

覆盖率 **74%**（56/76）

**有卡**：`QwenImage21Cache`、`GetImageSizeAndCount`、`ComfyMathExpression`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`PathchSageAttentionKJ`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`VAEDecode`、`ResolutionSelector`、`Textbox`、`SaveImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（2）：`easy cleanGpuUsed`、`easy clearCacheAll`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
