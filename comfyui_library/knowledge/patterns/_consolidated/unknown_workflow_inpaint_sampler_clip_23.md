---
name: unknown_workflow_inpaint_sampler_clip_23
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.899625
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GrowMaskWithBlur, ImageConcanate, ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/生图-图换装手动遮罩-flux_fill_nunchaku_1983512677819588609.json, 图片生成/图生图/生图-图换装自动遮罩-flux_fill_nunchaku_1972659750909485057.json, 图片生成/图生图/省心，不用画遮罩。换装_1907723273931792385.json, 平台全量/FLXU redux 换装【半自动FP16】_1898656980213682178.json, 平台全量/FLXU_redux_换装【全自动FP16】_1898653091645083650.json, 平台全量/完美复杂花纹换装换成品_1915325506273873921.json, 平台全量/换装换产品电商工作流（Aiwood原创，我改了全自动部分）_1860970792065613826.json, 平台全量/龙明换装换产品_1928677889284194305.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/生图-图换装手动遮罩-flux_fill_nunchaku_1983512677819588609.json、图片生成/图生图/生图-图换装自动遮罩-flux_fill_nunchaku_1972659750909485057.json、图片生成/图生图/省心，不用画遮罩。换装_1907723273931792385.json、平台全量/FLXU redux 换装【半自动FP16】_1898656980213682178.json、平台全量/FLXU_redux_换装【全自动FP16】_1898653091645083650.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 7/8 个有
- `EmptyImage` —— 6/8 个有
- `ImageCrop+` —— 6/8 个有
- `LayerMask: MaskPreview` —— 6/8 个有
- `UNETLoader` —— 6/8 个有
- `LayerMask: SegformerB2ClothesUltra` —— 4/8 个有
- `FaceDetailer` —— 3/8 个有
- `SAMLoader` —— 3/8 个有
- `UltralyticsDetectorProvider` —— 3/8 个有
- `GetImageSizeAndCount` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `InpaintExtendOutpaint` —— 2/8 个有
- `InpaintResize` —— 2/8 个有
- `Int` —— 2/8 个有
- `LayerUtility: ColorImage` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `MaskPreview+` —— 2/8 个有
- `NunchakuFluxDiTLoader` —— 2/8 个有
- `CR Upscale Image` —— 1/8 个有
- `ImageResizeKJ` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 50 | 8 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 0.1 - 1 | 8 | 50% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 50，8 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，8 个样本，取值分散，一致性仅 50%
