---
name: unknown_workflow_sampler_clip_unet_429
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.875
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ComfySwitchNode, ConditioningZeroOut, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), ImageColorMatch+, ImageResizeKJv2, KSamplerSelect, LoadImage, MathExpression|pysssss, PiDConditioning, PrimitiveBoolean, ResizeImagesByLongerEdge, SamplerCustom, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Nvidia_PID_4K_像素级无损放大工作流_2096521449128415233.json, 图片生成/图生图/Nvidia_PID_4K_像素级无损放大工作流_2096880620424224770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_429

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Nvidia_PID_4K_像素级无损放大工作流_2096521449128415233.json、图片生成/图生图/Nvidia_PID_4K_像素级无损放大工作流_2096880620424224770.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageColorMatch+`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `MathExpression|pysssss`
- `PiDConditioning`
- `PrimitiveBoolean`
- `ResizeImagesByLongerEdge`
- `SamplerCustom`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 2160 | - | 2 | 100% |
| 高度 | 4096 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 2160，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 4096，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
