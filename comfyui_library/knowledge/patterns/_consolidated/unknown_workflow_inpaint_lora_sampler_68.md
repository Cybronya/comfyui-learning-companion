---
name: unknown_workflow_inpaint_lora_sampler_68
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.877333
common_nodes: [AdvancedVisionLoader, CLIPTextEncode, CLIPVisionEncode, ConstrainImage|pysssss, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageCrop+, ImageResize+, ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LayerMask: MaskGrow, LayerMask: SegformerB2ClothesUltra, LayerUtility: ColorImage, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: PurgeVRAM, LoadImage, LoraLoader, LoraLoaderModelOnly, Mask Fill Holes, MaskToImage, ReduxAdvanced, SaveImage, StyleModelApply, StyleModelLoader, UnetLoaderGGUF, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [平台全量/BBN_1965585844071448578.json, 平台全量/redux换装-设计专用_1978436526315032577.json, 平台全量/换装换模特_1933721762905677825.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_68

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/BBN_1965585844071448578.json、平台全量/redux换装-设计专用_1978436526315032577.json、平台全量/换装换模特_1933721762905677825.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `AdvancedVisionLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `ConstrainImage|pysssss`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageCrop+`
- `ImageResize+`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: ColorImage`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoader`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskToImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `KSamplerAdvanced` —— 2/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/3 个有
- `MaskComposite` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `Bounded Image Crop with Mask` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `ImageAndMaskPreview` —— 1/3 个有
- `ImageStitch` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `RH_Captioner_Pro` —— 1/3 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/3 个有
- `RemoveAlphaChannel` —— 1/3 个有
- `TutuGeminiAPI` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 25 | 1 - 25 | 3 | 33% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 25，观测区间 1 - 25，3 个样本，取值分散，一致性仅 33%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
- 风险：Prompt 约束强度(CFG) 观测到 25，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
