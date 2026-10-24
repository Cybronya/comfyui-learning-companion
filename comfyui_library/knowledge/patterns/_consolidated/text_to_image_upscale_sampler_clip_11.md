---
name: text_to_image_upscale_sampler_clip_11
type: Text To Image
frequency: 8
level: strong
coverage: 0.7535
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxKVCache, ImageScaleToTotalPixels, ImageUpscaleWithModel, KSampler, LatentColorMatchSimple, PreviewImage, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Krea2-洗图加高清放大-大图专用_2071771710831022081.json, 图片生成/图生图/Krea2-洗图加高清放大-大图专用_2093239704954163201.json, 图片生成/图生图/Krea2-洗图加高清放大-大图专用_2093511680394354690.json, 图片生成/图生图/krea2图生图像百万像素_2072147342261833729.json, 图片生成/文生图/Krea2-大图专用 蓝神大佬优化 1600万像素_2071508472050577410.json, 图片生成/文生图/Krea2-文生图直出4K （效果惊人不输闭源）_2071588832386052097.json, 图片生成/文生图/krea2json格式图生图像百万像素_2071963341316255746.json, 图片生成/文生图/krea2json格式文生图像百万像素_2072007993671114754.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Krea2-洗图加高清放大-大图专用_2071771710831022081.json、图片生成/图生图/Krea2-洗图加高清放大-大图专用_2093239704954163201.json、图片生成/图生图/Krea2-洗图加高清放大-大图专用_2093511680394354690.json、图片生成/图生图/krea2图生图像百万像素_2072147342261833729.json、图片生成/文生图/Krea2-大图专用 蓝神大佬优化 1600万像素_2071508472050577410.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxKVCache`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSampler`
- `LatentColorMatchSimple`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/8 个有
- `Anything Everywhere3` —— 5/8 个有
- `Text Multiline` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `Anything Everywhere` —— 3/8 个有
- `TTResolutionSelector` —— 3/8 个有
- `Text` —— 3/8 个有
- `Text Concatenate` —— 3/8 个有
- `llama_cpp_instruct_adv` —— 3/8 个有
- `llama_cpp_model_loader` —— 3/8 个有
- `llama_cpp_parameters` —— 3/8 个有
- `Florence2ModelLoader` —— 2/8 个有
- `Florence2Run` —— 2/8 个有
- `Image Comparer (rgthree)` —— 2/8 个有
- `VAEEncode` —— 2/8 个有
- `Qwen3VL_Advanced` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 7 | 6 - 8 | 8 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler_ancestral | - | 8 | 88% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 0.75 | 0.2 - 1 | 8 | 49% |
| 宽度 | 1360 | 1360 - 1360 | 8 | 100% |
| 高度 | 2048 | 2048 - 2048 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 7，观测区间 6 - 8，8 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 0.75，观测区间 0.2 - 1，8 个样本，取值分散，一致性仅 49%
- 宽度 中位数 1360，观测区间 1360 - 1360，8 个样本，取值集中（一致性 100%）
- 高度 中位数 2048，观测区间 2048 - 2048，8 个样本，取值集中（一致性 100%）
- 高发问题（18/8 个样本）：Steps较低可能导致细节不足
