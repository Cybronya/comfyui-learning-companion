---
key: 视频生成/图生视频/Qwen Image 2.1故事分镜参考图生成支持九宫格六宫格四宫格，图生视频方案_2107217385190158338.json
name: Qwen Image 2.1故事分镜参考图生成支持九宫格六宫格四宫格，图生视频方案_2107217385190158338
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen Image 2.1故事分镜参考图生成支持九宫格六宫格四宫格，图生视频方案_2107217385190158338.json
hash: edc6feb5164ac417
coverage: 0.727273
learned_at: 2026-10-17 22:18:49
nodes: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, TextEncodeQwenImage21, PrimitiveInt, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, EmptyLatentImage, easy seed, GetNode, UNETLoader, QwenImage21Cache, CLIPLoader, VAELoader, SetNode, SetNode, SetNode, SaveImage, StringConcatenate, PrimitiveBoolean, ComfySwitchNode, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt, KSampler, VAEDecode, GetNode, GetNode, ComfySwitchNode, RHLLMChatNode, PreviewAny, PrimitiveStringMultiline, LoadImage, LoadImage, LoadImage, PrimitiveBoolean, PrimitiveBoolean, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, EmptyImage, PreviewImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Qwen Image 2.1故事分镜参考图生成支持九宫格六宫格四宫格，图生视频方案_2107217385190158338.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen Image 2.1故事分镜参考图生成支持九宫格六宫格四宫格，图生视频方案_2107217385190158338.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `PrimitiveInt`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `easy seed`
- `GetNode`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SaveImage`
- `StringConcatenate`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `RHLLMChatNode`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
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
- `EmptyImage`
- `PreviewImage`
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

覆盖率 **73%**（72/99）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`easy seed`、`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`SaveImage`、`StringConcatenate`、`PrimitiveBoolean`、`KSampler`、`VAEDecode`、`RHLLMChatNode`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
