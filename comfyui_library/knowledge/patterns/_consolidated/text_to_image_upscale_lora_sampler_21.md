---
name: text_to_image_upscale_lora_sampler_21
type: Text To Image
frequency: 9
level: strong
coverage: 0.849556
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, CR Prompt List, CR Text, ColorCorrectOfUtils, DapaoImageCompressionNode, EmptyLatentImage, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageUpscaleWithModel, KSampler, LayerFilter: FilmV2, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, PreviewImage, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, String Literal, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/001.Z-image生图巅峰019.瑶光真实+优化文生图_2037451201033277442.json, 图片生成/文生图/001.Z-image生图巅峰019.瑶光真实+优化文生图_2037701182256320514.json, 图片生成/文生图/Z-IMAGE 极致美学真实质感 优化提示词出图_2035517633864404994.json, 图片生成/文生图/Z-IMAGE 极致美学真实质感 优化提示词出图_2036778854009802753.json, 图片生成/文生图/Z-IMAGE 极致美学真实质感 优化提示词出图_2036779249297788929.json, 图片生成/文生图/Z-IMAGE 极致美学真实质感 优化提示词出图_2036798123510599682.json, 图片生成/文生图/Z-IMAGE 极致美学真实质感_2039286549157777409.json, 图片生成/文生图/ZIB-piaopiao-202605121843_2054127511310741505.json, 图片生成/文生图/改Z-IMAGE 极致美学真实质感20260407_2041489569769594882.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/001.Z-image生图巅峰019.瑶光真实+优化文生图_2037451201033277442.json、图片生成/文生图/001.Z-image生图巅峰019.瑶光真实+优化文生图_2037701182256320514.json、图片生成/文生图/Z-IMAGE 极致美学真实质感 优化提示词出图_2035517633864404994.json、图片生成/文生图/Z-IMAGE 极致美学真实质感 优化提示词出图_2036778854009802753.json、图片生成/文生图/Z-IMAGE 极致美学真实质感 优化提示词出图_2036779249297788929.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt List`
- `CR Text`
- `ColorCorrectOfUtils`
- `DapaoImageCompressionNode`
- `EmptyLatentImage`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerFilter: FilmV2`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `String Literal`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_Pro_Node` —— 7/9 个有
- `LoadImage` —— 3/9 个有
- `Note Plus (mtb)` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `PrimitiveBoolean` —— 2/9 个有
- `RH_LLMAPI_NODE` —— 2/9 个有
- `String` —— 2/9 个有
- `TT_img_enc_v2` —— 2/9 个有
- `ZML_SwitchOutput` —— 2/9 个有
- `ttN text` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1080 | 9 | 100% |
| 高度 | 1920 | 1920 - 1920 | 9 | 100% |
| 采样步数 | 8 | 8 - 8 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | res_2s | - | 9 | 100% |
| 调度器 | bong_tangent | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1080，9 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 8，观测区间 8 - 8，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，9 个样本，一致性 100%
- 调度器 最常用 bong_tangent，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
