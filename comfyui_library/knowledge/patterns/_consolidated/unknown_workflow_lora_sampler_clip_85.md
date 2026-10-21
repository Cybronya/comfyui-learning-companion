---
name: unknown_workflow_lora_sampler_clip_85
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.73575
common_nodes: [CLIPLoader, CLIPTextEncode, ComfySwitchNode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/KREA2 TURBO 图图最强文生图工作流（提示词增强 + Krea2T 双增强）_2072516698963537921.json, 图片生成/文生图/Qwen Image 港风霓虹街景_2058558846393741314.json, 图片生成/文生图/image_qwen_image_2099207941726498817.json, 图片生成/文生图/黑丝的专属工作流_2090809889026306049.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_85

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/KREA2 TURBO 图图最强文生图工作流（提示词增强 + Krea2T 双增强）_2072516698963537921.json、图片生成/文生图/Qwen Image 港风霓虹街景_2058558846393741314.json、图片生成/文生图/image_qwen_image_2099207941726498817.json、图片生成/文生图/黑丝的专属工作流_2090809889026306049.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfyUI-Krea2T-Enhancer` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `EmptyImage` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `StringConcatenate` —— 2/4 个有
- `Switch image [Crystools]` —— 2/4 个有
- `TextGenerate` —— 2/4 个有
- `ResolutionSelector` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 50 | 4 | 20% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 8 | 4 | 18% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 50，4 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 8，4 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
