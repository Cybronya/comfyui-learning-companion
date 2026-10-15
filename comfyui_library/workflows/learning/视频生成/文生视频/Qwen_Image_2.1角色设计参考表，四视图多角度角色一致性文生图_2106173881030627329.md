---
key: 视频生成/文生视频/Qwen_Image_2.1角色设计参考表，四视图多角度角色一致性文生图_2106173881030627329.json
name: Qwen_Image_2.1角色设计参考表，四视图多角度角色一致性文生图_2106173881030627329
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Qwen_Image_2.1角色设计参考表，四视图多角度角色一致性文生图_2106173881030627329.json
hash: bc444cceccae1717
coverage: 0.819672
learned_at: 2026-10-15 22:46:52
nodes: [easy setNode, VAEDecode, EmptyLatentImage, Seed (rgthree), KSampler, UNETLoader, QwenImage21Cache, VAELoader, Anything Everywhere3, SetNode, SetNode, GetNode, CLIPLoader, CLIPLoader, CLIPLoader, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageScaleToTotalPixels, PreviewImage, Image Comparer (rgthree), INTConstant, SaveImage, LayerUtility: TextJoin, SaveImage, ResolutionSelector, TextEncodeQwenImage21, easy showAnything, CR Prompt Text, TextGenerateLTX2Prompt, CR Prompt Text, Fast Groups Bypasser (rgthree), UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Qwen_Image_2.1角色设计参考表，四视图多角度角色一致性文生图_2106173881030627329.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Qwen_Image_2.1角色设计参考表，四视图多角度角色一致性文生图_2106173881030627329.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `easy setNode`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `Anything Everywhere3`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `INTConstant`
- `SaveImage`
- `LayerUtility: TextJoin`
- `SaveImage`
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `CR Prompt Text`
- `TextGenerateLTX2Prompt`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
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
- `EmptyImage`
- `PreviewImage`

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

覆盖率 **82%**（50/61）

**有卡**：`easy setNode`、`VAEDecode`、`EmptyLatentImage`、`Seed (rgthree)`、`KSampler`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`CLIPLoader`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`ImageScaleToTotalPixels`、`INTConstant`、`SaveImage`、`LayerUtility: TextJoin`、`ResolutionSelector`、`TextEncodeQwenImage21`、`CR Prompt Text`、`TextGenerateLTX2Prompt`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
