---
name: unknown_workflow_sampler_unet_vae_194
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.854
common_nodes: [CLIPLoader, CR Text, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 换头换脸｜6步加速版_2104126864011915266.json, 图片生成/图生图/Qwen-image2.1  抠图工作流，指哪扣哪！_2102380656931196930.json, 图片生成/图生图/开源最强图片模型_Qwen-image2.1_指定抠图模式_2105107851831234562.json, 图片生成/图生图/开源最强图片模型_Qwen-image2.1_指定抠图模式_2105488254140239873.json, 图片生成/图生图/自动抠图 Qwen-image2.1_2103125967697956866.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_194

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 换头换脸｜6步加速版_2104126864011915266.json、图片生成/图生图/Qwen-image2.1  抠图工作流，指哪扣哪！_2102380656931196930.json、图片生成/图生图/开源最强图片模型_Qwen-image2.1_指定抠图模式_2105107851831234562.json、图片生成/图生图/开源最强图片模型_Qwen-image2.1_指定抠图模式_2105488254140239873.json、图片生成/图生图/自动抠图 Qwen-image2.1_2103125967697956866.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 4/5 个有
- `CR Prompt Text` —— 1/5 个有
- `ConcatTextOfUtils` —— 1/5 个有
- `LoraLoaderBypassModelOnly` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `MultiTextConcatenate` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `QwenImage21SageAttentionT8` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 6 - 25 | 5 | 64% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 1024 - 1200 | 5 | 93% |
| 高度 | 1024 | 560 - 1600 | 5 | 68% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 6 - 25，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1200，5 个样本，取值集中（一致性 93%）
- 高度 中位数 1024，观测区间 560 - 1600，5 个样本
