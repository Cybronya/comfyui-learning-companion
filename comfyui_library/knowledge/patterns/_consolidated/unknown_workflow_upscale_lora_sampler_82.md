---
name: unknown_workflow_upscale_lora_sampler_82
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.953333
common_nodes: [CLIPLoader, CLIPTextEncode, ImageListToImageBatch, ImageScaleBy, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/【无用の阿杰】nunchaku-qwen-wan洗图工作流_1960524777196761089.json, 图片生成/文生图/【无用の阿杰】nunchaku-qwen-wan洗图工作流_1963043272090431490.json, 图片生成/文生图/千问写实-QWen-Image+TTP高清_1957071320292974593.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_82

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/【无用の阿杰】nunchaku-qwen-wan洗图工作流_1960524777196761089.json、图片生成/文生图/【无用の阿杰】nunchaku-qwen-wan洗图工作流_1963043272090431490.json、图片生成/文生图/千问写实-QWen-Image+TTP高清_1957071320292974593.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageListToImageBatch`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `LayerUtility: PurgeVRAM V2` —— 2/3 个有
- `ModelSamplingSD3` —— 2/3 个有
- `NunchakuQwenImageDiTLoader` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `WanVideoNAG` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `CR Simple Image Compare` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy seed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 5 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | exponential | - | 3 | 67% |
| 重绘幅度 | 0.6 | 0.4 - 1 | 3 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 5 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 exponential，3 个样本，一致性 67%
- 重绘幅度 中位数 0.6，观测区间 0.4 - 1，3 个样本
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
