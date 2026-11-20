---
key: 平台全量/MOSS +Qwen2.1-X动漫剧情运营1107 (1)_2118776927183003650.json
name: MOSS +Qwen2.1-X动漫剧情运营1107 (1)_2118776927183003650
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/MOSS +Qwen2.1-X动漫剧情运营1107 (1)_2118776927183003650.json
hash: bf44d09f76a7245f
coverage: 0.816327
learned_at: 2026-11-14 00:39:55
nodes: [ResolutionSelector, VAELoader, SkipLayerGuidanceDiTSimple, CLIPLoader, CLIPTextEncode, CLIPTextEncode, UNETLoader, EmptyFlux2LatentImage, KSampler, VAEDecode, MOSSMergePreset, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VOSR2Upscale, VOSR2ModelLoader, PDIMAGE_LongerSize, SaveImage, MarkdownNote, CR Text Concatenate, PrimitiveStringMultiline, PrimitiveStringMultiline, QwenPERewriteT8, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, easy showAnything, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, KSampler, VAEDecode, SaveImage, Lora Loader Stack (rgthree), Reroute, Reroute, Reroute, SaveImage, easy promptList, easy lengthAnything, easy forLoopStart, GetItemFromList, easy forLoopEnd, easy showAnything, QwenImage21SpectrumT8, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 685320426087354, "steps": 40, "width": 1024}
---

# 平台全量/MOSS +Qwen2.1-X动漫剧情运营1107 (1)_2118776927183003650.json

> 来源文件 `comfyui_library/workflows/平台全量/MOSS +Qwen2.1-X动漫剧情运营1107 (1)_2118776927183003650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `ResolutionSelector`
- `VAELoader`
- `SkipLayerGuidanceDiTSimple`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `EmptyFlux2LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `MOSSMergePreset`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `PDIMAGE_LongerSize`
- `SaveImage`
- `MarkdownNote`
- `CR Text Concatenate`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `QwenPERewriteT8`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Lora Loader Stack (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `SaveImage`
- `easy promptList`
- `easy lengthAnything`
- `easy forLoopStart`
- `GetItemFromList`
- `easy forLoopEnd`
- `easy showAnything`
- `QwenImage21SpectrumT8`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `685320426087354`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（40/49）

**有卡**：`ResolutionSelector`、`VAELoader`、`SkipLayerGuidanceDiTSimple`、`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`EmptyFlux2LatentImage`、`KSampler`、`VAEDecode`、`MOSSMergePreset`、`LoraLoaderModelOnly`、`VOSR2Upscale`、`VOSR2ModelLoader`、`PDIMAGE_LongerSize`、`SaveImage`、`CR Text Concatenate`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`CR Prompt Text`、`EmptyLatentImage`、`Lora Loader Stack (rgthree)`、`easy promptList`、`easy lengthAnything`、`easy forLoopStart`、`GetItemFromList`、`easy forLoopEnd`、`QwenImage21SpectrumT8`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode
