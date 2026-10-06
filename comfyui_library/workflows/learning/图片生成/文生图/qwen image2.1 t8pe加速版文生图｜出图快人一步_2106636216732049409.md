---
key: 图片生成/文生图/qwen image2.1 t8pe加速版文生图｜出图快人一步_2106636216732049409.json
name: qwen image2.1 t8pe加速版文生图｜出图快人一步_2106636216732049409
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image2.1 t8pe加速版文生图｜出图快人一步_2106636216732049409.json
hash: 1cc13b9c77a77338
coverage: 0.731343
learned_at: 2026-10-06 21:49:36
nodes: [QwenImage21Cache, CLIPLoader, EmptyLatentImage, ComfySwitchNode, VAELoader, KSampler, easy cleanGpuUsed, VAEDecode, ResolutionSelector, UNETLoader, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageScaleToTotalPixels, PreviewImage, Image Comparer (rgthree), INTConstant, SaveImage, SeedVR2LoadDiTModel, SaveImage, Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, easy showAnything, QwenPERewriteT8, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [Fast Groups Bypasser (rgthree), INTConstant, ImageScaleToTotalPixels, QwenPERewriteT8, easy cleanGpuUsed, CR Prompt Text, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `INTConstant` 知识库中没有该节点类型的任何知识, 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识, 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明, 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen image2.1 t8pe加速版文生图｜出图快人一步_2106636216732049409.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image2.1 t8pe加速版文生图｜出图快人一步_2106636216732049409.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `QwenImage21Cache`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAELoader`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `INTConstant`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `QwenPERewriteT8`
- `CR Prompt Text`
- `孤海注释`
- `孤海注释`
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

覆盖率 **73%**（49/67）

**有卡**：`QwenImage21Cache`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`KSampler`、`VAEDecode`、`ResolutionSelector`、`UNETLoader`、`SaveImage`、`TextEncodeQwenImage21`、`CLIPTextEncode`、`LoraLoaderModelOnly`

**缺卡**（10）：`Fast Groups Bypasser (rgthree)`、`INTConstant`、`ImageScaleToTotalPixels`、`QwenPERewriteT8`、`easy cleanGpuUsed`、`CR Prompt Text`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `INTConstant` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageScaleToTotalPixels` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadDiTModel` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2LoadVAEModel` 仅有 KSampler/VAE 的通用知识，没有该节点自己的说明
- 次要节点 `SeedVR2VideoUpscaler` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
