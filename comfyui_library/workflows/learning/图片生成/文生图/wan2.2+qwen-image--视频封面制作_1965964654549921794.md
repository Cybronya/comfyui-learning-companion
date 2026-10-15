---
key: 图片生成/文生图/wan2.2+qwen-image--视频封面制作_1965964654549921794.json
name: wan2.2+qwen-image--视频封面制作_1965964654549921794
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2+qwen-image--视频封面制作_1965964654549921794.json
hash: c8a84f53d65c4238
coverage: 0.684932
learned_at: 2026-10-15 22:27:58
nodes: [JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, LayerUtility: PurgeVRAM, JjkText, CLIPLoader, JjkText, EmptySD3LatentImage, LimitNumber, Note, EmptySD3LatentImage, LoadImage, PrimitiveInt, TextCombinerTwo, TextCombinerSix, TextCombinerTwo, TextCombinerTwo, JjkText, TextCombinerTwo, TextCombinerTwo, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, VAELoader, CLIPLoader, VAEDecode, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, RH_LLMAPI_NODE, ImpactSwitch, ModelSamplingAuraFlow, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, LayerUtility: PurgeVRAM V2, UNETLoader, easy showAnything, TextCombinerSix, TextCombinerSix, SeedVR2, RH_LLMAPI_NODE, JjkText, easy showAnything, easy showAnything, CLIPTextEncode, UNETLoader, JjkText, JjkText, PreviewImage, KSampler, SaveImage, SeedVR2BlockSwap, SaveImage, SaveImage, JjkText, VAEDecode, KSampler, EmptySD3LatentImage, VAELoader, VAEDecode, VAEEncode, easy showAnything, KSampler, easy seed, JjkText, JjkText]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3.5, "denoise": 0.8500000000000002, "sampler_name": "euler", "scheduler": "normal", "seed": 756467682942260, "steps": 20}
---

# 图片生成/文生图/wan2.2+qwen-image--视频封面制作_1965964654549921794.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2+qwen-image--视频封面制作_1965964654549921794.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAELoader`
- `CLIPLoader`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `ImpactSwitch`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `UNETLoader` ★核心
- `easy showAnything`
- `TextCombinerSix`
- `TextCombinerSix`
- `SeedVR2`
- `RH_LLMAPI_NODE`
- `JjkText`
- `easy showAnything`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `JjkText`
- `JjkText`
- `PreviewImage`
- `KSampler` ★核心
- `SaveImage`
- `SeedVR2BlockSwap`
- `SaveImage`
- `SaveImage`
- `JjkText`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `VAELoader`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `easy showAnything`
- `KSampler` ★核心
- `easy seed`
- `JjkText`
- `JjkText`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `756467682942260`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.8500000000000002`

## 知识

覆盖率 **68%**（50/73）

**有卡**：`LayerUtility: PurgeVRAM`、`CLIPLoader`、`EmptySD3LatentImage`、`LimitNumber`、`LoadImage`、`TextCombinerTwo`、`TextCombinerSix`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAELoader`、`VAEDecode`、`UNETLoader`、`RH_LLMAPI_NODE`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM V2`、`SeedVR2`、`KSampler`、`SaveImage`、`SeedVR2BlockSwap`、`VAEEncode`、`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
