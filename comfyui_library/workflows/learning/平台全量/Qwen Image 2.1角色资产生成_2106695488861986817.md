---
key: 平台全量/Qwen Image 2.1角色资产生成_2106695488861986817.json
name: Qwen Image 2.1角色资产生成_2106695488861986817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image 2.1角色资产生成_2106695488861986817.json
hash: 9b97d0732d60d1f9
coverage: 0.872093
learned_at: 2026-11-14 00:50:07
nodes: [SaveImageAdvanced, ResolutionSelector, SaveImageAdvanced, LoadImage, LoadImage, SaveImageAdvanced, ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, CLIPLoader, easy cleanGpuUsed, easy showAnything, TextEncodeQwenImage21, CR Prompt Text, UNETLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, easy cleanGpuUsed, LoadImage, ImageResizeKJv2, CLIPLoader, ResolutionSelector, easy showAnything, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, LoadImage, LoadImage, easy cleanGpuUsed, CLIPLoader, easy showAnything, 孤海注释, LoadImage, ImageResizeKJv2, UNETLoader, VAELoader, EmptyLatentImage, KSampler, QwenImage21Cache, VAEDecode, SaveImageAdvanced, PreviewImage, CLIPLoader, easy showAnything, TextEncodeQwenImage21, easy cleanGpuUsed, ImageStitch, TTResolutionSelector, CR Prompt Text, CLIPLoader, TTResolutionSelector, ImageResizeKJv2, TTResolutionSelector, MuyeTextEditOutput, TextGenerate, CR Prompt Text, MuyeTextEditOutput, PrimitiveStringMultiline, MuyeTextEditOutput, TextGenerate, TextGenerate, CR Prompt Text, MuyeTextEditOutput, TextGenerate, BatchImagesNode, Fast Groups Bypasser (rgthree), ResolutionSelector, CLIPLoader, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "res_2m", "scheduler": "beta", "seed": 712743632112443, "steps": 30, "width": 1024}
---

# 平台全量/Qwen Image 2.1角色资产生成_2106695488861986817.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image 2.1角色资产生成_2106695488861986817.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（86 个）：
- `SaveImageAdvanced`
- `ResolutionSelector`
- `SaveImageAdvanced`
- `LoadImage`
- `LoadImage`
- `SaveImageAdvanced`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `easy cleanGpuUsed`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `easy cleanGpuUsed`
- `LoadImage`
- `ImageResizeKJv2`
- `CLIPLoader`
- `ResolutionSelector`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `easy cleanGpuUsed`
- `CLIPLoader`
- `easy showAnything`
- `孤海注释`
- `LoadImage`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `PreviewImage`
- `CLIPLoader`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `easy cleanGpuUsed`
- `ImageStitch`
- `TTResolutionSelector`
- `CR Prompt Text`
- `CLIPLoader`
- `TTResolutionSelector`
- `ImageResizeKJv2`
- `TTResolutionSelector`
- `MuyeTextEditOutput`
- `TextGenerate`
- `CR Prompt Text`
- `MuyeTextEditOutput`
- `PrimitiveStringMultiline`
- `MuyeTextEditOutput`
- `TextGenerate`
- `TextGenerate`
- `CR Prompt Text`
- `MuyeTextEditOutput`
- `TextGenerate`
- `BatchImagesNode`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`
- `CLIPLoader`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `712743632112443`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `res_2m`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **87%**（75/86）

**有卡**：`SaveImageAdvanced`、`ResolutionSelector`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`easy cleanGpuUsed`、`TextEncodeQwenImage21`、`CR Prompt Text`、`ImageResizeKJv2`、`ImageStitch`、`TTResolutionSelector`、`MuyeTextEditOutput`、`TextGenerate`、`BatchImagesNode`、`SaveImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、SaveImage
