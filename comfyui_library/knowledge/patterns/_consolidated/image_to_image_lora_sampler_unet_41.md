---
name: image_to_image_lora_sampler_unet_41
type: Image To Image
frequency: 12
level: weak
coverage: 0.868333
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-Edit图像编辑用法【基础流】_1958688533957525505.json, 图片生成/图生图/Qwen-image-edit2059万物毛绒渲染_1998405103692447746.json, 图片生成/图生图/Qwen2511+模特换脸_2003793177066782722.json, 图片生成/图生图/Qwen2511+模特换装_2003728513553317889.json, 图片生成/图生图/Qwen2511去水印 换装 全能图片V1_2054130825704288257.json, 图片生成/图生图/Qwen2511图片编辑(自用版)_2062203408433635330.json, 图片生成/图生图/Qwen2511换装最新图像编辑_2072124811735822338.json, 图片生成/图生图/Qwen2511换装最新图像编辑_2072133881209384962.json, 图片生成/图生图/一键美瞳_2009605418158399489.json, 图片生成/图生图/图片去水印-Qwen-Edit-2511_2077755293496336386.json, 图片生成/图生图/是青慕啊_颠覆单帧创作！多视角人物生成，Qwen 让画面活起来⚡_2037200573065334786.json, 图片生成/文生图/Qwen-Edit 2509 (文改图 PLus版）_1979253121035702273.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_41

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen-image-Edit图像编辑用法【基础流】_1958688533957525505.json、图片生成/图生图/Qwen-image-edit2059万物毛绒渲染_1998405103692447746.json、图片生成/图生图/Qwen2511+模特换脸_2003793177066782722.json、图片生成/图生图/Qwen2511+模特换装_2003728513553317889.json、图片生成/图生图/Qwen2511去水印 换装 全能图片V1_2054130825704288257.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 12 个 workflow 都包含：
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
- `ImageScaleToTotalPixels` —— 11/12 个有
- `TextEncodeQwenImageEditPlus` —— 11/12 个有
- `CR Text` —— 8/12 个有
- `ImageConcanate` —— 8/12 个有
- `FluxKontextMultiReferenceLatentMethod` —— 7/12 个有
- `GetNode` —— 4/12 个有
- `PreviewImage` —— 4/12 个有
- `SetNode` —— 4/12 个有
- `Image Comparer (rgthree)` —— 3/12 个有
- `Anything Everywhere3` —— 2/12 个有
- `PrimitiveStringMultiline` —— 2/12 个有
- `Anything Everywhere` —— 1/12 个有
- `CR Seed` —— 1/12 个有
- `GetImageSize` —— 1/12 个有
- `ImageScale` —— 1/12 个有
- `RHHiddenNodes` —— 1/12 个有
- `TextEncodeQwenImageEditEnhanced` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 12 | 20% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 12 | 53% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，12 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，12 个样本
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（17/12 个样本）：Steps较低可能导致细节不足
