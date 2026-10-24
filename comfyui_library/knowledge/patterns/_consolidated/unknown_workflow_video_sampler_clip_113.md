---
name: unknown_workflow_video_sampler_clip_113
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9332
common_nodes: [ApplySageAttention, CLIPTextEncode, CheckpointLoaderSimple, KSampler, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/50.tonnie-Wan2.2 AiO图生视频_2007607946225651714.json, 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V3图生视频极速版_1969938692712374273.json, 视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V4图生视频极速版_1973027412923518977.json, 视频生成/图生视频/Wan2.2-Rapid-AiO图生视频_1987337054050824194.json, 视频生成/文生视频/Wan2.2-Rapid-AiO文生视频_1987862873089224706.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_113

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/50.tonnie-Wan2.2 AiO图生视频_2007607946225651714.json、视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V3图生视频极速版_1969938692712374273.json、视频生成/图生视频/Wan2.2 Rapid-AIO-Mega V4图生视频极速版_1973027412923518977.json、视频生成/图生视频/Wan2.2-Rapid-AiO图生视频_1987337054050824194.json、视频生成/文生视频/Wan2.2-Rapid-AiO文生视频_1987862873089224706.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `ApplySageAttention`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `WanVideoVACEStartToEndFrame` —— 4/5 个有
- `INTConstant` —— 3/5 个有
- `LayerUtility: TextJoin` —— 3/5 个有
- `SimpleMath+` —— 3/5 个有
- `Wan22PromptSelector` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `MuyeTextEditOutput` —— 2/5 个有
- `CR Text` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
