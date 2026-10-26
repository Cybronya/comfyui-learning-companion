---
name: unknown_workflow_sampler_unet_vae_277
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.741333
common_nodes: [BatchImagesNode, CLIPLoader, CR Text Concatenate, ComfySwitchNode, EmptySD3LatentImage, Int, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, OpenposePreprocessor, PreviewAny, PreviewImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader, kkGetImage]
problems: []
missing: []
members: [图片生成/图生图/Qwen_Image2.1丨姿势迁移_2110646296100032514.json, 图片生成/图生图/Qwen_Image2.1丨姿势迁移_2111276056136208386.json, 图片生成/图生图/（换姿势）QwenImage2.1 原生controlNet_2107976794220621826.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_277

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen_Image2.1丨姿势迁移_2110646296100032514.json、图片生成/图生图/Qwen_Image2.1丨姿势迁移_2111276056136208386.json、图片生成/图生图/（换姿势）QwenImage2.1 原生controlNet_2107976794220621826.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CR Text Concatenate`
- `ComfySwitchNode`
- `EmptySD3LatentImage`
- `Int`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `OpenposePreprocessor`
- `PreviewAny`
- `PreviewImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `kkGetImage`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
