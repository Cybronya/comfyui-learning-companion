---
name: unknown_workflow_video_lora_sampler_313
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.97475
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, CheckpointLoaderSimple, JWFloat, JWInteger, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, VAEDecode, VHS_VideoCombine, WanImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/live动图-图生视频_wan2.2_2095005372602994689.json, 视频生成/图生视频/图生视频极速版 人物表情真实自然 Wan2.2+All-in-one_2039525725417508865.json, 视频生成/图生视频/图生视频极速版+人物表情真实自然+Wan2.2+All-in-one_2046422966447116289.json, 视频生成/图生视频/图生视频极速版_2045034745590980609.json, 视频生成/图生视频/极速版图生视频 Wan2.2+All-in-one  人物模特表情真实自然_2039532814231670785.json, 视频生成/文生视频/Wan2.2+All-in-one 极速版 图生视频_2069595721451528193.json, 视频生成/文生视频/Wan2.2+All-in-one 极速版 图生视频_2070390350711189506.json, 视频生成/文生视频/极速版 图生视频Wan2.2+All-in-one_2044241810842718210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_313

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/live动图-图生视频_wan2.2_2095005372602994689.json、视频生成/图生视频/图生视频极速版 人物表情真实自然 Wan2.2+All-in-one_2039525725417508865.json、视频生成/图生视频/图生视频极速版+人物表情真实自然+Wan2.2+All-in-one_2046422966447116289.json、视频生成/图生视频/图生视频极速版_2045034745590980609.json、视频生成/图生视频/极速版图生视频 Wan2.2+All-in-one  人物模特表情真实自然_2039532814231670785.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `JWFloat`
- `JWInteger`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `JoinStrings` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `Qwen3_VQA` —— 1/8 个有
- `RH_Captioner` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `TextInput_` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | sa_solver | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
