---
name: text_to_image_lora_sampler_clip_405
type: Text To Image
frequency: 5
level: moderate
coverage: 0.5254
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, Create Grid Image from Batch, EmptyLatentImage, GetNode, ImpactMakeImageList, Int, JoinStrings, KSampler, Lora Loader, PreviewImage, PrimitiveInt, SaveImage, Seed_, SetNode, UNETLoader, VAEDecode, VAELoader, easy convertAnything, easy imageListToImageBatch, easy rangeFloat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Lora-xy测试工作流_2073237872278335489.json, 图片生成/文生图/Qwen_Lora测试工作流(V-Zion)_1997514435805790210.json, 图片生成/文生图/Z-image Base Lora-xy测试工作流_2073313146638520322.json, 图片生成/文生图/qwenlora模型文生图xy测试工作流v1_1970132982562496514.json, 图片生成/文生图/wan2.2低噪lora模型文生图xy测试工作流v2_1960228137802084354.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_405

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Qwen Lora-xy测试工作流_2073237872278335489.json、图片生成/文生图/Qwen_Lora测试工作流(V-Zion)_1997514435805790210.json、图片生成/文生图/Z-image Base Lora-xy测试工作流_2073313146638520322.json、图片生成/文生图/qwenlora模型文生图xy测试工作流v1_1970132982562496514.json、图片生成/文生图/wan2.2低噪lora模型文生图xy测试工作流v2_1960228137802084354.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：53%

## 共有节点

全部 5 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `Create Grid Image from Batch`
- `EmptyLatentImage`
- `GetNode`
- `ImpactMakeImageList`
- `Int`
- `JoinStrings`
- `KSampler`
- `Lora Loader`
- `PreviewImage`
- `PrimitiveInt`
- `SaveImage`
- `Seed_`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy convertAnything`
- `easy imageListToImageBatch`
- `easy rangeFloat`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `ReActorImageDublicator` —— 4/5 个有
- `TextInput_` —— 3/5 个有
- `ConstrainImage|pysssss` —— 2/5 个有
- `GetImageSize` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `JjkText` —— 2/5 个有
- `PrimitiveString` —— 2/5 个有
- `RH_Captioner` —— 2/5 个有
- `Text` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `ModelSamplingSD3` —— 1/5 个有
- `PMRF` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 5 | 69% |
| 高度 | 1024 | 512 - 1024 | 5 | 69% |
| 采样步数 | 8 | 8 - 25 | 5 | 44% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 5 | 25% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | beta | - | 5 | 40% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，5 个样本
- 高度 中位数 1024，观测区间 512 - 1024，5 个样本
- 采样步数 中位数 8，观测区间 8 - 25，5 个样本，取值分散，一致性仅 44%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 beta，5 个样本，一致性 40%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（16/5 个样本）：Steps较低可能导致细节不足
