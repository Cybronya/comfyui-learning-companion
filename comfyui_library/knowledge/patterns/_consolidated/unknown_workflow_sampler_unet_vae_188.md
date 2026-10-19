---
name: unknown_workflow_sampler_unet_vae_188
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.41
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, GetNode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewAny, PrimitiveBoolean, PrimitiveInt, QwenImage21Cache, SaveImage, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2, easy seed]
members: [图片生成/图生图/2102369371170623489.json, 图片生成/文生图/qwen-image2.1合集 文生图_单_多图编辑+提示词增强_1938466701136560129.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_188

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2102369371170623489.json、图片生成/文生图/qwen-image2.1合集 文生图_单_多图编辑+提示词增强_1938466701136560129.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：41%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `QwenImage21Cache`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `RHLLMChatNode` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `SaveImageAdvanced` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `TextGenerateLTX2Prompt` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | - | 2 | 67% |
| 高度 | 1536 | - | 2 | 67% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1536，样本不足，未给区间，2 个样本
- 高度 中位数 1536，样本不足，未给区间，2 个样本
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2、easy seed
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
