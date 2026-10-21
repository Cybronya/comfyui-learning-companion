---
name: unknown_workflow_lora_sampler_clip_10
type: Unknown Workflow
frequency: 16
level: weak
coverage: 0.884625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Prompt Text, Label (rgthree)]
members: [图片生成/文生图/1957313561636827138.json, 图片生成/文生图/1962804112075173889.json, 图片生成/文生图/1963167950662512641.json, 图片生成/文生图/1965257014656028674.json, 图片生成/文生图/1966317820562878466.json, 图片生成/文生图/1966728561858162689.json, 图片生成/文生图/1968571302049140738.json, 图片生成/文生图/1971395682378661889.json, 图片生成/文生图/1977995730776379394.json, 图片生成/文生图/1980164055954526209.json, 图片生成/文生图/1981265802265616385.json, 图片生成/文生图/Flow-DPO LoRA工作流：AI人像终于不像塑料了！这个LoRA让光照秒变真实✨_2028104630768504833.json, 图片生成/文生图/Qwen-Image-2512文生图大模型：人物更真实、毛发更自然、文字排版更准确！_2006620335499644929.json, 图片生成/文生图/Qwen-rebalance文生图_1999689524483682305.json, 图片生成/文生图/Z 手持质感 文生图_2021145496873607169.json, 图片生成/文生图/Z-Image-Turbo LoRA 出图+放大_2018944118063370242.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/1957313561636827138.json、图片生成/文生图/1962804112075173889.json、图片生成/文生图/1963167950662512641.json、图片生成/文生图/1965257014656028674.json、图片生成/文生图/1966317820562878466.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 14/16 个有
- `ConditioningZeroOut` —— 4/16 个有
- `Label (rgthree)` —— 3/16 个有
- `SeedVR2` —— 3/16 个有
- `SeedVR2BlockSwap` —— 3/16 个有
- `CR Prompt Text` —— 2/16 个有
- `Image Comparer (rgthree)` —— 1/16 个有
- `ImpactInt` —— 1/16 个有
- `SeedVR2ExtraArgs` —— 1/16 个有
- `TextConcatenator` —— 1/16 个有
- `easy cleanGpuUsed` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 50 | 16 | 10% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 16 | 40% |
| 采样算法 | euler | - | 16 | 81% |
| 调度器 | simple | - | 16 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 50，16 个样本，取值分散，一致性仅 10%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，16 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler，16 个样本，一致性 81%
- 调度器 最常用 simple，16 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 高发问题（10/16 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text、Label (rgthree)
