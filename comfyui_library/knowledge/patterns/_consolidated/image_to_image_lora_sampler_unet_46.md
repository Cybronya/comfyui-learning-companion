---
name: image_to_image_lora_sampler_unet_46
type: Image To Image
frequency: 13
level: weak
coverage: 0.831923
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-Edit图像编辑用法【基础流】_1958688533957525505.json, 图片生成/图生图/Qwen-image-edit2059万物毛绒渲染_1998405103692447746.json, 图片生成/图生图/Qwen-参考姿态一键换装_1977201193661407234.json, 图片生成/图生图/Qwen2511+模特换脸_2003793177066782722.json, 图片生成/图生图/Qwen2511+模特换装_2003728513553317889.json, 图片生成/图生图/Qwen2511去水印 换装 全能图片V1_2054130825704288257.json, 图片生成/图生图/Qwen2511图片编辑(自用版)_2062203408433635330.json, 图片生成/图生图/千问  镜头移动_1993500582268829697.json, 图片生成/图生图/图片去水印-Qwen-Edit-2511_2077755293496336386.json, 图片生成/图生图/工作流基础系列11-QwenImageEdit2511单图编辑_2004000394919485442.json, 图片生成/图生图/工作流基础系列12-QwenImageEdit2511双图编辑_2004026267299135489.json, 图片生成/图生图/组件系列12-QWEN-EDIT-2511单图编辑_2059098441153859586.json, 图片生成/图生图/组件系列13-QWEN-EDIT-2511多图编辑_2059099538136322050.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_46

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Qwen-image-Edit图像编辑用法【基础流】_1958688533957525505.json、图片生成/图生图/Qwen-image-edit2059万物毛绒渲染_1998405103692447746.json、图片生成/图生图/Qwen-参考姿态一键换装_1977201193661407234.json、图片生成/图生图/Qwen2511+模特换脸_2003793177066782722.json、图片生成/图生图/Qwen2511+模特换装_2003728513553317889.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `TextEncodeQwenImageEditPlus` —— 12/13 个有
- `ImageScaleToTotalPixels` —— 11/13 个有
- `CR Text` —— 9/13 个有
- `FluxKontextMultiReferenceLatentMethod` —— 8/13 个有
- `Image Comparer (rgthree)` —— 7/13 个有
- `PreviewImage` —— 7/13 个有
- `GetNode` —— 6/13 个有
- `SetNode` —— 6/13 个有
- `ImageConcanate` —— 5/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/13 个有
- `Seed (rgthree)` —— 4/13 个有
- `Anything Everywhere3` —— 2/13 个有
- `PrimitiveStringMultiline` —— 2/13 个有
- `ReferenceLatent` —— 2/13 个有
- `easy promptList` —— 2/13 个有
- `Anything Everywhere` —— 1/13 个有
- `OpenposePreprocessor` —— 1/13 个有
- `TextEncodeQwenImageEditEnhanced` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 13 | 20% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 13 | 56% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，13 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（11/13 个样本）：Steps较低可能导致细节不足
