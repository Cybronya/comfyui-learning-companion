---
name: image_to_image_lora_sampler_unet_231
type: Image To Image
frequency: 2
level: weak
coverage: 0.8455
common_nodes: [CLIPLoader, DF_Integer, Get Image Size, GetImageSize, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImpactMinMax, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ProcessString, RH_LLMAPI_NODE, SaveImage, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/单图扩写 多镜头-—制造分镜 2.0_1980655151860072450.json, 数字人/数字人/【乔巴】一键生成15个角度产品场景展示图+SeedVR2.5高清放大-自动版_2053291451966078977.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_231

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/单图扩写 多镜头-—制造分镜 2.0_1980655151860072450.json、数字人/数字人/【乔巴】一键生成15个角度产品场景展示图+SeedVR2.5高清放大-自动版_2053291451966078977.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `DF_Integer`
- `Get Image Size`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ProcessString`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `ImpactImageBatchToImageList` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `Mute / Bypass Relay (rgthree)` —— 1/2 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `SeedVR2LoadDiTModel` —— 1/2 个有
- `SeedVR2LoadVAEModel` —— 1/2 个有
- `SeedVR2VideoUpscaler` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6.5 | - | 2 | 62% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 50% |
| 调度器 | beta57 | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6.5，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 50%
- 调度器 最常用 beta57，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
