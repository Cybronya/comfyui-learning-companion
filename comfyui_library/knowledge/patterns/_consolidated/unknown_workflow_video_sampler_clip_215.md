---
name: unknown_workflow_video_sampler_clip_215
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.792
common_nodes: [CLIPLoader, CLIPTextEncode, ImageResizeKJv2, ImageStitch, JWFloatToInteger, KSampler, LayerUtility: TextJoin, LucyConditionConcatNode, ModelSamplingSD3, PrimitiveFloat, PrimitiveInt, RH_LLMAPI_NODE, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/电商服装配饰场景角色替换和编辑-Lucy-Edit视频编辑_1986343278314475522.json, 视频生成/文生视频/电商服装配饰场景角色替换和编辑-Lucy-Edit视频编辑_1986355209393893377.json, 视频生成/文生视频/电商服装配饰场景角色替换和编辑-Lucy-Edit视频编辑_1986362481859850242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_215

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/电商服装配饰场景角色替换和编辑-Lucy-Edit视频编辑_1986343278314475522.json、视频生成/文生视频/电商服装配饰场景角色替换和编辑-Lucy-Edit视频编辑_1986355209393893377.json、视频生成/文生视频/电商服装配饰场景角色替换和编辑-Lucy-Edit视频编辑_1986362481859850242.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageResizeKJv2`
- `ImageStitch`
- `JWFloatToInteger`
- `KSampler`
- `LayerUtility: TextJoin`
- `LucyConditionConcatNode`
- `ModelSamplingSD3`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 50 - 50 | 3 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 50 - 50，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
