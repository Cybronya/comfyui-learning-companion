---
key: 图片生成/文生图/Qwen Image 2.1图像编辑加二次采样放大，去提示词增强精简版图生图方案_2103533493711106050.json
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

# 图片生成/文生图/Qwen Image 2.1图像编辑加二次采样放大，去提示词增强精简版图生图方案_2103533493711106050.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1图像编辑加二次采样放大，去提示词增强精简版图生图方案_2103533493711106050.json`

## 结构

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
- `EmptyLatentImage`
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `KSampler`
- `GetNode`
- `GetNode`
- `UNETLoader`
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
- `KSampler`
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
- `EmptyLatentImage`
- `VAEDecode`
- `ResolutionSelector`
- `Textbox`
- `CLIPLoader`
- `PreviewImage`
- `VAEDecode`
- `SaveImage`
- `PrimitiveFloat`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **74%**（56/76）

**有卡**：`GetNode`、`QwenImage21Cache`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`easy clearCacheAll`、`ComfyMathExpression`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`PathchSageAttentionKJ`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`SetNode`、`VAEDecode`、`ResolutionSelector`、`Textbox`、`PreviewImage`、`SaveImage`、`PrimitiveFloat`、`孤海注释`、`LoraLoaderModelOnly`

**缺卡**（2）：`easy cleanGpuUsed`、`easy clearCacheAll`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
