---
name: image_to_image_sampler_clip_unet_32
type: Image To Image
frequency: 10
level: moderate
coverage: 0.9279
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image，反推洗图_1987161071591034881.json, 图片生成/图生图/Qwen-Image 图生图_1958119913732919297.json, 图片生成/图生图/Qwen-Image 手动遮罩局部修改_1958468974650540033.json, 图片生成/图生图/Z-image 平替Flux2 图片反推_1994616402810114049.json, 图片生成/图生图/Z-image自动洗图-图生图image to image_1994249998170865666.json, 图片生成/图生图/z-image【超强图片编辑】图像编辑_1994750669573791745.json, 图片生成/图生图/z-image图生图-洗图工作流_1994593121038180354.json, 图片生成/图生图/（换脸版-lora支持）Red-Z-image + Qwen3自动二阶段真实感洗图2K版_1998250117671059458.json, 图片生成/图生图/（换脸版-lora支持）Red-Z-image + Qwen3自动二阶段真实感洗图2K版_2003338801550327809.json, 图片生成/图生图/（自用）成人摄影Z-image + Qwen3自动洗图2K版_1993954685472227329.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_32

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen Image，反推洗图_1987161071591034881.json、图片生成/图生图/Qwen-Image 图生图_1958119913732919297.json、图片生成/图生图/Qwen-Image 手动遮罩局部修改_1958468974650540033.json、图片生成/图生图/Z-image 平替Flux2 图片反推_1994616402810114049.json、图片生成/图生图/Z-image自动洗图-图生图image to image_1994249998170865666.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/10 个有
- `Qwen3_VQA` —— 8/10 个有
- `easy showAnything` —— 8/10 个有
- `ConditioningZeroOut` —— 7/10 个有
- `ImageConcanate` —— 7/10 个有
- `LayerUtility: PurgeVRAM` —— 7/10 个有
- `Any To Any` —— 4/10 个有
- `VHS_VideoCombine` —— 4/10 个有
- `CR Prompt Text` —— 3/10 个有
- `Float` —— 3/10 个有
- `LoraLoaderModelOnly` —— 3/10 个有
- `ModelSamplingAuraFlow` —— 3/10 个有
- `VHS_SelectFilename` —— 3/10 个有
- `JjkText` —— 2/10 个有
- `Text Concatenate` —— 2/10 个有
- `DuckHideNode` —— 1/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `ImageConcatMulti` —— 1/10 个有
- `SetLatentNoiseMask` —— 1/10 个有
- `TT_img_enc` —— 1/10 个有
- `TT_img_enc_v2` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 6 - 20 | 10 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 10 | 33% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 60% |
| 重绘幅度 | 1 | 0.71 - 1 | 10 | 88% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 6 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，10 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.71 - 1，10 个样本，取值集中（一致性 88%）
