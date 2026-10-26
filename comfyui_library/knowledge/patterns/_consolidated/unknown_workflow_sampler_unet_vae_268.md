---
name: unknown_workflow_sampler_unet_vae_268
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.876333
common_nodes: [CLIPLoader, CR Text, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 换头换脸｜6步加速版_2104126864011915266.json, 图片生成/图生图/Qwen-image2.1  抠图工作流，指哪扣哪！_2102380656931196930.json, 图片生成/图生图/自动抠图 Qwen-image2.1_2112044955593166850.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_268

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 换头换脸｜6步加速版_2104126864011915266.json、图片生成/图生图/Qwen-image2.1  抠图工作流，指哪扣哪！_2102380656931196930.json、图片生成/图生图/自动抠图 Qwen-image2.1_2112044955593166850.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
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

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `ConcatTextOfUtils` —— 1/3 个有
- `LayerUtility: TextJoin` —— 1/3 个有
- `LoraLoaderBypassModelOnly` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `QwenImage21SageAttentionT8` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 6 - 25 | 3 | 52% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1200 | 3 | 92% |
| 高度 | 1024 | 560 - 1600 | 3 | 60% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 6 - 25，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1200，3 个样本，取值集中（一致性 92%）
- 高度 中位数 1024，观测区间 560 - 1600，3 个样本
