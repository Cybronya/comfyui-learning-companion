---
name: unknown_workflow_sampler_clip_vae_22
type: Unknown Workflow
frequency: 8
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, EmptySenseNovaLatentImage, JWInteger, KSampler, SaveImage, SenseNovaSamplingOptions, SenseNovaU15Loader, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/SenseNova 1.5 SFT图像编辑_2093391746997768193.json, 图片生成/图生图/SenseNova 1.5 SFT图像编辑_2093632408083058689.json, 图片生成/图生图/SenseNova 1.5 SFT图像编辑_2093662961184366594.json, 图片生成/图生图/SenseNova_1.5_SFT图像编辑_2097130331257270274.json, 图片生成/图生图/SenseNova_1.5_SFT图像编辑_2097229171482259458.json, 图片生成/文生图/SenseNova SFT 文生图_2093391761937887234.json, 图片生成/文生图/SenseNova SFT 文生图_2093628735328186370.json, 图片生成/文生图/SenseNova SFT 文生图_2093661381492035585.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_22

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/SenseNova 1.5 SFT图像编辑_2093391746997768193.json、图片生成/图生图/SenseNova 1.5 SFT图像编辑_2093632408083058689.json、图片生成/图生图/SenseNova 1.5 SFT图像编辑_2093662961184366594.json、图片生成/图生图/SenseNova_1.5_SFT图像编辑_2097130331257270274.json、图片生成/图生图/SenseNova_1.5_SFT图像编辑_2097229171482259458.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySenseNovaLatentImage`
- `JWInteger`
- `KSampler`
- `SaveImage`
- `SenseNovaSamplingOptions`
- `SenseNovaU15Loader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `LoadImage` —— 5/8 个有
- `SenseNovaReferenceImage` —— 5/8 个有
- `CR Prompt Text` —— 3/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 8 | 100% |
| Prompt 约束强度(CFG) | 3.5 | 3 - 3.5 | 8 | 93% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | normal | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 3 - 3.5，8 个样本，取值集中（一致性 93%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 normal，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
