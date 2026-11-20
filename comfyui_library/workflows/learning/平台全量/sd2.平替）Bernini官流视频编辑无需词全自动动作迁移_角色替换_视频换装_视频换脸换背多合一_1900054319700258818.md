---
key: 平台全量/sd2.平替）Bernini官流视频编辑无需词全自动动作迁移_角色替换_视频换装_视频换脸换背多合一_1900054319700258818.json
name: sd2.平替）Bernini官流视频编辑无需词全自动动作迁移_角色替换_视频换装_视频换脸换背多合一_1900054319700258818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/sd2.平替）Bernini官流视频编辑无需词全自动动作迁移_角色替换_视频换装_视频换脸换背多合一_1900054319700258818.json
hash: f39a80bcad2cfc99
coverage: 0.433962
learned_at: 2026-11-14 01:17:17
nodes: [SetNode, easy convertAnything, SetNode, SetNode, SetNode, SetNode, PathchSageAttentionKJ, PathchSageAttentionKJ, SetNode, UNETLoader, GetNode, MathExpression|pysssss, SetNode, GetNode, GetNode, MarkdownNote, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SeedVR2ExtraArgs, SeedVR2BlockSwap, GetNode, Note, SetNode, SetNode, VAELoader, SetNode, SetNode, CLIPLoader, GetNode, GetNode, GetNode, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, ImageConcatMulti, GetNode, GetNode, GetNode, GetNode, VAEDecode, easy seed, Note, VHS_VideoCombine, CLIPTextEncode, GetNode, SeedVR2GGUF, UNETLoader, easy int, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, easy int, CLIPTextEncode, GetNode, SetNode, PreviewImage, Fast Groups Bypasser (rgthree), MarkdownNote, Text Concatenate, CR Text, GetNode, BerniniConditioning, KSamplerAdvanced, KSamplerAdvanced, Fast Groups Muter (rgthree), SetNode, BatchImagesNode, easy imageScaleDownToSize, BerniniPromptEnhancer, SetNode, CR Text, MarkdownNote, TTResolutionSelector, MarkdownNote, LoadImage, LoadImage, MarkdownNote, easy int, GetNode, GetNode, CreateVideo, GetNode, GetNode, SetNode, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, GetNode, RHHiddenNodes, SetNode, ShowText|pysssss, RHLLMChatNode, ShowText|pysssss]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 平台全量/sd2.平替）Bernini官流视频编辑无需词全自动动作迁移_角色替换_视频换装_视频换脸换背多合一_1900054319700258818.json

> 来源文件 `comfyui_library/workflows/平台全量/sd2.平替）Bernini官流视频编辑无需词全自动动作迁移_角色替换_视频换装_视频换脸换背多合一_1900054319700258818.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
- `SetNode`
- `easy convertAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader` ★核心
- `GetNode`
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `GetNode`
- `Note`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `CLIPLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `easy seed`
- `Note`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SeedVR2GGUF`
- `UNETLoader` ★核心
- `easy int`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy int`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `Text Concatenate`
- `CR Text`
- `GetNode`
- `BerniniConditioning`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Fast Groups Muter (rgthree)`
- `SetNode`
- `BatchImagesNode`
- `easy imageScaleDownToSize`
- `BerniniPromptEnhancer`
- `SetNode`
- `CR Text`
- `MarkdownNote`
- `TTResolutionSelector`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `easy int`
- `GetNode`
- `GetNode`
- `CreateVideo`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `GetNode`
- `RHHiddenNodes`
- `SetNode`
- `ShowText|pysssss`
- `RHLLMChatNode`
- `ShowText|pysssss`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **43%**（46/106）

**有卡**：`easy convertAnything`、`PathchSageAttentionKJ`、`UNETLoader`、`MathExpression|pysssss`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`VAELoader`、`CLIPLoader`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`easy seed`、`VHS_VideoCombine`、`CLIPTextEncode`、`SeedVR2GGUF`、`easy int`、`LoraLoaderModelOnly`、`Text Concatenate`、`CR Text`、`BerniniConditioning`、`KSamplerAdvanced`、`BatchImagesNode`、`easy imageScaleDownToSize`、`BerniniPromptEnhancer`、`TTResolutionSelector`、`LoadImage`、`CreateVideo`、`VHS_LoadVideo`、`RHHiddenNodes`、`RHLLMChatNode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、easy seed
