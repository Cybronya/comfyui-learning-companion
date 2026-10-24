---
name: unknown_workflow_lora_sampler_unet_116
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.915333
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/模特套图工作流_1987890764711661569.json, 图片生成/图生图/模特套图工作流升级款_1995150525064785922.json, 图片生成/图生图/模特套图，一张可以生成9张不同姿势_2058598930799222786.json, 图片生成/图生图/超强写真套图_1995145813921869825.json, 图片生成/图生图/👾怪獸-IP打造神器-固定人物多场景照片👾_1992556792353976322.json, 图片生成/图生图/👾怪獸-圣诞节写真特级👾_1996148103365476354.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_116

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/模特套图工作流_1987890764711661569.json、图片生成/图生图/模特套图工作流升级款_1995150525064785922.json、图片生成/图生图/模特套图，一张可以生成9张不同姿势_2058598930799222786.json、图片生成/图生图/超强写真套图_1995145813921869825.json、图片生成/图生图/👾怪獸-IP打造神器-固定人物多场景照片👾_1992556792353976322.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JDCN_StringToList` —— 3/6 个有
- `RHHiddenNodes` —— 3/6 个有
- `RH_LLMAPI_NODE` —— 3/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `AILab_QwenVL` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 6 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta57 | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta57，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
