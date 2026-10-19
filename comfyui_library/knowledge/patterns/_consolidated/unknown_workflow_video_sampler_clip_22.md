---
name: unknown_workflow_video_sampler_clip_22
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.880563
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LucyConditionConcatNode, ModelSamplingSD3, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [视频生成/图生视频/1969945935545573378.json, 视频生成/图生视频/1969947895673856001.json, 视频生成/图生视频/1969948275333865474.json, 视频生成/图生视频/1969954015096283137.json, 视频生成/图生视频/2013153772620488705.json, 视频生成/图生视频/2064156316251283458.json, 视频生成/图生视频/2080106360926199809.json, 视频生成/文生视频/1969845849503264769.json, 视频生成/文生视频/1969945935545573378.json, 视频生成/文生视频/1969947895673856001.json, 视频生成/文生视频/1969948275333865474.json, 视频生成/文生视频/1969954015096283137.json, 视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051828457667088386.json, 视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051846229662937090.json, 视频生成/文生视频/1970021776442990594.json, 音频生成/音频生成/一句话编辑你的视频，放弃vace吧_1970462951100608514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_22

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/1969945935545573378.json、视频生成/图生视频/1969947895673856001.json、视频生成/图生视频/1969948275333865474.json、视频生成/图生视频/1969954015096283137.json、视频生成/图生视频/2013153772620488705.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LucyConditionConcatNode`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 15/16 个有
- `JWInteger` —— 15/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 15/16 个有
- `PrimitiveInt` —— 15/16 个有
- `PrimitiveFloat` —— 14/16 个有
- `VHS_VideoInfo` —— 2/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 16 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2
