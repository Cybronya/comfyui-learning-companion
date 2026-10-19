---
name: unknown_workflow_video_sampler_clip_113
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9326
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, UNETLoader, VAELoader, VHS_VideoCombine]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/1894981008754343938.json, 视频生成/图生视频/1894918771771572226.json, 视频生成/图生视频/1899683017957265409.json, 视频生成/图生视频/1898936758191771650.json, 视频生成/文生视频/1936054594244087809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_113

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1894981008754343938.json、视频生成/图生视频/1894918771771572226.json、视频生成/图生视频/1899683017957265409.json、视频生成/图生视频/1898936758191771650.json、视频生成/文生视频/1936054594244087809.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 4/5 个有
- `CLIPVisionLoader` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `VAEDecode` —— 4/5 个有
- `WanImageToVideo` —— 4/5 个有
- `EmptyHunyuanLatentVideo` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `CM_IntToFloat` —— 2/5 个有
- `ModelSamplingSD3` —— 2/5 个有
- `Primitive integer [Crystools]` —— 2/5 个有
- `VAEDecodeTiled` —— 2/5 个有
- `WanVideoTeaCacheKJ` —— 2/5 个有
- `Text Multiline` —— 1/5 个有
- `UnetLoaderGGUF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 30 | 5 | 58% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 5 | 60% |
| 采样算法 | uni_pc | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 1/5 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，5 个样本
- 采样算法 最常用 uni_pc，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
