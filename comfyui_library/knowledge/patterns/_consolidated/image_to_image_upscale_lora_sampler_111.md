---
name: image_to_image_upscale_lora_sampler_111
type: Image To Image
frequency: 2
level: weak
coverage: 0.7775
common_nodes: [Anything Everywhere3, CLIPLoader, CLIPTextEncode, Image Comparer (rgthree), ImageUpscaleWithModel, JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelSamplingSD3, PreviewImage, RH_Captioner, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy int, easy promptConcat, easy showAnything, wanBlockSwap]
problems: []
missing: []
members: [图片生成/图生图/【组合非收敛版】wan2.1洗图+4K超清放大_1962106681834586114.json, 平台全量/【9成还原】wan2.1图像4K超清放大_1962886386615562242.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_111

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【组合非收敛版】wan2.1洗图+4K超清放大_1962106681834586114.json、平台全量/【9成还原】wan2.1图像4K超清放大_1962886386615562242.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PreviewImage`
- `RH_Captioner`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy int`
- `easy promptConcat`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16 | - | 2 | 75% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 0.225 | - | 2 | 44% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 16，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 0.225，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
