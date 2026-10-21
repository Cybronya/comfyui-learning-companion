---
name: unknown_workflow_sampler_checkpoint_vae_2
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.872
common_nodes: [CR Prompt Text, CheckpointLoaderSimple, EmptyLatentImage, Int, KSampler, PrimitiveInt, SaveImage, TT_img_enc, TT_img_enc_v2, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: [Text Multiline, CR Prompt Text]
members: [图片生成/文生图/1977742873120702466.json, 图片生成/文生图/1978126522127147010.json, 图片生成/文生图/1980187939579793410.json, 图片生成/文生图/1985324572306194434.json, 图片生成/文生图/（含本地解码）QwenEdit AIO V14.1  文生图、图声图，单图编辑，多图编辑。_2002288657212010497.json, 图片生成/文生图/（含本地解码）QwenEdit AIO V16  文生图、图声图，单图编辑，多图编辑。_2004214698298011650.json, 图片生成/文生图/（自用）QwenEdit AIO V4文生图_2057843179868745729.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1977742873120702466.json、图片生成/文生图/1978126522127147010.json、图片生成/文生图/1980187939579793410.json、图片生成/文生图/1985324572306194434.json、图片生成/文生图/（含本地解码）QwenEdit AIO V14.1  文生图、图声图，单图编辑，多图编辑。_2002288657212010497.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `Int`
- `KSampler`
- `PrimitiveInt`
- `SaveImage`
- `TT_img_enc`
- `TT_img_enc_v2`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 7 | 100% |
| 高度 | 512 | 512 - 512 | 7 | 100% |
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler_ancestral | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Text Multiline、CR Prompt Text
