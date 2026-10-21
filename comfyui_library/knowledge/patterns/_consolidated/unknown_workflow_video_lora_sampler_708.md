---
name: unknown_workflow_video_lora_sampler_708
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, FastFilmGrain, KSampler, Label (rgthree), LoraLoader, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, VAEDecode, VAELoader, WanVideoNAG, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: [Label (rgthree), easy cleanGpuUsed, easy clearCacheAll, Text Multiline]
members: [图片生成/文生图/1942908235353374722.json, 图片生成/文生图/1945020657232175106.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_708

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1942908235353374722.json、图片生成/文生图/1945020657232175106.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `FastFilmGrain`
- `KSampler`
- `Label (rgthree)`
- `LoraLoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `WanVideoNAG`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `Text Multiline` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、easy cleanGpuUsed、easy clearCacheAll、Text Multiline
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
