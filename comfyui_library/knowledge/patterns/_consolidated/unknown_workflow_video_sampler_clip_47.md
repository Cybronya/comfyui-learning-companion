---
name: unknown_workflow_video_sampler_clip_47
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.781909
common_nodes: [CLIPLoader, CLIPTextEncode, ImageStitch, KSampler, LayerUtility: TextJoin, LucyConditionConcatNode, ModelSamplingSD3, RH_LLMAPI_NODE, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [平台全量/Lucy-Edit视频开源编辑工具_1970321565307052034.json, 平台全量/【Gensor·AI】lucy-edit视频编辑_1970687667228844033.json, 平台全量/【Lucy-Edit视频编辑】服装配饰场景角色替换和编辑_1970760016120737794.json, 平台全量/一句话视频场景编辑-Lucy-Edit视频编辑_1969914107665281026.json, 平台全量/电商服装配饰场景角色替换和编辑-Lucy-Edit视频编辑_1968834962847932418.json, 平台全量/电商服装配饰场景角色替换和编辑-Lucy-Edit视频编辑_1971003798988693506.json, 平台全量/电商服装配饰场景角色替换和视频编辑_2039172218898354178.json, 平台全量/角色替换-Lucy-Edit视频编辑_1970084461931077634.json, 视频生成/文生视频/电商服装配饰场景角色替换和编辑-Lucy-Edit视频编辑_1986343278314475522.json, 视频生成/文生视频/电商服装配饰场景角色替换和编辑-Lucy-Edit视频编辑_1986355209393893377.json, 视频生成/文生视频/电商服装配饰场景角色替换和编辑-Lucy-Edit视频编辑_1986362481859850242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（平台全量/Lucy-Edit视频开源编辑工具_1970321565307052034.json、平台全量/【Gensor·AI】lucy-edit视频编辑_1970687667228844033.json、平台全量/【Lucy-Edit视频编辑】服装配饰场景角色替换和编辑_1970760016120737794.json、平台全量/一句话视频场景编辑-Lucy-Edit视频编辑_1969914107665281026.json、平台全量/电商服装配饰场景角色替换和编辑-Lucy-Edit视频编辑_1968834962847932418.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageStitch`
- `KSampler`
- `LayerUtility: TextJoin`
- `LucyConditionConcatNode`
- `ModelSamplingSD3`
- `RH_LLMAPI_NODE`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 10/11 个有
- `JWFloatToInteger` —— 10/11 个有
- `PrimitiveFloat` —— 10/11 个有
- `PrimitiveInt` —— 10/11 个有
- `Text Multiline` —— 10/11 个有
- `ImpactInt` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `RH_Translator` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 11 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
