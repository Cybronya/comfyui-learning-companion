---
name: unknown_workflow_sampler_clip_unet_121
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8161
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 3.0提示词增强生图工作流｜两段式闭环_2103056782804480002.json, 图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json, 图片生成/文生图/Qwen Image BF16满血版_1954768333373620226.json, 图片生成/文生图/Qwen Image Distill蒸馏模型加速版文生图（文字增强版）_1953813624924110849.json, 图片生成/文生图/Qwen Image fp8蒸馏版_1954773431147479041.json, 图片生成/文生图/Qwen Image多种加速方式效果对比版_1954593530536718337.json, 图片生成/文生图/Qwen image文生图Comfy fp8加速版本_1954314194239811586.json, 图片生成/文生图/Qwen image文生图Comfy官方fp8加lora版本_1954743795998965761.json, 图片生成/文生图/Qwen image文生图Comfy官方fp8版本_1952659040263421954.json, 图片生成/文生图/Qwen-image文生图 FP8 RAPID_1955920019513376770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_121

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Qwen Image 3.0提示词增强生图工作流｜两段式闭环_2103056782804480002.json、图片生成/文生图/Qwen Image 3.0文生图工作流｜阿里旗舰图像模型_2103055683909410817.json、图片生成/文生图/Qwen Image BF16满血版_1954768333373620226.json、图片生成/文生图/Qwen Image Distill蒸馏模型加速版文生图（文字增强版）_1953813624924110849.json、图片生成/文生图/Qwen Image fp8蒸馏版_1954773431147479041.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 8/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `PrimitiveInt` —— 6/10 个有
- `CR Prompt Text` —— 3/10 个有
- `LoraLoader` —— 3/10 个有
- `AV_LoraLoader` —— 2/10 个有
- `Float` —— 2/10 个有
- `TextEncodeQwenImageEditPlus` —— 2/10 个有
- `LoraLoaderModelOnly` —— 1/10 个有
- `RH_QwenImagePromptEnhancer` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 24 | 10 | 64% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 4 | 10 | 42% |
| 采样算法 | euler | - | 10 | 70% |
| 调度器 | simple | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 24，10 个样本
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 4，10 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，10 个样本，一致性 70%
- 调度器 最常用 simple，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
