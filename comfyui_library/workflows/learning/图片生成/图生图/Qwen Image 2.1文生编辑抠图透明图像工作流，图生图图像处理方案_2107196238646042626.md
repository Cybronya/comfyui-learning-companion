---
key: 图片生成/图生图/Qwen Image 2.1文生编辑抠图透明图像工作流，图生图图像处理方案_2107196238646042626.json
name: Qwen Image 2.1文生编辑抠图透明图像工作流，图生图图像处理方案_2107196238646042626
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1文生编辑抠图透明图像工作流，图生图图像处理方案_2107196238646042626.json
hash: 77f5e2f4c0bd54b2
coverage: 0.701754
learned_at: 2026-10-06 21:41:34
nodes: [TextEncodeQwenImage21, ComfySwitchNode, LoadImage, LoadImage, Image Comparer (rgthree), KSampler, SaveImage, VOSR2ModelLoader, Change Channel Count, VOSR2Upscale, SaveImage, LoadImage, QwenImage21Cache, VAEDecode, QwenPERewriteT8, easy showAnything, EmptyLatentImage, Fast Groups Bypasser (rgthree), PrimitiveBoolean, PrimitiveBoolean, SaveImageAdvanced, LoadImage, ResolutionSelector, CR Text, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text, Change Channel Count, Fast Groups Bypasser (rgthree), PrimitiveBoolean, PrimitiveBoolean, QwenPERewriteT8, VOSR2ModelLoader, VOSR2Upscale, SaveImageAdvanced, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `Change Channel Count` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识, 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识, 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识, 次要节点 `VOSR2ModelLoader` 知识库中没有该节点类型的任何知识, 次要节点 `VOSR2Upscale` 相关主题 Upscale 在知识库中无对应知识, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1文生编辑抠图透明图像工作流，图生图图像处理方案_2107196238646042626.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1文生编辑抠图透明图像工作流，图生图图像处理方案_2107196238646042626.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `SaveImage`
- `VOSR2ModelLoader`
- `Change Channel Count`
- `VOSR2Upscale`
- `SaveImage`
- `LoadImage`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `QwenPERewriteT8`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `SaveImageAdvanced`
- `LoadImage`
- `ResolutionSelector`
- `CR Text`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
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

覆盖率 **70%**（40/57）

**有卡**：`TextEncodeQwenImage21`、`LoadImage`、`KSampler`、`SaveImage`、`QwenImage21Cache`、`VAEDecode`、`EmptyLatentImage`、`ResolutionSelector`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`

**缺卡**（10）：`CR Text`、`Change Channel Count`、`Fast Groups Bypasser (rgthree)`、`PrimitiveBoolean`、`PrimitiveBoolean`、`QwenPERewriteT8`、`VOSR2ModelLoader`、`VOSR2Upscale`、`SaveImageAdvanced`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `Change Channel Count` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识
- 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识
- 次要节点 `VOSR2ModelLoader` 知识库中没有该节点类型的任何知识
- 次要节点 `VOSR2Upscale` 相关主题 Upscale 在知识库中无对应知识
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
