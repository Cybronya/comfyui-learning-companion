---
name: unknown_workflow_lora_sampler_unet_308
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.613
common_nodes: [CLIPLoader, ConditioningZeroOut, GetNode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RH_LLMAPI_NODE, RH_RhartImageG2ImageToImage, SaveImage, SetNode, Text, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/手帐魔术师 —— 把你的空白变成魔法_2058793141746102273.json, 图片生成/文生图/方案输出手帐日记空白填写内容朋友圈运营内容美化图片_2068925956189937666.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_308

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/手帐魔术师 —— 把你的空白变成魔法_2058793141746102273.json、图片生成/文生图/方案输出手帐日记空白填写内容朋友圈运营内容美化图片_2068925956189937666.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `GetNode`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_LLMAPI_NODE`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `SetNode`
- `Text`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | beta | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 beta，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
