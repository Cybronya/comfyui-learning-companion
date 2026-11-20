---
name: text_to_image_lora_sampler_clip_331
type: Text To Image
frequency: 6
level: strong
coverage: 0.899167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1超细节多图像编辑，最多十一张参考图局部重绘风格化_2102875534593183745.json, 图片生成/图生图/Qwen Image 2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2114467187418292225.json, 图片生成/图生图/Qwen image2.1抠图去背景，图生图去水印一步到位_2110505250099646465.json, 图片生成/图生图/Qwen_Image_2.1超细节多图像编辑，最多十一张参考图局部重绘风格化_2105123251163848705.json, 图片生成/图生图/Qwen_Image_2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2117098298497658882.json, 图片生成/图生图/Qwen_image2.1抠图去背景，图生图去水印一步到位_2112349116150935553.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_331

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1超细节多图像编辑，最多十一张参考图局部重绘风格化_2102875534593183745.json、图片生成/图生图/Qwen Image 2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2114467187418292225.json、图片生成/图生图/Qwen image2.1抠图去背景，图生图去水印一步到位_2110505250099646465.json、图片生成/图生图/Qwen_Image_2.1超细节多图像编辑，最多十一张参考图局部重绘风格化_2105123251163848705.json、图片生成/图生图/Qwen_Image_2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2117098298497658882.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 4/6 个有
- `INTConstant` —— 4/6 个有
- `EmptyImage` —— 3/6 个有
- `孤海注释` —— 3/6 个有
- `LoadSharpModel` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `PrimitiveStringMultiline` —— 2/6 个有
- `ResolutionSelector` —— 2/6 个有
- `SharpPredict` —— 2/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `Text Multiline` —— 2/6 个有
- `YCGaussianPreview` —— 2/6 个有
- `easy seed` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
