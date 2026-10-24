---
name: image_to_image_upscale_sampler_unet
type: Image To Image
frequency: 8
level: moderate
coverage: 0.752625
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image图生图、反推、放大，无controlnet_1998247610295156737.json, 图片生成/图生图/Z-image超真实高清洗图-无AI感_2007465177616228353.json, 图片生成/图生图/z-image洗图_2064621958779727873.json, 图片生成/图生图/一键转Q版工作流V1_2059531242244231169.json, 图片生成/图生图/一键转Q版工作流V1_2066400918530252802.json, 图片生成/图生图/动漫图一键转Q版图工作流_2057792823910551554.json, 图片生成/图生图/图生图一键转Q版工作流V1_2064508373718102018.json, 图片生成/图生图/真人动漫二次元 一键转Q版_2057794622239371266.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_unet

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Z-image图生图、反推、放大，无controlnet_1998247610295156737.json、图片生成/图生图/Z-image超真实高清洗图-无AI感_2007465177616228353.json、图片生成/图生图/z-image洗图_2064621958779727873.json、图片生成/图生图/一键转Q版工作流V1_2059531242244231169.json、图片生成/图生图/一键转Q版工作流V1_2066400918530252802.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `Image Comparer (rgthree)` —— 7/8 个有
- `SetNode` —— 7/8 个有
- `GetNode` —— 6/8 个有
- `ImageScaleToTotalPixels` —— 6/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `easy cleanGpuUsed` —— 6/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `TextEncodeQwenImageEditPlus` —— 5/8 个有
- `easy imageConcat` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `CLIPTextEncode` —— 3/8 个有
- `ShowText|pysssss` —— 2/8 个有
- `孤海注释` —— 2/8 个有
- `AILab_QwenVL` —— 1/8 个有
- `JjkShowText` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `Qwen2.5VL` —— 1/8 个有
- `RH_Captioner_Pro` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 12 | 8 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | sgm_uniform | - | 8 | 75% |
| 重绘幅度 | 1 | 0.15 - 1 | 8 | 58% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 12，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 sgm_uniform，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，8 个样本
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足
