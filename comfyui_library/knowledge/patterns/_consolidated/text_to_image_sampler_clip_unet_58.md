---
name: text_to_image_sampler_clip_unet_58
type: Text To Image
frequency: 12
level: strong
coverage: 0.839667
common_nodes: [CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-Art 文生图+高清放大_2017835536668434434.json, 图片生成/文生图/Z-image-Super 3.0 文生图_2018286243913670658.json, 图片生成/文生图/Z-image-turbo基础文生图+高清放大_2063174571645296642.json, 图片生成/文生图/Z-image批量文生图+放大 提示词行 浮云1.14_2011020840770478081.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2070356235764977666.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2070398228675252226.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2070414848839737345.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2070428303873368066.json, 图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2078331213101752321.json, 图片生成/文生图/美少女量贩式生成_1994800940983181313.json, 图片生成/文生图/（量贩版）Z-Image Eyes Deatailed美少女自动扩写文生图V3_1994411563819864066.json, 图片生成/文生图/（量贩版）Z-Image-Turbo D-OPSD美少女文生图V2_2064906233831841794.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_58

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Z-image-Art 文生图+高清放大_2017835536668434434.json、图片生成/文生图/Z-image-Super 3.0 文生图_2018286243913670658.json、图片生成/文生图/Z-image-turbo基础文生图+高清放大_2063174571645296642.json、图片生成/文生图/Z-image批量文生图+放大 提示词行 浮云1.14_2011020840770478081.json、图片生成/文生图/boogu turbo文生图+seedvr2高清放大_2070356235764977666.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 11/12 个有
- `ConditioningZeroOut` —— 10/12 个有
- `SeedVR2LoadDiTModel` —— 10/12 个有
- `SeedVR2LoadVAEModel` —— 10/12 个有
- `SeedVR2VideoUpscaler` —— 10/12 个有
- `CR Text` —— 9/12 个有
- `Image Comparer (rgthree)` —— 8/12 个有
- `PrimitiveInt` —— 7/12 个有
- `CR Prompt Text` —— 5/12 个有
- `PreviewImage` —— 5/12 个有
- `CR Text Replace` —— 4/12 个有
- `ImageScaleBy` —— 4/12 个有
- `JDCN_StringToList` —— 4/12 个有
- `LayerUtility: PurgeVRAM` —— 4/12 个有
- `ProcessString` —— 4/12 个有
- `RH_LLMAPI_Pro_Node` —— 4/12 个有
- `easy showAnything` —— 4/12 个有
- `LoraLoaderModelOnly` —— 3/12 个有
- `Text Concatenate` —— 3/12 个有
- `Seed (rgthree)` —— 2/12 个有
- `ClipLoaderGGUF` —— 1/12 个有
- `GetImageSize+` —— 1/12 个有
- `ImageCASharpening+` —— 1/12 个有
- `ImageResize+` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `QwenImageEngineer` —— 1/12 个有
- `RunningHub Deepcleaner` —— 1/12 个有
- `TTP_Image_Assy` —— 1/12 个有
- `TTP_Image_Tile_Batch` —— 1/12 个有
- `TTP_Tile_image_size` —— 1/12 个有
- `easy cleanGpuUsed` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 15 | 12 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 92% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1052 | 720 - 1080 | 12 | 91% |
| 高度 | 1728 | 1280 - 1920 | 12 | 87% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 15，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 92%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 720 - 1080，12 个样本，取值集中（一致性 91%）
- 高度 中位数 1728，观测区间 1280 - 1920，12 个样本，取值集中（一致性 87%）
- 高发问题（7/12 个样本）：Steps较低可能导致细节不足
