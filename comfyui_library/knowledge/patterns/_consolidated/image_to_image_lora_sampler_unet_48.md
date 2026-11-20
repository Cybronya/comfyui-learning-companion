---
name: image_to_image_lora_sampler_unet_48
type: Image To Image
frequency: 11
level: moderate
coverage: 0.892636
common_nodes: [CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen去水印_1986102218543824897.json, 图片生成/图生图/Z-Image图生图洗图_2046840416087052290.json, 图片生成/图生图/Z-Image图生图洗图_2094304765537771521.json, 图片生成/图生图/Z-Image图生图洗图_2101937229131243521.json, 图片生成/图生图/Z-Image图生图洗图_2105121490088841217.json, 图片生成/图生图/Z-Image图生图洗图_2105498770577387521.json, 图片生成/图生图/Z-Image图生图洗图_2112490094929203201.json, 图片生成/图生图/Z-image + LoRA 图生图工作流_2059600757091033090.json, 图片生成/图生图/Z-image ControlNet 图生图工作流_2059610100196798465.json, 图片生成/图生图/Z-image ControlNet 图生图工作流_2091491515486003202.json, 图片生成/图生图/【工作台】图生图洗图+lora换脸_2075928247342292993.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_48

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Qwen去水印_1986102218543824897.json、图片生成/图生图/Z-Image图生图洗图_2046840416087052290.json、图片生成/图生图/Z-Image图生图洗图_2094304765537771521.json、图片生成/图生图/Z-Image图生图洗图_2101937229131243521.json、图片生成/图生图/Z-Image图生图洗图_2105121490088841217.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 10/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/11 个有
- `RepeatLatentBatch` —— 4/11 个有
- `PreviewImage` —— 3/11 个有
- `AIO_Preprocessor` —— 2/11 个有
- `ConditioningZeroOut` —— 2/11 个有
- `ModelPatchLoader` —— 2/11 个有
- `ZImageFunControlnet` —— 2/11 个有
- `DuckHideNode` —— 1/11 个有
- `DuckQREncodeNode` —— 1/11 个有
- `ImageScale` —— 1/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 10 | 11 | 82% |
| Prompt 约束强度(CFG) | 1.5 | 1 - 2 | 11 | 77% |
| 采样算法 | euler | - | 11 | 91% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 0.85 | 0.4 - 1 | 11 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 10，11 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1.5，观测区间 1 - 2，11 个样本
- 采样算法 最常用 euler，11 个样本，一致性 91%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 0.85，观测区间 0.4 - 1，11 个样本
- 高发问题（8/11 个样本）：Steps较低可能导致细节不足
