---
name: unknown_workflow_lora_sampler_clip_283
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.676
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ColorMatch, DualCLIPLoader, Florence2ModelLoader, Florence2Run, FluxGuidance, GetNode, Image Comparer (rgthree), ImageListToImageBatch, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, workflow>放大预处理]
problems: []
missing: []
members: [图片生成/图生图/无损高清放大工作流｜一键超清_1914134415251861506.json, 图片生成/图生图/无损高清放大工作流｜一键超清_1942154651460595713.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_283

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/无损高清放大工作流｜一键超清_1914134415251861506.json、图片生成/图生图/无损高清放大工作流｜一键超清_1942154651460595713.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ColorMatch`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `workflow>放大预处理`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
