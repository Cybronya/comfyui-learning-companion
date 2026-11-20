---
name: unknown_workflow_lora_sampler_checkpoint_11
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.930333
common_nodes: [CFGNorm, CLIPLoader, CheckpointLoaderSimple, EmptySD3LatentImage, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenMultiangleCameraNode, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader, easy promptList, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/（自用-（自用））Qwen 2511 Aio N版V19姿势_2011713822649753601.json, 图片生成/图生图/（自用）Qwen 2511 Aio N版V19 multi angle可视化角度编辑V2_2009742592530980866.json, 图片生成/文生图/Qwen 2511 multi angle可视化角度编辑_2010599039884075009.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_11

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/（自用-（自用））Qwen 2511 Aio N版V19姿势_2011713822649753601.json、图片生成/图生图/（自用）Qwen 2511 Aio N版V19 multi angle可视化角度编辑V2_2009742592530980866.json、图片生成/文生图/Qwen 2511 multi angle可视化角度编辑_2010599039884075009.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CheckpointLoaderSimple`
- `EmptySD3LatentImage`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`
- `easy promptList`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `DuckHideNode` —— 2/3 个有
- `TT_img_enc` —— 2/3 个有
- `TT_img_enc_v2` —— 2/3 个有
- `Int` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
