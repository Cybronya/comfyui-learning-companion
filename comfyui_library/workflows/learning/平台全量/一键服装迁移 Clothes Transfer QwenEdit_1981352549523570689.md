---
key: 平台全量/一键服装迁移 Clothes Transfer QwenEdit_1981352549523570689.json
name: 一键服装迁移 Clothes Transfer QwenEdit_1981352549523570689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/一键服装迁移 Clothes Transfer QwenEdit_1981352549523570689.json
hash: 8e75465efb5402aa
coverage: 0.888889
learned_at: 2026-11-14 01:28:59
nodes: [VAEEncode, TextEncodeQwenImageEditPlus, ConditioningZeroOut, LayerUtility: PurgeVRAM V2, Anything Everywhere, Anything Everywhere, VAEEncode, easy imageRemBg, SeedVR2BlockSwap, LayerUtility: PurgeVRAM V2, SeedVR2, KSampler (Efficient), CFGNorm, ModelSamplingAuraFlow, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: PurgeVRAM V2, VAELoader, CLIPLoader, UNETLoader, ConditioningZeroOut, TextEncodeQwenImageEditPlus, ImageResize+, PathchSageAttentionKJ, ModelSamplingAuraFlow, CFGNorm, LoraLoaderModelOnly, ModelSamplingAuraFlow, ConditioningZeroOut, ImageResize+, CFGNorm, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImageEdit, VAEEncode, KSampler (Efficient), ImageStitch, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, KSampler (Efficient), PreviewImage, LoadImage, LoadImage, LayerUtility: PurgeVRAM V2, SaveImage, ImageStitch, LoadImage, LoadImage, MarkdownNote, SaveImage, PreviewImage, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "sgm_uniform", "seed": 1020974164342332, "steps": 8}
---

# 平台全量/一键服装迁移 Clothes Transfer QwenEdit_1981352549523570689.json

> 来源文件 `comfyui_library/workflows/平台全量/一键服装迁移 Clothes Transfer QwenEdit_1981352549523570689.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Process → Output → Other

**节点**（54 个）：
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `ConditioningZeroOut`
- `LayerUtility: PurgeVRAM V2`
- `Anything Everywhere`
- `Anything Everywhere`
- `VAEEncode` ★核心
- `easy imageRemBg`
- `SeedVR2BlockSwap`
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2`
- `KSampler (Efficient)` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlus`
- `ImageResize+`
- `PathchSageAttentionKJ`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `ImageResize+`
- `CFGNorm`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImageEdit`
- `VAEEncode` ★核心
- `KSampler (Efficient)` ★核心
- `ImageStitch`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `KSampler (Efficient)` ★核心
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LayerUtility: PurgeVRAM V2`
- `SaveImage`
- `ImageStitch`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`

## 关键参数

- `seed` = `1020974164342332`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **89%**（48/54）

**有卡**：`VAEEncode`、`TextEncodeQwenImageEditPlus`、`ConditioningZeroOut`、`LayerUtility: PurgeVRAM V2`、`easy imageRemBg`、`SeedVR2BlockSwap`、`SeedVR2`、`KSampler (Efficient)`、`CFGNorm`、`ModelSamplingAuraFlow`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`ImageResize+`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImageEdit`、`ImageStitch`、`LoadImage`、`SaveImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、UNETLoader、CFGNorm
