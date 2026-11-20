---
name: image_to_image_lora_sampler_clip_161
type: Image To Image
frequency: 2
level: weak
coverage: 0.789
common_nodes: [CLIPLoader, CLIPTextEncode, CR Simple Image Compare, FastFilmGrain, GetNode, ImageSharpen, ImpactFloat, JWImageResizeByLongerSide, KSampler, LoadImage, LoraLoader, ModelSamplingSD3, PatchModelPatcherOrder, PathchSageAttentionKJ, RH_Captioner, SaveImage, Seed (rgthree), SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy clearCacheAll, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/图片一键增加真实感_1979357472601313282.json, 图片生成/图生图/🥪【大炮摄影】WAN单帧洗图 图片一键增加真实感🥪_1946392997475807234.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_161

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图片一键增加真实感_1979357472601313282.json、图片生成/图生图/🥪【大炮摄影】WAN单帧洗图 图片一键增加真实感🥪_1946392997475807234.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Simple Image Compare`
- `FastFilmGrain`
- `GetNode`
- `ImageSharpen`
- `ImpactFloat`
- `JWImageResizeByLongerSide`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingSD3`
- `PatchModelPatcherOrder`
- `PathchSageAttentionKJ`
- `RH_Captioner`
- `SaveImage`
- `Seed (rgthree)`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy clearCacheAll`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 0.25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 0.25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
