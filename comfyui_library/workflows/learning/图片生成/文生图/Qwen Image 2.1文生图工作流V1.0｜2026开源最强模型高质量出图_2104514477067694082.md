---
key: 图片生成/文生图/Qwen Image 2.1文生图工作流V1.0｜2026开源最强模型高质量出图_2104514477067694082.json
name: Qwen Image 2.1文生图工作流V1.0｜2026开源最强模型高质量出图_2104514477067694082
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图工作流V1.0｜2026开源最强模型高质量出图_2104514477067694082.json
hash: c326dbcbdba1577d
coverage: 0.851351
learned_at: 2026-10-07 02:20:45
nodes: [llama_cpp_parameters, llama_cpp_instruct_adv, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, LoadImage, CR Prompt Text, llama_cpp_model_loader, UNETLoader, CLIPLoader, QwenImage21Cache, SaveImageAdvanced, TextEncodeQwenImage21, KSampler, VAELoader, PixaromaResolution, EmptyLatentImage, KSampler, LoraLoaderModelOnly, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), VAEDecode, VAEDecode, Fast Bypasser (rgthree), PreviewAny, QwenPERewriteT8, Any Switch (rgthree), Any Switch (rgthree), SaveImage, PixaromaGroupSwitch, PixaromaGroupSwitch, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图工作流V1.0｜2026开源最强模型高质量出图_2104514477067694082.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图工作流V1.0｜2026开源最强模型高质量出图_2104514477067694082.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（74 个）：
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoadImage`
- `CR Prompt Text`
- `llama_cpp_model_loader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `QwenImage21Cache`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAELoader`
- `PixaromaResolution`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `Mute / Bypass Repeater (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Fast Bypasser (rgthree)`
- `PreviewAny`
- `QwenPERewriteT8`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `SaveImage`
- `PixaromaGroupSwitch`
- `PixaromaGroupSwitch`
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

覆盖率 **85%**（63/74）

**有卡**：`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LoadImage`、`llama_cpp_model_loader`、`UNETLoader`、`CLIPLoader`、`QwenImage21Cache`、`SaveImageAdvanced`、`TextEncodeQwenImage21`、`KSampler`、`VAELoader`、`PixaromaResolution`、`EmptyLatentImage`、`VAEDecode`、`QwenPERewriteT8`、`SaveImage`、`PixaromaGroupSwitch`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（4）：`Fast Bypasser (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
