---
name: unknown_workflow_video_sampler_clip_99
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.955333
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2055627357901336578.json, 视频生成/图生视频/2050537311854710785.json, 视频生成/图生视频/2023300078865223682.json, 视频生成/图生视频/1949968677410136066.json, 视频生成/图生视频/1952579457632669698.json, 视频生成/图生视频/1952589946924273666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_99

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2055627357901336578.json、视频生成/图生视频/2050537311854710785.json、视频生成/图生视频/2023300078865223682.json、视频生成/图生视频/1949968677410136066.json、视频生成/图生视频/1952579457632669698.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `JWInteger` —— 3/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/6 个有
- `LayerUtility: PurgeVRAM` —— 3/6 个有
- `LoadLatent` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `MemoryCleaner` —— 1/6 个有
- `Power Lora Loader (rgthree)` —— 1/6 个有
- `RIFE VFI` —— 1/6 个有
- `SaveLatent` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 83% |
| Prompt 约束强度(CFG) | 6 | 4 - 8 | 6 | 78% |
| 采样算法 | 1 | 1 - 1.1 | 6 | 96% |
| 调度器 | euler | - | 6 | 67% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 6，观测区间 4 - 8，6 个样本
- 采样算法 中位数 1，观测区间 1 - 1.1，6 个样本，取值集中（一致性 96%）
- 调度器 最常用 euler，6 个样本，一致性 67%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
