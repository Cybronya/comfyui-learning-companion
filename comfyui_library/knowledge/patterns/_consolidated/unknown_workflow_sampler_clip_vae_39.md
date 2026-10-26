---
name: unknown_workflow_sampler_clip_vae_39
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.977667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/61zhenshiwenshentu_2052418692000034817.json, 图片生成/文生图/09.Wan2.2文生图_1993297565200351233.json, 图片生成/文生图/WAN2.1文生图_1946266988476030978.json, 图片生成/文生图/Wan2.1文生图+真实感=艾橘溪_1944626515541676033.json, 图片生成/文生图/Wan2.2 文生图_1951184476380536834.json, 图片生成/文生图/wan2.2快速低燥文生图_2032451540241354753.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_39

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/61zhenshiwenshentu_2052418692000034817.json、图片生成/文生图/09.Wan2.2文生图_1993297565200351233.json、图片生成/文生图/WAN2.1文生图_1946266988476030978.json、图片生成/文生图/Wan2.1文生图+真实感=艾橘溪_1944626515541676033.json、图片生成/文生图/Wan2.2 文生图_1951184476380536834.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `Int` —— 3/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `Float` —— 1/6 个有
- `LoraLoader` —— 1/6 个有
- `PathchSageAttentionKJ` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 8 - 20 | 6 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 6 | 36% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 0.3 - 1 | 6 | 64% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，6 个样本
