---
name: unknown_workflow_video_sampler_clip_27
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.885062
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LucyConditionConcatNode, ModelSamplingSD3, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/Lucy Edit视频编辑工作流_1970095736555794433.json, 平台全量/Lucy Edit视频编辑（加物体）_1972725228923232258.json, 平台全量/Lucy Edit视频编辑（替换服饰颜色与材质）_1972719987293134849.json, 平台全量/Lucy-Edit视频编辑（增减物品，人物替换，风格转换）_1969948773789167618.json, 平台全量/basic-lucy-edit video edit workflow_1970148731762974721.json, 视频生成/图生视频/Lucy Edit视频换装（手动提示词）_2013153772620488705.json, 视频生成/图生视频/Lucy+Edit视频换装（文本控制）V1.1_2064156316251283458.json, 视频生成/图生视频/视频换装（文本控制）V1.1_2080106360926199809.json, 视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_1969845849503264769.json, 视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051828457667088386.json, 视频生成/文生视频/Lucy Edit视频换装（文本控制）V1.1_2051846229662937090.json, 视频生成/文生视频/Lucy Edit视频编辑（P视频神器）_1970021776442990594.json, 视频生成/文生视频/Lucy Edit视频编辑（主体替换）V1.1_1969945935545573378.json, 视频生成/文生视频/Lucy Edit视频编辑（全局改变-概率抽卡）V1.1_1969954015096283137.json, 视频生成/文生视频/Lucy Edit视频编辑（物体添加）V1.1_1969947895673856001.json, 视频生成/文生视频/Lucy Edit视频编辑（颜色与材质）V1.1_1969948275333865474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（平台全量/Lucy Edit视频编辑工作流_1970095736555794433.json、平台全量/Lucy Edit视频编辑（加物体）_1972725228923232258.json、平台全量/Lucy Edit视频编辑（替换服饰颜色与材质）_1972719987293134849.json、平台全量/Lucy-Edit视频编辑（增减物品，人物替换，风格转换）_1969948773789167618.json、平台全量/basic-lucy-edit video edit workflow_1970148731762974721.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：89%

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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 15/16 个有
- `PrimitiveInt` —— 15/16 个有
- `ImageConcanate` —— 13/16 个有
- `JWInteger` —— 13/16 个有
- `PrimitiveFloat` —— 13/16 个有
- `CR Prompt Text` —— 2/16 个有
- `ImageResizeKJv2` —— 2/16 个有
- `ImageStitch` —— 1/16 个有
- `JWFloatToInteger` —— 1/16 个有
- `VHS_VideoInfo` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 16 | 100% |
| Prompt 约束强度(CFG) | 5 | 3 - 5 | 16 | 90% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，16 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 3 - 5，16 个样本，取值集中（一致性 90%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
