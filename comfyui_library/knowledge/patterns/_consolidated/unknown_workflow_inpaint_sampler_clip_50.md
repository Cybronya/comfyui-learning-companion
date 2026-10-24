---
name: unknown_workflow_inpaint_sampler_clip_50
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.925333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintResize, InpaintStitch, KSampler, LayerMask: MaskByColor, LayerMask: MediapipeFacialSegment, LayerMask: PersonMaskUltra V2, LoadImage, Mask Gaussian Region, MaskComposite, MaskToImage, SaveImage, SmoothMask, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/人像面部精修磨皮_1895022720600440834.json, 图片生成/图生图/拒绝“塑料感”假脸！真正保留皮肤质感的高级磨皮工作流_1991715361710092290.json, 图片生成/图生图/高级磨皮_2085992749328850945.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_50

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/人像面部精修磨皮_1895022720600440834.json、图片生成/图生图/拒绝“塑料感”假脸！真正保留皮肤质感的高级磨皮工作流_1991715361710092290.json、图片生成/图生图/高级磨皮_2085992749328850945.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintResize`
- `InpaintStitch`
- `KSampler`
- `LayerMask: MaskByColor`
- `LayerMask: MediapipeFacialSegment`
- `LayerMask: PersonMaskUltra V2`
- `LoadImage`
- `Mask Gaussian Region`
- `MaskComposite`
- `MaskToImage`
- `SaveImage`
- `SmoothMask`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DisplayAny` —— 2/3 个有
- `Get Image Size` —— 2/3 个有
- `SimpleComparison+` —— 2/3 个有
- `SimpleCondition+` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `SimpleMathInt+` —— 2/3 个有
- `Switch any [Crystools]` —— 2/3 个有
- `ArgosTranslateTextNode` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `workflow>获取图像尺寸` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 0.2 | 0.2 - 0.4 | 3 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 0.2，观测区间 0.2 - 0.4，3 个样本
