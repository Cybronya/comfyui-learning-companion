---
name: image_to_image_sampler_clip_unet_89
type: Image To Image
frequency: 5
level: moderate
coverage: 0.9522
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-klein角色替换_2012312687472025602.json, 图片生成/图生图/Z-image增加人物质感_1993876234681729025.json, 图片生成/图生图/cad平面图转彩图-室内设计专用-Flux2-klein_2012841471073853441.json, 图片生成/图生图/室内-klein-平面图转彩图工作流_2040793589877317633.json, 图片生成/文生图/毛坯转效果图-室内设计专用-Flux2-klein_2012839162801557505.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_89

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux2-klein角色替换_2012312687472025602.json、图片生成/图生图/Z-image增加人物质感_1993876234681729025.json、图片生成/图生图/cad平面图转彩图-室内设计专用-Flux2-klein_2012841471073853441.json、图片生成/图生图/室内-klein-平面图转彩图工作流_2040793589877317633.json、图片生成/文生图/毛坯转效果图-室内设计专用-Flux2-klein_2012839162801557505.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PIP_图像联结` —— 4/5 个有
- `ReferenceLatent` —— 4/5 个有
- `RH_Captioner` —— 2/5 个有
- `JjkText` —— 1/5 个有
- `MultiTextConcatenate` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 10 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.2 - 1 | 5 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，5 个样本
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
