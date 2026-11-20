---
key: 平台全量/sd2.0平替）贝尔尼尼Bernini多功能视频编辑4步加速精简流plus版动作迁移_角色替换_去水印字幕_风格转换-优化2_2063139172780691458.json
name: sd2.0平替）贝尔尼尼Bernini多功能视频编辑4步加速精简流plus版动作迁移_角色替换_去水印字幕_风格转换-优化2_2063139172780691458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/sd2.0平替）贝尔尼尼Bernini多功能视频编辑4步加速精简流plus版动作迁移_角色替换_去水印字幕_风格转换-优化2_2063139172780691458.json
hash: 3cd4b2b45f38eabe
coverage: 0.397849
learned_at: 2026-11-14 01:17:15
nodes: [GetNode, MarkdownNote, LoadImage, SetNode, easy convertAnything, SetNode, SetNode, SetNode, SetNode, MarkdownNote, SetNode, VAELoader, SetNode, CLIPLoader, UNETLoader, UNETLoader, TTResolutionSelector, GetNode, MathExpression|pysssss, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MarkdownNote, SetNode, GetNode, Fast Groups Bypasser (rgthree), GetNode, SetNode, GetNode, Text Concatenate, SetNode, easy seed, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, CLIPTextEncode, VAEDecode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, easy imageScaleDownToSize, GetNode, ImageFromBatch, PreviewImage, CR Text, easy int, CR Text, MarkdownNote, MarkdownNote, Note, VHS_LoadVideo, GetNode, GetNode, GetNode, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, ImageConcatMulti, LayerUtility: ImageScaleByAspectRatio V2, Note, Note, VHS_VideoInfoLoaded, easy showAnything, easy showAnything, BatchImagesNode, PreviewImage, MarkdownNote, VHS_VideoCombine, LoadImage, CR Text, PathchSageAttentionKJ, SetNode, PathchSageAttentionKJ, SetNode, VHS_VideoCombine, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, easy int, BerniniConditioning, KSamplerAdvanced, KSamplerAdvanced, Fast Groups Muter (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 平台全量/sd2.0平替）贝尔尼尼Bernini多功能视频编辑4步加速精简流plus版动作迁移_角色替换_去水印字幕_风格转换-优化2_2063139172780691458.json

> 来源文件 `comfyui_library/workflows/平台全量/sd2.0平替）贝尔尼尼Bernini多功能视频编辑4步加速精简流plus版动作迁移_角色替换_去水印字幕_风格转换-优化2_2063139172780691458.json`

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
- `Fast Groups Bypasser (rgthree)`
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
- `SetNode`
- `easy imageScaleDownToSize`
- `GetNode`
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `Note`
- `VHS_VideoInfoLoaded`
- `easy showAnything`
- `easy showAnything`
- `BatchImagesNode`
- `PreviewImage`
- `MarkdownNote`
- `VHS_VideoCombine`
- `LoadImage`
- `CR Text`
- `PathchSageAttentionKJ`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `easy int`
- `BerniniConditioning`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Fast Groups Muter (rgthree)`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **40%**（37/93）

**有卡**：`LoadImage`、`easy convertAnything`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`TTResolutionSelector`、`MathExpression|pysssss`、`Text Concatenate`、`easy seed`、`CLIPTextEncode`、`VAEDecode`、`easy imageScaleDownToSize`、`ImageFromBatch`、`CR Text`、`easy int`、`VHS_LoadVideo`、`ImageConcatMulti`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfoLoaded`、`BatchImagesNode`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`BerniniConditioning`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、easy seed
