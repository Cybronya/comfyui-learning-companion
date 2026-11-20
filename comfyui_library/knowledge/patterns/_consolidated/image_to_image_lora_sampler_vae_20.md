---
name: image_to_image_lora_sampler_vae_20
type: Image To Image
frequency: 3
level: moderate
coverage: 0.728667
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-edit2509（双截棍版）-图像编辑_1993588971607441409.json, 图片生成/图生图/qwen-edit-2509姿势迁移_1982348327364771842.json, 图片生成/图生图/姿态控制_1985545203467624449.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_20

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen-edit2509（双截棍版）-图像编辑_1993588971607441409.json、图片生成/图生图/qwen-edit-2509姿势迁移_1982348327364771842.json、图片生成/图生图/姿态控制_1985545203467624449.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `JoinStrings` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PrimitiveStringMultiline` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageScaleToMegapixels` —— 1/3 个有
- `JWImageResizeByLongerSide` —— 1/3 个有
- `NunchakuQwenImageDiTLoader` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `VAEDecodeTiled` —— 1/3 个有
- `VAEEncodeTiled` —— 1/3 个有
- `easy imageScaleToNormPixels` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.35 - 1 | 3 | 61% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，3 个样本
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
