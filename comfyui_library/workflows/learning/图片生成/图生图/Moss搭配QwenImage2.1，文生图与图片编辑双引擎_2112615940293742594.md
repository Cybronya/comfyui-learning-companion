---
key: 图片生成/图生图/Moss搭配QwenImage2.1，文生图与图片编辑双引擎_2112615940293742594.json
name: Moss搭配QwenImage2.1，文生图与图片编辑双引擎_2112615940293742594
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Moss搭配QwenImage2.1，文生图与图片编辑双引擎_2112615940293742594.json
hash: da9fabfa2bdd4bfa
coverage: 0.773333
learned_at: 2026-10-23 11:09:41
nodes: [VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, ResolutionSelector, VAEDecode, SaveImage, PrimitiveStringMultiline, SamplerCustomAdvanced, RandomNoise, ManualSigmas, CFGGuider, KSamplerSelect, PrimitiveStringMultiline, ComfySwitchNode, easy isNone, VAELoader, easy showAnything, TextEncodeQwenImage21, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, TextGenerate, CLIPLoader, LoadImage, LoadImage, LoadImage, Any Switch (rgthree), LoadImage, LoadImage, LoadImage, CLIPLoader, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, SkipLayerGuidanceDiTSimple, UNETLoader, ComfySwitchNode, LoadImage, easy showAnything, JsonExtractString, PrimitiveStringMultiline, CLIPLoader, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Moss搭配QwenImage2.1，文生图与图片编辑双引擎_2112615940293742594.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Moss搭配QwenImage2.1，文生图与图片编辑双引擎_2112615940293742594.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（75 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `VAEDecode` ★核心
- `SaveImage`
- `PrimitiveStringMultiline`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `ManualSigmas`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `easy isNone`
- `VAELoader`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `TextGenerate`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Any Switch (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SkipLayerGuidanceDiTSimple`
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `easy showAnything`
- `JsonExtractString`
- `PrimitiveStringMultiline`
- `CLIPLoader`
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

覆盖率 **77%**（58/75）

**有卡**：`VAELoader`、`CLIPTextEncode`、`EmptyLatentImage`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`SamplerCustomAdvanced`、`RandomNoise`、`ManualSigmas`、`CFGGuider`、`KSamplerSelect`、`easy isNone`、`TextEncodeQwenImage21`、`TextGenerate`、`CLIPLoader`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`SkipLayerGuidanceDiTSimple`、`JsonExtractString`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
