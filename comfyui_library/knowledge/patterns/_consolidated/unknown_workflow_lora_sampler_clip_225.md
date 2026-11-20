---
name: unknown_workflow_lora_sampler_clip_225
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.656333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveFloat, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/qwen-image文生图_2112188060006965250.json, 图片生成/文生图/文生图-qwen-image-2512版_2109854228004036610.json, 图片生成/文生图/爱小墨-图片-文生图-综合生成v1.0_2077346986138882050.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_225

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/qwen-image文生图_2112188060006965250.json、图片生成/文生图/文生图-qwen-image-2512版_2109854228004036610.json、图片生成/文生图/爱小墨-图片-文生图-综合生成v1.0_2077346986138882050.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ComfyNumberConvert` —— 2/3 个有
- `CustomCombo` —— 2/3 个有
- `RegexExtract` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveBoolean` —— 1/3 个有
- `StringFormat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 3 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 3 | 1% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，3 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，3 个样本，取值分散，一致性仅 1%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
