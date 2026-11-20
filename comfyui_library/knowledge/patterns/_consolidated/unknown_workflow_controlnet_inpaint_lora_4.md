---
name: unknown_workflow_controlnet_inpaint_lora_4
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.845
common_nodes: [AIO_Preprocessor, AddMask, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, CutForInpaint, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, Get Image Size, ImageAndMaskPreview, ImageConcanate, ImageCrop+, ImageScale, ImageToMask, InpaintModelConditioning, Int Literal, KSampler, LayerColor: Brightness & Contrast, LayerMask: SegformerClothesPipelineLoader, LayerMask: SegformerUltraV2, LayerUtility: ColorImage V2, LayerUtility: CropByMask V2, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskToImage, PreviewBridge, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, SubtractMask, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/fluxfill强势换装lora杜绝口头最强_1971935747785879554.json, 平台全量/最佳版换装流_1915301020816048130.json, 平台全量/顶级换装流_1921436899473555458.json, 平台全量/顶级换装流_1971507911245643778.json, 平台全量/顶级换装流_1985629605317025793.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_4

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/fluxfill强势换装lora杜绝口头最强_1971935747785879554.json、平台全量/最佳版换装流_1915301020816048130.json、平台全量/顶级换装流_1921436899473555458.json、平台全量/顶级换装流_1971507911245643778.json、平台全量/顶级换装流_1985629605317025793.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `AIO_Preprocessor`
- `AddMask`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CutForInpaint`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `Get Image Size`
- `ImageAndMaskPreview`
- `ImageConcanate`
- `ImageCrop+`
- `ImageScale`
- `ImageToMask`
- `InpaintModelConditioning`
- `Int Literal`
- `KSampler`
- `LayerColor: Brightness & Contrast`
- `LayerMask: SegformerClothesPipelineLoader`
- `LayerMask: SegformerUltraV2`
- `LayerUtility: ColorImage V2`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskToImage`
- `PreviewBridge`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `SubtractMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadFlorence2Model` —— 4/5 个有
- `Florence2Run` —— 4/5 个有
- `GetImageSize` —— 4/5 个有
- `easy mathInt` —— 4/5 个有
- `RHHiddenNodes` —— 3/5 个有
- `BlendInpaint` —— 2/5 个有
- `LayerUtility: TextJoin` —— 2/5 个有
- `CM_IntBinaryOperation` —— 1/5 个有
- `CM_NumberToInt` —— 1/5 个有
- `CR Image Input Switch` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GrowMask` —— 1/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `Image Rotate` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImageMaskSwitch` —— 1/5 个有
- `InspyrenetRembg` —— 1/5 个有
- `IsMaskEmpty` —— 1/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/5 个有
- `LayerUtility: ColorPicker` —— 1/5 个有
- `MaskSmooth+` —— 1/5 个有
- `ModelSamplingFlux` —— 1/5 个有
- `NunchakuFluxDiTLoader` —— 1/5 个有
- `NunchakuFluxLoraLoader` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `RepeatLatentBatch` —— 1/5 个有
- `SetUnionControlNetType` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy compare` —— 1/5 个有
- `easy imageSize` —— 1/5 个有
- `easy imageSizeByLongerSide` —— 1/5 个有
- `easy positive` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 100 | 5 | 21% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| ControlNet 权重 | 1 | 0.6 - 1 | 5 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 100，5 个样本，取值分散，一致性仅 21%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 0.6 - 1，5 个样本，取值集中（一致性 82%）
- 风险：采样步数 观测到 100，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
