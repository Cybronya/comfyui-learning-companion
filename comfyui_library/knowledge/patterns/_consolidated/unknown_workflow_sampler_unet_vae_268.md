---
name: unknown_workflow_sampler_unet_vae_268
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6816
common_nodes: [CLIPLoader, ComfySwitchNode, ConditioningZeroOut, JsonExtractString, KSampler, MiniMaxH3ImageConditioning, PreviewAny, PrimitiveStringMultiline, ResolutionSelector, SaveImage, StringReplace, TextGenerateV2, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/MINIMAXH3 Image文生图优化版_2120326054731673601.json, 平台全量/MiniMax H3 Image文生图官方优化工作流V1.0_2120372977433931777.json, 平台全量/MiniMax H3-Image｜文生图（经典KSampler·可选PE）_2120388077565865985.json, 平台全量/Minimax H3 Image - t2i 文生图官方版_2120359483347136514.json, 平台全量/Minimax H3 Image 文生图 官方工作流_2120389207335198722.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_268

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/MINIMAXH3 Image文生图优化版_2120326054731673601.json、平台全量/MiniMax H3 Image文生图官方优化工作流V1.0_2120372977433931777.json、平台全量/MiniMax H3-Image｜文生图（经典KSampler·可选PE）_2120388077565865985.json、平台全量/Minimax H3 Image - t2i 文生图官方版_2120359483347136514.json、平台全量/Minimax H3 Image 文生图 官方工作流_2120389207335198722.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `JsonExtractString`
- `KSampler`
- `MiniMaxH3ImageConditioning`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `StringReplace`
- `TextGenerateV2`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `Image Comparer (rgthree)` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `SeedVR2LoadDiTModel` —— 1/5 个有
- `SeedVR2LoadVAEModel` —— 1/5 个有
- `SeedVR2VideoUpscaler` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
