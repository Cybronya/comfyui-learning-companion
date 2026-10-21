---
name: image_to_image_lora_sampler_unet_11
type: Image To Image
frequency: 6
level: strong
coverage: 0.907667
common_nodes: [CLIPLoader, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/krea2 edit turbo 文改图工作流_2080951422828503042.json, 图片生成/文生图/krea2-人物四视图_2094627103068217345.json, 图片生成/文生图/pipi-krea2单图编辑单图洗图换图片元素改图改元素洗图神器_2089518838948917250.json, 图片生成/文生图/pipi-krea2换装编辑工作流换衣服模特换装人物换衣换装图片工作流_2089518265252012034.json, 图片生成/文生图/道具-01-krea2-物品三视图_2089700978005200898.json, 视频生成/文生视频/Krea2-单图编辑_完美一致性_2089920204829716481.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_11

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/krea2 edit turbo 文改图工作流_2080951422828503042.json、图片生成/文生图/krea2-人物四视图_2094627103068217345.json、图片生成/文生图/pipi-krea2单图编辑单图洗图换图片元素改图改元素洗图神器_2089518838948917250.json、图片生成/文生图/pipi-krea2换装编辑工作流换衣服模特换装人物换衣换装图片工作流_2089518265252012034.json、图片生成/文生图/道具-01-krea2-物品三视图_2089700978005200898.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
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
- `EmptySD3LatentImage` —— 4/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `Label (rgthree)` —— 3/6 个有
- `EmptyLatentImage` —— 2/6 个有
- `Fast Groups Muter (rgthree)` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `Seed (rgthree)` —— 2/6 个有
- `String Literal` —— 2/6 个有
- `GetImageSize+` —— 1/6 个有
- `ImageResize+` —— 1/6 个有
- `ResolutionSelector` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 872 | - | 2 | 83% |
| 高度 | 1152 | - | 2 | 89% |
| 采样步数 | 10 | 8 - 10 | 6 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 872，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 1152，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样步数 中位数 10，观测区间 8 - 10，6 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
