---
key: Flux图像反推Chroma,Dev,Flex.2,Shuttle Jugar对比工作流_1922552538472792066.json
name: Flux图像反推Chroma,Dev,Flex.2,Shuttle Jugar对比工作流_1922552538472792066
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux图像反推Chroma,Dev,Flex.2,Shuttle Jugar对比工作流_1922552538472792066.json
hash: 0d8964acf5661190
coverage: 0.882353
learned_at: 2026-10-10 20:58:37
nodes: [VAELoader, EmptySD3LatentImage, CLIPTextEncode, Note, CLIPLoader, T5TokenizerOptions, UNETLoader, EmptyLatentImage, KSamplerSelect, VAELoader, RandomNoise, BasicScheduler, SamplerCustomAdvanced, NunchakuTextEncoderLoader, CLIPTextEncode, NunchakuFluxDiTLoader, LoraLoaderModelOnly, CLIPTextEncode, BasicGuider, VAEDecode, VAEDecode, EmptySD3LatentImage, ApplyFBCacheOnModel, FlexGuidance, VAELoader, ImpactInt, DualCLIPLoader, ConditioningZeroOut, Flex2Conditioner, KSampler, VAEDecode, SamplerCustomAdvanced, VAELoader, KSamplerSelect, BasicGuider, LoraLoaderModelOnly, DualCLIPLoader, BasicScheduler, UNETLoader, VAEDecode, RandomNoise, EmptyLatentImage, ImageConcanate, ImageConcanate, ImageConcanate, CLIPTextEncode, AddLabel, LayerUtility: PurgeVRAM, AddLabel, LayerUtility: PurgeVRAM, AddLabel, AddLabel, LayerUtility: PurgeVRAM, SaveImage, LayerUtility: PurgeVRAM, SaveImage, SaveImage, UNETLoader, LayerUtility: PurgeVRAM, RH_Captioner, RH_Translator, CLIPTextEncode, SaveImage, LayerUtility: PurgeVRAM, KSampler, easy showAnything, SaveImage, LoadImage]
patterns: [text_to_image]
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM]
parameters: {"batch_size": 1, "cfg": 4, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 819665775881981, "steps": 30, "width": 1024}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识]
---

# Flux图像反推Chroma,Dev,Flex.2,Shuttle Jugar对比工作流_1922552538472792066.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux图像反推Chroma,Dev,Flex.2,Shuttle Jugar对比工作流_1922552538472792066.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `VAELoader`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPLoader`
- `T5TokenizerOptions`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `KSamplerSelect` ★核心
- `VAELoader`
- `RandomNoise`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `NunchakuTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `NunchakuFluxDiTLoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `BasicGuider`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `ApplyFBCacheOnModel`
- `FlexGuidance`
- `VAELoader`
- `ImpactInt`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `Flex2Conditioner`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `BasicScheduler`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `EmptyLatentImage` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `AddLabel`
- `LayerUtility: PurgeVRAM`
- `AddLabel`
- `LayerUtility: PurgeVRAM`
- `AddLabel`
- `AddLabel`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `RH_Captioner`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `easy showAnything`
- `SaveImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `819665775881981`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（60/68）

**有卡**：`VAELoader`、`EmptySD3LatentImage`、`CLIPTextEncode`、`CLIPLoader`、`T5TokenizerOptions`、`UNETLoader`、`EmptyLatentImage`、`KSamplerSelect`、`RandomNoise`、`BasicScheduler`、`SamplerCustomAdvanced`、`NunchakuTextEncoderLoader`、`NunchakuFluxDiTLoader`、`LoraLoaderModelOnly`、`BasicGuider`、`VAEDecode`、`ApplyFBCacheOnModel`、`FlexGuidance`、`ImpactInt`、`DualCLIPLoader`、`ConditioningZeroOut`、`Flex2Conditioner`、`KSampler`、`ImageConcanate`、`AddLabel`、`SaveImage`、`RH_Captioner`、`RH_Translator`、`LoadImage`

**缺卡**（6）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
