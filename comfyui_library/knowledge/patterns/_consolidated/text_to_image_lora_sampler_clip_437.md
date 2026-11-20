---
name: text_to_image_lora_sampler_clip_437
type: Text To Image
frequency: 4
level: strong
coverage: 0.887
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2114467187418292225.json, 图片生成/图生图/Qwen image 2.1一键模特换装｜服装迁移试衣黑科技｜电商换装省成本_2112088875962290178.json, 图片生成/图生图/Qwen image2.1抠图去背景，图生图去水印一步到位_2110505250099646465.json, 图片生成/图生图/Qwen_image2.1抠图去背景，图生图去水印一步到位_2112349116150935553.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_437

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1高斯泼溅版任意角度旋转，图像自由360°转换更精准_2114467187418292225.json、图片生成/图生图/Qwen image 2.1一键模特换装｜服装迁移试衣黑科技｜电商换装省成本_2112088875962290178.json、图片生成/图生图/Qwen image2.1抠图去背景，图生图去水印一步到位_2110505250099646465.json、图片生成/图生图/Qwen_image2.1抠图去背景，图生图去水印一步到位_2112349116150935553.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `QwenImage21Cache` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `EmptyImage` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `Int` —— 1/4 个有
- `LoadSharpModel` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `SharpPredict` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `YCGaussianPreview` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
