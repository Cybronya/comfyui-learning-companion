---
name: image_to_image_sampler_clip_unet_161
type: Image To Image
frequency: 2
level: weak
coverage: 0.824
common_nodes: [CLIPTextEncodeFlux, DualCLIPLoader, Image Comparer (rgthree), Joy_caption_two, Joy_caption_two_load, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux SRPO 细节增强洗图_1971579868788027394.json, 图片生成/图生图/Flux洗图+PMRF放大工作流（更新）_1955444798025076737.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_161

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux SRPO 细节增强洗图_1971579868788027394.json、图片生成/图生图/Flux洗图+PMRF放大工作流（更新）_1955444798025076737.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Float` —— 1/2 个有
- `JWImageResizeByLongerSide` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `PMRF` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 50% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 0.4 | - | 2 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 0.4，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
