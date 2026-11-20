---
key: 平台全量/方汤圆flux-2-klein高级应用V1.2_2038933428191629313.json
name: 方汤圆flux-2-klein高级应用V1.2_2038933428191629313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/方汤圆flux-2-klein高级应用V1.2_2038933428191629313.json
hash: f1275e78e302cf29
coverage: 0.777778
learned_at: 2026-11-14 02:12:26
nodes: [easy positive, TTP_text_mix, Note, TTP_text_mix, TTP_text_mix, easy positive, easy positive, easy positive, TTP_text_mix, easy positive, easy positive, TTP_text_mix, Note, easy positive, TTP_text_mix, TTP_text_mix, easy positive, easy positive, LoraLoaderModelOnly, Note, TTP_text_mix, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy positive, easy positive, easy positive, LoadImageOutput, Flux2KleinConfigPreparer_EditUtils, PreviewImage, VAEDecode, ReferenceLatent, CLIPTextEncode, Flux2KleinModelConfig_EditUtils, PrimitiveInt, LayerUtility: PurgeVRAM V2, CropWithPadInfo_EditUtils, Note, Flux2KleinOutputExtractor_EditUtils, UNETLoader, CLIPLoader, VAELoader, Flux2KleinModelConfig_EditUtils, EditTextEncode_EditUtils, Flux2KleinOutputExtractor_EditUtils, AdaptiveLongestEdge_EditUtils, ShowText|pysssss, Text Concatenate, Any Switch (rgthree), KSampler, ImpactInt, Fast Groups Muter (rgthree), easy positive, Image Save, LayerUtility: ImageReel, Image Comparer (rgthree), Image Save, JWStringMultiline, Any Switch (rgthree), LoadImage, Any Switch (rgthree), Fast Groups Muter (rgthree), PreviewImage, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 679664208963255, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/方汤圆flux-2-klein高级应用V1.2_2038933428191629313.json

> 来源文件 `comfyui_library/workflows/平台全量/方汤圆flux-2-klein高级应用V1.2_2038933428191629313.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（63 个）：
- `easy positive`
- `TTP_text_mix`
- `Note`
- `TTP_text_mix`
- `TTP_text_mix`
- `easy positive`
- `easy positive`
- `easy positive`
- `TTP_text_mix`
- `easy positive`
- `easy positive`
- `TTP_text_mix`
- `Note`
- `easy positive`
- `TTP_text_mix`
- `TTP_text_mix`
- `easy positive`
- `easy positive`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `TTP_text_mix`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `easy positive`
- `easy positive`
- `easy positive`
- `LoadImageOutput`
- `Flux2KleinConfigPreparer_EditUtils`
- `PreviewImage`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `Flux2KleinModelConfig_EditUtils`
- `PrimitiveInt`
- `LayerUtility: PurgeVRAM V2`
- `CropWithPadInfo_EditUtils`
- `Note`
- `Flux2KleinOutputExtractor_EditUtils`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Flux2KleinModelConfig_EditUtils`
- `EditTextEncode_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `AdaptiveLongestEdge_EditUtils`
- `ShowText|pysssss`
- `Text Concatenate`
- `Any Switch (rgthree)`
- `KSampler` ★核心
- `ImpactInt`
- `Fast Groups Muter (rgthree)`
- `easy positive`
- `Image Save`
- `LayerUtility: ImageReel`
- `Image Comparer (rgthree)`
- `Image Save`
- `JWStringMultiline`
- `Any Switch (rgthree)`
- `LoadImage`
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `PreviewImage`
- `SaveImage`

## 关键参数

- `seed` = `679664208963255`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（49/63）

**有卡**：`easy positive`、`TTP_text_mix`、`LoraLoaderModelOnly`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LoadImageOutput`、`Flux2KleinConfigPreparer_EditUtils`、`VAEDecode`、`ReferenceLatent`、`CLIPTextEncode`、`Flux2KleinModelConfig_EditUtils`、`LayerUtility: PurgeVRAM V2`、`CropWithPadInfo_EditUtils`、`Flux2KleinOutputExtractor_EditUtils`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EditTextEncode_EditUtils`、`AdaptiveLongestEdge_EditUtils`、`Text Concatenate`、`KSampler`、`ImpactInt`、`Image Save`、`JWStringMultiline`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
