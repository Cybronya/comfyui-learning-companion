---
name: unknown_workflow_sampler_clip_vae_27
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.98225
common_nodes: [CLIPTextEncode, EmptySenseNovaLatentImage, JWInteger, KSampler, SaveImage, SenseNovaSamplingOptions, SenseNovaU15Loader, VAEDecode]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/图生图/2093632408083058689.json, 图片生成/文生图/SenseNova SFT 文生图_2093391761937887234.json, 图片生成/文生图/SenseNova SFT 文生图_2093628735328186370.json, 图片生成/文生图/SenseNova SFT 文生图_2093661381492035585.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_27

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2093632408083058689.json、图片生成/文生图/SenseNova SFT 文生图_2093391761937887234.json、图片生成/文生图/SenseNova SFT 文生图_2093628735328186370.json、图片生成/文生图/SenseNova SFT 文生图_2093661381492035585.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySenseNovaLatentImage`
- `JWInteger`
- `KSampler`
- `SaveImage`
- `SenseNovaSamplingOptions`
- `SenseNovaU15Loader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `ImageConcanate` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `SenseNovaReferenceImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 4 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3.5 | 4 | 93% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3.5，4 个样本，取值集中（一致性 93%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2
