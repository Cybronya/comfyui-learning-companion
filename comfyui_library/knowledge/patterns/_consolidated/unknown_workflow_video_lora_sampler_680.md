---
name: unknown_workflow_video_lora_sampler_680
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.417667
common_nodes: [BerniniConditioning, CLIPLoader, CLIPTextEncode, GetNode, KSamplerAdvanced, Label (rgthree), LoadImage, LoraLoaderModelOnly, MaxNode, PrimitiveFloat, PrimitiveInt, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2067574598878715906.json, 视频生成/图生视频/2067577219454693378.json, 视频生成/文生视频/工作流基础系列31.1-Bernini 文本到视频（t2v）工作流_2067573571404263425.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_680

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/2067574598878715906.json、视频生成/图生视频/2067577219454693378.json、视频生成/文生视频/工作流基础系列31.1-Bernini 文本到视频（t2v）工作流_2067573571404263425.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：42%

## 共有节点

全部 3 个 workflow 都包含：
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `KSamplerAdvanced`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaxNode`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: TextBox` —— 2/3 个有
- `ResizeImageMaskNode` —— 2/3 个有
- `BerniniPromptEnhancer` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `RHLLMChatNode` —— 1/3 个有
- `RH_Translator` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 10 | 6 - 10 | 3 | 78% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 10，观测区间 6 - 10，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
