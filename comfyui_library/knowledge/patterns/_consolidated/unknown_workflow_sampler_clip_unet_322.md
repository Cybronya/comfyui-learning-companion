---
name: unknown_workflow_sampler_clip_unet_322
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8885
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptySD3LatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen3VL反推+千问文生图（无需写提示词）_1981195188544634881.json, 图片生成/文生图/Qwen千问UI图标制作_1953131721208303618.json, 图片生成/文生图/千问image文生图真实感增强_1996838932895735809.json, 图片生成/文生图/千问文生图-剪纸风格V2_1976891524531339266.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_322

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Qwen3VL反推+千问文生图（无需写提示词）_1981195188544634881.json、图片生成/文生图/Qwen千问UI图标制作_1953131721208303618.json、图片生成/文生图/千问image文生图真实感增强_1996838932895735809.json、图片生成/文生图/千问文生图-剪纸风格V2_1976891524531339266.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `String` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `AILab_QwenVL` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `LayerUtility: RoundedRectangle` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 4 | 57% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 2.5 | 4 | 57% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta57 | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta57，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
