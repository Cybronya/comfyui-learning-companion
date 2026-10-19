---
name: unknown_workflow_sampler_clip_vae_12
type: Unknown Workflow
frequency: 6
level: strong
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, KSampler, LoadImage, VAELoader, WanImageToVideo]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/1920615619392110593.json, 视频生成/图生视频/1937276822209896450.json, 视频生成/图生视频/1895293426588385281.json, 视频生成/图生视频/1934136795636355074.json, 视频生成/图生视频/1901974657921081346.json, 视频生成/图生视频/1933315168342581250.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_12

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1920615619392110593.json、视频生成/图生视频/1937276822209896450.json、视频生成/图生视频/1895293426588385281.json、视频生成/图生视频/1934136795636355074.json、视频生成/图生视频/1901974657921081346.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `KSampler`
- `LoadImage`
- `VAELoader`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `VAEDecode` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `UNETLoader` —— 4/6 个有
- `ModelSamplingSD3` —— 3/6 个有
- `MagCache` —— 2/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `ImageResizeKJ` —— 1/6 个有
- `Primitive integer [Crystools]` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `SaveLatent` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 6 | 89% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 6 | 100% |
| 采样算法 | uni_pc | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 1/6 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，6 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
