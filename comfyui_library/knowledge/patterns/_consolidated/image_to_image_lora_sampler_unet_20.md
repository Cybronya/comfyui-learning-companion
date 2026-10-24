---
name: image_to_image_lora_sampler_unet_20
type: Image To Image
frequency: 16
level: moderate
coverage: 0.910687
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/(Flymy场景一致性增加)Qwen Edit图像编辑BF16满血版V1_1958453381591416833.json, 图片生成/图生图/(修复版)Qwen Edit图像编辑V1_1958336878166622210.json, 图片生成/图生图/(光线恢复)Qwen-Edit图像编辑_2039539381182144514.json, 图片生成/图生图/002.Qwen编辑之王013.批量洗图_2034653609324978178.json, 图片生成/图生图/1225-test_2004096081766064130.json, 图片生成/图生图/83 Qwen+2511+图生图一致性之王！_2059094357931810817.json, 图片生成/图生图/Qwen 2511 三图一致性组合_2004791701359263745.json, 图片生成/图生图/Qwen 2511 图生图一致性之王！_2003998202372235265.json, 图片生成/图生图/Qwen 2511-单多图编辑_2007651003973246978.json, 图片生成/图生图/Qwen 2511_一键Chibi角色风格转换 Q版风格化_2012096670162489345.json, 图片生成/图生图/Qwen Image Edit -多图编辑_2008007728786055170.json, 图片生成/图生图/Qwen Image Edit 2511-单图多图编辑_2054200267113025537.json, 图片生成/图生图/Qwen Image Edit 2511-图片编辑_2003699045224857601.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑 单图编辑 动图合成_2008531575331364865.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2003539764081008641.json, 图片生成/图生图/Qwen Image Edit 2511-支持单图多图编辑_2004231861838770178.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_20

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/(Flymy场景一致性增加)Qwen Edit图像编辑BF16满血版V1_1958453381591416833.json、图片生成/图生图/(修复版)Qwen Edit图像编辑V1_1958336878166622210.json、图片生成/图生图/(光线恢复)Qwen-Edit图像编辑_2039539381182144514.json、图片生成/图生图/002.Qwen编辑之王013.批量洗图_2034653609324978178.json、图片生成/图生图/1225-test_2004096081766064130.json…）

- **类型**：Image To Image
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 13/16 个有
- `TextEncodeQwenImageEditPlus` —— 13/16 个有
- `Image Comparer (rgthree)` —— 12/16 个有
- `FluxKontextMultiReferenceLatentMethod` —— 11/16 个有
- `ImageConcatMulti` —— 10/16 个有
- `EmptySD3LatentImage` —— 8/16 个有
- `CR Prompt Text` —— 3/16 个有
- `EmptyLatentImage` —— 3/16 个有
- `TextEncodeQwenImageEdit` —— 3/16 个有
- `CR Text` —— 2/16 个有
- `easy imageSize` —— 2/16 个有
- `AILab_QwenVL` —— 1/16 个有
- `ImageScaleToMaxDimension` —— 1/16 个有
- `LHSTW30M_BatchLoadImageList` —— 1/16 个有
- `LHSTW30M_Comment` —— 1/16 个有
- `LHSTW30M_PromptInput` —— 1/16 个有
- `LayerUtility: PurgeVRAM` —— 1/16 个有
- `Qwen3_VQA` —— 1/16 个有
- `easy saveText` —— 1/16 个有
- `easy showAnything` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 16 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 16 | 58% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | simple | - | 16 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |
| 宽度 | 1024 | 512 - 1024 | 3 | 72% |
| 高度 | 768 | 512 - 768 | 3 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/16 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，16 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，16 个样本
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 simple，16 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1024，3 个样本
- 高度 中位数 768，观测区间 512 - 768，3 个样本，取值集中（一致性 82%）
- 高发问题（14/16 个样本）：Steps较低可能导致细节不足
