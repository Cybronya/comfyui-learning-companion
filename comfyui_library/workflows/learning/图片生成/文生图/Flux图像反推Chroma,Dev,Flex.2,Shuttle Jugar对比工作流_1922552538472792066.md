---
key: 图片生成/文生图/Flux图像反推Chroma,Dev,Flex.2,Shuttle Jugar对比工作流_1922552538472792066.json
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

# 图片生成/文生图/Flux图像反推Chroma,Dev,Flex.2,Shuttle Jugar对比工作流_1922552538472792066.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux图像反推Chroma,Dev,Flex.2,Shuttle Jugar对比工作流_1922552538472792066.json`

## 结构

**节点**（68 个）：
- `VAELoader`
- `EmptySD3LatentImage`
- `CLIPTextEncode`
- `Note`
- `CLIPLoader`
- `T5TokenizerOptions`
- `UNETLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `VAELoader`
- `RandomNoise`
- `BasicScheduler`
- `SamplerCustomAdvanced`
- `NunchakuTextEncoderLoader`
- `CLIPTextEncode`
- `NunchakuFluxDiTLoader`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `BasicGuider`
- `VAEDecode`
- `VAEDecode`
- `EmptySD3LatentImage`
- `ApplyFBCacheOnModel`
- `FlexGuidance`
- `VAELoader`
- `ImpactInt`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `Flex2Conditioner`
- `KSampler`
- `VAEDecode`
- `SamplerCustomAdvanced`
- `VAELoader`
- `KSamplerSelect`
- `BasicGuider`
- `LoraLoaderModelOnly`
- `DualCLIPLoader`
- `BasicScheduler`
- `UNETLoader`
- `VAEDecode`
- `RandomNoise`
- `EmptyLatentImage`
- `ImageConcanate`
- `ImageConcanate`
- `ImageConcanate`
- `CLIPTextEncode`
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
- `UNETLoader`
- `LayerUtility: PurgeVRAM`
- `RH_Captioner`
- `RH_Translator`
- `CLIPTextEncode`
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `KSampler`
- `easy showAnything`
- `SaveImage`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `819665775881981`
- `steps` = `30`
- `width` = `1024`

## 知识

覆盖率 **88%**（60/68）

**有卡**：`VAELoader`、`EmptySD3LatentImage`、`CLIPTextEncode`、`Note`、`CLIPLoader`、`T5TokenizerOptions`、`UNETLoader`、`EmptyLatentImage`、`KSamplerSelect`、`RandomNoise`、`BasicScheduler`、`SamplerCustomAdvanced`、`NunchakuTextEncoderLoader`、`NunchakuFluxDiTLoader`、`LoraLoaderModelOnly`、`BasicGuider`、`VAEDecode`、`ApplyFBCacheOnModel`、`FlexGuidance`、`ImpactInt`、`DualCLIPLoader`、`ConditioningZeroOut`、`Flex2Conditioner`、`KSampler`、`ImageConcanate`、`AddLabel`、`LayerUtility: PurgeVRAM`、`SaveImage`、`RH_Captioner`

**缺卡**（6）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
