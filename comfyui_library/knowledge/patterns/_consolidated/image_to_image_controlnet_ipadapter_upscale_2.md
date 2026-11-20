---
name: image_to_image_controlnet_ipadapter_upscale_2
type: Image To Image
frequency: 7
level: moderate
coverage: 0.942714
common_nodes: [BNK_CLIPTextEncodeAdvanced, BasicGuider, BasicScheduler, BrushNet, BrushNetLoader, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplySD3, ControlNetLoader, DepthAnythingV2Preprocessor, DualCLIPLoader, FluxGuidance, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Comparer (rgthree), ImageListToImageBatch, ImageResizeKJ, ImageScaleToTotalPixels, ImageUpscaleWithModel, InvertMask, Joy_caption_two, Joy_caption_two_load, KSampler, KSamplerSelect, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerUtility: PurgeVRAM, LoadImage, LoraLoader, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/电商产品换背景丨台灯_1898009446906286081.json, 图片生成/文生图/电商产品换背景_1943112026795499522.json, 平台全量/电商产品换背景_1926533180126564353.json, 平台全量/电商产品换背景丨主卧大床_1901287802187980802.json, 平台全量/电商产品换背景溶图万物迁移匹配光影_1933350752813522946.json, 平台全量/电商产品换背景（家具类沙发桌椅套件）_1918965261272289281.json, 平台全量/跨境电商产品换背景（凉亭）_1919007596139974657.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_upscale_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/电商产品换背景丨台灯_1898009446906286081.json、图片生成/文生图/电商产品换背景_1943112026795499522.json、平台全量/电商产品换背景_1926533180126564353.json、平台全量/电商产品换背景丨主卧大床_1901287802187980802.json、平台全量/电商产品换背景溶图万物迁移匹配光影_1933350752813522946.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `BNK_CLIPTextEncodeAdvanced`
- `BasicGuider`
- `BasicScheduler`
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DepthAnythingV2Preprocessor`
- `DualCLIPLoader`
- `FluxGuidance`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `ImageListToImageBatch`
- `ImageResizeKJ`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `InvertMask`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
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

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/7 个有
- `CR Latent Batch Size` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `DF_Get_image_size` —— 1/7 个有
- `DifferentialDiffusion` —— 1/7 个有
- `ImagePadKJ` —— 1/7 个有
- `MaxNode` —— 1/7 个有
- `UpscaleImageByUsingModel` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.1 | 0.1 - 0.1 | 7 | 100% |
| 采样步数 | 30 | 25 - 30 | 7 | 91% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 3.5 | 7 | 72% |
| 采样算法 | euler_ancestral | - | 7 | 86% |
| 调度器 | karras | - | 7 | 86% |
| 重绘幅度 | 0.2 | 0.2 - 1 | 7 | 17% |
| LoRA 模型强度 | 0.59 | 0.59 - 1 | 7 | 75% |
| LoRA 文本强度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.1，观测区间 0.1 - 0.1，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 25 - 30，7 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 3.5，7 个样本
- 采样算法 最常用 euler_ancestral，7 个样本，一致性 86%
- 调度器 最常用 karras，7 个样本，一致性 86%
- 重绘幅度 中位数 0.2，观测区间 0.2 - 1，7 个样本，取值分散，一致性仅 17%
- LoRA 模型强度 中位数 0.59，观测区间 0.59 - 1，7 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
