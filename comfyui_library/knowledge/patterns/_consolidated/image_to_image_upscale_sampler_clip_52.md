---
name: image_to_image_upscale_sampler_clip_52
type: Image To Image
frequency: 3
level: strong
coverage: 0.880667
common_nodes: [CLIPTextEncode, DualCLIPLoader, ImageListToImageBatch, ImageScaleBy, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, LoadImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/升级-Flux1-Krea-Dev最强美学模型  + JOP CAPTION BETA最强反推模型_1951105950621048833.json, 图片生成/文生图/升级-Flux1-Krea-Dev最强美学模型  + JOP CAPTION BETA最强反推模型_2039150798575243265.json, 平台全量/Kontext+TTP高清放大最强组合_1949652915347705857.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_52

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/升级-Flux1-Krea-Dev最强美学模型  + JOP CAPTION BETA最强反推模型_1951105950621048833.json、图片生成/文生图/升级-Flux1-Krea-Dev最强美学模型  + JOP CAPTION BETA最强反推模型_2039150798575243265.json、平台全量/Kontext+TTP高清放大最强组合_1949652915347705857.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `ImageListToImageBatch`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `CR Text Concatenate` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `FluxGuidance` —— 2/3 个有
- `LayerUtility: JoyCaptionBeta1` —— 2/3 个有
- `LayerUtility: LoadJoyCaptionBeta1Model` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `SDXL Empty Latent Image (rgthree)` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `VAEDecode` —— 2/3 个有
- `CR Simple Image Compare` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | exponential | - | 3 | 100% |
| 重绘幅度 | 0.9 | 0.9 - 0.9 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 1/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 exponential，3 个样本，一致性 100%
- 重绘幅度 中位数 0.9，观测区间 0.9 - 0.9，3 个样本，取值集中（一致性 100%）
