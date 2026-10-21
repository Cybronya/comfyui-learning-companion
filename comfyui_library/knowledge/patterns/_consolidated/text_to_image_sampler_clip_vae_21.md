---
name: text_to_image_sampler_clip_vae_21
type: Text To Image
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [数字人/数字人/分镜图生成_2093149514755559425.json, 视频生成/文生视频/文生图 Qwen2512  领军模型 完美中文_2021581695731900418.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_21

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/分镜图生成_2093149514755559425.json、视频生成/文生视频/文生图 Qwen2512  领军模型 完美中文_2021581695731900418.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EnhancedLoadDiffusionModel` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 912 | - | 2 | 88% |
| 高度 | 1368 | - | 2 | 88% |
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 912，样本不足，未给区间，2 个样本，取值集中（一致性 88%）
- 高度 中位数 1368，样本不足，未给区间，2 个样本，取值集中（一致性 88%）
- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
