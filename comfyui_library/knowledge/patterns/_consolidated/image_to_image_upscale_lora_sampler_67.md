---
name: image_to_image_upscale_lora_sampler_67
type: Image To Image
frequency: 3
level: strong
coverage: 0.864667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoader, ReferenceLatent, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/模型图生成效果图+_1969336789913772033.json, 图片生成/图生图/溶图 色彩变动小_Kontext_2064292965186621441.json, 图片生成/图生图/😼服装开发到平铺拍摄商用落地comfyui全流程😸_2000087491791159297.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_67

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/模型图生成效果图+_1969336789913772033.json、图片生成/图生图/溶图 色彩变动小_Kontext_2064292965186621441.json、图片生成/图生图/😼服装开发到平铺拍摄商用落地comfyui全流程😸_2000087491791159297.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Latent Batch Size` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `FastCanvas` —— 1/3 个有
- `FastCanvasTool` —— 1/3 个有
- `ImageCrop+` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `ImageStitch` —— 1/3 个有
- `LayerMask: BiRefNetUltraV2` —— 1/3 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/3 个有
- `LoadImageOutput` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 25 | 3 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | 0.5 - 1 | 3 | 72% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 25，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.5 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
