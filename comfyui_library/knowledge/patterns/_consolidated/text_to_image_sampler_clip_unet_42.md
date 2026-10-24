---
name: text_to_image_sampler_clip_unet_42
type: Text To Image
frequency: 13
level: moderate
coverage: 0.982231
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/boogu_turbo工作流含提示词_2067780518917271554.json, 图片生成/文生图/boogu_turbo文生图_2068941150962147330.json, 图片生成/文生图/boogu_turbo文生图_2068959350126891010.json, 图片生成/文生图/boogu_turbo文生图工作流_2069287215741624322.json, 图片生成/文生图/boogu文生图_2069052782014984193.json, 图片生成/文生图/boogu文生图满血版工作流_2067862555661520898.json, 图片生成/文生图/boogu文生图满血版工作流_2067880773423816705.json, 图片生成/文生图/boogu模型快速出图_2069078655669727234.json, 图片生成/文生图/boogu满血版文生图V1_2067838674468958210.json, 图片生成/文生图/boogu满血版文生图V1_2068275477441236993.json, 图片生成/文生图/flux 2文生图 丨电商场景图_1997117365974405121.json, 图片生成/文生图/krea-2文生图_2070065443259375617.json, 图片生成/文生图/krea2-turbo_2070710904806789122.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_42

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/boogu_turbo工作流含提示词_2067780518917271554.json、图片生成/文生图/boogu_turbo文生图_2068941150962147330.json、图片生成/文生图/boogu_turbo文生图_2068959350126891010.json、图片生成/文生图/boogu_turbo文生图工作流_2069287215741624322.json、图片生成/文生图/boogu文生图_2069052782014984193.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 12/13 个有
- `CR Prompt Text` —— 4/13 个有
- `JjkText` —— 3/13 个有
- `RH_Translator` —— 3/13 个有
- `Int` —— 2/13 个有
- `FluxGuidance` —— 1/13 个有
- `ImageSizeCalculator` —— 1/13 个有
- `ResolutionSelector` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 13 | 11% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 13 | 32% |
| 采样算法 | lcm | - | 13 | 38% |
| 调度器 | sgm_uniform | - | 13 | 38% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1024 | 720 - 1024 | 13 | 90% |
| 高度 | 1200 | 1024 - 1536 | 13 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，13 个样本，取值分散，一致性仅 11%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，13 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 lcm，13 个样本，一致性 38%
- 调度器 最常用 sgm_uniform，13 个样本，一致性 38%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 720 - 1024，13 个样本，取值集中（一致性 90%）
- 高度 中位数 1200，观测区间 1024 - 1536，13 个样本，取值集中（一致性 82%）
- 高发问题（7/13 个样本）：Steps较低可能导致细节不足
