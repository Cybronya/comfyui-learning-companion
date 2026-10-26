---
name: image_to_image_sampler_unet_vae_22
type: Image To Image
frequency: 8
level: moderate
coverage: 0.888625
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit_图像编辑_1958798109751078913.json, 图片生成/图生图/QwenImageEdit AI图像编辑_1970710306030821378.json, 图片生成/图生图/Qwen_edit产品精修+白底_1976290317739626497.json, 图片生成/图生图/Qwen_image_edit 官方流_1957812877073772546.json, 图片生成/图生图/Qwen_image_edit官方工作流_1958175164557115394.json, 图片生成/图生图/Qwen_精准图像编辑_1960253257828478978.json, 图片生成/图生图/Qwen_通用图像编辑_1959538867303034882.json, 图片生成/图生图/Qwen终极编辑及CN控制网_1961097608129351682.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_22

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/QwenEdit_图像编辑_1958798109751078913.json、图片生成/图生图/QwenImageEdit AI图像编辑_1970710306030821378.json、图片生成/图生图/Qwen_edit产品精修+白底_1976290317739626497.json、图片生成/图生图/Qwen_image_edit 官方流_1957812877073772546.json、图片生成/图生图/Qwen_image_edit官方工作流_1958175164557115394.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `ModelPatchTorchSettings` —— 4/8 个有
- `PathchSageAttentionKJ` —— 4/8 个有
- `TorchCompileModel` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `BatchCropFromMaskAdvanced` —— 2/8 个有
- `BboxVisualize` —— 2/8 个有
- `ImageConcatenate_UTK` —— 2/8 个有
- `LayerUtility: TextBox` —— 2/8 个有
- `AIO_Preprocessor` —— 1/8 个有
- `CR Image Input Switch` —— 1/8 个有
- `ControlNetApplyAdvanced` —— 1/8 个有
- `ControlNetLoader` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `easy imagePixelPerfect` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 8 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 8 | 54% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，8 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（5/8 个样本）：Steps较低可能导致细节不足
