---
name: image_to_image_lora_sampler_unet_39
type: Image To Image
frequency: 2
level: weak
coverage: 0.619
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, GetNode, ImageResizeKJv2, ImpactImageInfo, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, Krea2OstrisEditModelPatch, LoadImage, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveStringMultiline, ResizeImagesByLongerEdge, SaveImage, SetNode, TextEncodeKrea2OstrisEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/krea2图像编辑多功能工作流_2077940591131971586.json, 图片生成/文生图/图像编辑多功krea2能工作流ENG文生图图生图其它图片处理_2087092997019234306.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_39

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/krea2图像编辑多功能工作流_2077940591131971586.json、图片生成/文生图/图像编辑多功krea2能工作流ENG文生图图生图其它图片处理_2087092997019234306.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：62%

## 共有节点

全部 2 个 workflow 都包含：
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
| 采样步数 | 12 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
