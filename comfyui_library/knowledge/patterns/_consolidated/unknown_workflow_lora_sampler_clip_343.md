---
name: unknown_workflow_lora_sampler_clip_343
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8175
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncodeFlux, DualCLIPLoader, Image Comparer (rgthree), KSamplerSelect, LoadImage, LoraLoader, RandomNoise, RepeatLatentBatch, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Upscaler-F.1专属高清放大CN模型_1925152412171235330.json, 平台全量/【ComfyUI_Flux】人物模特质感增强，提升皮肤真实性_1902174656567386114.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_343

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Upscaler-F.1专属高清放大CN模型_1925152412171235330.json、平台全量/【ComfyUI_Flux】人物模特质感增强，提升皮肤真实性_1902174656567386114.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoader`
- `RandomNoise`
- `RepeatLatentBatch`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `Display Any (rgthree)` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `LatentUpscaleBy` —— 1/2 个有
- `Miaoshouai_Tagger` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `StringFunction|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.75 | - | 2 | 93% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.7 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.75，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
