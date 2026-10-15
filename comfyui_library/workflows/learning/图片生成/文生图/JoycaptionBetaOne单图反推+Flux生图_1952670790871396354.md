---
key: 图片生成/文生图/JoycaptionBetaOne单图反推+Flux生图_1952670790871396354.json
name: JoycaptionBetaOne单图反推+Flux生图_1952670790871396354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/JoycaptionBetaOne单图反推+Flux生图_1952670790871396354.json
hash: 0b1dd5bcfa622153
coverage: 0.842105
learned_at: 2026-10-10 20:58:41
nodes: [LoadImage, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, VAELoader, KSamplerSelect, BasicGuider, BasicScheduler, SamplerCustomAdvanced, VAEDecode, DualCLIPLoader, RandomNoise, UNETLoader, CLIPTextEncode, ShowText, LoraLoaderModelOnly, EmptyLatentImage, SaveImage, LoraLoaderModelOnly]
patterns: []
missing: [LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model]
parameters: {"batch_size": 1, "height": 1024, "width": 1280}
discoveries: [次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/JoycaptionBetaOne单图反推+Flux生图_1952670790871396354.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/JoycaptionBetaOne单图反推+Flux生图_1952670790871396354.json`

## 结构

**节点**（19 个）：
- `LoadImage`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `VAELoader`
- `KSamplerSelect`
- `BasicGuider`
- `BasicScheduler`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `DualCLIPLoader`
- `RandomNoise`
- `UNETLoader`
- `CLIPTextEncode`
- `ShowText`
- `LoraLoaderModelOnly`
- `EmptyLatentImage`
- `SaveImage`
- `LoraLoaderModelOnly`

## 关键参数

- `batch_size` = `1`
- `height` = `1024`
- `width` = `1280`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`LoadImage`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`VAELoader`、`KSamplerSelect`、`BasicGuider`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`DualCLIPLoader`、`RandomNoise`、`UNETLoader`、`CLIPTextEncode`、`ShowText`、`LoraLoaderModelOnly`

**缺卡**（3）：`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: LoadJoyCaptionBeta1Model`

## 学习发现

- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
