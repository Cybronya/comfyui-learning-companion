---
name: unknown_workflow_lora_sampler_clip_152
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.4355
common_nodes: [BerniniConditioning, CLIPLoader, CLIPTextEncode, GetNode, KSamplerAdvanced, Label (rgthree), LoadImage, LoraLoaderModelOnly, MaxNode, PrimitiveInt, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/工作流基础系列31.3-Bernini+图像编辑（i2i）工作流_2067577195912060930.json, 视频生成/图生视频/工作流基础系列31.2-Bernini+图生视频（i2v）工作流_2067574598878715906.json, 视频生成/图生视频/工作流基础系列31.4-Bernini+多参考图生视频（r2v）工作流_2067577219454693378.json, 视频生成/文生视频/工作流基础系列31.1-Bernini 文本到视频（t2v）工作流_2067573571404263425.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_152

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/工作流基础系列31.3-Bernini+图像编辑（i2i）工作流_2067577195912060930.json、视频生成/图生视频/工作流基础系列31.2-Bernini+图生视频（i2v）工作流_2067574598878715906.json、视频生成/图生视频/工作流基础系列31.4-Bernini+多参考图生视频（r2v）工作流_2067577219454693378.json、视频生成/文生视频/工作流基础系列31.1-Bernini 文本到视频（t2v）工作流_2067573571404263425.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：44%

## 共有节点

全部 4 个 workflow 都包含：
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `GetNode`
- `KSamplerAdvanced`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaxNode`
- `PrimitiveInt`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: TextBox` —— 3/4 个有
- `PrimitiveFloat` —— 3/4 个有
- `ResizeImageMaskNode` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `BerniniPromptEnhancer` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `RHLLMChatNode` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `SaveImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 10 | 6 - 10 | 4 | 81% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 10，观测区间 6 - 10，4 个样本，取值集中（一致性 81%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
