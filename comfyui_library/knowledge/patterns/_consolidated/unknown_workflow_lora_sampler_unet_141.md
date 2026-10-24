---
name: unknown_workflow_lora_sampler_unet_141
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8366
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键换脸工作流V1_1955881410198425602.json, 图片生成/图生图/雪1.tonnie-edit 2509-提示词换装_2002550729497821185.json, 图片生成/图生图/雪10.tonnie-edit 2509-创建人物手办_2002809078772559873.json, 图片生成/图生图/雪2.tonnie-edit 2509-毛坯房装修_2002555895177441282.json, 图片生成/图生图/雪3.tonnie-edit 2509-参考图换装_2002559549150228481.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_141

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/一键换脸工作流V1_1955881410198425602.json、图片生成/图生图/雪1.tonnie-edit 2509-提示词换装_2002550729497821185.json、图片生成/图生图/雪10.tonnie-edit 2509-创建人物手办_2002809078772559873.json、图片生成/图生图/雪2.tonnie-edit 2509-毛坯房装修_2002555895177441282.json、图片生成/图生图/雪3.tonnie-edit 2509-参考图换装_2002559549150228481.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `FaceAnalysisModels` —— 1/5 个有
- `FaceBoundingBox` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `easy imageScaleDown` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 5 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 768 | 768 - 768 | 4 | 100% |
| 高度 | 1280 | 1024 - 1280 | 4 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 768，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1024 - 1280，4 个样本，取值集中（一致性 91%）
