---
name: image_to_image_lora_sampler_unet_159
type: Image To Image
frequency: 4
level: strong
coverage: 0.6365
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, GetNode, ImageResizeKJv2, ImpactImageInfo, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, Krea2OstrisEditModelPatch, LoadImage, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveStringMultiline, ResizeImagesByLongerEdge, SaveImage, SetNode, TextEncodeKrea2OstrisEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/krea2图像编辑多功能工作流_2097218406566154241.json, 图片生成/图生图/krea2图像编辑多功能工作流_2097515091607511042.json, 图片生成/文生图/krea2图像编辑多功能工作流_2077940591131971586.json, 图片生成/文生图/图像编辑多功krea2能工作流ENG文生图图生图其它图片处理_2087092997019234306.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_159

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/krea2图像编辑多功能工作流_2097218406566154241.json、图片生成/图生图/krea2图像编辑多功能工作流_2097515091607511042.json、图片生成/文生图/krea2图像编辑多功能工作流_2077940591131971586.json、图片生成/文生图/图像编辑多功krea2能工作流ENG文生图图生图其它图片处理_2087092997019234306.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：64%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `GetNode`
- `ImageResizeKJv2`
- `ImpactImageInfo`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `Krea2OstrisEditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `ResizeImagesByLongerEdge`
- `SaveImage`
- `SetNode`
- `TextEncodeKrea2OstrisEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 12 - 12 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1536 | 1536 - 1536 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，观测区间 12 - 12，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，4 个样本，取值集中（一致性 100%）
