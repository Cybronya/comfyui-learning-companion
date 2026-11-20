---
name: text_to_image_lora_sampler_clip_507
type: Text To Image
frequency: 3
level: strong
coverage: 0.851
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskFillHoles, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/G2.5细节修复参考版图生图处理生成工具_2101377463984152578.json, 图片生成/图生图/Qwen Image 2.1一键换脸｜图生图人物面部替换神器_2103027527827677185.json, 图片生成/图生图/Qwen Image 2.1换脸工作流，一键面部替换的图生图处理工具_2103172786389864449.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_507

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/G2.5细节修复参考版图生图处理生成工具_2101377463984152578.json、图片生成/图生图/Qwen Image 2.1一键换脸｜图生图人物面部替换神器_2103027527827677185.json、图片生成/图生图/Qwen Image 2.1换脸工作流，一键面部替换的图生图处理工具_2103172786389864449.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskFillHoles`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 2/3 个有
- `TextEncodeQwenImage21` —— 2/3 个有
- `GH_CropRestore` —— 1/3 个有
- `GH_MaskCropV2` —— 1/3 个有
- `GoohaiUniversalSlider` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `RH_RhartImageG25SunburstImageToImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
