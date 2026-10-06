---
key: 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106409021661077505.json
name: Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106409021661077505
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106409021661077505.json
hash: 986ff21c9547b42c
coverage: 0.564516
learned_at: 2026-10-06 21:37:01
nodes: [LoadImage, LoadImage, Reroute, Reroute, Reroute, Reroute, Reroute, SetNode, VAEDecode, CLIPLoader, VAELoader, Reroute, LoadImage, LoadImage, UNETLoader, QwenImage21SageAttentionT8, KSampler, GoohaiRouteBlocker, ShowText|pysssss, QwenImage21SpectrumT8, RestoreQwenImage21GH, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, DF_Text_Box, GoohaiRatioAndResolution, Image Comparer (rgthree), QwenImagePromptOptimizer, GetNode, QwenImage21BlockCacheT8, TextEncodeQwenImage21GH, Reroute, GoohaiRouteBlocker, LoadImage, LoadImageGoohai]
patterns: [text_to_image]
missing: [DF_Text_Box, GoohaiRouteBlocker, GoohaiRouteBlocker, LoadImageGoohai, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, RestoreQwenImage21GH, GoohaiRatioAndResolution, QwenImagePromptOptimizer, TextEncodeQwenImage21GH, solarL_SaveImagesToZip]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `DF_Text_Box` 知识库中没有该节点类型的任何知识, 次要节点 `GoohaiRouteBlocker` 知识库中没有该节点类型的任何知识, 次要节点 `GoohaiRouteBlocker` 知识库中没有该节点类型的任何知识, 次要节点 `LoadImageGoohai` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21BlockCacheT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21SageAttentionT8` 知识库中没有该节点类型的任何知识, 次要节点 `QwenImage21SpectrumT8` 知识库中没有该节点类型的任何知识, 次要节点 `RestoreQwenImage21GH` 知识库中没有该节点类型的任何知识, 次要节点 `GoohaiRatioAndResolution` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `QwenImagePromptOptimizer` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `TextEncodeQwenImage21GH` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106409021661077505.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/Qwen Image 2.1文生图像编辑一体化，文生图反推提示词图生图方案_2106409021661077505.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（62 个）：
- `LoadImage`
- `LoadImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SetNode`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `QwenImage21SageAttentionT8`
- `KSampler` ★核心
- `GoohaiRouteBlocker`
- `ShowText|pysssss`
- `QwenImage21SpectrumT8`
- `RestoreQwenImage21GH`
- `SaveImage`
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
- `DF_Text_Box`
- `GoohaiRatioAndResolution`
- `Image Comparer (rgthree)`
- `QwenImagePromptOptimizer`
- `GetNode`
- `QwenImage21BlockCacheT8`
- `TextEncodeQwenImage21GH`
- `Reroute`
- `GoohaiRouteBlocker`
- `LoadImage`
- `LoadImageGoohai`

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

覆盖率 **56%**（35/62）

**有卡**：`LoadImage`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSampler`、`SaveImage`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`CLIPTextEncode`

**缺卡**（12）：`DF_Text_Box`、`GoohaiRouteBlocker`、`GoohaiRouteBlocker`、`LoadImageGoohai`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`QwenImage21SpectrumT8`、`RestoreQwenImage21GH`、`GoohaiRatioAndResolution`、`QwenImagePromptOptimizer`、`TextEncodeQwenImage21GH`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `DF_Text_Box` 知识库中没有该节点类型的任何知识
- 次要节点 `GoohaiRouteBlocker` 知识库中没有该节点类型的任何知识
- 次要节点 `GoohaiRouteBlocker` 知识库中没有该节点类型的任何知识
- 次要节点 `LoadImageGoohai` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21BlockCacheT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21SageAttentionT8` 知识库中没有该节点类型的任何知识
- 次要节点 `QwenImage21SpectrumT8` 知识库中没有该节点类型的任何知识
- 次要节点 `RestoreQwenImage21GH` 知识库中没有该节点类型的任何知识
- 次要节点 `GoohaiRatioAndResolution` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `QwenImagePromptOptimizer` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `TextEncodeQwenImage21GH` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `solarL_SaveImagesToZip` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
