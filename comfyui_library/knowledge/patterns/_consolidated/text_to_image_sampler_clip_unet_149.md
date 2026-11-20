---
name: text_to_image_sampler_clip_unet_149
type: Text To Image
frequency: 5
level: moderate
coverage: 0.937
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-seedvr2文生图-N版_2011072001724653570.json, 图片生成/文生图/Z-image-turbo：最简文生图工作流_1996508267809480705.json, 图片生成/文生图/Z-image_1996868918985773057.json, 图片生成/文生图/Zimage文生图_2058258679962624001.json, 图片生成/文生图/image_Z-16秒_2013832572974927874.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_149

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Z-image-seedvr2文生图-N版_2011072001724653570.json、图片生成/文生图/Z-image-turbo：最简文生图工作流_1996508267809480705.json、图片生成/文生图/Z-image_1996868918985773057.json、图片生成/文生图/Zimage文生图_2058258679962624001.json、图片生成/文生图/image_Z-16秒_2013832572974927874.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
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
- `Text` —— 2/5 个有
- `Text _O` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `Display Any (rgthree)` —— 1/5 个有
- `DuckHideNode` —— 1/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有
- `Int` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 2416 | 5 | 59% |
| 高度 | 1080 | 1024 - 1920 | 5 | 69% |
| 采样步数 | 10 | 8 - 15 | 5 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 2416，5 个样本
- 高度 中位数 1080，观测区间 1024 - 1920，5 个样本
- 采样步数 中位数 10，观测区间 8 - 15，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
