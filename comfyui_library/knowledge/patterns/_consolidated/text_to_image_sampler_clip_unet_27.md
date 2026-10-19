---
name: text_to_image_sampler_clip_unet_27
type: Text To Image
frequency: 2
level: weak
coverage: 0.831
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [easy cleanGpuUsed, SDXL Resolutions (JPS)]
members: [图片生成/文生图/1960231389213962242.json, 视频生成/文生视频/Boogu-Image Base 文生图工作流_2067856528262127617.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_27

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1960231389213962242.json、视频生成/文生视频/Boogu-Image Base 文生图工作流_2067856528262127617.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 1/2 个有
- `ModelSamplingSD3` —— 1/2 个有
- `SDXL Resolutions (JPS)` —— 1/2 个有
- `SeargePromptCombiner` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1024 | - | 2 | 100% |
| 采样步数 | 27.5 | - | 2 | 73% |
| Prompt 约束强度(CFG) | 3.5 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.6 | - | 2 | 33% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 27.5，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值分散，一致性仅 33%
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed、SDXL Resolutions (JPS)
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
