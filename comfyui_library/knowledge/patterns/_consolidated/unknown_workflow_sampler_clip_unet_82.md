---
name: unknown_workflow_sampler_clip_unet_82
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.960154
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问文生图-超写实风格V4。_2066441527123070977.json, 图片生成/图生图/千问文生图-超写实风格V4。_2070041358575947777.json, 图片生成/文生图/12月最新文生图 Qwen 2512 标准模型非FP8_2007791461693136897.json, 图片生成/文生图/AI模特文生图_2005619684131172353.json, 图片生成/文生图/DreamCore-梦核_2073300420767862785.json, 图片生成/文生图/Qwen 2512文生图_2007744253128089601.json, 图片生成/文生图/Qwen-image文生图优化工作流_1953624443421687810.json, 图片生成/文生图/Qwen3VL反推+千问文生图（无需写提示词）_1981195188544634881.json, 图片生成/文生图/qwen-image文生图-超写实风格V4。_2054466280689807362.json, 图片生成/文生图/qwen-image文生图-超写实风格电商图片文生图中文输入英文输入提示词_2067604904981647362.json, 图片生成/文生图/qwen-image文生图-超写实风格电商图片文生图中文输入英文输入提示词_2082433240765386754.json, 图片生成/文生图/qwen文生图-超写实风格V4。_2054841790506782721.json, 图片生成/文生图/千问image文生图真实感增强_1996838932895735809.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_82

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/千问文生图-超写实风格V4。_2066441527123070977.json、图片生成/图生图/千问文生图-超写实风格V4。_2070041358575947777.json、图片生成/文生图/12月最新文生图 Qwen 2512 标准模型非FP8_2007791461693136897.json、图片生成/文生图/AI模特文生图_2005619684131172353.json、图片生成/文生图/DreamCore-梦核_2073300420767862785.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 12/13 个有
- `CR Text` —— 11/13 个有
- `easy cleanGpuUsed` —— 9/13 个有
- `CR Text Concatenate` —— 8/13 个有
- `String` —— 8/13 个有
- `Int` —— 2/13 个有
- `LoadImage` —— 2/13 个有
- `AILab_QwenVL` —— 1/13 个有
- `JWInteger` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `PrimitiveInt` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `ShowText|pysssss` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 50 | 13 | 48% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 13 | 60% |
| 采样算法 | euler | - | 13 | 85% |
| 调度器 | beta57 | - | 13 | 77% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 50，13 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 85%
- 调度器 最常用 beta57，13 个样本，一致性 77%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
