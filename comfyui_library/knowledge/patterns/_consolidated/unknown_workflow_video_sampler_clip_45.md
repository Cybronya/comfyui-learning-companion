---
name: unknown_workflow_video_sampler_clip_45
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.856818
common_nodes: [ApplySageAttention, CLIPTextEncode, CR Prompt Text, CheckpointLoaderSimple, JWInteger, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, SaveImage, TT_img_enc, VAEDecode, WanVaceToVideo, WanVideoVACEStartToEndFrame]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text]
members: [视频生成/图生视频/1985334147310829570.json, 视频生成/图生视频/1973021430713593858.json, 视频生成/图生视频/1973020589118066690.json, 视频生成/图生视频/1974823195108880385.json, 视频生成/图生视频/1976907332506587138.json, 视频生成/图生视频/1975831152592334850.json, 视频生成/图生视频/1975830994022436866.json, 视频生成/图生视频/1977747995724840961.json, 视频生成/图生视频/1967932359611940866.json, 视频生成/图生视频/1968344636660035586.json, 视频生成/文生视频/1974823222036271106.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_45

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1985334147310829570.json、视频生成/图生视频/1973021430713593858.json、视频生成/图生视频/1973020589118066690.json、视频生成/图生视频/1974823195108880385.json、视频生成/图生视频/1976907332506587138.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `ApplySageAttention`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `JWInteger`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveImage`
- `TT_img_enc`
- `VAEDecode`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`

**可变部分**（部分 workflow 才有）：
- `HunyuanVideoFoley` —— 4/11 个有
- `LayerUtility: PurgeVRAM V2` —— 4/11 个有
- `CLIPLoader` —— 2/11 个有
- `TT_img_enc_v2` —— 2/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | ipndm | - | 11 | 55% |
| 调度器 | sgm_uniform | - | 11 | 55% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，11 个样本，一致性 55%
- 调度器 最常用 sgm_uniform，11 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、CR Prompt Text
