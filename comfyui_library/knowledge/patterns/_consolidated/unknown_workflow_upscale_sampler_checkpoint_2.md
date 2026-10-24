---
name: unknown_workflow_upscale_sampler_checkpoint_2
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.942583
common_nodes: [CheckpointLoaderSimple, EmptyLatentImage, GetImageSizeAndCount, ImageConcanate, ImageScaleBy, ImageScaleToTotalPixels, KSampler, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit 2511 Aio V23单图编辑_2022419309317857281.json, 图片生成/图生图/Qwen-Edit-2511 AIO V16单图编辑_2004388615297925121.json, 图片生成/图生图/Qwen-Edit-2511 AIO V16单图编辑_2005162806481743874.json, 图片生成/图生图/Qwen-Edit-2511单图编辑电商产品单图编辑个人图片编辑_2067606862656266241.json, 图片生成/图生图/Qwen-Edit-2511单图编辑电商产品单图编辑个人图片编辑_2082430622047494145.json, 图片生成/图生图/Qwen-Edit-2511单图编辑电商产品单图编辑个人图片编辑_2102362850449776641.json, 图片生成/图生图/Qwen-Edit-2511单图编辑电商产品单图编辑个人图片编辑_2102365478101536769.json, 图片生成/图生图/Qwen-edit-2511 动漫转真人风格_2005160648608808961.json, 图片生成/图生图/Qwen-edit-2511 动漫转真人风格_2006619655112232961.json, 图片生成/图生图/【全能图片G4o同款】 Qwen-edit-2511 图像编辑_2005161845830938626.json, 图片生成/图生图/动漫转真人风格Qwen-edit-2511_2006624773798891521.json, 图片生成/图生图/千问Qwen-Edit-2511 AIO V16单图编辑123_2008921130123399170.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit 2511 Aio V23单图编辑_2022419309317857281.json、图片生成/图生图/Qwen-Edit-2511 AIO V16单图编辑_2004388615297925121.json、图片生成/图生图/Qwen-Edit-2511 AIO V16单图编辑_2005162806481743874.json、图片生成/图生图/Qwen-Edit-2511单图编辑电商产品单图编辑个人图片编辑_2067606862656266241.json、图片生成/图生图/Qwen-Edit-2511单图编辑电商产品单图编辑个人图片编辑_2082430622047494145.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 12 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 11/12 个有
- `CR Prompt Text` —— 1/12 个有
- `DuckHideNode` —— 1/12 个有
- `GetImageSize+` —— 1/12 个有
- `ImageResize+` —— 1/12 个有
- `KOOK_ImageCompression` —— 1/12 个有
- `TTP_Image_Assy` —— 1/12 个有
- `TTP_Image_Tile_Batch` —— 1/12 个有
- `TTP_Tile_image_size` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 12 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 768 | 768 - 768 | 12 | 100% |
| 高度 | 768 | 768 - 768 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，12 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 768，观测区间 768 - 768，12 个样本，取值集中（一致性 100%）
- 高度 中位数 768，观测区间 768 - 768，12 个样本，取值集中（一致性 100%）
- 高发问题（11/12 个样本）：Steps较低可能导致细节不足
