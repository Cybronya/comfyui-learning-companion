---
name: unknown_workflow_upscale_lora_sampler_27
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.849429
common_nodes: [CLIPTextEncode, DualCLIPLoader, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, LoraLoaderModelOnly, PreviewImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD极速版_2K高清放大工作流-可在线或线下运行_1951953561489977345.json, 图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD极速版_4K高清放大工作流-可在线或线下运行_1951982323178917889.json, 图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD标准版_2K高清放大工作流-可在线和本地使用_1951946483614560258.json, 图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD标准版_4K高清放大工作流-可在线和本地使用_1951977232698953729.json, 图片生成/文生图/Flux Krea-文生图+ttp高清放大_1967396109779865602.json, 图片生成/文生图/【混元HUNYUAN2.1】文生图+TTP高清修复_1976498417276985345.json, 图片生成/文生图/混元HUNYUAN2.1文生图+TTP高清修复_1977247385053208578.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD极速版_2K高清放大工作流-可在线或线下运行_1951953561489977345.json、图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD极速版_4K高清放大工作流-可在线或线下运行_1951982323178917889.json、图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD标准版_2K高清放大工作流-可在线和本地使用_1951946483614560258.json、图片生成/文生图/F.1 Krea [dev] 文生图Lora_TTD标准版_4K高清放大工作流-可在线和本地使用_1951977232698953729.json、图片生成/文生图/Flux Krea-文生图+ttp高清放大_1967396109779865602.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoaderModelOnly`
- `PreviewImage`
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
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/7 个有
- `EmptySD3LatentImage` —— 5/7 个有
- `ImageResizeKJ` —— 5/7 个有
- `ImageSmartSharpen+` —— 5/7 个有
- `Fast Groups Muter (rgthree)` —— 4/7 个有
- `Anything Everywhere3` —— 3/7 个有
- `EmptyHunyuanImageLatent` —— 2/7 个有
- `FluxResolutionNode` —— 2/7 个有
- `HunyuanRefinerLatent` —— 2/7 个有
- `ImageCASharpening+` —— 2/7 个有
- `ImageScaleBy` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `RH_Translator` —— 2/7 个有
- `VAEEncodeTiled` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 2 - 30 | 7 | 8% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 7 | 67% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | sgm_uniform | - | 7 | 43% |
| 重绘幅度 | 0.3 | 0.3 - 1 | 7 | 37% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 2 - 30，7 个样本，取值分散，一致性仅 8%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，7 个样本，一致性 43%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 1，7 个样本，取值分散，一致性仅 37%
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
