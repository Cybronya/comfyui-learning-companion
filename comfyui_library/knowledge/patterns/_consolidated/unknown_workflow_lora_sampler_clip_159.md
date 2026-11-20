---
name: unknown_workflow_lora_sampler_clip_159
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.846
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/qwen2512-Cc风情万种_2020495804342996994.json, 平台全量/Qwen-小红书风格封面设计工作流1.0_1960880289218269185.json, 平台全量/Qwen-小红书风格潮流拼贴海报_1966388891777478658.json, 平台全量/Qwen-手写艺术字_1997965725543333890.json, 平台全量/文生图-产品创意海报_2065237719982370818.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_159

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/qwen2512-Cc风情万种_2020495804342996994.json、平台全量/Qwen-小红书风格封面设计工作流1.0_1960880289218269185.json、平台全量/Qwen-小红书风格潮流拼贴海报_1966388891777478658.json、平台全量/Qwen-手写艺术字_1997965725543333890.json、平台全量/文生图-产品创意海报_2065237719982370818.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 4/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `TextCombinerTwo` —— 3/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `LayerColor: AutoAdjustV2` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 30 | 5 | 64% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 5.5 | 5 | 59% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 5.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
