---
name: unknown_workflow_upscale_sampler_clip_35
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.82425
common_nodes: [CLIPTextEncode, EmptySD3LatentImage, ImageResize+, ImageScaleBy, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Base 文生图+高清放大+全节点注释_2055591595319275522.json, 图片生成/文生图/Zimage-Cc-风情万种_2020170940788772866.json, 图片生成/文生图/（贞贞-Ai Toolkit 3W步）Z-Image-Base文生图V1_2036432332558704642.json, 图片生成/文生图/（贞贞版-15W步-none）Z-image-base文生图高清版_2036429688607875074.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-Image-Base 文生图+高清放大+全节点注释_2055591595319275522.json、图片生成/文生图/Zimage-Cc-风情万种_2020170940788772866.json、图片生成/文生图/（贞贞-Ai Toolkit 3W步）Z-Image-Base文生图V1_2036432332558704642.json、图片生成/文生图/（贞贞版-15W步-none）Z-image-base文生图高清版_2036429688607875074.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `ImageResize+`
- `ImageScaleBy`
- `KSampler`
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
- `CLIPLoader` —— 3/4 个有
- `GetImageSize+` —— 3/4 个有
- `ImageCASharpening+` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `KOOK_SaveJPGImage` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `RunningHub Deepcleaner` —— 2/4 个有
- `CLIPLoaderGGUF` —— 1/4 个有
- `ConstrainImage|pysssss` —— 1/4 个有
- `Get Image Size` —— 1/4 个有
- `Image Filter Adjustments` —— 1/4 个有
- `JWFloat` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | 8 - 30 | 4 | 61% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 3 | 4 | 57% |
| 采样算法 | res_multistep | - | 4 | 50% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 27.5，观测区间 8 - 30，4 个样本
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 3，4 个样本
- 采样算法 最常用 res_multistep，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
