---
name: text_to_image_sampler_clip_unet_2
type: Text To Image
frequency: 42
level: weak
coverage: 0.981976
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-seedvr2文生图-N版_2011072001724653570.json, 图片生成/文生图/Z-image文生图_1993860574876467201.json, 图片生成/文生图/Z-image文生图_1993881668454907906.json, 图片生成/文生图/Z-image文生图_1993883811278684161.json, 图片生成/文生图/Z-image文生图_1993952320304201730.json, 图片生成/文生图/Z-image文生图_1994050196562706434.json, 图片生成/文生图/Z-image文生图_1994253056955138050.json, 图片生成/文生图/Z-image文生图_1994323420024422402.json, 图片生成/文生图/Z-image文生图_2002734393544306690.json, 图片生成/文生图/Z-image文生图写实，真实感_1999363958169628673.json, 图片生成/文生图/Z-image文生图新王-支持中文_1995027322610888706.json, 图片生成/文生图/Z-image文生图新王-支持中文_1995287563680276482.json, 图片生成/文生图/Z-image文生图极速高质量_1996077196244631554.json, 图片生成/文生图/Z-image文生图（速度与质量兼得）_1995796523411705857.json, 图片生成/文生图/Z-image最强文生图模型_1994953430059954178.json, 图片生成/文生图/Z-image生图_2102776816992866305.json, 图片生成/文生图/Z-image造像-文生图（最强写实人像）_1994314682653671425.json, 图片生成/文生图/Z-image高优化文生图、可生成多张_2053636873704226817.json, 图片生成/文生图/Z-image，出图 效果炸裂，效果超越Flux2_1993931824883843074.json, 图片生成/文生图/Z-image，最强文生图_1994408486224207874.json, 图片生成/文生图/Zimage文生图_2058258679962624001.json, 图片生成/文生图/boogu base文生图_2067452727042592770.json, 图片生成/文生图/boogu image turbo 文生图_2069087085788749825.json, 图片生成/文生图/boogu turbo文生图_2067882978142941186.json, 图片生成/文生图/boogu. image电商海报_2040459014437347330.json, 图片生成/文生图/boogu_base_example_2068252685769461761.json, 图片生成/文生图/boogu_image_turbo_2067441416753737730.json, 图片生成/文生图/boogu_turbo-文生图极速-人像真实感_2070712427402055682.json, 图片生成/文生图/boogu_turbo_2067856663108997122.json, 图片生成/文生图/boogu_turbo_example_2068872865654599681.json, 图片生成/文生图/boogu_turbo_文生图_2068263819142590465.json, 图片生成/文生图/boogu_turbo_文生图_2068962805402923010.json, 图片生成/文生图/boogu_turbo_文生图_2069223329772429313.json, 图片生成/文生图/boogu_turbo_文生图_2069231725925978114.json, 图片生成/文生图/boogu_turbo_文生图_2071491115995455489.json, 图片生成/文生图/boogu_turbo工作流_2067417417038516225.json, 图片生成/文生图/krea turbo反推文生图_2070393483688505346.json, 图片生成/文生图/krea2反推文生图_2070420567852937217.json, 图片生成/文生图/krea2反推文生图_2070466486245879810.json, 图片生成/文生图/krea2反推文生图无需提示词_2070349490783088642.json, 图片生成/文生图/ovis image文生图-图生图海报_2000224221550739457.json, 图片生成/文生图/【Supermate】百度-ERNIE-Image-文生图及图生图集合_2044580867879735297.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_2

> 由 `engine/knowledge_consolidation` 从 42 个 workflow 归纳得出（图片生成/文生图/Z-image-seedvr2文生图-N版_2011072001724653570.json、图片生成/文生图/Z-image文生图_1993860574876467201.json、图片生成/文生图/Z-image文生图_1993881668454907906.json、图片生成/文生图/Z-image文生图_1993883811278684161.json、图片生成/文生图/Z-image文生图_1993952320304201730.json…）

- **类型**：Text To Image
- **样本数**：42
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 42 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 41/42 个有
- `AILab_QwenVL` —— 6/42 个有
- `LoadImage` —— 6/42 个有
- `Text` —— 3/42 个有
- `Fast Groups Muter (rgthree)` —— 2/42 个有
- `Display Any (rgthree)` —— 1/42 个有
- `DuckHideNode` —— 1/42 个有
- `Label (rgthree)` —— 1/42 个有
- `VAEEncode` —— 1/42 个有
- `scale` —— 1/42 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 688 - 1920 | 42 | 83% |
| 高度 | 1536 | 1024 - 1920 | 42 | 78% |
| 采样步数 | 10 | 4 - 50 | 42 | 6% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 42 | 30% |
| 采样算法 | euler | - | 42 | 60% |
| 调度器 | simple | - | 42 | 64% |
| 重绘幅度 | 1 | 0.5 - 1 | 42 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/42 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 688 - 1920，42 个样本，取值集中（一致性 83%）
- 高度 中位数 1536，观测区间 1024 - 1920，42 个样本
- 采样步数 中位数 10，观测区间 4 - 50，42 个样本，取值分散，一致性仅 6%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，42 个样本，取值分散，一致性仅 30%
- 采样算法 最常用 euler，42 个样本，一致性 60%
- 调度器 最常用 simple，42 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，42 个样本，取值集中（一致性 92%）
