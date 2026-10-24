---
name: unknown_workflow_video_sampler_clip_38
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.896417
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LucyConditionConcatNode, ModelSamplingSD3, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Lucy Edit视频换装（手动提示词）_2013153772620488705.json, 视频生成/图生视频/Lucy+Edit视频换装（文本控制）V1.1_2064156316251283458.json, 视频生成/图生视频/视频换装（文本控制）V1.1_2080106360926199809.json, 视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_1969845849503264769.json, 视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051828457667088386.json, 视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051846229662937090.json, 视频生成/文生视频/Lucy Edit视频编辑（P视频神器）_1970021776442990594.json, 视频生成/文生视频/Lucy Edit视频编辑（主体替换）V1.1_1969945935545573378.json, 视频生成/文生视频/Lucy Edit视频编辑（全局改变-概率抽卡）V1.1_1969954015096283137.json, 视频生成/文生视频/Lucy Edit视频编辑（物体添加）V1.1_1969947895673856001.json, 视频生成/文生视频/Lucy Edit视频编辑（颜色与材质）V1.1_1969948275333865474.json, 音频生成/音频生成/一句话编辑你的视频，放弃vace吧_1970462951100608514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_38

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Lucy Edit视频换装（手动提示词）_2013153772620488705.json、视频生成/图生视频/Lucy+Edit视频换装（文本控制）V1.1_2064156316251283458.json、视频生成/图生视频/视频换装（文本控制）V1.1_2080106360926199809.json、视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_1969845849503264769.json、视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051828457667088386.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 12 个 workflow 都包含：
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
- `ImageConcanate` —— 11/12 个有
- `JWInteger` —— 11/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `PrimitiveFloat` —— 11/12 个有
- `PrimitiveInt` —— 11/12 个有
- `VHS_VideoInfo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 12 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
