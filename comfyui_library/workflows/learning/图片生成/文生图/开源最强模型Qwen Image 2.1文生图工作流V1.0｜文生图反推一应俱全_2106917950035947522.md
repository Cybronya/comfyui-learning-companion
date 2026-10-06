---
key: 图片生成/文生图/开源最强模型Qwen Image 2.1文生图工作流V1.0｜文生图反推一应俱全_2106917950035947522.json
name: 开源最强模型Qwen Image 2.1文生图工作流V1.0｜文生图反推一应俱全_2106917950035947522
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/开源最强模型Qwen Image 2.1文生图工作流V1.0｜文生图反推一应俱全_2106917950035947522.json
hash: 05056e409a59dd8d
coverage: 0.716216
learned_at: 2026-10-06 21:52:04
nodes: [llama_cpp_parameters, llama_cpp_instruct_adv, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, LoadImage, CR Prompt Text, llama_cpp_model_loader, PixaromaGroupSwitch, PixaromaGroupSwitch, UNETLoader, CLIPLoader, QwenImage21Cache, SaveImageAdvanced, TextEncodeQwenImage21, KSampler, VAELoader, PixaromaResolution, EmptyLatentImage, KSampler, LoraLoaderModelOnly, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), VAEDecode, VAEDecode, Fast Bypasser (rgthree), PreviewAny, QwenPERewriteT8, Any Switch (rgthree), Any Switch (rgthree), SaveImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: [Fast Bypasser (rgthree), Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PixaromaGroupSwitch, PixaromaGroupSwitch, QwenPERewriteT8, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, CR Prompt Text, PixaromaResolution, PreviewAny, SaveImageAdvanced, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `PathchSageAttentionKJ` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识, 次要节点 `llama_cpp_parameters` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `PixaromaResolution` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/开源最强模型Qwen Image 2.1文生图工作流V1.0｜文生图反推一应俱全_2106917950035947522.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/开源最强模型Qwen Image 2.1文生图工作流V1.0｜文生图反推一应俱全_2106917950035947522.json`

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
- `PixaromaGroupSwitch`
- `PixaromaGroupSwitch`
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

覆盖率 **72%**（53/74）

**有卡**：`LoraLoaderModelOnly`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`

**缺卡**（15）：`Fast Bypasser (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`PathchSageAttentionKJ`、`PixaromaGroupSwitch`、`PixaromaGroupSwitch`、`QwenPERewriteT8`、`llama_cpp_instruct_adv`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`CR Prompt Text`、`PixaromaResolution`、`PreviewAny`、`SaveImageAdvanced`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `PathchSageAttentionKJ` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `PixaromaGroupSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenPERewriteT8` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_instruct_adv` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_model_loader` 知识库中没有该节点类型的任何知识
- 次要节点 `llama_cpp_parameters` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `PixaromaResolution` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
