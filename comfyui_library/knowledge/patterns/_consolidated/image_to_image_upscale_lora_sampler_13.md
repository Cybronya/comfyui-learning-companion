---
name: image_to_image_upscale_lora_sampler_13
type: Image To Image
frequency: 12
level: strong
coverage: 0.915667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, PreviewImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAEEncodeTiled, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/人像——去ai感_2081677258783281153.json, 图片生成/图生图/人像——去ai感_2085027514606510081.json, 图片生成/图生图/人像——去ai感_2085029908484550658.json, 图片生成/图生图/人像——去ai感_2085216401987559426.json, 图片生成/图生图/人像——去除 AI 生硬质感精修_2085733503337066498.json, 图片生成/图生图/全身去ai感工作流_1977724357835456513.json, 图片生成/图生图/去ai感工作流_2051914099612762113.json, 图片生成/图生图/去ai感工作流_2058753876072951810.json, 图片生成/图生图/去ai感工作流_2062000900113256449.json, 图片生成/图生图/去ai感工作流_2063429228833624066.json, 图片生成/图生图/去ai感工作流_2083541760839610370.json, 图片生成/图生图/去ai感工作流_2083567100928548866.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/人像——去ai感_2081677258783281153.json、图片生成/图生图/人像——去ai感_2085027514606510081.json、图片生成/图生图/人像——去ai感_2085029908484550658.json、图片生成/图生图/人像——去ai感_2085216401987559426.json、图片生成/图生图/人像——去除 AI 生硬质感精修_2085733503337066498.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `PreviewImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplySageAttention` —— 11/12 个有
- `CLIPLoader` —— 11/12 个有
- `UNETLoader` —— 11/12 个有
- `ColorMatch` —— 1/12 个有
- `GetImageSize+` —— 1/12 个有
- `ImageComposite+` —— 1/12 个有
- `ImageScale` —— 1/12 个有
- `LayerMask: MaskGrow` —— 1/12 个有
- `LayerUtility: CropBoxResolve` —— 1/12 个有
- `LayerUtility: CropByMask` —— 1/12 个有
- `easy humanSegmentation` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 92% |
| 调度器 | kl_optimal | - | 12 | 100% |
| 重绘幅度 | 0.5 | 0.3 - 0.5 | 12 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 92%
- 调度器 最常用 kl_optimal，12 个样本，一致性 100%
- 重绘幅度 中位数 0.5，观测区间 0.3 - 0.5，12 个样本，取值集中（一致性 89%）
