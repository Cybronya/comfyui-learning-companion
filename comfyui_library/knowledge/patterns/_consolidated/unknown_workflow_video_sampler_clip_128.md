---
name: unknown_workflow_video_sampler_clip_128
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9112
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LucyConditionConcatNode, ModelSamplingSD3, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/-lucy-edit-视频编辑-换装-换物件_1970803195431841793.json, 平台全量/Luch Edit视频编辑一句话修改视频_1969980913499205634.json, 平台全量/Lucy Edit一句话编辑视频_1969990600990859266.json, 平台全量/Lucy Edit自然语言编辑视频_1970020731989991425.json, 平台全量/Lucy Edit视频换装（主体替换）V1_1969941601395109889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_128

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/-lucy-edit-视频编辑-换装-换物件_1970803195431841793.json、平台全量/Luch Edit视频编辑一句话修改视频_1969980913499205634.json、平台全量/Lucy Edit一句话编辑视频_1969990600990859266.json、平台全量/Lucy Edit自然语言编辑视频_1970020731989991425.json、平台全量/Lucy Edit视频换装（主体替换）V1_1969941601395109889.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LucyConditionConcatNode`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 4/5 个有
- `JWInteger` —— 3/5 个有
- `PrimitiveFloat` —— 3/5 个有
- `PrimitiveInt` —— 2/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `Int` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `SetNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 5 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
