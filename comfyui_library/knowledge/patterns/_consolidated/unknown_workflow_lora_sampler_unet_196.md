---
name: unknown_workflow_lora_sampler_unet_196
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9185
common_nodes: [CLIPLoader, JDCN_StringToList, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, RH_LLMAPI_NODE, SaveImage, ShowText|pysssss, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/模特套图工作流_1987890764711661569.json, 图片生成/图生图/模特套图工作流升级款_1995150525064785922.json, 图片生成/图生图/模特套图，一张可以生成9张不同姿势_2058598930799222786.json, 视频生成/图生视频/图生视频IP一致性 真实自然_2004525590436868097.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_196

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/模特套图工作流_1987890764711661569.json、图片生成/图生图/模特套图工作流升级款_1995150525064785922.json、图片生成/图生图/模特套图，一张可以生成9张不同姿势_2058598930799222786.json、视频生成/图生视频/图生视频IP一致性 真实自然_2004525590436868097.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `JDCN_StringToList`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `CR Text Replace` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `ProcessString` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta57 | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta57，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
