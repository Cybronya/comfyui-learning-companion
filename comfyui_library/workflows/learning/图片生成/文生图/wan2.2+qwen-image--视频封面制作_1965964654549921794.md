---
key: 图片生成/文生图/wan2.2+qwen-image--视频封面制作_1965964654549921794.json
name: wan2.2+qwen-image--视频封面制作_1965964654549921794
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2+qwen-image--视频封面制作_1965964654549921794.json
hash: c8a84f53d65c4238
coverage: 0.643836
learned_at: 2026-10-10 20:59:27
nodes: [JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, LayerUtility: PurgeVRAM, JjkText, CLIPLoader, JjkText, EmptySD3LatentImage, LimitNumber, Note, EmptySD3LatentImage, LoadImage, PrimitiveInt, TextCombinerTwo, TextCombinerSix, TextCombinerTwo, TextCombinerTwo, JjkText, TextCombinerTwo, TextCombinerTwo, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, VAELoader, CLIPLoader, VAEDecode, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, RH_LLMAPI_NODE, ImpactSwitch, ModelSamplingAuraFlow, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, LayerUtility: PurgeVRAM V2, UNETLoader, easy showAnything, TextCombinerSix, TextCombinerSix, SeedVR2, RH_LLMAPI_NODE, JjkText, easy showAnything, easy showAnything, CLIPTextEncode, UNETLoader, JjkText, JjkText, PreviewImage, KSampler, SaveImage, SeedVR2BlockSwap, SaveImage, SaveImage, JjkText, VAEDecode, KSampler, EmptySD3LatentImage, VAELoader, VAEDecode, VAEEncode, easy showAnything, KSampler, easy seed, JjkText, JjkText]
patterns: [image_to_image]
missing: [LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, easy seed]
parameters: {"cfg": 3.5, "denoise": 0.8500000000000002, "sampler_name": "euler", "scheduler": "normal", "seed": 756467682942260, "steps": 20}
discoveries: [次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/wan2.2+qwen-image--视频封面制作_1965964654549921794.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2+qwen-image--视频封面制作_1965964654549921794.json`

## 结构

**节点**（73 个）：
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `LayerUtility: PurgeVRAM`
- `JjkText`
- `CLIPLoader`
- `JjkText`
- `EmptySD3LatentImage`
- `LimitNumber`
- `Note`
- `EmptySD3LatentImage`
- `LoadImage`
- `PrimitiveInt`
- `TextCombinerTwo`
- `TextCombinerSix`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `JjkText`
- `TextCombinerTwo`
- `TextCombinerTwo`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPLoader`
- `VAEDecode`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `LayerUtility: PurgeVRAM V2`
- `UNETLoader`
- `easy showAnything`
- `TextCombinerSix`
- `TextCombinerSix`
- `SeedVR2`
- `RH_LLMAPI_NODE`
- `JjkText`
- `easy showAnything`
- `easy showAnything`
- `CLIPTextEncode`
- `UNETLoader`
- `JjkText`
- `JjkText`
- `PreviewImage`
- `KSampler`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SaveImage`
- `SaveImage`
- `JjkText`
- `VAEDecode`
- `KSampler`
- `EmptySD3LatentImage`
- `VAELoader`
- `VAEDecode`
- `VAEEncode`
- `easy showAnything`
- `KSampler`
- `easy seed`
- `JjkText`
- `JjkText`

**识别到的模式**：image_to_image

## 关键参数

- `cfg` = `3.5`
- `denoise` = `0.8500000000000002`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `seed` = `756467682942260`
- `steps` = `20`

## 知识

覆盖率 **64%**（47/73）

**有卡**：`JjkText`、`LayerUtility: PurgeVRAM`、`CLIPLoader`、`EmptySD3LatentImage`、`LimitNumber`、`Note`、`LoadImage`、`PrimitiveInt`、`TextCombinerTwo`、`TextCombinerSix`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAELoader`、`VAEDecode`、`UNETLoader`、`RH_LLMAPI_NODE`、`ImpactSwitch`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM V2`、`easy showAnything`、`SeedVR2`

**缺卡**（3）：`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM V2`、`easy seed`

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
