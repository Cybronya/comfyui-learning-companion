---
name: text_to_image_sampler_clip_unet_15
type: Text To Image
frequency: 18
level: weak
coverage: 0.974167
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-seedvr2文生图-N版_2011072001724653570.json, 图片生成/文生图/Z-image基础文生图_1995758425134993409.json, 图片生成/文生图/Z-image文生图_1993860574876467201.json, 图片生成/文生图/Z-image文生图_1993881668454907906.json, 图片生成/文生图/Z-image文生图_1993883811278684161.json, 图片生成/文生图/Z-image文生图_1993952320304201730.json, 图片生成/文生图/Z-image文生图写实，真实感_1999363958169628673.json, 图片生成/文生图/Z-image文生图新王-支持中文_1995027322610888706.json, 图片生成/文生图/Z-image文生图新王-支持中文_1995287563680276482.json, 图片生成/文生图/Z-image文生图极速高质量_1996077196244631554.json, 图片生成/文生图/Z-image文生图（速度与质量兼得）_1995796523411705857.json, 图片生成/文生图/Zimage文生图_2058258679962624001.json, 图片生成/文生图/boogu_base_example_2068252685769461761.json, 图片生成/文生图/krea turbo反推文生图_2070393483688505346.json, 图片生成/文生图/krea2反推文生图_2070420567852937217.json, 图片生成/文生图/krea2反推文生图_2070466486245879810.json, 图片生成/文生图/krea2反推文生图无需提示词_2070349490783088642.json, 图片生成/文生图/ovis image文生图-图生图海报_2000224221550739457.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_15

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/Z-image-seedvr2文生图-N版_2011072001724653570.json、图片生成/文生图/Z-image基础文生图_1995758425134993409.json、图片生成/文生图/Z-image文生图_1993860574876467201.json、图片生成/文生图/Z-image文生图_1993881668454907906.json、图片生成/文生图/Z-image文生图_1993883811278684161.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 18 个 workflow 都包含：
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
- `AILab_QwenVL` —— 6/18 个有
- `LoadImage` —— 5/18 个有
- `Text` —— 2/18 个有
- `Display Any (rgthree)` —— 1/18 个有
- `DuckHideNode` —— 1/18 个有
- `Fast Groups Muter (rgthree)` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 544 - 1920 | 18 | 77% |
| 高度 | 1536 | 960 - 1920 | 18 | 77% |
| 采样步数 | 10 | 8 - 50 | 18 | 18% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 18 | 20% |
| 采样算法 | euler | - | 18 | 78% |
| 调度器 | simple | - | 18 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 544 - 1920，18 个样本
- 高度 中位数 1536，观测区间 960 - 1920，18 个样本
- 采样步数 中位数 10，观测区间 8 - 50，18 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，18 个样本，取值分散，一致性仅 20%
- 采样算法 最常用 euler，18 个样本，一致性 78%
- 调度器 最常用 simple，18 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
