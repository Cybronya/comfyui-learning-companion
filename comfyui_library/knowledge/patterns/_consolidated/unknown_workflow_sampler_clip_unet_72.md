---
name: unknown_workflow_sampler_clip_unet_72
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.925111
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/千问2512文生图海报、图片设计_2093310820385116161.json, 图片生成/文生图/小红书风格加黑丝_2003393169008041986.json, 图片生成/文生图/小腰精_01_2037141728938958849.json, 图片生成/文生图/小腰精_胸部_2103720016867848193.json, 图片生成/文生图/微软-Lens VS Z Image 文生图工作流_2059584817586593793.json, 图片生成/文生图/文生图  boogu_2067835171948290050.json, 图片生成/文生图/自己用小i文生图：Qwen+Lora_2021825579867185154.json, 图片生成/文生图/菜单菜品商品电商人物动物品文生图 【用积分】_2074679846487289857.json, 视频生成/图生视频/1955581722751483906.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_72

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/千问2512文生图海报、图片设计_2093310820385116161.json、图片生成/文生图/小红书风格加黑丝_2003393169008041986.json、图片生成/文生图/小腰精_01_2037141728938958849.json、图片生成/文生图/小腰精_胸部_2103720016867848193.json、图片生成/文生图/微软-Lens VS Z Image 文生图工作流_2059584817586593793.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 7/9 个有
- `ConditioningZeroOut` —— 6/9 个有
- `EmptySD3LatentImage` —— 6/9 个有
- `LoraLoader` —— 6/9 个有
- `PreviewImage` —— 4/9 个有
- `QwenImageLatentAspectRatio` —— 3/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `FluxResolutionNode` —— 1/9 个有
- `RH_LLMAPI_NODE` —— 1/9 个有
- `VideoLinearCFGGuidance` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 40 | 9 | 7% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 9 | 5% |
| 采样算法 | euler | - | 9 | 67% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 模型强度 | 1 | 0.8 - 1 | 6 | 92% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 40，9 个样本，取值分散，一致性仅 7%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，9 个样本，取值分散，一致性仅 5%
- 采样算法 最常用 euler，9 个样本，一致性 67%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，6 个样本，取值集中（一致性 92%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
