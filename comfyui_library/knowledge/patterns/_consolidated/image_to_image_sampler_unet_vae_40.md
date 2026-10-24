---
name: image_to_image_sampler_unet_vae_40
type: Image To Image
frequency: 6
level: strong
coverage: 0.8735
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2511 图像编辑_遮罩编辑_2004146251220328449.json, 图片生成/图生图/Qwen Edit 2511 零偏移编辑图像_2003862140756893698.json, 图片生成/图生图/Qwen-Edit+2511-细化改图-零偏移图生图_2036406339810889730.json, 图片生成/图生图/Qwen-Edit-2511 Anypose 精确控制人体姿势_2084960929535582210.json, 图片生成/图生图/Qwen2511室内设计-局部修改变效果_2013202880232169474.json, 视频生成/文生视频/QwenEdit 2511（FH修复油腻感模型）_2004948756900573185.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_40

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2511 图像编辑_遮罩编辑_2004146251220328449.json、图片生成/图生图/Qwen Edit 2511 零偏移编辑图像_2003862140756893698.json、图片生成/图生图/Qwen-Edit+2511-细化改图-零偏移图生图_2036406339810889730.json、图片生成/图生图/Qwen-Edit-2511 Anypose 精确控制人体姿势_2084960929535582210.json、图片生成/图生图/Qwen2511室内设计-局部修改变效果_2013202880232169474.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `PreviewImage` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/6 个有
- `Get Image Size` —— 3/6 个有
- `LayerUtility: ImageReel` —— 3/6 个有
- `LayerUtility: ImageReelComposit` —— 3/6 个有
- `MaxNode` —— 3/6 个有
- `ReferenceLatent` —— 3/6 个有
- `TextInput_` —— 3/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `SetLatentNoiseMask` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `MaskPreview+` —— 1/6 个有
- `easy imageConcat` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 6 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
