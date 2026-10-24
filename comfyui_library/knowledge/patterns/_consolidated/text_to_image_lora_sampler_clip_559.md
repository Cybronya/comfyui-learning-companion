---
name: text_to_image_lora_sampler_clip_559
type: Text To Image
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLatentImage, ImpactSwitch, Int, KSampler, LoraLoader, ModelSamplingFlux, RH_Translator, SaveImagePlus, TextCombinerSix, TextCombinerTwo, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux与Krea2图生图工作流｜图片风格化高质量生成_2097506146767687682.json, 图片生成/文生图/Flux-Krea2文生图_2097219806482227201.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_559

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux与Krea2图生图工作流｜图片风格化高质量生成_2097506146767687682.json、图片生成/文生图/Flux-Krea2文生图_2097219806482227201.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `LoraLoader`
- `ModelSamplingFlux`
- `RH_Translator`
- `SaveImagePlus`
- `TextCombinerSix`
- `TextCombinerTwo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `RepeatLatentBatch` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `solarL_SaveImagesToZip` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0 | - | 2 | 100% |
| LoRA 文本强度 | 0 | - | 2 | 100% |
| 采样步数 | 12 | - | 2 | 33% |
| Prompt 约束强度(CFG) | 2.75 | - | 2 | 36% |
| 采样算法 | er_sde | - | 2 | 50% |
| 调度器 | beta | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 296 | - | 2 | 27% |
| 高度 | 296 | - | 2 | 27% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 0，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 12，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 2.75，样本不足，未给区间，2 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 er_sde，2 个样本，一致性 50%
- 调度器 最常用 beta，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 296，样本不足，未给区间，2 个样本，取值分散，一致性仅 27%
- 高度 中位数 296，样本不足，未给区间，2 个样本，取值分散，一致性仅 27%
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
