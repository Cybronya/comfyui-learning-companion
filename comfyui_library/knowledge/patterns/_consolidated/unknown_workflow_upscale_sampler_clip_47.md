---
name: unknown_workflow_upscale_sampler_clip_47
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7865
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Upscale Image, DetailDaemonSamplerNode, DualCLIPLoader, EmptySD3LatentImage, Florence2ModelLoader, Florence2Run, FluxGuidance, Image Tiled, ImageConcanateOfUtils, ImageFromBatch, KSamplerSelect, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TeaCache, UNETLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/B站：AI绘画师-数码宝贝-天女兽生图工作流_1904073338157965314.json, 图片生成/文生图/星空女孩lora-工作流_1967085637759275009.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/B站：AI绘画师-数码宝贝-天女兽生图工作流_1904073338157965314.json、图片生成/文生图/星空女孩lora-工作流_1967085637759275009.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Upscale Image`
- `DetailDaemonSamplerNode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `Image Tiled`
- `ImageConcanateOfUtils`
- `ImageFromBatch`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TeaCache`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
