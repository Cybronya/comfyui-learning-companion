---
name: unknown_workflow_video_lora_sampler_694
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.599
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, EmptyImage, GetImageSizeAndCount, GetNode, INTConstant, ImpactFloat, JWFloatToString, LoraLoaderModelOnly, MathExpression|pysssss, PathchSageAttentionKJ, PrimitiveFloat, RH_LLMAPI_NODE, SetNode, StringFunction|pysssss, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanMoeKSampler, WanVideoVACEStartToEndFrame, easy anythingIndexSwitch, easy imageSize, easy int, easy positive, easy saveText, easy seed, easy showAnything]
problems: []
missing: [MathExpression|pysssss, StringFunction|pysssss, easy anythingIndexSwitch, easy int, easy positive, easy imageSize, easy saveText, easy seed]
members: [视频生成/文生视频/1972671707976802306.json, 视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-官方_1982718924657704961.json, 视频生成/文生视频/2066055894355734528.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_694

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/1972671707976802306.json、视频生成/文生视频/视频-文生视频扩写-wan2.2-smoothMix-官方_1982718924657704961.json、视频生成/文生视频/2066055894355734528.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImpactFloat`
- `JWFloatToString`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RH_LLMAPI_NODE`
- `SetNode`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`
- `WanVideoVACEStartToEndFrame`
- `easy anythingIndexSwitch`
- `easy imageSize`
- `easy int`
- `easy positive`
- `easy saveText`
- `easy seed`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 20 | 20 - 20 | 3 | 100% |
| 采样算法 | 1.5 | 1.5 - 1.5 | 3 | 100% |
| 调度器 | 1 | 1 - 1 | 3 | 100% |
| 重绘幅度 | sa_solver | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1.5，观测区间 1.5 - 1.5，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 sa_solver，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：MathExpression|pysssss、StringFunction|pysssss、easy anythingIndexSwitch、easy int、easy positive
