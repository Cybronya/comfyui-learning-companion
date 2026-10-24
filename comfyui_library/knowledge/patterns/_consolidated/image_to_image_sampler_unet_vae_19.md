---
name: image_to_image_sampler_unet_vae_19
type: Image To Image
frequency: 10
level: moderate
coverage: 0.8661
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit_图像编辑_1958798109751078913.json, 图片生成/图生图/QwenImageEdit AI图像编辑_1970710306030821378.json, 图片生成/图生图/Qwen_Image_Edit 超强编辑 _ 万物可改 _ 开源可部署_1959226946603397122.json, 图片生成/图生图/Qwen_edit产品精修+白底_1976290317739626497.json, 图片生成/图生图/Qwen_image_edit 官方流_1957812877073772546.json, 图片生成/图生图/Qwen_image_edit官方工作流_1958175164557115394.json, 图片生成/图生图/Qwen_通用图像编辑_1959538867303034882.json, 图片生成/图生图/▶Qwen图像编辑流_1958456013403877377.json, 图片生成/图生图/千问Edit印花提取_1965114537508786178.json, 图片生成/图生图/说话改图工作流大集合_1971841856017526785.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_19

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/QwenEdit_图像编辑_1958798109751078913.json、图片生成/图生图/QwenImageEdit AI图像编辑_1970710306030821378.json、图片生成/图生图/Qwen_Image_Edit 超强编辑 _ 万物可改 _ 开源可部署_1959226946603397122.json、图片生成/图生图/Qwen_edit产品精修+白底_1976290317739626497.json、图片生成/图生图/Qwen_image_edit 官方流_1957812877073772546.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 8/10 个有
- `Image Comparer (rgthree)` —— 4/10 个有
- `PreviewImage` —— 4/10 个有
- `Fast Groups Bypasser (rgthree)` —— 3/10 个有
- `ConditioningZeroOut` —— 2/10 个有
- `LayerUtility: TextBox` —— 2/10 个有
- `ModelPatchTorchSettings` —— 2/10 个有
- `PathchSageAttentionKJ` —— 2/10 个有
- `RH_Translator` —— 2/10 个有
- `TorchCompileModel` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `ImageConcatenate_UTK` —— 1/10 个有
- `RH_ComfyFluxKontext` —— 1/10 个有
- `RH_Jimeng4_Image2Image` —— 1/10 个有
- `RH_Nano_Banana_Image2Image` —— 1/10 个有
- `TextEncodeQwenImageEditPlus` —— 1/10 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 20 | 10 | 52% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 10 | 61% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（5/10 个样本）：Steps较低可能导致细节不足
