---
name: unknown_workflow_video_sampler_clip_119
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9108
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, UnetLoaderGGUF, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1911197940504035330.json, 视频生成/图生视频/1895515644396240897.json, 视频生成/图生视频/1895517453516996610.json, 视频生成/图生视频/1895423724621529089.json, 视频生成/图生视频/1895732639271878658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_119

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1911197940504035330.json、视频生成/图生视频/1895515644396240897.json、视频生成/图生视频/1895517453516996610.json、视频生成/图生视频/1895423724621529089.json、视频生成/图生视频/1895732639271878658.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 3/5 个有
- `ApplySageAttention` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `ModelSamplingSD3` —— 1/5 个有
- `Note _O` —— 1/5 个有
- `TeaCache` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 30 | 5 | 50% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 5 | 100% |
| 采样算法 | uni_pc | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 0.3 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
