---
name: image_to_image_sampler_unet_vae_40
type: Image To Image
frequency: 4
level: moderate
coverage: 0.93325
common_nodes: [CFGNorm, CLIPLoader, CR Text, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen_image_Edit千问图片局部重绘2509版_1970742241134321665.json, 图片生成/图生图/Qwen光影_2002990949435338754.json, 图片生成/图生图/千问Edit-Plus局部精准编辑_1970474938392059905.json, 图片生成/图生图/千问Edit局部精准编辑_1965034120084602882.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_40

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen_image_Edit千问图片局部重绘2509版_1970742241134321665.json、图片生成/图生图/Qwen光影_2002990949435338754.json、图片生成/图生图/千问Edit-Plus局部精准编辑_1970474938392059905.json、图片生成/图生图/千问Edit局部精准编辑_1965034120084602882.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 3/4 个有
- `INPAINT_MaskedFill` —— 3/4 个有
- `Mask Fill Holes` —— 3/4 个有
- `TextEncodeQwenImageEditPlus` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `Text` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `TextEncodeQwenImageEdit` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 4 | 81% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 4 | 69% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
