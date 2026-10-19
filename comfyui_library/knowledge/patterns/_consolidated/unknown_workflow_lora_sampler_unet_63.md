---
name: unknown_workflow_lora_sampler_unet_63
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.3195
common_nodes: [CLIPLoader, CR Prompt Text, CR Text, ComfySwitchNode, Context (rgthree), EmptyLatentImage, Fast Groups Bypasser (rgthree), GetNode, ImpactSwitch, JoinStringMulti, JoinStrings, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21BlockCacheT8, QwenImage21Cache, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, QwenPERewriteT8, ResolutionSelector, SaveImage, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy boolean, easy float, easy ifElse, easy showAnything]
problems: []
missing: [CR Text, Context (rgthree), easy anythingIndexSwitch, easy boolean, easy float, CR Prompt Text]
members: [图片生成/反推提示词/qwen 2.1小岚整合版_2105981670468972546.json, 图片生成/图生图/2105981670468972546.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_63

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/qwen 2.1小岚整合版_2105981670468972546.json、图片生成/图生图/2105981670468972546.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：32%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `CR Text`
- `ComfySwitchNode`
- `Context (rgthree)`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImpactSwitch`
- `JoinStringMulti`
- `JoinStrings`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21BlockCacheT8`
- `QwenImage21Cache`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `QwenPERewriteT8`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy boolean`
- `easy float`
- `easy ifElse`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 40 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、Context (rgthree)、easy anythingIndexSwitch、easy boolean、easy float
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
