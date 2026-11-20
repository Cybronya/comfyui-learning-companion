---
name: image_to_image_lora_sampler_unet_147
type: Image To Image
frequency: 4
level: strong
coverage: 0.91225
common_nodes: [Anything Everywhere3, CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed 转写实 带剪裁和标准化处理v2_2031261630184562689.json, 图片生成/图生图/FireRed 转写实_2030669437854027777.json, 图片生成/图生图/Qwen-Image-Edit 2509-自动溶图+透视矫正_1987847089428344834.json, 图片生成/图生图/Qwen-Image-Edit 2509-自动溶图+透视矫正_1987858824298172417.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_147

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FireRed 转写实 带剪裁和标准化处理v2_2031261630184562689.json、图片生成/图生图/FireRed 转写实_2030669437854027777.json、图片生成/图生图/Qwen-Image-Edit 2509-自动溶图+透视矫正_1987847089428344834.json、图片生成/图生图/Qwen-Image-Edit 2509-自动溶图+透视矫正_1987858824298172417.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere3`
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `FluxKontextImageScale` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `easy positive` —— 2/4 个有
- `AddLabel` —— 1/4 个有
- `FastCanvas` —— 1/4 个有
- `FastCanvasTool` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `InpaintCropImproved` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `RunningHub Deepcleaner` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
