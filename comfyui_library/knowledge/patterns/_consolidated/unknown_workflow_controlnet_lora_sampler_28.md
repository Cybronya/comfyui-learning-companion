---
name: unknown_workflow_controlnet_lora_sampler_28
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.828
common_nodes: [Anything Everywhere3, ApplyInstantID, ApplyPulid, BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, BatchPromptSchedule, CLIPTextEncode, CR Apply LoRA Stack, CR Simple Prompt List, CR Simple Prompt List Keyframes, CheckpointLoaderSimple, ControlNetLoader, EmptyLatentImage, FreeU_V2, GrowMask, Image Overlay, InstantIDFaceAnalysis, InstantIDModelLoader, InvertMask, KSampler (Efficient), LoadImage, PreviewImage, PulidEvaClipLoader, PulidInsightFaceLoader, PulidModelLoader, SDXLPromptStyler, SaveImage, Seed Everywhere, ShowText|pysssss, StyleAlignedBatchAlign, easy loraStack]
problems: []
missing: []
members: [平台全量/欧洲杯贴纸_1815701532028596226.json, 平台全量/贴纸人像_1831516020925480962.json, 平台全量/迷你版人物贴纸+名字_1847084126414442497.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_28

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/欧洲杯贴纸_1815701532028596226.json、平台全量/贴纸人像_1831516020925480962.json、平台全量/迷你版人物贴纸+名字_1847084126414442497.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere3`
- `ApplyInstantID`
- `ApplyPulid`
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `BatchPromptSchedule`
- `CLIPTextEncode`
- `CR Apply LoRA Stack`
- `CR Simple Prompt List`
- `CR Simple Prompt List Keyframes`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `EmptyLatentImage`
- `FreeU_V2`
- `GrowMask`
- `Image Overlay`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `InvertMask`
- `KSampler (Efficient)`
- `LoadImage`
- `PreviewImage`
- `PulidEvaClipLoader`
- `PulidInsightFaceLoader`
- `PulidModelLoader`
- `SDXLPromptStyler`
- `SaveImage`
- `Seed Everywhere`
- `ShowText|pysssss`
- `StyleAlignedBatchAlign`
- `easy loraStack`

**可变部分**（部分 workflow 才有）：
- `DF_Image_scale_to_side` —— 2/3 个有
- `DF_Integer` —— 2/3 个有
- `FaceRestoreCFWithModel` —— 2/3 个有
- `FaceRestoreModelLoader` —— 2/3 个有
- `Image Rembg (Remove Background)` —— 2/3 个有
- `ImageScaleToMegapixels` —— 2/3 个有
- `ImageUpscaleWithModel` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `WD14Tagger|pysssss` —— 2/3 个有
- `CR Image Grid Panel` —— 1/3 个有
- `DeepTranslatorTextNode` —— 1/3 个有
- `EG_WB_KSH` —— 1/3 个有
- `ImageBatchToList` —— 1/3 个有
- `ImageCompositeAbsolute` —— 1/3 个有
- `ImageFromBatch+` —— 1/3 个有
- `ImageListToBatch_` —— 1/3 个有
- `ImpactMakeImageBatch` —— 1/3 个有
- `Joy_caption` —— 1/3 个有
- `Joy_caption_load` —— 1/3 个有
- `LatentUpscale` —— 1/3 个有
- `LayerUtility: ColorImage V2` —— 1/3 个有
- `LayerUtility: ImageBlendAdvance` —— 1/3 个有
- `MaskFromBatch+` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `MaskToImage` —— 1/3 个有
- `StringConstant` —— 1/3 个有
- `TextImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 3 | 82% |
| Prompt 约束强度(CFG) | 2.5 | 2 - 2.5 | 3 | 90% |
| 采样算法 | dpmpp_sde | - | 3 | 67% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 0.6 - 1 | 3 | 78% |
| 宽度 | 1024 | 768 - 1024 | 3 | 87% |
| 高度 | 1024 | 768 - 1024 | 3 | 87% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2 - 2.5，3 个样本，取值集中（一致性 90%）
- 采样算法 最常用 dpmpp_sde，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，3 个样本
- 宽度 中位数 1024，观测区间 768 - 1024，3 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 768 - 1024，3 个样本，取值集中（一致性 87%）
