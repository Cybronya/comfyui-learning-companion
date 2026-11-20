---
name: unknown_workflow_sampler_clip_unet_334
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.89375
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), KSamplerSelect, LoadImage, MathExpression|pysssss, PiDConditioning, SamplerCustom, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Nvidia_PID_4K_像素级无损放大工作流_2096521449128415233.json, 图片生成/图生图/Nvidia_PID_4K_像素级无损放大工作流_2096880620424224770.json, 平台全量/Nvidia PID 4K 像素级无损放大工作流_2075430045367234562.json, 平台全量/PiD 高清放大_2063864892125442049.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_334

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Nvidia_PID_4K_像素级无损放大工作流_2096521449128415233.json、图片生成/图生图/Nvidia_PID_4K_像素级无损放大工作流_2096880620424224770.json、平台全量/Nvidia PID 4K 像素级无损放大工作流_2075430045367234562.json、平台全量/PiD 高清放大_2063864892125442049.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `MathExpression|pysssss`
- `PiDConditioning`
- `SamplerCustom`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 3/4 个有
- `EmptyLatentImage` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `ImageColorMatch+` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `PrimitiveBoolean` —— 3/4 个有
- `ResizeImagesByLongerEdge` —— 3/4 个有
- `EmptyChromaRadianceLatentImage` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `JWImageResizeByLongerSide` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 2160 | 2160 - 2160 | 3 | 100% |
| 高度 | 4096 | 4096 - 4096 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 2160，观测区间 2160 - 2160，3 个样本，取值集中（一致性 100%）
- 高度 中位数 4096，观测区间 4096 - 4096，3 个样本，取值集中（一致性 100%）
