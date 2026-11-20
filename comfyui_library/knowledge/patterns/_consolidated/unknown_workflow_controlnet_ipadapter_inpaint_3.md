---
name: unknown_workflow_controlnet_ipadapter_inpaint_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.816
common_nodes: [Apply ControlNet Stack, Blur, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, Control Net Stacker, ControlNetApplyAdvanced, ControlNetLoader, Cut By Mask, IPAdapterFaceID, IPAdapterInsightFaceLoader, IPAdapterModelLoader, Image To Mask, Images to RGB, InpaintPreprocessor, KSampler (Efficient), LayerMask: PersonMaskUltra V2, LayerUtility: ImageShift, LoadImage, Mask Morphology, Mask To Region, MaskToImage, Paste By Mask, PreviewImage, ReActorFaceSwap, SaveImage, SetLatentNoiseMask, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/一键换模特(保留服装)_1929902235998916610.json, 图片生成/图生图/一键模特换脸（保留衣服）_1902522771056832514.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_inpaint_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键换模特(保留服装)_1929902235998916610.json、图片生成/图生图/一键模特换脸（保留衣服）_1902522771056832514.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `Apply ControlNet Stack`
- `Blur`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `Control Net Stacker`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `Cut By Mask`
- `IPAdapterFaceID`
- `IPAdapterInsightFaceLoader`
- `IPAdapterModelLoader`
- `Image To Mask`
- `Images to RGB`
- `InpaintPreprocessor`
- `KSampler (Efficient)`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageShift`
- `LoadImage`
- `Mask Morphology`
- `Mask To Region`
- `MaskToImage`
- `Paste By Mask`
- `PreviewImage`
- `ReActorFaceSwap`
- `SaveImage`
- `SetLatentNoiseMask`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| 采样步数 | 30 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 3 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.3 | - | 2 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.3，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
