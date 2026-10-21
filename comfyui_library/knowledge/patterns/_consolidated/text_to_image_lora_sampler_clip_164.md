---
name: text_to_image_lora_sampler_clip_164
type: Text To Image
frequency: 7
level: moderate
coverage: 0.768286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Int, JjkText, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, SaveImage, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: [easy cleanGpuUsed, LayerUtility: TextJoin]
members: [图片生成/文生图/1955571767731523585.json, 图片生成/文生图/1955679085127241729.json, 图片生成/文生图/1956241572574756865.json, 图片生成/文生图/1957351833759051778.json, 图片生成/文生图/1978645121417760769.json, 图片生成/文生图/1979863423804674049.json, 图片生成/文生图/Qwen 千问文生图_2000589481319202818.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_164

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1955571767731523585.json、图片生成/文生图/1955679085127241729.json、图片生成/文生图/1956241572574756865.json、图片生成/文生图/1957351833759051778.json、图片生成/文生图/1978645121417760769.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 7 个 workflow 都包含：
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
- `ConditioningZeroOut` —— 6/7 个有
- `ImpactSwitch` —— 6/7 个有
- `LoraLoader` —— 4/7 个有
- `TextCombinerTwo` —— 4/7 个有
- `UnetLoaderGGUF` —— 4/7 个有
- `UNETLoader` —— 3/7 个有
- `RH_Prompter` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `AddWater_MarkNode` —— 1/7 个有
- `DifferentialDiffusion` —— 1/7 个有
- `LayerUtility: TextJoin` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.75 | 0.7 - 1 | 4 | 85% |
| LoRA 文本强度 | 0.65 | 0.5 - 1 | 4 | 70% |
| 宽度 | 512 | 512 - 512 | 7 | 100% |
| 高度 | 512 | 512 - 512 | 7 | 100% |
| 采样步数 | 4 | 4 - 35 | 7 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0.75，观测区间 0.7 - 1，4 个样本，取值集中（一致性 85%）
- LoRA 文本强度 中位数 0.65，观测区间 0.5 - 1，4 个样本
- 宽度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 35，7 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、LayerUtility: TextJoin
