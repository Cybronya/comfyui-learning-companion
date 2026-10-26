---
name: unknown_workflow_sampler_clip_unet_398
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.821333
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, ComfySwitchNode, ConditioningZeroOut, EmptyFlux2LatentImage, Fast Groups Bypasser (rgthree), KSamplerAdvanced, LayerUtility: PurgeVRAM V2, PrimitiveBoolean, PrimitiveStringMultiline, SaveImage, Seed (rgthree), StringReplace, TextGenerate, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/ernie image turbo+klein-9B 洗图_2044752629661704194.json, 图片生成/文生图/ernie turbo+klein-9B 超真实出图_2044922289199779841.json, 图片生成/文生图/ernie-image-turbo+zimage-turbo_双采样人像去油去拟合感_2044777572101267457.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_398

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/ernie image turbo+klein-9B 洗图_2044752629661704194.json、图片生成/文生图/ernie turbo+klein-9B 超真实出图_2044922289199779841.json、图片生成/文生图/ernie-image-turbo+zimage-turbo_双采样人像去油去拟合感_2044777572101267457.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM V2`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `SaveImage`
- `Seed (rgthree)`
- `StringReplace`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 2/3 个有
- `easy int` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `Int` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `Reroute (rgthree)` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `TTResolutionSelector` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 12 | 3 | 80% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 12，3 个样本
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
