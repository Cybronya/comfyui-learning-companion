---
name: text_to_image_sampler_clip_unet_144
type: Text To Image
frequency: 4
level: strong
coverage: 0.8155
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/001.Z-image生图巅峰003.文生图_2033719257393012738.json, 图片生成/文生图/001.Z-image生图巅峰006.回车批量文生图.json_2033729781623164930.json, 图片生成/文生图/Krea2纯欲美学工作流_2069352137276088322.json, 图片生成/文生图/极致美学文生图（真实+姿态向）V3.0_1993866096310763521.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_144

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/001.Z-image生图巅峰003.文生图_2033719257393012738.json、图片生成/文生图/001.Z-image生图巅峰006.回车批量文生图.json_2033729781623164930.json、图片生成/文生图/Krea2纯欲美学工作流_2069352137276088322.json、图片生成/文生图/极致美学文生图（真实+姿态向）V3.0_1993866096310763521.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
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
- `CR Text` —— 3/4 个有
- `CR Text Replace` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `JDCN_StringToList` —— 2/4 个有
- `ProcessString` —— 2/4 个有
- `RH_LLMAPI_NODE` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `easy int` —— 2/4 个有
- `ImpactInt` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `easy promptLine` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 956 | 720 - 1280 | 4 | 78% |
| 高度 | 1408 | 480 - 1920 | 4 | 60% |
| 采样步数 | 8.5 | 8 - 10 | 4 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 25% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 956，观测区间 720 - 1280，4 个样本
- 高度 中位数 1408，观测区间 480 - 1920，4 个样本
- 采样步数 中位数 8.5，观测区间 8 - 10，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 25%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
