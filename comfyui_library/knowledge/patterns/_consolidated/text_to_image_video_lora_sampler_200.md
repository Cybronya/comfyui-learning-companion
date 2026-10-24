---
name: text_to_image_video_lora_sampler_200
type: Text To Image
frequency: 2
level: weak
coverage: 0.943
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, FastFilmGrain, KSampler, LoraLoader, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAELoader, WanVideoNAG, easy cleanGpuUsed, easy clearCacheAll]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Wan2.2 低噪模型 文生图_1962185965135663106.json, 图片生成/文生图/wan2.1文生图，速度质量类似于Flux_1942865764128854017.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_200

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Wan2.2 低噪模型 文生图_1962185965135663106.json、图片生成/文生图/wan2.1文生图，速度质量类似于Flux_1942865764128854017.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `FastFilmGrain`
- `KSampler`
- `LoraLoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanVideoNAG`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `CR Upscale Image` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `EmptyHunyuanLatentVideo` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `Text Multiline` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 1412 | - | 2 | 64% |
| 高度 | 1344 | - | 2 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1412，样本不足，未给区间，2 个样本
- 高度 中位数 1344，样本不足，未给区间，2 个样本，取值集中（一致性 81%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
