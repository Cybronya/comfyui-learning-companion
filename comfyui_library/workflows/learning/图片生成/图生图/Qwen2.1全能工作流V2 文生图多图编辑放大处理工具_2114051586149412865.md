---
key: 图片生成/图生图/Qwen2.1全能工作流V2 文生图多图编辑放大处理工具_2114051586149412865.json
name: Qwen2.1全能工作流V2 文生图多图编辑放大处理工具_2114051586149412865
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1全能工作流V2 文生图多图编辑放大处理工具_2114051586149412865.json
hash: 748bbf73ac3c6af8
coverage: 0.88764
learned_at: 2026-10-26 22:03:28
nodes: [easy getNode, easy setNode, CLIPLoader, easy setNode, VAELoader, LoraLoaderModelOnly, easy setNode, LoadImageGoohai, easy setNode, easy setNode, LoadImage, LoadImage, easy setNode, LoadImage, easy setNode, LoadImage, easy setNode, LoadImage, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, GoohaiAnyExists, easy getNode, easy ifElse, VAEDecode, RestoreQwenImage21GH, easy getNode, easy getNode, UNETLoader, LoraLoaderModelOnly, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, KOOK_ImageCompression, KSamplerAdvanced, GoohaiRouteBlocker, Seed (rgthree), ShowText|pysssss, easy boolean, Fast Groups Bypasser (rgthree), easy boolean, Image Comparer (rgthree), easy ifElse, TextEncodeQwenImage21GH, SaveImage, Fast Groups Bypasser (rgthree), GoohaiRouteBlocker, QwenImage21SageAttentionT8, QwenImagePromptOptimizer, easy positive, ResolutionSelector, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen2.1全能工作流V2 文生图多图编辑放大处理工具_2114051586149412865.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1全能工作流V2 文生图多图编辑放大处理工具_2114051586149412865.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（89 个）：
- `easy getNode`
- `easy setNode`
- `CLIPLoader`
- `easy setNode`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `easy setNode`
- `LoadImageGoohai`
- `easy setNode`
- `easy setNode`
- `LoadImage`
- `LoadImage`
- `easy setNode`
- `LoadImage`
- `easy setNode`
- `LoadImage`
- `easy setNode`
- `LoadImage`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `GoohaiAnyExists`
- `easy getNode`
- `easy ifElse`
- `VAEDecode` ★核心
- `RestoreQwenImage21GH`
- `easy getNode`
- `easy getNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenImage21BlockCacheT8`
- `QwenImage21SpectrumT8`
- `KOOK_ImageCompression`
- `KSamplerAdvanced` ★核心
- `GoohaiRouteBlocker`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `easy boolean`
- `Fast Groups Bypasser (rgthree)`
- `easy boolean`
- `Image Comparer (rgthree)`
- `easy ifElse`
- `TextEncodeQwenImage21GH`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `GoohaiRouteBlocker`
- `QwenImage21SageAttentionT8`
- `QwenImagePromptOptimizer`
- `easy positive`
- `ResolutionSelector`
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

覆盖率 **89%**（79/89）

**有卡**：`easy getNode`、`easy setNode`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImageGoohai`、`LoadImage`、`GoohaiAnyExists`、`VAEDecode`、`RestoreQwenImage21GH`、`UNETLoader`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`KOOK_ImageCompression`、`KSamplerAdvanced`、`GoohaiRouteBlocker`、`Seed (rgthree)`、`easy boolean`、`TextEncodeQwenImage21GH`、`SaveImage`、`QwenImage21SageAttentionT8`、`QwenImagePromptOptimizer`、`easy positive`、`ResolutionSelector`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
