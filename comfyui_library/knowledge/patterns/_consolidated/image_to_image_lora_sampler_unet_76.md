---
name: image_to_image_lora_sampler_unet_76
type: Image To Image
frequency: 8
level: strong
coverage: 0.97475
common_nodes: [CLIPLoader, ConditioningZeroOut, ImageStitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, Text Multiline, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Nunchaku-Pose+服装3图参考-Edit2509图像编辑_1972111718035943426.json, 图片生成/图生图/Nunchaku-Pose姿势+服装3图参考-Edit2509图像编辑_1970877208757735425.json, 图片生成/图生图/Pose姿势参考-千问Edit2509图像编辑_1970537694130544641.json, 图片生成/图生图/【两图】Pose参考-千问Edit2509图像编辑_1972111568060215298.json, 图片生成/图生图/场景融合 多人 - 千问 Edit 2509 图像编辑 Qwen_1993939055859744769.json, 图片生成/图生图/多人场景融合-千问Edit2509图像编辑_1970545543497871362.json, 图片生成/图生图/多人场景融合-千问Edit2509图像编辑_2010998632887095298.json, 图片生成/图生图/多人场景融合-千问Edit2509图像编辑_2039335767264206849.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_76

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Nunchaku-Pose+服装3图参考-Edit2509图像编辑_1972111718035943426.json、图片生成/图生图/Nunchaku-Pose姿势+服装3图参考-Edit2509图像编辑_1970877208757735425.json、图片生成/图生图/Pose姿势参考-千问Edit2509图像编辑_1970537694130544641.json、图片生成/图生图/【两图】Pose参考-千问Edit2509图像编辑_1972111568060215298.json、图片生成/图生图/场景融合 多人 - 千问 Edit 2509 图像编辑 Qwen_1993939055859744769.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `ImageStitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlus_lrzjason` —— 6/8 个有
- `AIO_Preprocessor` —— 4/8 个有
- `EmptyLatentImage` —— 4/8 个有
- `GetImageSizeAndCount` —— 4/8 个有
- `ImageConcatMulti` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `NunchakuQwenImageDiTLoader` —— 2/8 个有
- `CR Latent Batch Size` —— 1/8 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/8 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 8 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | beta57 | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 beta57，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
