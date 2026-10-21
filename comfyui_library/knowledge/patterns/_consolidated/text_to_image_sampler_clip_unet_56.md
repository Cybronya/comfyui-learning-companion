---
name: text_to_image_sampler_clip_unet_56
type: Text To Image
frequency: 8
level: weak
coverage: 0.969375
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Boogu 满血版文生图_2068176743512502273.json, 图片生成/文生图/Boogu-Base 高清质感文生图_2068717818228592642.json, 图片生成/文生图/Krea 2_2072697671621636097.json, 图片生成/文生图/Krea2_Turbo反推提示词生图_2071103038554726401.json, 图片生成/文生图/Krea2_Turbo生图（无审查版）_2071109949048053761.json, 图片生成/文生图/Z-image-distall-patch文生图_2002052529569579010.json, 图片生成/文生图/Z-image-distall-patch（文生图）写实性lora_2004006107569897473.json, 图片生成/文生图/Z-image文生图_1993860952581931009.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_56

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Boogu 满血版文生图_2068176743512502273.json、图片生成/文生图/Boogu-Base 高清质感文生图_2068717818228592642.json、图片生成/文生图/Krea 2_2072697671621636097.json、图片生成/文生图/Krea2_Turbo反推提示词生图_2071103038554726401.json、图片生成/文生图/Krea2_Turbo生图（无审查版）_2071109949048053761.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/8 个有
- `easy promptLine` —— 4/8 个有
- `LoraLoaderModelOnly` —— 3/8 个有
- `ResolutionSelector` —— 3/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `孤海注释` —— 2/8 个有
- `ProcessString` —— 1/8 个有
- `SizeSelector` —— 1/8 个有
- `easy promptList` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1920 | 8 | 69% |
| 高度 | 1052 | 1024 - 1560 | 8 | 81% |
| 采样步数 | 10 | 8 - 50 | 8 | 13% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 26% |
| 采样算法 | euler | - | 8 | 62% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1920，8 个样本
- 高度 中位数 1052，观测区间 1024 - 1560，8 个样本，取值集中（一致性 81%）
- 采样步数 中位数 10，观测区间 8 - 50，8 个样本，取值分散，一致性仅 13%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，8 个样本，一致性 62%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
