---
name: unknown_workflow_sampler_checkpoint_vae_14
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.941375
common_nodes: [CR Prompt Text, CheckpointLoaderSimple, EmptyLatentImage, Int, KSampler, PrimitiveInt, SaveImage, TT_img_enc, TT_img_enc_v2, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/（自用）QwenEdit AIO V5.2文生图_1982145276716695554.json, 图片生成/文生图/（含本地解码）QwenEdit AIO V14.1  文生图、图声图，单图编辑，多图编辑。_2002288657212010497.json, 图片生成/文生图/（含本地解码）QwenEdit AIO V16  文生图、图声图，单图编辑，多图编辑。_2004214698298011650.json, 图片生成/文生图/（自用）N版QwenEdit AIO V5.1文生图_1980187939579793410.json, 图片生成/文生图/（自用）QwenEdit AIO V4文生图_1977742873120702466.json, 图片生成/文生图/（自用）QwenEdit AIO V4文生图_2057843179868745729.json, 图片生成/文生图/（自用）QwenEdit AIO V5文生图_1978126522127147010.json, 图片生成/文生图/（自用）QwenEdit AIO V7.1文生图_1985324572306194434.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_14

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/（自用）QwenEdit AIO V5.2文生图_1982145276716695554.json、图片生成/文生图/（含本地解码）QwenEdit AIO V14.1  文生图、图声图，单图编辑，多图编辑。_2002288657212010497.json、图片生成/文生图/（含本地解码）QwenEdit AIO V16  文生图、图声图，单图编辑，多图编辑。_2004214698298011650.json、图片生成/文生图/（自用）N版QwenEdit AIO V5.1文生图_1980187939579793410.json、图片生成/文生图/（自用）QwenEdit AIO V4文生图_1977742873120702466.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 8 个 workflow 都包含：
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
- `LoadImage` —— 3/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 8 | 100% |
| 高度 | 512 | 512 - 512 | 8 | 100% |
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler_ancestral | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，8 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
