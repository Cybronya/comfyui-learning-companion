---
name: unknown_workflow_lora_sampler_unet_140
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.877
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen-2511 Cosplay任何角色_2028679612187811842.json, 图片生成/图生图/qwen-edit-2509-动漫转真人_1988122840039845889.json, 图片生成/图生图/冷蓝夜景CCD_2075043329271750658.json, 图片生成/图生图/千问Edit2509图像编辑-多图结婚照_1971036029203423233.json, 图片生成/图生图/多人场景融合-千问Edit2509图像编辑_1970822561934282754.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_140

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/qwen-2511 Cosplay任何角色_2028679612187811842.json、图片生成/图生图/qwen-edit-2509-动漫转真人_1988122840039845889.json、图片生成/图生图/冷蓝夜景CCD_2075043329271750658.json、图片生成/图生图/千问Edit2509图像编辑-多图结婚照_1971036029203423233.json、图片生成/图生图/多人场景融合-千问Edit2509图像编辑_1970822561934282754.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `ImageConcanate` —— 3/5 个有
- `ImageStitch` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `Anything Everywhere3` —— 2/5 个有
- `CR Text` —— 2/5 个有
- `PrimitiveInt` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `孤海图像缩放按像素` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 5 | 42% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 5 | 61% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | beta57 | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，5 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 beta57，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
