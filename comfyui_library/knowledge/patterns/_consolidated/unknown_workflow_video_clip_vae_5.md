---
name: unknown_workflow_video_clip_vae_5
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.914
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, FastFilmGrain, ModelSamplingSD3, SaveImage, VAEDecode, VAELoader, WanVideoNAG, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [图片生成/文生图/AniWan文生图_1945020657232175106.json, 图片生成/文生图/Wan2.2文生图(低噪版)_1951900115835498497.json, 图片生成/文生图/Wan2.2文生图(高低噪)_1951482093362688001.json, 图片生成/文生图/Wan_2.1_文生图_1942908235353374722.json, 图片生成/文生图/wan2.1真实感最强文生图_1899402301214248961.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_vae_5

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/AniWan文生图_1945020657232175106.json、图片生成/文生图/Wan2.2文生图(低噪版)_1951900115835498497.json、图片生成/文生图/Wan2.2文生图(高低噪)_1951482093362688001.json、图片生成/文生图/Wan_2.1_文生图_1942908235353374722.json、图片生成/文生图/wan2.1真实感最强文生图_1899402301214248961.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `FastFilmGrain`
- `ModelSamplingSD3`
- `SaveImage`
- `VAEDecode`
- `VAELoader`
- `WanVideoNAG`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `Label (rgthree)` —— 2/5 个有
- `LoraLoader` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `KSamplerAdvanced` —— 1/5 个有
- `ModelPatchTorchSettings` —— 1/5 个有
- `Text Multiline` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 10 | 5 | 0% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 10，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
