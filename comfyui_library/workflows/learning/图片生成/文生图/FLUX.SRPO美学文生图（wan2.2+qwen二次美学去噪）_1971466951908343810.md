---
key: FLUX.SRPO美学文生图（wan2.2+qwen二次美学去噪）_1971466951908343810.json
name: FLUX.SRPO美学文生图（wan2.2+qwen二次美学去噪）_1971466951908343810
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.SRPO美学文生图（wan2.2+qwen二次美学去噪）_1971466951908343810.json
hash: 0a7ae90f43ba82da
coverage: 0.807018
learned_at: 2026-10-10 20:58:32
nodes: [DualCLIPLoader, VAELoader, ModelSamplingFlux, ConditioningZeroOut, CLIPLoader, UNETLoader, RH_Translator, LoraLoaderModelOnly, UNETLoader, VAELoader, CLIPTextEncode, LoraLoaderModelOnly, ModelSamplingSD3, KSampler, VAEEncode, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, VAEEncode, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, CLIPTextEncodeFlux, EmptyLatentImage, CLIPTextEncode, CLIPLoader, CLIPTextEncode, CLIPTextEncode, ModelSamplingAuraFlow, LoraLoaderModelOnly, KSampler, KSampler, LayerUtility: PurgeVRAM V2, PreviewImage, PreviewImage, ImageScaleToMegapixels, PreviewImage, VAEDecode, PreviewImage, PreviewImage, LoraLoaderModelOnly, LoraLoaderModelOnly, NunchakuQwenImageDiTLoader, PreviewImage, CR Text, Int, Int, ImageConcatMulti, PreviewImage, SaveImage, SaveImage, SaveImage, VAEDecode, SaveImage, SeedVR2, SeedVR2, SeedVR2]
patterns: [text_to_image]
missing: [CR Text, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 675660653212283, "steps": 12, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# FLUX.SRPO美学文生图（wan2.2+qwen二次美学去噪）_1971466951908343810.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.SRPO美学文生图（wan2.2+qwen二次美学去噪）_1971466951908343810.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `DualCLIPLoader`
- `VAELoader`
- `ModelSamplingFlux`
- `ConditioningZeroOut`
- `CLIPLoader`
- `UNETLoader` ★核心
- `RH_Translator`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `VAEEncode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncodeFlux` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `PreviewImage`
- `ImageScaleToMegapixels`
- `PreviewImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `NunchakuQwenImageDiTLoader`
- `PreviewImage`
- `CR Text`
- `Int`
- `Int`
- `ImageConcatMulti`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `SeedVR2`
- `SeedVR2`
- `SeedVR2`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `675660653212283`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（46/57）

**有卡**：`DualCLIPLoader`、`VAELoader`、`ModelSamplingFlux`、`ConditioningZeroOut`、`CLIPLoader`、`UNETLoader`、`RH_Translator`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSampler`、`VAEEncode`、`VAEDecode`、`CLIPTextEncodeFlux`、`EmptyLatentImage`、`ModelSamplingAuraFlow`、`ImageScaleToMegapixels`、`NunchakuQwenImageDiTLoader`、`Int`、`ImageConcatMulti`、`SaveImage`、`SeedVR2`

**缺卡**（4）：`CR Text`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
