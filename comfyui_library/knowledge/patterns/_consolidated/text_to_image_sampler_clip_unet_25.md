---
name: text_to_image_sampler_clip_unet_25
type: Text To Image
frequency: 17
level: weak
coverage: 0.928647
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图_2108503764775821313.json, 图片生成/文生图/文生图z-image-turbo_2080295709659713538.json, 图片生成/文生图/文生图ziamge_2015340435937431553.json, 图片生成/文生图/文生图。Zimage（支持真人的国产加速模型）_2028059294964387841.json, 图片生成/文生图/文生图工作流_2050735539829125122.json, 图片生成/文生图/文生图工作流_2052551381218799617.json, 图片生成/文生图/文生图工作流_2092188994711937026.json, 图片生成/文生图/文生图工作流_2108853554176946177.json, 图片生成/文生图/文生图超快生成_2101274758447980545.json, 图片生成/文生图/文生图高优化-_2051832739187441666.json, 图片生成/文生图/文生图高优化-邻家AI大女孩_2041750749352304641.json, 图片生成/文生图/文生图高优化-邻家AI大女孩_2046853470312992769.json, 图片生成/文生图/文生图高优化-邻家女孩_2049386831170510849.json, 图片生成/文生图/文生图（最强最快真实感Z-image）_1993837816855592961.json, 图片生成/文生图/文生图（生成高清手机壁纸）_2064532712718950402.json, 图片生成/文生图/最新Krea2+Turbo文生图 双采样加强版_2071061410838302722.json, 图片生成/文生图/最新文生图Krea2+Turbo 双采样加强版_2071101261251960834.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_25

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/文生图_2108503764775821313.json、图片生成/文生图/文生图z-image-turbo_2080295709659713538.json、图片生成/文生图/文生图ziamge_2015340435937431553.json、图片生成/文生图/文生图。Zimage（支持真人的国产加速模型）_2028059294964387841.json、图片生成/文生图/文生图工作流_2050735539829125122.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 11/17 个有
- `PrimitiveStringMultiline` —— 3/17 个有
- `Int` —— 2/17 个有
- `PreviewImage` —— 2/17 个有
- `Fast Groups Bypasser (rgthree)` —— 1/17 个有
- `LoadImage` —— 1/17 个有
- `PreviewAny` —— 1/17 个有
- `PrimitiveInt` —— 1/17 个有
- `RH_Captioner` —— 1/17 个有
- `TTResolutionSelector` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 1920 | 17 | 81% |
| 高度 | 1080 | 720 - 2640 | 17 | 65% |
| 采样步数 | 9 | 6 - 35 | 17 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 17 | 0% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 76% |
| 重绘幅度 | 1 | 0.4 - 1 | 17 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 1920，17 个样本，取值集中（一致性 81%）
- 高度 中位数 1080，观测区间 720 - 2640，17 个样本
- 采样步数 中位数 9，观测区间 6 - 35，17 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，17 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 76%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，17 个样本
- 高发问题（13/17 个样本）：Steps较低可能导致细节不足
