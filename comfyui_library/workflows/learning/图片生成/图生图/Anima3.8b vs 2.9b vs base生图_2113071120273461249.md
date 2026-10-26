---
key: 图片生成/图生图/Anima3.8b vs 2.9b vs base生图_2113071120273461249.json
name: Anima3.8b vs 2.9b vs base生图_2113071120273461249
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Anima3.8b vs 2.9b vs base生图_2113071120273461249.json
hash: 479c24d76c7a4d7d
coverage: 0.875
learned_at: 2026-10-26 22:01:21
nodes: [VAELoader, CLIPLoader, CLIPTextEncode, VAEDecode, Fast Groups Bypasser (rgthree), Note, ModelSamplingAuraFlow, PreviewAny, LayerUtility: TextJoin, VAELoader, CLIPLoader, CLIPTextEncode, EmptyLatentImage, ModelSamplingAuraFlow, CLIPTextEncode, VAEDecode, SaveImage, KSampler, Text, CLIPTextEncode, EmptyLatentImage, UNETLoader, UNETLoader, SaveImage, SaveImage, ImageConcanate, KSampler, PrimitiveInt, PrimitiveInt, AddLabel, AddLabel, Text, Text, VAELoader, CLIPLoader, Anima38BV2Loader, AnimaQwen35Loader, Anima38BV2Prompt, Anima38BV2Prompt, EmptyLatentImage, VAEDecode, SaveImage, AddLabel, ImageConcanate, KSampler, AddLabel, ModelSamplingAuraFlow, PreviewImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 5, "denoise": 1, "height": 1536, "sampler_name": "res_multistep", "scheduler": "beta", "seed": 666, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Anima3.8b vs 2.9b vs base生图_2113071120273461249.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Anima3.8b vs 2.9b vs base生图_2113071120273461249.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `ModelSamplingAuraFlow`
- `PreviewAny`
- `LayerUtility: TextJoin`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `Text`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `SaveImage`
- `ImageConcanate`
- `KSampler` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `AddLabel`
- `AddLabel`
- `Text`
- `Text`
- `VAELoader`
- `CLIPLoader`
- `Anima38BV2Loader`
- `AnimaQwen35Loader`
- `Anima38BV2Prompt`
- `Anima38BV2Prompt`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `AddLabel`
- `ImageConcanate`
- `KSampler` ★核心
- `AddLabel`
- `ModelSamplingAuraFlow`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `666`
- `steps` = `40`
- `cfg` = `5`
- `sampler_name` = `res_multistep`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（42/48）

**有卡**：`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`VAEDecode`、`ModelSamplingAuraFlow`、`LayerUtility: TextJoin`、`EmptyLatentImage`、`SaveImage`、`KSampler`、`Text`、`UNETLoader`、`ImageConcanate`、`AddLabel`、`Anima38BV2Loader`、`AnimaQwen35Loader`、`Anima38BV2Prompt`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、Anima38BV2Prompt
