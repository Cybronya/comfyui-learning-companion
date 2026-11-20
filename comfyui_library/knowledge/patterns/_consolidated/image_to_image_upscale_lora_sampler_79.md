---
name: image_to_image_upscale_lora_sampler_79
type: Image To Image
frequency: 3
level: strong
coverage: 0.896333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, LoadImage, LoraLoader, ReferenceLatent, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/😼服装开发到平铺拍摄商用落地comfyui全流程😸_2000087491791159297.json, 图片生成/文生图/【全网独家模型】阮旭东_F.1 Kontext DEV国庆举国欢庆喜庆氛围工作流_20250827_1960606116021493762.json, 平台全量/阮旭东_全网首个怀孕后变怀孕前Kontext工作流_1961625220354347010.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_79

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/😼服装开发到平铺拍摄商用落地comfyui全流程😸_2000087491791159297.json、图片生成/文生图/【全网独家模型】阮旭东_F.1 Kontext DEV国庆举国欢庆喜庆氛围工作流_20250827_1960606116021493762.json、平台全量/阮旭东_全网首个怀孕后变怀孕前Kontext工作流_1961625220354347010.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `CR Latent Batch Size` —— 1/3 个有
- `CR Prompt Text` —— 1/3 个有
- `FastCanvas` —— 1/3 个有
- `FastCanvasTool` —— 1/3 个有
- `ImageCrop+` —— 1/3 个有
- `LayerMask: BiRefNetUltraV2` —— 1/3 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/3 个有
- `LoadImageOutput` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | 1 - 1.2 | 3 | 91% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1.2，3 个样本，取值集中（一致性 91%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
