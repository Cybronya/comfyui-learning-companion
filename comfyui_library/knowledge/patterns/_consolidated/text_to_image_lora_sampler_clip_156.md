---
name: text_to_image_lora_sampler_clip_156
type: Text To Image
frequency: 6
level: moderate
coverage: 0.7535
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Int, JjkText, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, SaveImage, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: [easy cleanGpuUsed, LayerUtility: TextJoin]
members: [图片生成/文生图/1955571767731523585.json, 图片生成/文生图/1955679085127241729.json, 图片生成/文生图/1956241572574756865.json, 图片生成/文生图/1957351833759051778.json, 图片生成/文生图/1978645121417760769.json, 图片生成/文生图/1979863423804674049.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_156

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1955571767731523585.json、图片生成/文生图/1955679085127241729.json、图片生成/文生图/1956241572574756865.json、图片生成/文生图/1957351833759051778.json、图片生成/文生图/1978645121417760769.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Int`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `ImpactSwitch` —— 5/6 个有
- `LoraLoader` —— 3/6 个有
- `TextCombinerTwo` —— 3/6 个有
- `UNETLoader` —— 3/6 个有
- `UnetLoaderGGUF` —— 3/6 个有
- `RH_Prompter` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `AddWater_MarkNode` —— 1/6 个有
- `DifferentialDiffusion` —— 1/6 个有
- `LayerUtility: TextJoin` —— 1/6 个有
- `LoadImage` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.8 | 0.7 - 1 | 3 | 85% |
| LoRA 文本强度 | 0.8 | 0.5 - 1 | 3 | 73% |
| 宽度 | 512 | 512 - 512 | 6 | 100% |
| 高度 | 512 | 512 - 512 | 6 | 100% |
| 采样步数 | 4 | 4 - 35 | 6 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.8，观测区间 0.7 - 1，3 个样本，取值集中（一致性 85%）
- LoRA 文本强度 中位数 0.8，观测区间 0.5 - 1，3 个样本
- 宽度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 35，6 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、LayerUtility: TextJoin
