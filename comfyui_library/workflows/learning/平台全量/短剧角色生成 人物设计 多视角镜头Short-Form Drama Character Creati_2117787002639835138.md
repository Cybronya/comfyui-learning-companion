---
key: 平台全量/短剧角色生成 人物设计 多视角镜头Short-Form Drama Character Creati_2117787002639835138.json
name: 短剧角色生成 人物设计 多视角镜头Short-Form Drama Character Creati_2117787002639835138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/短剧角色生成 人物设计 多视角镜头Short-Form Drama Character Creati_2117787002639835138.json
hash: 8720a64f061f2dc1
coverage: 0.823529
learned_at: 2026-11-14 02:27:09
nodes: [easy getNode, easy setNode, CLIPLoader, easy setNode, VAELoader, LoraLoaderModelOnly, easy setNode, LoadImageGoohai, easy setNode, easy setNode, LoadImage, LoadImage, easy setNode, LoadImage, easy setNode, LoadImage, easy setNode, LoadImage, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, GoohaiAnyExists, easy getNode, easy ifElse, VAEDecode, RestoreQwenImage21GH, easy getNode, easy getNode, UNETLoader, LoraLoaderModelOnly, QwenImage21BlockCacheT8, QwenImage21SpectrumT8, KOOK_ImageCompression, KSamplerAdvanced, Note, ShowText|pysssss, Fast Groups Bypasser (rgthree), SaveImage, QwenImagePromptOptimizer, GoohaiRouteBlocker, QwenImage21SageAttentionT8, easy ifElse, easy ifElse, EmptyLatentImage, TextEncodeQwenImage21GH, easy positive, Seed (rgthree), Fast Groups Bypasser (rgthree), ResolutionSelector, Note, Note, GoohaiRouteBlocker, easy boolean, easy boolean, Note, LoraLoaderModelOnly, Note, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 30, "denoise": "simple", "height": 1024, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 1024}
---

# 平台全量/短剧角色生成 人物设计 多视角镜头Short-Form Drama Character Creati_2117787002639835138.json

> 来源文件 `comfyui_library/workflows/平台全量/短剧角色生成 人物设计 多视角镜头Short-Form Drama Character Creati_2117787002639835138.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
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
- `Note`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `QwenImagePromptOptimizer`
- `GoohaiRouteBlocker`
- `QwenImage21SageAttentionT8`
- `easy ifElse`
- `easy ifElse`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21GH`
- `easy positive`
- `Seed (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`
- `Note`
- `Note`
- `GoohaiRouteBlocker`
- `easy boolean`
- `easy boolean`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `30`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（56/68）

**有卡**：`easy getNode`、`easy setNode`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`LoadImageGoohai`、`LoadImage`、`GoohaiAnyExists`、`VAEDecode`、`RestoreQwenImage21GH`、`UNETLoader`、`QwenImage21BlockCacheT8`、`QwenImage21SpectrumT8`、`KOOK_ImageCompression`、`KSamplerAdvanced`、`SaveImage`、`QwenImagePromptOptimizer`、`GoohaiRouteBlocker`、`QwenImage21SageAttentionT8`、`EmptyLatentImage`、`TextEncodeQwenImage21GH`、`easy positive`、`Seed (rgthree)`、`ResolutionSelector`、`easy boolean`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage、UNETLoader
