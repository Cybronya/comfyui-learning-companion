---
name: unknown_workflow_sampler_clip_vae_53
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8978
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/极速版文生图V1-Qwen-ImageNunchaku Ran_2046513028291633154.json, 图片生成/文生图/玄幻壁纸_1950582399950327809.json, 图片生成/文生图/电商生成多镜头图片 qwen2512_2017062093035413506.json, 图片生成/文生图/粗线条插画_2016470143131459586.json, 图片生成/文生图/粗线条水彩_2021242555865763842.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_53

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/极速版文生图V1-Qwen-ImageNunchaku Ran_2046513028291633154.json、图片生成/文生图/玄幻壁纸_1950582399950327809.json、图片生成/文生图/电商生成多镜头图片 qwen2512_2017062093035413506.json、图片生成/文生图/粗线条插画_2016470143131459586.json、图片生成/文生图/粗线条水彩_2021242555865763842.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `JjkText` —— 2/5 个有
- `SeedVR2` —— 2/5 个有
- `SeedVR2BlockSwap` —— 2/5 个有
- `LatentUpscaleBy` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `NunchakuQwenImageDiTLoader` —— 1/5 个有
- `easy stylesSelector` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 8 - 20 | 5 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
