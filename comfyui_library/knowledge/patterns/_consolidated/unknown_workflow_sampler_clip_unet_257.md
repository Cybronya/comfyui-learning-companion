---
name: unknown_workflow_sampler_clip_unet_257
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8394
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Fast Groups Bypasser (rgthree), FluxGuidance, GetImageSize, Image Comparer (rgthree), ImageScale, ImageScaleToTotalPixels, LanPaint_KSampler, LoadImage, PrimitiveFloat, ReferenceLatent, SaveImage, SetLatentNoiseMask, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Klein多图局部编辑无像素偏移_2013109962473480194.json, 图片生成/图生图/全自动商用级-换脸换头_2082030904230367234.json, 图片生成/图生图/商用级-全自动换脸换头_2072586310119944194.json, 图片生成/图生图/商用级-全自动换脸换头_2082644570055200769.json, 图片生成/图生图/商用级-全自动换脸换头_2082663416522690562.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_257

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Klein多图局部编辑无像素偏移_2013109962473480194.json、图片生成/图生图/全自动商用级-换脸换头_2082030904230367234.json、图片生成/图生图/商用级-全自动换脸换头_2072586310119944194.json、图片生成/图生图/商用级-全自动换脸换头_2082644570055200769.json、图片生成/图生图/商用级-全自动换脸换头_2082663416522690562.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `LanPaint_KSampler`
- `LoadImage`
- `PrimitiveFloat`
- `ReferenceLatent`
- `SaveImage`
- `SetLatentNoiseMask`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 4/5 个有
- `EmptyFlux2LatentImage` —— 4/5 个有
- `ImageResizeKJv2` —— 4/5 个有
- `KSamplerAdvanced` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `MaskPreview` —— 4/5 个有
- `ResizeImageMaskNode` —— 4/5 个有
- `easy imageColorMatch` —— 4/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `ResizeMask` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 80% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 5 | 65% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | sa_solver | - | 5 | 80% |
| 重绘幅度 | FlowMatchEulerDiscreteScheduler | - | 5 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，5 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 sa_solver，5 个样本，一致性 80%
- 重绘幅度 最常用 FlowMatchEulerDiscreteScheduler，5 个样本，一致性 80%
