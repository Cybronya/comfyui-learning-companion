---
name: image_to_image_lora_sampler_vae_15
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8322
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-edit2509（双截棍版）-图像编辑_1993588971607441409.json, 图片生成/图生图/Qwen-image-edit2059万物毛绒渲染_1998405103692447746.json, 图片生成/图生图/Qwen-image-edit2511指哪打哪工作流_1959082223985176577.json, 图片生成/图生图/Qwen-参考姿态一键换装_1977201193661407234.json, 图片生成/图生图/qwen edit 2509 双人合影工作流_1973757541383581697.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_vae_15

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-edit2509（双截棍版）-图像编辑_1993588971607441409.json、图片生成/图生图/Qwen-image-edit2059万物毛绒渲染_1998405103692447746.json、图片生成/图生图/Qwen-image-edit2511指哪打哪工作流_1959082223985176577.json、图片生成/图生图/Qwen-参考姿态一键换装_1977201193661407234.json、图片生成/图生图/qwen edit 2509 双人合影工作流_1973757541383581697.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `CR SDXL Aspect Ratio` —— 1/5 个有
- `EmptySD3LatentImage` —— 1/5 个有
- `ImageAndMaskPreview` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `JWImageResizeByLongerSide` —— 1/5 个有
- `NunchakuQwenImageDiTLoader` —— 1/5 个有
- `OpenposePreprocessor` —— 1/5 个有
- `easy imageScaleToNormPixels` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 5 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，5 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
