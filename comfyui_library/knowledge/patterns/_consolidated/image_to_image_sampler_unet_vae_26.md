---
name: image_to_image_sampler_unet_vae_26
type: Image To Image
frequency: 9
level: strong
coverage: 0.935556
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2512图生图工作流（摄影、电商洗图）_2022140446385901569.json, 图片生成/图生图/Qwen Image，反推洗图_1987161071591034881.json, 图片生成/图生图/Z-Image-Turbo-洗图工作流_1994007499646894081.json, 图片生成/图生图/动漫转真实 Qwen-edit+Zimage 双采样_2013604515278229505.json, 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑_2033152678896869378.json, 图片生成/图生图/小红书FireRed1.1 (单图编辑)_2031636180478992385.json, 图片生成/图生图/小红书FireRed1.1单图编辑_2047551024805715969.json, 图片生成/图生图/小红书双图编辑器_2034535893565968385.json, 图片生成/图生图/（自用）小红书FireRed-Image-edit 双图编辑（换装）_2029612197713813506.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_26

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen 2512图生图工作流（摄影、电商洗图）_2022140446385901569.json、图片生成/图生图/Qwen Image，反推洗图_1987161071591034881.json、图片生成/图生图/Z-Image-Turbo-洗图工作流_1994007499646894081.json、图片生成/图生图/动漫转真实 Qwen-edit+Zimage 双采样_2013604515278229505.json、图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑_2033152678896869378.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/9 个有
- `LoraLoaderModelOnly` —— 8/9 个有
- `ModelSamplingAuraFlow` —— 8/9 个有
- `CFGNorm` —— 7/9 个有
- `easy cleanGpuUsed` —— 7/9 个有
- `TextEncodeQwenImageEditPlus` —— 6/9 个有
- `CR Prompt Text` —— 5/9 个有
- `Image Comparer (rgthree)` —— 5/9 个有
- `CLIPTextEncode` —— 4/9 个有
- `easy int` —— 3/9 个有
- `AILab_QwenVL` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `Display Any (rgthree)` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `Int` —— 1/9 个有
- `Qwen3_VQA` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 2 - 8 | 9 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 0.6 - 1 | 9 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 2 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.6 - 1，9 个样本，取值集中（一致性 86%）
- 高发问题（10/9 个样本）：Steps较低可能导致细节不足
