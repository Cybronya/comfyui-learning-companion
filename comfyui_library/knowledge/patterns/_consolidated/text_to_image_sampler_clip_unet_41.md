---
name: text_to_image_sampler_clip_unet_41
type: Text To Image
frequency: 13
level: moderate
coverage: 0.932923
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/anima_api_2075524651396198402.json, 图片生成/文生图/anima基础工作流_2050251032118210561.json, 图片生成/文生图/boogu turbo文生图_2069610874171641858.json, 图片生成/文生图/boogu turbo文生图_2069633350947663873.json, 图片生成/文生图/boogu turbo文生图_2069634712343244801.json, 图片生成/文生图/boogu turbo文生图急速生图_2069629401351933954.json, 图片生成/文生图/krea2_文生图_2081989846117216258.json, 图片生成/文生图/krea2文生图_2069618400707567618.json, 图片生成/文生图/krea2文生图_2069962144506011649.json, 图片生成/文生图/krea2文生图批量版_2070339623888441346.json, 图片生成/文生图/krea2文生图批量版_2070388445238878210.json, 图片生成/文生图/krea2文生图批量版_2070421570203508737.json, 图片生成/文生图/krea2文生图批量版_2070468131897827330.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_41

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/anima_api_2075524651396198402.json、图片生成/文生图/anima基础工作流_2050251032118210561.json、图片生成/文生图/boogu turbo文生图_2069610874171641858.json、图片生成/文生图/boogu turbo文生图_2069633350947663873.json、图片生成/文生图/boogu turbo文生图_2069634712343244801.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：93%

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
- `ConditioningZeroOut` —— 11/13 个有
- `CR Text` —— 9/13 个有
- `HAIGC_SaveImagesToZip` —— 4/13 个有
- `PromptBatchQueue` —— 4/13 个有
- `FluxResolutionNode` —— 1/13 个有
- `LoaderGGUF` —— 1/13 个有
- `SeedNode` —— 1/13 个有
- `TT_img_enc` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 50 | 13 | 6% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 13 | 26% |
| 采样算法 | euler | - | 13 | 54% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 13 | 100% |
| 高度 | 1536 | 1024 - 1536 | 13 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 50，13 个样本，取值分散，一致性仅 6%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，13 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，13 个样本，一致性 54%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，13 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1024 - 1536，13 个样本，取值集中（一致性 87%）
- 高发问题（11/13 个样本）：Steps较低可能导致细节不足
