---
key: 图片生成/图生图/Qwen-Image_2.1多图参考智能提示词，AI生图编辑一步到位_2112340219432357890.json
name: Qwen-Image_2.1多图参考智能提示词，AI生图编辑一步到位_2112340219432357890
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image_2.1多图参考智能提示词，AI生图编辑一步到位_2112340219432357890.json
hash: 7bebed659788bbff
coverage: 0.859375
learned_at: 2026-10-23 11:17:22
nodes: [LoadImage, LoadImage, LoadImage, VAEDecode, CLIPLoader, VAELoader, LoadImage, LoadImage, UNETLoader, GoohaiRouteBlocker, GoohaiRatioAndResolution, QwenImage21SageAttentionT8, KSampler, GoohaiRouteBlocker, ShowText|pysssss, Image Comparer (rgthree), QwenImagePromptOptimizer, DF_Text_Box, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, RestoreQwenImage21GH, TextEncodeQwenImage21GH, LoadImageGoohai, SaveImage, PrimitiveBoolean, ComfySwitchNode, ComfySwitchNode, PrimitiveBoolean, PrimitiveBoolean, ComfySwitchNode, GoohaiRouteBlocker, GoohaiRouteBlocker, GoohaiRouteBlocker, GoohaiRouteBlocker, GoohaiRouteBlocker, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image_2.1多图参考智能提示词，AI生图编辑一步到位_2112340219432357890.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image_2.1多图参考智能提示词，AI生图编辑一步到位_2112340219432357890.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `GoohaiRouteBlocker`
- `GoohaiRatioAndResolution`
- `QwenImage21SageAttentionT8`
- `KSampler` ★核心
- `GoohaiRouteBlocker`
- `ShowText|pysssss`
- `Image Comparer (rgthree)`
- `QwenImagePromptOptimizer`
- `DF_Text_Box`
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `RestoreQwenImage21GH`
- `TextEncodeQwenImage21GH`
- `LoadImageGoohai`
- `SaveImage`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `GoohaiRouteBlocker`
- `GoohaiRouteBlocker`
- `GoohaiRouteBlocker`
- `GoohaiRouteBlocker`
- `GoohaiRouteBlocker`
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

覆盖率 **86%**（55/64）

**有卡**：`LoadImage`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`GoohaiRouteBlocker`、`GoohaiRatioAndResolution`、`QwenImage21SageAttentionT8`、`KSampler`、`QwenImagePromptOptimizer`、`DF_Text_Box`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`RestoreQwenImage21GH`、`TextEncodeQwenImage21GH`、`LoadImageGoohai`、`SaveImage`、`PrimitiveBoolean`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
