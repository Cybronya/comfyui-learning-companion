---
name: image_to_image_upscale_sampler_clip_4
type: Image To Image
frequency: 21
level: weak
coverage: 0.910429
common_nodes: [CLIPTextEncode, CR Simple Image Compare, DualCLIPLoader, ImageListToImageBatch, ImageScaleBy, ImageScaleDownToSize, ImageUpscaleWithModel, ImpactImageBatchToImageList, KSampler, LoadImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/TTP高清放大+细节增强_1948373114209087490.json, 图片生成/图生图/TTP高清放大细节修复_2009831874436272130.json, 图片生成/图生图/WAN2.1单帧+TTP细节增强洗图_1946819482188963842.json, 图片生成/图生图/WAN2.1图生图细节增强_1992473209345994753.json, 图片生成/图生图/WAN2.1手机摄影-图生图单帧细节增强洗图(TTP)_1949665393657958401.json, 图片生成/图生图/Wan2.2 图生图 洗图  TTP高清_1986345889805598722.json, 图片生成/图生图/Wan2.2 图生图 洗图 -可TTP高清_1970990617306243074.json, 图片生成/图生图/Wan2.2单帧仅图生图(可TTP高清)_1950256761166020610.json, 图片生成/图生图/Wan2.2单帧图像生成洗图(可TTP高清)_1949890053692678146.json, 图片生成/图生图/Wan2.2单帧图像生成洗图(可TTP高清)_1986363381999431682.json, 图片生成/图生图/Wan2.2单帧图像生成洗图(可TTP高清)_1986368993206431746.json, 图片生成/图生图/Wan2.2单帧图像生成洗图(可TTP高清)_2039151835746930690.json, 图片生成/图生图/Wan2.2单帧文生图_图生图洗图(可TTP高清)_1951276680302243841.json, 图片生成/图生图/图生图_1954727121572786178.json, 图片生成/图生图/图生图重绘细节增强(WAN2.1)_1992501081584324609.json, 图片生成/图生图/网红图片洗图——高射炮打蚊子系列三：wan2.1洗图+真实自拍lora+TTP高清放大（强烈推荐）_1947150362493247490.json, 图片生成/文生图/WAN2.1图生图单帧细节增强洗图(TTP)_1944310191020232705.json, 图片生成/文生图/Wan2.2单帧图像生成洗图(可TTP高清)_2039508663844474881.json, 图片生成/文生图/细节增强洗图3.0_1947217865588035585.json, 图片生成/文生图/细节增强洗图3.0_1947618979507548162.json, 视频生成/文生视频/WAN2.1图生图单帧细节增强洗图(TTP)_2034438567707021314.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/TTP高清放大+细节增强_1948373114209087490.json、图片生成/图生图/TTP高清放大细节修复_2009831874436272130.json、图片生成/图生图/WAN2.1单帧+TTP细节增强洗图_1946819482188963842.json、图片生成/图生图/WAN2.1图生图细节增强_1992473209345994753.json、图片生成/图生图/WAN2.1手机摄影-图生图单帧细节增强洗图(TTP)_1949665393657958401.json…）

- **类型**：Image To Image
- **样本数**：21
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Simple Image Compare`
- `DualCLIPLoader`
- `ImageListToImageBatch`
- `ImageScaleBy`
- `ImageScaleDownToSize`
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
- `CLIPLoader` —— 19/21 个有
- `PathchSageAttentionKJ` —— 19/21 个有
- `PreviewImage` —— 19/21 个有
- `RH_Captioner` —— 19/21 个有
- `Text Concatenate` —— 19/21 个有
- `Text Multiline` —— 19/21 个有
- `VAEDecode` —— 19/21 个有
- `easy showAnything` —— 19/21 个有
- `LoraLoaderModelOnly` —— 10/21 个有
- `ModelSamplingSD3` —— 10/21 个有
- `EsesImageEffectBloom` —— 9/21 个有
- `ImageSharpen` —— 9/21 个有
- `LayerFilter: FilmV2` —— 9/21 个有
- `LoraLoader` —— 9/21 个有
- `BetterFilmGrain` —— 8/21 个有
- `EmptyHunyuanLatentVideo` —— 6/21 个有
- `GetImageSizeAndCount` —— 6/21 个有
- `KSamplerAdvanced` —— 6/21 个有
- `Primitive integer [Crystools]` —— 6/21 个有
- `easy anythingIndexSwitch` —— 6/21 个有
- `Fast Groups Bypasser (rgthree)` —— 3/21 个有
- `PrimitiveFloat` —— 2/21 个有
- `Image Comparer (rgthree)` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 20 | 15 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 12 | 21 | 0% |
| 采样算法 | res_2s | - | 21 | 43% |
| 调度器 | bong_tangent | - | 21 | 43% |
| 重绘幅度 | 0.4 | 0.2 - 0.9 | 15 | 37% |
| LoRA 模型强度 | 1 | 0.6 - 1 | 9 | 87% |
| LoRA 文本强度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/21 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 2/21 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 20，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 12，21 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 res_2s，21 个样本，一致性 43%
- 调度器 最常用 bong_tangent，21 个样本，一致性 43%
- 重绘幅度 中位数 0.4，观测区间 0.2 - 0.9，15 个样本，取值分散，一致性仅 37%
- LoRA 模型强度 中位数 1，观测区间 0.6 - 1，9 个样本，取值集中（一致性 87%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
