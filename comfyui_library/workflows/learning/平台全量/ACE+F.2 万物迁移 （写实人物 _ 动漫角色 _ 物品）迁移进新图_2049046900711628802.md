---
key: 平台全量/ACE+F.2 万物迁移 （写实人物 _ 动漫角色 _ 物品）迁移进新图_2049046900711628802.json
name: ACE+F.2 万物迁移 （写实人物 _ 动漫角色 _ 物品）迁移进新图_2049046900711628802
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/ACE+F.2 万物迁移 （写实人物 _ 动漫角色 _ 物品）迁移进新图_2049046900711628802.json
hash: c0133b2cc09961eb
coverage: 0.742424
learned_at: 2026-11-14 00:14:46
nodes: [VAELoader, DualCLIPLoader, ReferenceLatent, ReferenceLatent, CLIPLoader, VAELoader, UNETLoader, Int, Image Comparer (rgthree), LoadImage, LoadImage, VAEDecode, SaveImage, ConditioningZeroOut, FluxGuidance, UNETLoader, CLIPTextEncode, Note, InpaintModelConditioning, KSampler, FastCanvas, FastCanvasTool, PreviewImage, easy imageColorMatch, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Fast Groups Bypasser (rgthree), SaveImage, Any Switch (rgthree), Note, LoadImage, LoadImage, Int, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, VAEDecode, ImageCrop, KSampler, LoadImage, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, PreviewImage, PreviewImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, easy imageConcat, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, VAEEncode, StyleModelApply, CLIPVisionEncode, CLIPVisionLoader, easy makeImageForICLora, MarkdownNote, StyleModelLoader, PreviewImage, RHHiddenNodes, ShowText|pysssss, LoraLoaderModelOnly, Any Switch (rgthree), CFGNorm, RMBG]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 469633162603980, "steps": 20}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/ACE+F.2 万物迁移 （写实人物 _ 动漫角色 _ 物品）迁移进新图_2049046900711628802.json

> 来源文件 `comfyui_library/workflows/平台全量/ACE+F.2 万物迁移 （写实人物 _ 动漫角色 _ 物品）迁移进新图_2049046900711628802.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `VAELoader`
- `DualCLIPLoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `Int`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `FluxGuidance`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `FastCanvas`
- `FastCanvasTool`
- `PreviewImage`
- `easy imageColorMatch`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `Any Switch (rgthree)`
- `Note`
- `LoadImage`
- `LoadImage`
- `Int`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageCrop`
- `KSampler` ★核心
- `LoadImage`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `easy imageConcat`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `VAEEncode` ★核心
- `StyleModelApply`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `easy makeImageForICLora`
- `MarkdownNote`
- `StyleModelLoader`
- `PreviewImage`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `LoraLoaderModelOnly` ★核心
- `Any Switch (rgthree)`
- `CFGNorm`
- `RMBG`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `469633162603980`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **74%**（49/66）

**有卡**：`VAELoader`、`DualCLIPLoader`、`ReferenceLatent`、`CLIPLoader`、`UNETLoader`、`Int`、`LoadImage`、`VAEDecode`、`SaveImage`、`ConditioningZeroOut`、`FluxGuidance`、`CLIPTextEncode`、`InpaintModelConditioning`、`KSampler`、`FastCanvas`、`FastCanvasTool`、`easy imageColorMatch`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCrop`、`LayerMask: MaskPreview`、`easy imageConcat`、`VAEEncode`、`StyleModelApply`、`CLIPVisionEncode`、`CLIPVisionLoader`、`easy makeImageForICLora`、`StyleModelLoader`、`RHHiddenNodes`、`LoraLoaderModelOnly`、`CFGNorm`、`RMBG`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
