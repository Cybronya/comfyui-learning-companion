---
name: text_to_image_lora_sampler_clip_655
type: Text To Image
frequency: 2
level: weak
coverage: 0.9015
common_nodes: [CLIPLoaderGGUF, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Float, HAIGC_LoadImagesFromZip, ImageConcatMulti, ImageResizeAdvanced, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, Qwen3_VQA, RepeatLatentBatch, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/图生图洗图-直出4Z-image（批量工作流）_2045060291414728705.json, 图片生成/图生图/杰洛特-图生图洗图-Z-image（单张工作流）_2044953447383961602.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_655

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图生图洗图-直出4Z-image（批量工作流）_2045060291414728705.json、图片生成/图生图/杰洛特-图生图洗图-Z-image（单张工作流）_2044953447383961602.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Float`
- `HAIGC_LoadImagesFromZip`
- `ImageConcatMulti`
- `ImageResizeAdvanced`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Qwen3_VQA`
- `RepeatLatentBatch`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `ModelPatchLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `ZImageFunControlnet` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1216 | - | 2 | 100% |
| 高度 | 2160 | - | 2 | 100% |
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 0.7 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.2 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1216，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 2160，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 0.7，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
