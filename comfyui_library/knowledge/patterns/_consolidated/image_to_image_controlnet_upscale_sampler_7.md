---
name: image_to_image_controlnet_upscale_sampler_7
type: Image To Image
frequency: 3
level: moderate
coverage: 0.861333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, ImageUpscaleWithModel, KSampler, LineArtPreprocessor, LoadImage, PreviewImage, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode, Zoe-DepthMapPreprocessor]
problems: []
missing: []
members: [图片生成/图生图/【全网最强】老照片修复_1887837453884260353.json, 平台全量/sd1.5-老照片修复上色_1887073323971670017.json, 平台全量/素描建筑线稿生成器_1804057774526554113.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_sampler_7

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【全网最强】老照片修复_1887837453884260353.json、平台全量/sd1.5-老照片修复上色_1887073323971670017.json、平台全量/素描建筑线稿生成器_1804057774526554113.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `ImageUpscaleWithModel`
- `KSampler`
- `LineArtPreprocessor`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `Zoe-DepthMapPreprocessor`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `Joy_caption_two` —— 2/3 个有
- `Joy_caption_two_load` —— 2/3 个有
- `OpenposePreprocessor` —— 2/3 个有
- `ReActorFaceSwap` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `ImageCrop` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `LoraLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.4 | 0.4 - 0.85 | 3 | 61% |
| 采样步数 | 25 | 20 - 25 | 3 | 90% |
| Prompt 约束强度(CFG) | 7.5 | 7.5 - 8 | 3 | 97% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 0.6 | 0.6 - 1 | 3 | 74% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.4，观测区间 0.4 - 0.85，3 个样本
- 采样步数 中位数 25，观测区间 20 - 25，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 7.5，观测区间 7.5 - 8，3 个样本，取值集中（一致性 97%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 1，3 个样本
