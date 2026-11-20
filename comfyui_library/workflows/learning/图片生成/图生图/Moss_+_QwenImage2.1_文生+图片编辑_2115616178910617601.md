---
key: 图片生成/图生图/Moss_+_QwenImage2.1_文生+图片编辑_2115616178910617601.json
name: Moss_+_QwenImage2.1_文生+图片编辑_2115616178910617601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Moss_+_QwenImage2.1_文生+图片编辑_2115616178910617601.json
hash: d0c4026382afa896
coverage: 0.711111
learned_at: 2026-10-30 17:50:44
nodes: [VAELoader, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, VAEDecode, SaveImage, PrimitiveStringMultiline, SamplerCustomAdvanced, RandomNoise, ManualSigmas, CFGGuider, KSamplerSelect, PrimitiveStringMultiline, ComfySwitchNode, easy isNone, VAELoader, easy showAnything, TextEncodeQwenImage21, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, TextGenerate, CLIPLoader, LoadImage, LoadImage, LoadImage, Any Switch (rgthree), LoadImage, LoadImage, LoadImage, CLIPLoader, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, SkipLayerGuidanceDiTSimple, UNETLoader, ComfySwitchNode, LoadImage, easy showAnything, JsonExtractString, PrimitiveStringMultiline, CLIPLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/Moss_+_QwenImage2.1_文生+图片编辑_2115616178910617601.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Moss_+_QwenImage2.1_文生+图片编辑_2115616178910617601.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（45 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
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

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（32/45）

**有卡**：`VAELoader`、`CLIPTextEncode`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`、`SamplerCustomAdvanced`、`RandomNoise`、`ManualSigmas`、`CFGGuider`、`KSamplerSelect`、`easy isNone`、`TextEncodeQwenImage21`、`TextGenerate`、`CLIPLoader`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`SkipLayerGuidanceDiTSimple`、`JsonExtractString`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage
