---
name: image_to_image_lora_sampler_unet_173
type: Image To Image
frequency: 4
level: strong
coverage: 0.88675
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2511图像编辑多合一工作流_2003654587804467201.json, 图片生成/图生图/Qwen-Image-Edit-2511新版图像编辑（单图模式工作流）_2011577913421864962.json, 图片生成/图生图/Qwen_360° 视图 多视角工作流_1993279358852939777.json, 图片生成/图生图/Qwen_人物_物品_产品 多视图 一键生成工作流_1993649585836982273.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_173

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2511图像编辑多合一工作流_2003654587804467201.json、图片生成/图生图/Qwen-Image-Edit-2511新版图像编辑（单图模式工作流）_2011577913421864962.json、图片生成/图生图/Qwen_360° 视图 多视角工作流_1993279358852939777.json、图片生成/图生图/Qwen_人物_物品_产品 多视图 一键生成工作流_1993649585836982273.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
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
- `CFGNorm` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `CameraControlPromptNode` —— 2/4 个有
- `ImageUpscaleWithModel` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `InpaintModelConditioning` —— 1/4 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/4 个有
- `MaskFillHoles` —— 1/4 个有
- `Textbox` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（23/4 个样本）：Steps较低可能导致细节不足
