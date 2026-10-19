---
name: unknown_workflow_sampler_clip_vae_3
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.870643
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, CR SDXL Aspect Ratio, easy cleanGpuUsed, Seed (rgthree)]
members: [图片生成/文生图/1952243963510075394.json, 图片生成/文生图/1952725589155319810.json, 图片生成/文生图/1952728050552270850.json, 图片生成/文生图/1952737054142697473.json, 图片生成/文生图/1952787828896952322.json, 图片生成/文生图/1952836741905510402.json, 图片生成/文生图/1952892525439873025.json, 图片生成/文生图/1952903251559649281.json, 图片生成/文生图/1953699331356459009.json, 图片生成/文生图/1954932098835496961.json, 图片生成/文生图/1954932387395223553.json, 图片生成/文生图/1954932461516963842.json, 图片生成/文生图/1956936946464296962.json, 图片生成/文生图/1983771974319153153.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_3

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/1952243963510075394.json、图片生成/文生图/1952725589155319810.json、图片生成/文生图/1952728050552270850.json、图片生成/文生图/1952737054142697473.json、图片生成/文生图/1952787828896952322.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 13/14 个有
- `UNETLoader` —— 13/14 个有
- `EmptySD3LatentImage` —— 12/14 个有
- `CR Text` —— 7/14 个有
- `CR SDXL Aspect Ratio` —— 6/14 个有
- `LoraLoaderModelOnly` —— 4/14 个有
- `UnetLoaderGGUF` —— 2/14 个有
- `easy cleanGpuUsed` —— 2/14 个有
- `CLIPLoaderGGUF` —— 1/14 个有
- `Float` —— 1/14 个有
- `FluxEmptyLatentSizePicker` —— 1/14 个有
- `ImpactInt` —— 1/14 个有
- `Int` —— 1/14 个有
- `Seed (rgthree)` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 35 | 14 | 51% |
| Prompt 约束强度(CFG) | 3 | 1 - 4 | 14 | 58% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 832x1152 (0.96MP) - 3:4 | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 35，14 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 4，14 个样本
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR SDXL Aspect Ratio、easy cleanGpuUsed、Seed (rgthree)
