---
key: 平台全量/sd2.0平替）贝尔尼尼Bernini多功能视频编辑4步加速精简流动作迁移_角色替换_去水印字幕_风格转换-优化2_2062060975137841154.json
name: sd2.0平替）贝尔尼尼Bernini多功能视频编辑4步加速精简流动作迁移_角色替换_去水印字幕_风格转换-优化2_2062060975137841154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/sd2.0平替）贝尔尼尼Bernini多功能视频编辑4步加速精简流动作迁移_角色替换_去水印字幕_风格转换-优化2_2062060975137841154.json
hash: e5a2d184d6b7aa63
coverage: 0.397849
learned_at: 2026-11-14 01:17:15
nodes: [GetNode, MarkdownNote, LoadImage, SetNode, easy convertAnything, SetNode, SetNode, SetNode, SetNode, MarkdownNote, SetNode, VAELoader, SetNode, CLIPLoader, UNETLoader, UNETLoader, TTResolutionSelector, GetNode, MathExpression|pysssss, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MarkdownNote, SetNode, GetNode, GetNode, SetNode, GetNode, Text Concatenate, SetNode, easy seed, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, VAEDecode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy int, ImageFromBatch, PreviewImage, CR Text, easy int, CR Text, MarkdownNote, MarkdownNote, Note, VHS_LoadVideo, GetNode, GetNode, GetNode, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, ImageConcatMulti, SetNode, LayerUtility: ImageScaleByAspectRatio V2, Note, VHS_VideoInfoLoaded, easy showAnything, easy showAnything, VHS_VideoCombine, PathchSageAttentionKJ, SetNode, PathchSageAttentionKJ, SetNode, BerniniConditioning, CR Text, Fast Groups Bypasser (rgthree), Note, VHS_VideoCombine, KSamplerAdvanced, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, MarkdownNote, Fast Groups Muter (rgthree), PreviewImage, BatchImagesNode, SetNode, LoadImage, easy imageScaleDownToSize]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 平台全量/sd2.0平替）贝尔尼尼Bernini多功能视频编辑4步加速精简流动作迁移_角色替换_去水印字幕_风格转换-优化2_2062060975137841154.json

> 来源文件 `comfyui_library/workflows/平台全量/sd2.0平替）贝尔尼尼Bernini多功能视频编辑4步加速精简流动作迁移_角色替换_去水印字幕_风格转换-优化2_2062060975137841154.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
- `GetNode`
- `MarkdownNote`
- `LoadImage`
- `SetNode`
- `easy convertAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `SetNode`
- `VAELoader`
- `SetNode`
- `CLIPLoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `TTResolutionSelector`
- `GetNode`
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Text Concatenate`
- `SetNode`
- `easy seed`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy int`
- `ImageFromBatch`
- `PreviewImage`
- `CR Text`
- `easy int`
- `CR Text`
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `easy showAnything`
- `VHS_VideoCombine`
- `PathchSageAttentionKJ`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `BerniniConditioning`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `Fast Groups Muter (rgthree)`
- `PreviewImage`
- `BatchImagesNode`
- `SetNode`
- `LoadImage`
- `easy imageScaleDownToSize`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **40%**（37/93）

**有卡**：`LoadImage`、`easy convertAnything`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`TTResolutionSelector`、`MathExpression|pysssss`、`Text Concatenate`、`easy seed`、`CLIPTextEncode`、`VAEDecode`、`easy int`、`ImageFromBatch`、`CR Text`、`VHS_LoadVideo`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`BerniniConditioning`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`BatchImagesNode`、`easy imageScaleDownToSize`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、easy seed
