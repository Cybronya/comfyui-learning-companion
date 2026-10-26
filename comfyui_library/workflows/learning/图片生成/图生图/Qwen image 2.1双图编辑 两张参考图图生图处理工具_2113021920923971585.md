---
key: 图片生成/图生图/Qwen image 2.1双图编辑 两张参考图图生图处理工具_2113021920923971585.json
name: Qwen image 2.1双图编辑 两张参考图图生图处理工具_2113021920923971585
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1双图编辑 两张参考图图生图处理工具_2113021920923971585.json
hash: 676b8b9380da965a
coverage: 0.811321
learned_at: 2026-10-26 22:03:12
nodes: [PathchSageAttentionKJ, CLIPLoader, VAELoader, VAEDecode, Any Switch (rgthree), SaveImage, UNETLoader, QwenImage21Cache, ShowText|pysssss, QwenPERewriteT8, LoadImage, LoadImage, CR Prompt Text, TextEncodeQwenImage21, EmptyLatentImage, PrimitiveString, StringToInt, StringToInt, PrimitiveString, KSampler, StringToInt, PrimitiveString, StringToInt, PrimitiveString, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1双图编辑 两张参考图图生图处理工具_2113021920923971585.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1双图编辑 两张参考图图生图处理工具_2113021920923971585.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（53 个）：
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `Any Switch (rgthree)`
- `SaveImage`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `ShowText|pysssss`
- `QwenPERewriteT8`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `PrimitiveString`
- `StringToInt`
- `StringToInt`
- `PrimitiveString`
- `KSampler` ★核心
- `StringToInt`
- `PrimitiveString`
- `StringToInt`
- `PrimitiveString`
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
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

覆盖率 **81%**（43/53）

**有卡**：`PathchSageAttentionKJ`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`SaveImage`、`UNETLoader`、`QwenImage21Cache`、`QwenPERewriteT8`、`LoadImage`、`CR Prompt Text`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`StringToInt`、`KSampler`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
