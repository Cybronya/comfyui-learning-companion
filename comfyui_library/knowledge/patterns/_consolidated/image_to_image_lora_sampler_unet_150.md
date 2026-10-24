---
name: image_to_image_lora_sampler_unet_150
type: Image To Image
frequency: 4
level: strong
coverage: 0.75425
common_nodes: [CLIPLoader, EmptySD3LatentImage, ImageScaleToTotalPixels, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/krea2-风格扩展流_2107466786307403778.json, 图片生成/图生图/krea2_identity_edit_单图双图编辑_2080481946932695041.json, 图片生成/图生图/krea2_identity_edit_单图双图编辑_2080938734081626114.json, 视频生成/文生视频/Krea2-单图编辑_完美一致性_2089920204829716481.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_150

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/krea2-风格扩展流_2107466786307403778.json、图片生成/图生图/krea2_identity_edit_单图双图编辑_2080481946932695041.json、图片生成/图生图/krea2_identity_edit_单图双图编辑_2080938734081626114.json、视频生成/文生视频/Krea2-单图编辑_完美一致性_2089920204829716481.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `GetImageSize+` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `Label (rgthree)` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `JoinStrings` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `SeedNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
