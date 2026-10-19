---
name: unknown_workflow_video_lora_clip_2
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.99325
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, VAEDecode, VHS_VideoCombine, WanImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2039989765587607554.json, 视频生成/图生视频/1985889345833971714.json, 视频生成/图生视频/2069950709994442753.json, 视频生成/图生视频/2044586130233888770.json, 视频生成/图生视频/2042866151662821378.json, 视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_1983515933761314818.json, 视频生成/图生视频/2041324315588698113.json, 视频生成/图生视频/2069791627677356033.json, 视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_2099699527749038082.json, 视频生成/图生视频/图生视频Wan2.2+All-in-one极速版_2099791658589188097.json, 视频生成/图生视频/2046033851276857346.json, 视频生成/图生视频/2062575894211948546.json, 视频生成/图生视频/2044590119671304193.json, 视频生成/图生视频/2039525725417508865.json, 视频生成/图生视频/2046422966447116289.json, 视频生成/图生视频/2045034745590980609.json, 视频生成/图生视频/2039532814231670785.json, 视频生成/文生视频/Wan2.2+All-in-one 极速版 图生视频_2069595721451528193.json, 视频生成/文生视频/Wan2.2+All-in-one 极速版 图生视频_2070390350711189506.json, 视频生成/文生视频/极速版 图生视频Wan2.2+All-in-one_2044241810842718210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_clip_2

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/2039989765587607554.json、视频生成/图生视频/1985889345833971714.json、视频生成/图生视频/2069950709994442753.json、视频生成/图生视频/2044586130233888770.json、视频生成/图生视频/2042866151662821378.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 19/20 个有
- `JWFloat` —— 19/20 个有
- `KSampler` —— 19/20 个有
- `MathExpression|pysssss` —— 19/20 个有
- `VAELoader` —— 11/20 个有
- `LoadLatent` —— 10/20 个有
- `SaveImage` —— 7/20 个有
- `ImageFromBatch+` —— 1/20 个有
- `KSamplerAdvanced` —— 1/20 个有
- `PrimitiveBoolean` —— 1/20 个有
- `TT_img_enc_v2` —— 1/20 个有
- `UNETLoader` —— 1/20 个有
- `ZML_SwitchOutput` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 19 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 20 | 13% |
| 采样算法 | sa_solver | - | 20 | 95% |
| 调度器 | beta | - | 20 | 95% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，20 个样本，取值分散，一致性仅 13%
- 采样算法 最常用 sa_solver，20 个样本，一致性 95%
- 调度器 最常用 beta，20 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（19/20 个样本）：Steps较低可能导致细节不足
