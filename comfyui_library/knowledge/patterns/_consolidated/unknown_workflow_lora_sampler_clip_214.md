---
name: unknown_workflow_lora_sampler_clip_214
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.910333
common_nodes: [CFGZeroStar, CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, RH_LLMAPI_NODE, SaveImage, UNETLoader, VAEDecode, VAELoader, easy promptConcat, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Qwen Image想象力创意海报_1971073668736552962.json, 图片生成/文生图/Qwen-image_海报生成_1955172373663137794.json, 图片生成/文生图/疯狂星期四Qwen Image想象力创意海报（四图）_1954598236717760514.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_214

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen Image想象力创意海报_1971073668736552962.json、图片生成/文生图/Qwen-image_海报生成_1955172373663137794.json、图片生成/文生图/疯狂星期四Qwen Image想象力创意海报（四图）_1954598236717760514.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptConcat`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
