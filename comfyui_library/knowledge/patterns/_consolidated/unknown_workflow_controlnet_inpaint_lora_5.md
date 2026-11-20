---
name: unknown_workflow_controlnet_inpaint_lora_5
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9148
common_nodes: [AIO_Preprocessor, CLIPTextEncodeFlux, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, GrowMaskWithBlur, InpaintModelConditioning, KSampler, LayerMask: SegformerB2ClothesUltra, LayerUtility: CropByMask V2, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LoraLoaderModelOnly, MaskComposite, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/HT洗稿-宽度790_1930887670950461441.json, 平台全量/PDD800X800专属logo_1932358095559979010.json, 平台全量/单图换头—特殊角度只换头_1945378074294931457.json, 平台全量/原-普通角度换模特—带肢体皮肤_1948290427295268865.json, 平台全量/普通角度换模特—带肢体皮肤_1940341832737755138.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_lora_5

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/HT洗稿-宽度790_1930887670950461441.json、平台全量/PDD800X800专属logo_1932358095559979010.json、平台全量/单图换头—特殊角度只换头_1945378074294931457.json、平台全量/原-普通角度换模特—带肢体皮肤_1948290427295268865.json、平台全量/普通角度换模特—带肢体皮肤_1940341832737755138.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `GrowMaskWithBlur`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: RestoreCropBox`
- `LoraLoaderModelOnly`
- `MaskComposite`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 4/5 个有
- `Anything Everywhere3` —— 4/5 个有
- `ImageCompositeMasked` —— 4/5 个有
- `InvertMask` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `Image Overlay` —— 3/5 个有
- `ImageToMask` —— 3/5 个有
- `CR Overlay Transparent Image` —— 2/5 个有
- `GetImageSize` —— 2/5 个有
- `LayerUtility: ColorImage V2` —— 2/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `ImageScale` —— 1/5 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/5 个有
- `MaskPreview+` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RHBatchImages:` —— 1/5 个有
- `RHExtractImage` —— 1/5 个有
- `RHUploadZip` —— 1/5 个有
- `easy forLoopEnd` —— 1/5 个有
- `easy forLoopStart` —— 1/5 个有
- `easy imageCount` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | 0.5 - 0.5 | 5 | 100% |
| 采样步数 | 8 | 8 - 10 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 0.85 | 0.5 - 0.85 | 5 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.5，观测区间 0.5 - 0.5，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 10，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 0.85，观测区间 0.5 - 0.85，5 个样本，取值集中（一致性 82%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
