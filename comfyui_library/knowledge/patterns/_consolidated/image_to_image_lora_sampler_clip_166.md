---
name: image_to_image_lora_sampler_clip_166
type: Image To Image
frequency: 2
level: weak
coverage: 0.8885
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, ConstrainImage|pysssss, DualCLIPLoader, FloatSlider, Image Filter Adjustments, ImageCompositeMasked, ImageNoiseAugmentation, InspyrenetRembg, InvertMask, Joy_caption_two, Joy_caption_two_load, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, RepeatLatentBatch, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/景深 - 图生图 - F.1_1900235357496012801.json, 图片生成/图生图/景深 - 图生图 - 控制 - F.1_1900753740746629122.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_166

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/景深 - 图生图 - F.1_1900235357496012801.json、图片生成/图生图/景深 - 图生图 - 控制 - F.1_1900753740746629122.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `ConstrainImage|pysssss`
- `DualCLIPLoader`
- `FloatSlider`
- `Image Filter Adjustments`
- `ImageCompositeMasked`
- `ImageNoiseAugmentation`
- `InspyrenetRembg`
- `InvertMask`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RepeatLatentBatch`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `FaceDetailer` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageColorMatch+` —— 1/2 个有
- `SAMLoader` —— 1/2 个有
- `SetShakkerLabsUnionControlNetType` —— 1/2 个有
- `UltralyticsDetectorProvider` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | deis | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.85 | - | 2 | 100% |
| ControlNet 权重 | 0.7 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 35，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
