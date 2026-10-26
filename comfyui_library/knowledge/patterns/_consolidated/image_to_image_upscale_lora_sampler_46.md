---
name: image_to_image_upscale_lora_sampler_46
type: Image To Image
frequency: 4
level: strong
coverage: 0.668
common_nodes: [CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, DF_Float, DualCLIPLoader, DyPE_FLUX, FluxGuidance, GetImageSize, Image Comparer (rgthree), ImageScaleBy, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, Light-Tool: TextConnect, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen3_VQA, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, SetNode, ShowText|pysssss, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy imageListToImageBatch, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Portrait HD+Beauty-终级高清人像放大+美颜-自然真实质感_1991333314445312002.json, 图片生成/图生图/Qwen-image动漫转3D人像-超高清修复_1990671806451388418.json, 图片生成/图生图/Qwen-image真人转动漫-超高清修复_1989567976863092737.json, 图片生成/文生图/Qwen-image动漫转真人写实人像-超高清修复_1988957962741878786.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_46

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Portrait HD+Beauty-终级高清人像放大+美颜-自然真实质感_1991333314445312002.json、图片生成/图生图/Qwen-image动漫转3D人像-超高清修复_1990671806451388418.json、图片生成/图生图/Qwen-image真人转动漫-超高清修复_1989567976863092737.json、图片生成/文生图/Qwen-image动漫转真人写实人像-超高清修复_1988957962741878786.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `DF_Float`
- `DualCLIPLoader`
- `DyPE_FLUX`
- `FluxGuidance`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Light-Tool: TextConnect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SetNode`
- `ShowText|pysssss`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 3/4 个有
- `Anything Everywhere` —— 3/4 个有
- `CR SDXL Aspect Ratio` —— 3/4 个有
- `ControlNetApplyAdvanced` —— 3/4 个有
- `ControlNetLoader` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `Int` —— 3/4 个有
- `JoinStrings` —— 3/4 个有
- `PrimitiveBoolean` —— 3/4 个有
- `SetUnionControlNetType` —— 3/4 个有
- `TextInput_` —— 3/4 个有
- `easy ifElse` —— 3/4 个有
- `easy imageConcat` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `BaiduTranslateNode` —— 1/4 个有
- `Float` —— 1/4 个有
- `FluxKontextImageScale` —— 1/4 个有
- `ImageListToImageBatch` —— 1/4 个有
- `MaskToImage` —— 1/4 个有
- `ModelSamplingSD3` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 28 - 28 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_2s | - | 4 | 100% |
| 调度器 | beta57 | - | 4 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 4 | 100% |
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 28，观测区间 28 - 28，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，4 个样本，一致性 100%
- 调度器 最常用 beta57，4 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，4 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
