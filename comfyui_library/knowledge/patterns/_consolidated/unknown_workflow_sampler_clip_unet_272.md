---
name: unknown_workflow_sampler_clip_unet_272
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.907333
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2512（bf16）文生图_2006636107433254914.json, 图片生成/文生图/Qwen Image Distill蒸馏模型加速版文生图（文字增强版）_1953813624924110849.json, 图片生成/文生图/Qwen Image多种加速方式效果对比版_1954593530536718337.json, 图片生成/文生图/Qwen Image想象力创意海报_1971073668736552962.json, 图片生成/文生图/Qwen-image_海报生成_1955172373663137794.json, 图片生成/文生图/疯狂星期四Qwen Image想象力创意海报（四图）_1954598236717760514.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_272

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2512（bf16）文生图_2006636107433254914.json、图片生成/文生图/Qwen Image Distill蒸馏模型加速版文生图（文字增强版）_1953813624924110849.json、图片生成/文生图/Qwen Image多种加速方式效果对比版_1954593530536718337.json、图片生成/文生图/Qwen Image想象力创意海报_1971073668736552962.json、图片生成/文生图/Qwen-image_海报生成_1955172373663137794.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `Float` —— 4/6 个有
- `CFGZeroStar` —— 3/6 个有
- `RH_LLMAPI_NODE` —— 3/6 个有
- `easy promptConcat` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `CFGNorm` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `Prompts Everywhere` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 20 | 6 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | normal | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 normal，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
