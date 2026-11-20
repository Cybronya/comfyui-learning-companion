---
name: unknown_workflow_inpaint_sampler_clip_34
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8635
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, GrowMask, Image Comparer (rgthree), ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintResize, InpaintStitch, KSampler, LayerMask: MediapipeFacialSegment, LayerMask: PersonMaskUltra V2, LoadImage, Mask Gaussian Region, MaskComposite, MaskPreview+, MaskToImage, PreviewImage, SaveImage, SmoothMask, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/人像摄影高级修图 皮肤护理｜光滑皮肤_1937338401832255489.json, 图片生成/图生图/人像无损磨皮_2050469512079785986.json, 图片生成/图生图/提升皮肤质感｜提升皮肤质感_1946796235267432450.json, 图片生成/图生图/高级皮肤修复工作流_1919949043512836097.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/人像摄影高级修图 皮肤护理｜光滑皮肤_1937338401832255489.json、图片生成/图生图/人像无损磨皮_2050469512079785986.json、图片生成/图生图/提升皮肤质感｜提升皮肤质感_1946796235267432450.json、图片生成/图生图/高级皮肤修复工作流_1919949043512836097.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintResize`
- `InpaintStitch`
- `KSampler`
- `LayerMask: MediapipeFacialSegment`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `Mask Gaussian Region`
- `MaskComposite`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `SmoothMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 3/4 个有
- `ConstrainImage|pysssss` —— 1/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 4 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 0.2 | 0.2 - 0.36 | 4 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，4 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 0.2，观测区间 0.2 - 0.36，4 个样本
