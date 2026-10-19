---
name: unknown_workflow_upscale_lora_sampler_23
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.784
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, ImageListToImageBatch, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList]
problems: [Steps较低可能导致细节不足]
missing: [easy cleanGpuUsed, easy getNode, easy imageBatchToImageList, easy setNode]
members: [图片生成/文生图/1950577515129655297.json, 图片生成/文生图/1951143607715737601.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1950577515129655297.json、图片生成/文生图/1951143607715737601.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SaveAnimatedWEBP` —— 1/2 个有
- `easy getNode` —— 1/2 个有
- `easy setNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | heun | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 heun，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、easy getNode、easy imageBatchToImageList、easy setNode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
