---
name: image_to_image_sampler_clip_unet_121
type: Image To Image
frequency: 4
level: strong
coverage: 0.87775
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/fluxkontext_一键生成字效_1929844250890944514.json, 图片生成/图生图/kontext _ 基础开源版_1938657888149950466.json, 图片生成/图生图/kontext dev系列-黑红剪影风转绘_1945695804692811778.json, 图片生成/图生图/模型图生成效果图+_1969336789913772033.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_121

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/fluxkontext_一键生成字效_1929844250890944514.json、图片生成/图生图/kontext _ 基础开源版_1938657888149950466.json、图片生成/图生图/kontext dev系列-黑红剪影风转绘_1945695804692811778.json、图片生成/图生图/模型图生成效果图+_1969336789913772033.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `RH_Translator` —— 3/4 个有
- `ImageUpscaleWithModel` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageResize` —— 1/4 个有
- `ImageScaleBy` —— 1/4 个有
- `JWImageResizeByLongerSide` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `ShowText` —— 1/4 个有
- `easy textSwitch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 0.5 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
