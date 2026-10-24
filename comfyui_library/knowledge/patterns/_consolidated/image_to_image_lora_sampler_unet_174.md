---
name: image_to_image_lora_sampler_unet_174
type: Image To Image
frequency: 3
level: strong
coverage: 0.839333
common_nodes: [BatchCropFromMaskAdvanced, BboxVisualize, CFGNorm, CLIPLoader, Fast Groups Bypasser (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingAuraFlow, PathchSageAttentionKJ, PreviewImage, SaveImage, TorchCompileModel, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit终极编辑增强版Plus_1970547405684940802.json, 图片生成/图生图/Qwen_精准图像编辑_1960253257828478978.json, 图片生成/图生图/Qwen终极编辑及CN控制网_1961097608129351682.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_174

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/QwenEdit终极编辑增强版Plus_1970547405684940802.json、图片生成/图生图/Qwen_精准图像编辑_1960253257828478978.json、图片生成/图生图/Qwen终极编辑及CN控制网_1961097608129351682.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BatchCropFromMaskAdvanced`
- `BboxVisualize`
- `CFGNorm`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `SaveImage`
- `TorchCompileModel`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `CR Image Input Switch` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `TextEncodeQwenImageEdit` —— 2/3 个有
- `easy imagePixelPerfect` —— 2/3 个有
- `ControlNetApplyAdvanced` —— 1/3 个有
- `ControlNetLoader` —— 1/3 个有
- `ImageConcatenateMulti_UTK` —— 1/3 个有
- `ImageConcatenate_UTK` —— 1/3 个有
- `ImageScaleByAspectRatio_UTK` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_multistep | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
