---
name: image_to_image_sampler_clip_unet_131
type: Image To Image
frequency: 5
level: strong
coverage: 0.8176
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/万物皆可涂鸦_1965395252951531521.json, 图片生成/图生图/人物去除+衣服提取+透明背景_1945018713423929346.json, 平台全量/Kontext一句话换装最新版_1956389233252597761.json, 平台全量/kontext_一键移除-2.0_1957771054355771394.json, 平台全量/万物移除_kontext版本_1987336775465152514.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_131

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/万物皆可涂鸦_1965395252951531521.json、图片生成/图生图/人物去除+衣服提取+透明背景_1945018713423929346.json、平台全量/Kontext一句话换装最新版_1956389233252597761.json、平台全量/kontext_一键移除-2.0_1957771054355771394.json、平台全量/万物移除_kontext版本_1987336775465152514.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `Anything Everywhere` —— 3/5 个有
- `Anything Everywhere3` —— 2/5 个有
- `ChinesePrompt_Mix` —— 2/5 个有
- `INPAINT_MaskedFill` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `Evaluate Strings` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 5 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
