---
key: 图片生成/文生图/Z-Image-i2L (Image to LoRA)快速lora训练+联合CN测试_2023370355200495617.json
name: Z-Image-i2L (Image to LoRA)快速lora训练+联合CN测试_2023370355200495617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-i2L (Image to LoRA)快速lora训练+联合CN测试_2023370355200495617.json
hash: 745885940e32fc61
coverage: 0.930233
learned_at: 2026-10-19 22:30:00
nodes: [RandomNoise, DetailDaemonSamplerNode, LoraLoaderModelOnly, ModelPatchLoader, VAELoader, SamplerEulerAncestral, UNETLoader, SamplerCustomAdvanced, EmptyLatentImage, image_scale_pixel_v2, ZImageFunControlnet, AIO_Preprocessor, BasicScheduler, SamplerEulerAncestral, VAELoader, VAEDecode, RunningHub_ZImageI2L_Saver, easy cleanGpuUsed, RunningHub_ZImageI2L_Loader, PreviewAny, ImageBatchMulti, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ModelSamplingAuraFlow, CLIPLoader, CLIPTextEncode, LoraLoader, easy int, SplitSigmas, CFGGuider, LoadImage, PreviewImage, CLIPTextEncode, SamplerCustomAdvanced, RandomNoise, CFGGuider, RunningHub_ZImageI2L_LoraGenerator, SaveImage, PrimitiveStringMultiline]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 472, "lora_name": null, "strength_clip": 1.0000000000000002, "strength_model": 1.1000000000000003, "width": 512}
---

# 图片生成/文生图/Z-Image-i2L (Image to LoRA)快速lora训练+联合CN测试_2023370355200495617.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-i2L (Image to LoRA)快速lora训练+联合CN测试_2023370355200495617.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `RandomNoise`
- `DetailDaemonSamplerNode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchLoader`
- `VAELoader`
- `SamplerEulerAncestral` ★核心
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `image_scale_pixel_v2`
- `ZImageFunControlnet`
- `AIO_Preprocessor`
- `BasicScheduler`
- `SamplerEulerAncestral` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `RunningHub_ZImageI2L_Saver`
- `easy cleanGpuUsed`
- `RunningHub_ZImageI2L_Loader`
- `PreviewAny`
- `ImageBatchMulti`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `easy int`
- `SplitSigmas`
- `CFGGuider`
- `LoadImage`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `RunningHub_ZImageI2L_LoraGenerator`
- `SaveImage`
- `PrimitiveStringMultiline`

**识别到的模式**：lora

## 关键参数

- `width` = `512`
- `height` = `472`
- `batch_size` = `1`
- `lora_name` = `None`
- `strength_model` = `1.1000000000000003`
- `strength_clip` = `1.0000000000000002`

## 知识

覆盖率 **93%**（40/43）

**有卡**：`RandomNoise`、`DetailDaemonSamplerNode`、`LoraLoaderModelOnly`、`ModelPatchLoader`、`VAELoader`、`SamplerEulerAncestral`、`UNETLoader`、`SamplerCustomAdvanced`、`EmptyLatentImage`、`image_scale_pixel_v2`、`ZImageFunControlnet`、`AIO_Preprocessor`、`BasicScheduler`、`VAEDecode`、`RunningHub_ZImageI2L_Saver`、`easy cleanGpuUsed`、`RunningHub_ZImageI2L_Loader`、`ImageBatchMulti`、`LoadImage`、`ModelSamplingAuraFlow`、`CLIPLoader`、`CLIPTextEncode`、`LoraLoader`、`easy int`、`SplitSigmas`、`CFGGuider`、`RunningHub_ZImageI2L_LoraGenerator`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
