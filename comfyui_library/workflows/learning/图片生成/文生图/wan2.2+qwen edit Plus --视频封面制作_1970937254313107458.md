---
key: 图片生成/文生图/wan2.2+qwen edit Plus --视频封面制作_1970937254313107458.json
name: wan2.2+qwen edit Plus --视频封面制作_1970937254313107458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2+qwen edit Plus --视频封面制作_1970937254313107458.json
hash: d070d9645013bf7d
coverage: 0.719298
learned_at: 2026-10-15 22:27:57
nodes: [EmptySD3LatentImage, LimitNumber, Note, EmptySD3LatentImage, LoadImage, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, VAELoader, CLIPLoader, VAEDecode, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, ImpactSwitch, CLIPTextEncode, CLIPTextEncode, LayerUtility: PurgeVRAM V2, UNETLoader, PreviewImage, KSampler, SaveImage, KSampler, EmptySD3LatentImage, TextCombinerSix, JjkText, JjkText, easy showAnything, TextCombinerTwo, JjkText, JjkText, JjkText, RH_LLMAPI_NODE, TextCombinerTwo, CLIPLoader, VAELoader, ConditioningZeroOut, Image Comparer (rgthree), ImageConcanate, SaveImage, VAEDecode, Note, PrimitiveInt, UNETLoader, JjkText, TextEncodeQwenImageEditPlus_lrzjason, VAEDecode, SaveImage, easy showAnything, JjkText, JjkText, easy seed, TextCombinerSix, KSampler]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 718236195075323, "steps": 40}
---

# 图片生成/文生图/wan2.2+qwen edit Plus --视频封面制作_1970937254313107458.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2+qwen edit Plus --视频封面制作_1970937254313107458.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `EmptySD3LatentImage`
- `LimitNumber`
- `Note`
- `EmptySD3LatentImage`
- `LoadImage`
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
- `ImpactSwitch`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM V2`
- `UNETLoader` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `SaveImage`
- `KSampler` ★核心
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
- `VAEDecode` ★核心
- `Note`
- `PrimitiveInt`
- `UNETLoader` ★核心
- `JjkText`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `VAEDecode` ★核心
- `SaveImage`
- `easy showAnything`
- `JjkText`
- `JjkText`
- `easy seed`
- `TextCombinerSix`
- `KSampler` ★核心

## 关键参数

- `seed` = `718236195075323`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **72%**（41/57）

**有卡**：`EmptySD3LatentImage`、`LimitNumber`、`LoadImage`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`UNETLoader`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM V2`、`KSampler`、`SaveImage`、`TextCombinerSix`、`TextCombinerTwo`、`RH_LLMAPI_NODE`、`ConditioningZeroOut`、`ImageConcanate`、`TextEncodeQwenImageEditPlus_lrzjason`、`easy seed`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
