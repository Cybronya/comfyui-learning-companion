---
key: 图片生成/图生图/ACE+F.2_万物迁移_写实人物_动漫角色_物品迁移进新图_2097504995510935553.json
name: ACE+F.2_万物迁移_写实人物_动漫角色_物品迁移进新图_2097504995510935553
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/ACE+F.2_万物迁移_写实人物_动漫角色_物品迁移进新图_2097504995510935553.json
hash: 6f1e138fd8814fd8
coverage: 0.733333
learned_at: 2026-10-21 00:38:36
nodes: [VAELoader, DualCLIPLoader, ReferenceLatent, ReferenceLatent, CLIPLoader, VAELoader, UNETLoader, Int, Image Comparer (rgthree), VAEDecode, SaveImage, ConditioningZeroOut, FluxGuidance, UNETLoader, CLIPTextEncode, Note, InpaintModelConditioning, KSampler, FastCanvas, FastCanvasTool, PreviewImage, easy imageColorMatch, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Fast Groups Bypasser (rgthree), SaveImage, Any Switch (rgthree), Note, Int, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, VAEDecode, ImageCrop, KSampler, LoadImage, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, PreviewImage, PreviewImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), easy imageConcat, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, VAEEncode, StyleModelApply, CLIPVisionEncode, CLIPVisionLoader, easy makeImageForICLora, StyleModelLoader, PreviewImage, RHHiddenNodes, ShowText|pysssss, LoraLoaderModelOnly, Any Switch (rgthree), CFGNorm, RMBG]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 595111498623711, "steps": 20}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/ACE+F.2_万物迁移_写实人物_动漫角色_物品迁移进新图_2097504995510935553.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/ACE+F.2_万物迁移_写实人物_动漫角色_物品迁移进新图_2097504995510935553.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `VAELoader`
- `DualCLIPLoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `Int`
- `Image Comparer (rgthree)`
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
- `easy imageConcat`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `VAEEncode` ★核心
- `StyleModelApply`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `easy makeImageForICLora`
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

- `seed` = `595111498623711`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **73%**（44/60）

**有卡**：`VAELoader`、`DualCLIPLoader`、`ReferenceLatent`、`CLIPLoader`、`UNETLoader`、`Int`、`VAEDecode`、`SaveImage`、`ConditioningZeroOut`、`FluxGuidance`、`CLIPTextEncode`、`InpaintModelConditioning`、`KSampler`、`FastCanvas`、`FastCanvasTool`、`easy imageColorMatch`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCrop`、`LayerMask: MaskPreview`、`easy imageConcat`、`VAEEncode`、`StyleModelApply`、`CLIPVisionEncode`、`CLIPVisionLoader`、`easy makeImageForICLora`、`StyleModelLoader`、`RHHiddenNodes`、`LoraLoaderModelOnly`、`CFGNorm`、`RMBG`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
