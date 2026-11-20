---
name: image_to_image_sampler_unet_vae_28
type: Image To Image
frequency: 9
level: moderate
coverage: 0.890556
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen_image_Edit千问图片局部重绘2509版_1970742241134321665.json, 图片生成/图生图/Qwen一句话改变图片 单图编辑_1991781423713562626.json, 图片生成/图生图/qwen-edit-2509三图万物迁移_1993203591836008450.json, 图片生成/图生图/qwen-edit-plus一键换装（最强编辑）_1970796555513065473.json, 图片生成/图生图/千问Edit-Plus局部精准编辑_1970474938392059905.json, 图片生成/图生图/千问Edit局部精准编辑_1965034120084602882.json, 图片生成/图生图/千问编辑put it here万物溶图_1965372671791874050.json, 图片生成/图生图/溶图打光-透视纠正_1980932243189317633.json, 平台全量/Flux2-溶图合成打光-最新全流程_2087374503692300290.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_28

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen_image_Edit千问图片局部重绘2509版_1970742241134321665.json、图片生成/图生图/Qwen一句话改变图片 单图编辑_1991781423713562626.json、图片生成/图生图/qwen-edit-2509三图万物迁移_1993203591836008450.json、图片生成/图生图/qwen-edit-plus一键换装（最强编辑）_1970796555513065473.json、图片生成/图生图/千问Edit-Plus局部精准编辑_1970474938392059905.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 7/9 个有
- `Image Comparer (rgthree)` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `TextEncodeQwenImageEditPlus` —— 6/9 个有
- `CR Text` —— 5/9 个有
- `LoraLoaderModelOnly` —— 5/9 个有
- `TextEncodeQwenImageEdit` —— 5/9 个有
- `CR Text Concatenate` —— 4/9 个有
- `FastCanvas` —— 3/9 个有
- `FastCanvasTool` —— 3/9 个有
- `INPAINT_MaskedFill` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `Mask Fill Holes` —— 3/9 个有
- `ImageConcanate` —— 2/9 个有
- `LayerUtility: CropByMask V2` —— 2/9 个有
- `RMBG` —— 2/9 个有
- `Text` —— 1/9 个有
- `easy imageScaleDownToSize` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 9 | 59% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 9 | 59% |
| 采样算法 | euler | - | 9 | 78% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 78%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（6/9 个样本）：Steps较低可能导致细节不足
