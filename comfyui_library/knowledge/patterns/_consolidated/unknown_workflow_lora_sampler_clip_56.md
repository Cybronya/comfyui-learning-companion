---
name: unknown_workflow_lora_sampler_clip_56
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.753
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [CR Prompt Text, easy promptConcat, LayerUtility: ImageScaleByAspectRatio V2, CR Text, Fast Muter (rgthree)]
members: [图片生成/文生图/1954598236717760514.json, 图片生成/文生图/1955172373663137794.json, 图片生成/文生图/1971073668736552962.json, 图片生成/文生图/1983480106519830529.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_56

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1954598236717760514.json、图片生成/文生图/1955172373663137794.json、图片生成/文生图/1971073668736552962.json、图片生成/文生图/1983480106519830529.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStar` —— 3/4 个有
- `CR Prompt Text` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `easy promptConcat` —— 3/4 个有
- `Float` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `RH_Captioner` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `Fast Muter (rgthree)` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 4 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text、easy promptConcat、LayerUtility: ImageScaleByAspectRatio V2、CR Text、Fast Muter (rgthree)
