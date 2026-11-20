---
name: image_to_image_lora_sampler_clip_126
type: Image To Image
frequency: 2
level: weak
coverage: 0.905
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DisplayText, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageConcanate, ImageResizeKJv2, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen2.5VL, RepeatLatentBatch, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/Flux_Krea真人洗图_1958462222928343041.json, 图片生成/图生图/Flux_Krea真人洗图_2072206265215971330.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_126

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux_Krea真人洗图_1958462222928343041.json、图片生成/图生图/Flux_Krea真人洗图_2072206265215971330.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DisplayText`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Qwen2.5VL`
- `RepeatLatentBatch`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.7 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
