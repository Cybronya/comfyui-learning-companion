---
name: unknown_workflow_controlnet_upscale_latent_upscale_2
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.926
common_nodes: [Anything Everywhere3, ApplyInstantID, ApplyPulid, BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, BatchPromptSchedule, CLIPTextEncode, CR Apply LoRA Stack, CR Image Grid Panel, CR Simple Prompt List, CR Simple Prompt List Keyframes, CheckpointLoaderSimple, Concat Text _O, ControlNetLoader, DF_Image_scale_to_side, DF_Integer, EmptyLatentImage, FreeU_V2, ImageCompositeAbsolute, ImageCompositeAbsoluteByContainer, ImageGenResolutionFromImage, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler (Efficient), LLava Loader Simple, LLavaSamplerSimple, LatentUpscale, LayerUtility: ColorImage V2, LayerUtility: ColorPicker, LayerUtility: ExtendCanvas, LlavaClipLoader, LoadImage, PulidEvaClipLoader, PulidInsightFaceLoader, PulidModelLoader, SDXLPromptStyler, SaveImage, Seed Everywhere, ShowText|pysssss, SimpleMath+, SimpleText, StyleAlignedBatchAlign, Text _O, Text_Image_Multiline_Zho, easy loraStack]
problems: []
missing: []
members: [图片生成/图生图/形象卡通贴纸生成_1949395306793861122.json, 图片生成/文生图/形象卡通贴纸生成_1961439298954399746.json, 图片生成/文生图/形象卡通贴纸生成_1961447394091188226.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_latent_upscale_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/形象卡通贴纸生成_1949395306793861122.json、图片生成/文生图/形象卡通贴纸生成_1961439298954399746.json、图片生成/文生图/形象卡通贴纸生成_1961447394091188226.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

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
- `CR Image Grid Panel`
- `CR Simple Prompt List`
- `CR Simple Prompt List Keyframes`
- `CheckpointLoaderSimple`
- `Concat Text _O`
- `ControlNetLoader`
- `DF_Image_scale_to_side`
- `DF_Integer`
- `EmptyLatentImage`
- `FreeU_V2`
- `ImageCompositeAbsolute`
- `ImageCompositeAbsoluteByContainer`
- `ImageGenResolutionFromImage`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler (Efficient)`
- `LLava Loader Simple`
- `LLavaSamplerSimple`
- `LatentUpscale`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ColorPicker`
- `LayerUtility: ExtendCanvas`
- `LlavaClipLoader`
- `LoadImage`
- `PulidEvaClipLoader`
- `PulidInsightFaceLoader`
- `PulidModelLoader`
- `SDXLPromptStyler`
- `SaveImage`
- `Seed Everywhere`
- `ShowText|pysssss`
- `SimpleMath+`
- `SimpleText`
- `StyleAlignedBatchAlign`
- `Text _O`
- `Text_Image_Multiline_Zho`
- `easy loraStack`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 2 | 2 - 2 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 3 | 100% |
| 宽度 | 768 | 768 - 768 | 3 | 100% |
| 高度 | 768 | 768 - 768 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 高度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
