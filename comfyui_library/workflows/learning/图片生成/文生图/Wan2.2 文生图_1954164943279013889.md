---
key: Wan2.2 文生图_1954164943279013889.json
name: Wan2.2 文生图_1954164943279013889
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 文生图_1954164943279013889.json
hash: 68a65e3992369fb4
coverage: 0.648649
learned_at: 2026-10-10 20:59:13
nodes: [UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, VAEDecode, SaveImage, SaveImage, SaveImage, VAEDecode, VAEDecode, VAEDecode, KSampler, KSampler, KSampler, KSampler, LoraLoaderModelOnly, SaveImage, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, Text Concatenate (JPS), Anything Everywhere, CLIPLoader, VAELoader, EmptyLatentImage, Anything Everywhere3, Mute / Bypass Repeater (rgthree), JjkText, CLIPTextEncode, Reroute, CLIPTextEncode, Mute / Bypass Repeater (rgthree), LoadImage, Fast Bypasser (rgthree), LayerUtility: JoyCaptionBeta1, ShowText|pysssss, Fast Bypasser (rgthree)]
patterns: [text_to_image]
missing: [Fast Bypasser (rgthree), Fast Bypasser (rgthree), LayerUtility: JoyCaptionBeta1, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, Mute / Bypass Repeater (rgthree), Mute / Bypass Repeater (rgthree), Text Concatenate (JPS)]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "res_2s", "scheduler": "bong_tangent", "seed": 53526747252266, "steps": 8, "width": 1024}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate (JPS)` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Wan2.2 文生图_1954164943279013889.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 文生图_1954164943279013889.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（37 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `Text Concatenate (JPS)`
- `Anything Everywhere`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `Anything Everywhere3`
- `Mute / Bypass Repeater (rgthree)`
- `JjkText`
- `CLIPTextEncode` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `Mute / Bypass Repeater (rgthree)`
- `LoadImage`
- `Fast Bypasser (rgthree)`
- `LayerUtility: JoyCaptionBeta1`
- `ShowText|pysssss`
- `Fast Bypasser (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `53526747252266`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `bong_tangent`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **65%**（24/37）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEDecode`、`SaveImage`、`KSampler`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`CLIPTextEncode`、`LoadImage`

**缺卡**（8）：`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: LoadJoyCaptionBeta1Model`、`Mute / Bypass Repeater (rgthree)`、`Mute / Bypass Repeater (rgthree)`、`Text Concatenate (JPS)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: JoyCaptionBeta1ExtraOptions` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LoadJoyCaptionBeta1Model` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Mute / Bypass Repeater (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate (JPS)` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
