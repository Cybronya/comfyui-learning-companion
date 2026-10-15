---
key: 图片生成/文生图/wan2.2+qwen edit Plus --视频封面制作_1970937254313107458.json
name: wan2.2+qwen edit Plus --视频封面制作_1970937254313107458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2+qwen edit Plus --视频封面制作_1970937254313107458.json
hash: d070d9645013bf7d
coverage: 0.684211
learned_at: 2026-10-10 20:59:27
nodes: [EmptySD3LatentImage, LimitNumber, Note, EmptySD3LatentImage, LoadImage, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, VAELoader, CLIPLoader, VAEDecode, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ImpactSwitch, CLIPTextEncode, CLIPTextEncode, LayerUtility: PurgeVRAM V2, UNETLoader, PreviewImage, KSampler, SaveImage, KSampler, EmptySD3LatentImage, TextCombinerSix, JjkText, JjkText, easy showAnything, TextCombinerTwo, JjkText, JjkText, JjkText, RH_LLMAPI_NODE, TextCombinerTwo, CLIPLoader, VAELoader, ConditioningZeroOut, Image Comparer (rgthree), ImageConcanate, SaveImage, VAEDecode, Note, PrimitiveInt, UNETLoader, JjkText, TextEncodeQwenImageEditPlus_lrzjason, VAEDecode, SaveImage, easy showAnything, JjkText, JjkText, easy seed, TextCombinerSix, KSampler]
patterns: []
missing: [LayerUtility: PurgeVRAM V2, easy seed]
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 718236195075323, "steps": 40}
discoveries: [次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/wan2.2+qwen edit Plus --视频封面制作_1970937254313107458.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2+qwen edit Plus --视频封面制作_1970937254313107458.json`

## 结构

**节点**（57 个）：
- `EmptySD3LatentImage`
- `LimitNumber`
- `Note`
- `EmptySD3LatentImage`
- `LoadImage`
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
- `ImpactSwitch`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `LayerUtility: PurgeVRAM V2`
- `UNETLoader`
- `PreviewImage`
- `KSampler`
- `SaveImage`
- `KSampler`
- `EmptySD3LatentImage`
- `TextCombinerSix`
- `JjkText`
- `JjkText`
- `easy showAnything`
- `TextCombinerTwo`
- `JjkText`
- `JjkText`
- `JjkText`
- `RH_LLMAPI_NODE`
- `TextCombinerTwo`
- `CLIPLoader`
- `VAELoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `SaveImage`
- `VAEDecode`
- `Note`
- `PrimitiveInt`
- `UNETLoader`
- `JjkText`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `VAEDecode`
- `SaveImage`
- `easy showAnything`
- `JjkText`
- `JjkText`
- `easy seed`
- `TextCombinerSix`
- `KSampler`

## 关键参数

- `cfg` = `4`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `seed` = `718236195075323`
- `steps` = `40`

## 知识

覆盖率 **68%**（39/57）

**有卡**：`EmptySD3LatentImage`、`LimitNumber`、`Note`、`LoadImage`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`UNETLoader`、`ImpactSwitch`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM V2`、`PreviewImage`、`KSampler`、`SaveImage`、`TextCombinerSix`、`JjkText`、`easy showAnything`、`TextCombinerTwo`、`RH_LLMAPI_NODE`

**缺卡**（2）：`LayerUtility: PurgeVRAM V2`、`easy seed`

## 学习发现

- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
