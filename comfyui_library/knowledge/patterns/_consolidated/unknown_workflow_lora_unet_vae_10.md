---
name: unknown_workflow_lora_unet_vae_10
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.73
common_nodes: [CLIPLoader, CreateVideo, EmptyLatentImage, ImageBatchMulti, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveInt, RHHiddenNodes, SaveImage, SaveVideo, UNETLoader, VAELoader, easy imageListToImageBatch, easy indexAnything, workflow>千问图像生成]
problems: []
missing: []
members: [图片生成/图生图/Qwen 2509 人物多角度视图生成_2009308960213442562.json, 图片生成/文生图/Qwen 2509 提示词多角度视图生成_1999448126555553794.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_unet_vae_10

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen 2509 人物多角度视图生成_2009308960213442562.json、图片生成/文生图/Qwen 2509 提示词多角度视图生成_1999448126555553794.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CreateVideo`
- `EmptyLatentImage`
- `ImageBatchMulti`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveInt`
- `RHHiddenNodes`
- `SaveImage`
- `SaveVideo`
- `UNETLoader`
- `VAELoader`
- `easy imageListToImageBatch`
- `easy indexAnything`
- `workflow>千问图像生成`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
