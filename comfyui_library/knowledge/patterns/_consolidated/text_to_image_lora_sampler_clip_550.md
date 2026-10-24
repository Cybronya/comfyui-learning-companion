---
name: text_to_image_lora_sampler_clip_550
type: Text To Image
frequency: 2
level: weak
coverage: 0.919
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAEEncode, VAELoader, easy int]
problems: [CFG值较高可能导致Prompt约束过强]
missing: []
members: [图片生成/图生图/6g显存可用动漫二次元anima优化版_2055881040941600769.json, 图片生成/文生图/超强动漫模型ANIMA正式版-全自动版本_仅鸭子图输出版_插件控制版_断开92到11_2058571952813592578.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_550

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/6g显存可用动漫二次元anima优化版_2055881040941600769.json、图片生成/文生图/超强动漫模型ANIMA正式版-全自动版本_仅鸭子图输出版_插件控制版_断开92到11_2058571952813592578.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `DuckHideNode` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImageStitch` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RegexReplace` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `easy imageColorMatch` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | - | 2 | 86% |
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 89% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1920 | - | 2 | 100% |
| 高度 | 1128 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| CFG值较高可能导致Prompt约束过强 | 3/2 | medium | CFG值较高，可能导致Prompt约束过强 → 建议尝试CFG 7-10 |

## 建议与风险

- 采样步数 中位数 35，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1128，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：CFG值较高可能导致Prompt约束过强
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
