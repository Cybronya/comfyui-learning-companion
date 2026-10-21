---
name: unknown_workflow_video_sampler_clip_142
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.94525
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, UNETLoader, VAELoader, VHS_VideoCombine]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/1894981008754343938.json, 视频生成/图生视频/1894918771771572226.json, 视频生成/图生视频/1899683017957265409.json, 视频生成/图生视频/1898936758191771650.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_142

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1894981008754343938.json、视频生成/图生视频/1894918771771572226.json、视频生成/图生视频/1899683017957265409.json、视频生成/图生视频/1898936758191771650.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 3/4 个有
- `CLIPVisionLoader` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `VAEDecode` —— 3/4 个有
- `WanImageToVideo` —— 3/4 个有
- `CM_IntToFloat` —— 2/4 个有
- `EmptyHunyuanLatentVideo` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `Primitive integer [Crystools]` —— 2/4 个有
- `VAEDecodeTiled` —— 2/4 个有
- `WanVideoTeaCacheKJ` —— 2/4 个有
- `ModelSamplingSD3` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 30 | 4 | 65% |
| Prompt 约束强度(CFG) | 6 | 5.97 - 6 | 4 | 100% |
| 采样算法 | uni_pc | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 1/4 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 30，4 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 5.97 - 6，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
