---
name: image_to_image_lora_sampler_unet_102
type: Image To Image
frequency: 6
level: moderate
coverage: 0.709833
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed Image Edit 1.1 8步加速_2031361650225319938.json, 图片生成/图生图/FireRed Image-Edit 1.1_2032008809652166657.json, 图片生成/图生图/FireRed-Image-Edit-1.1 图像编辑_2027773296359514113.json, 图片生成/图生图/FireRed-Image-EditV1.1单图编辑_2029504867747766274.json, 图片生成/图生图/QWEN_CAMERA摄像机镜头角度切换图像编辑工作流_2066750376380035073.json, 图片生成/图生图/QWEN_多图编辑工作流（用于图像合成）_2066759807960440834.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_102

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FireRed Image Edit 1.1 8步加速_2031361650225319938.json、图片生成/图生图/FireRed Image-Edit 1.1_2032008809652166657.json、图片生成/图生图/FireRed-Image-Edit-1.1 图像编辑_2027773296359514113.json、图片生成/图生图/FireRed-Image-EditV1.1单图编辑_2029504867747766274.json、图片生成/图生图/QWEN_CAMERA摄像机镜头角度切换图像编辑工作流_2066750376380035073.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 5/6 个有
- `FluxKontextImageScale` —— 5/6 个有
- `TextEncodeQwenImageEditPlus` —— 5/6 个有
- `TextConcatenate` —— 2/6 个有
- `DF_Get_image_size` —— 1/6 个有
- `EmptyLatentImage` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Image Saver` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `QwenMultiangleCameraNode` —— 1/6 个有
- `ReferenceLatent` —— 1/6 个有
- `Switch any [Crystools]` —— 1/6 个有
- `TextEncodeQwenImageEdit` —— 1/6 个有
- `easy showAnything` —— 1/6 个有
- `ttN text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 4 - 40 | 6 | 39% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 6 | 53% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1920 | - | 1 | 100% |
| 高度 | 1080 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 40，观测区间 4 - 40，6 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
