---
name: unknown_workflow_upscale_sampler_clip_15
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.84975
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, GetImageSize+, ImageResize+, ImageScaleBy, KSampler, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/洗图 反推  提示词 图生图 Z-image zimage_2043551448385982466.json, 图片生成/文生图/QWEN image VS QWEN image 2512  文生图效果对比_2008909893788508162.json, 图片生成/文生图/Z-Anime_2048642624793354242.json, 图片生成/文生图/Z-Anime动漫图片生成工作流_2048674302190428161.json, 图片生成/文生图/Z-Anime动漫生图专属_2048961758227865601.json, 图片生成/文生图/凡工的zhenzhen生成器Z-Image-Base文生图V1_2038488514748223489.json, 图片生成/文生图/凡工的zhenzhen生成器（批量）Z-Image-Base文生图V1_2040721747342790657.json, 图片生成/文生图/（老白lokr版-贞贞22W步）Z-Image-Base文生图V1_2036429610866450434.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_15

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/洗图 反推  提示词 图生图 Z-image zimage_2043551448385982466.json、图片生成/文生图/QWEN image VS QWEN image 2512  文生图效果对比_2008909893788508162.json、图片生成/文生图/Z-Anime_2048642624793354242.json、图片生成/文生图/Z-Anime动漫图片生成工作流_2048674302190428161.json、图片生成/文生图/Z-Anime动漫生图专属_2048961758227865601.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageCASharpening+` —— 7/8 个有
- `LoadImage` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `KOOK_SaveJPGImage` —— 4/8 个有
- `LayerUtility: PurgeVRAM` —— 4/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `RunningHub Deepcleaner` —— 4/8 个有
- `easy cleanGpuUsed` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `JWFloat` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `easy int` —— 3/8 个有
- `CR Text` —— 1/8 个有
- `KOOK_ImageCompression` —— 1/8 个有
- `Qwen3_VQA` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `easy promptLine` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 50 | 8 | 45% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 3.5 | 8 | 53% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 50，8 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 3.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
