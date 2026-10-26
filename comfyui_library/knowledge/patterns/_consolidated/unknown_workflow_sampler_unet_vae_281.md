---
name: unknown_workflow_sampler_unet_vae_281
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.472667
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, GetNode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewAny, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, QwenImage21Cache, SaveImage, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: []
missing: []
members: [图片生成/图生图/qwen-image2.1_人物定装照四视图_六视图_2102742894242263042.json, 图片生成/图生图/qwen-image2.1故事分镜_参考图生成_九六四宫格三模式_2102369371170623489.json, 图片生成/图生图/故事分镜_参考图生成_九六四宫格三模式_自动裁剪单图放大_2105611989971197954.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_281

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/qwen-image2.1_人物定装照四视图_六视图_2102742894242263042.json、图片生成/图生图/qwen-image2.1故事分镜_参考图生成_九六四宫格三模式_2102369371170623489.json、图片生成/图生图/故事分镜_参考图生成_九六四宫格三模式_自动裁剪单图放大_2105611989971197954.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 3 个 workflow 都包含：
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
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `RHLLMChatNode` —— 2/3 个有
- `StringConcatenate` —— 2/3 个有
- `EmptyImage` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageBatch` —— 1/3 个有
- `ImageCrop+` —— 1/3 个有
- `ImageFromBatch` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `easy forLoopEnd` —— 1/3 个有
- `easy forLoopStart` —— 1/3 个有
- `easy imageSplitGrid` —— 1/3 个有
- `easy mathInt` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 40 | 3 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 2048 | 2048 - 2048 | 3 | 100% |
| 高度 | 2048 | 1152 - 2048 | 3 | 76% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 40，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 2048，观测区间 2048 - 2048，3 个样本，取值集中（一致性 100%）
- 高度 中位数 2048，观测区间 1152 - 2048，3 个样本
