---
name: text_to_image_lora_sampler_clip_381
type: Text To Image
frequency: 2
level: weak
coverage: 0.883
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: []
missing: []
members: [图片生成/文生图/Z-Image四种文生图（原版、真实幻想、BEYOND REALITY、红潮）_2019536292714909697.json, 图片生成/文生图/Z-Image四种模型文生图对比（原版、真实幻想、BEYOND REALITY、红潮）_2003305225530245121.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_381

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-Image四种文生图（原版、真实幻想、BEYOND REALITY、红潮）_2019536292714909697.json、图片生成/文生图/Z-Image四种模型文生图对比（原版、真实幻想、BEYOND REALITY、红潮）_2003305225530245121.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `easy promptLine` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
