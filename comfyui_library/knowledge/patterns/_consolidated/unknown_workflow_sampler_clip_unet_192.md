---
name: unknown_workflow_sampler_clip_unet_192
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.892286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 3.0提示词增强生图工作流｜两段式闭环_2103056782804480002.json, 图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json, 图片生成/文生图/Qwen Image Distill蒸馏模型加速版文生图（文字增强版）_1953813624924110849.json, 图片生成/文生图/Qwen Image多种加速方式效果对比版_1954593530536718337.json, 图片生成/文生图/Qwen Image想象力创意海报_1971073668736552962.json, 图片生成/文生图/Qwen-image_海报生成_1955172373663137794.json, 图片生成/文生图/疯狂星期四Qwen Image想象力创意海报（四图）_1954598236717760514.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_192

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen Image 3.0提示词增强生图工作流｜两段式闭环_2103056782804480002.json、图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json、图片生成/文生图/Qwen Image Distill蒸馏模型加速版文生图（文字增强版）_1953813624924110849.json、图片生成/文生图/Qwen Image多种加速方式效果对比版_1954593530536718337.json、图片生成/文生图/Qwen Image想象力创意海报_1971073668736552962.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 6/7 个有
- `ModelSamplingAuraFlow` —— 5/7 个有
- `Float` —— 4/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `CFGZeroStar` —— 3/7 个有
- `RH_LLMAPI_NODE` —— 3/7 个有
- `easy promptConcat` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `TextEncodeQwenImageEditPlus` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `PrimitiveStringMultiline` —— 1/7 个有
- `RH_Captioner` —— 1/7 个有
- `RH_QwenImagePromptEnhancer` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 24 | 7 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 7 | 53% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | normal | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 24，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 normal，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
