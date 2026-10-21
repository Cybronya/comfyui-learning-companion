---
name: text_to_image_lora_sampler_clip_275
type: Text To Image
frequency: 4
level: strong
coverage: 0.857
common_nodes: [CLIPLoader, CLIPTextEncode, ComfyMiniMaxH3Director, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/导演台任意数量参考生视频｜MiniMax H3官方版_2095963275925213185.json, 视频生成/文生视频/4步极速版｜Fast H3文生视频快速生成工作流_2095122682907029505.json, 视频生成/文生视频/Fast H3四步极速版｜文生视频快速生成_2095132261908832257.json, 视频生成/文生视频/MiniMax H3全能导演台｜文生图生视频三合一_2092044499680845826.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_275

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/导演台任意数量参考生视频｜MiniMax H3官方版_2095963275925213185.json、视频生成/文生视频/4步极速版｜Fast H3文生视频快速生成工作流_2095122682907029505.json、视频生成/文生视频/Fast H3四步极速版｜文生视频快速生成_2095132261908832257.json、视频生成/文生视频/MiniMax H3全能导演台｜文生图生视频三合一_2092044499680845826.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMiniMaxH3Director`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3DirectorRefine` —— 3/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `LoraLoaderBypassModelOnly` —— 1/4 个有
- `MemoryCleaner` —— 1/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `StringFunction|pysssss` —— 1/4 个有
- `easy positive` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
