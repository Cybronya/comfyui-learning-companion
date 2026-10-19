---
name: text_to_image_sampler_clip_vae_7
type: Text To Image
frequency: 3
level: moderate
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [数字人/数字人/分镜图生成_2093149514755559425.json, 视频生成/文生视频/文生图 Qwen2512  领军模型 完美中文_2021581695731900418.json, 视频生成/文生视频/高清超真实Z-image文生图_1999125125809176577.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_7

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/分镜图生成_2093149514755559425.json、视频生成/文生视频/文生图 Qwen2512  领军模型 完美中文_2021581695731900418.json、视频生成/文生视频/高清超真实Z-image文生图_1999125125809176577.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `EnhancedLoadDiffusionModel` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 800 - 1184 | 3 | 84% |
| 高度 | 1536 | 1200 - 1536 | 3 | 89% |
| 采样步数 | 20 | 10 - 25 | 3 | 66% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 3 | 53% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 800 - 1184，3 个样本，取值集中（一致性 84%）
- 高度 中位数 1536，观测区间 1200 - 1536，3 个样本，取值集中（一致性 89%）
- 采样步数 中位数 20，观测区间 10 - 25，3 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
