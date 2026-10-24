---
name: unknown_workflow_video_sampler_clip_195
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.870667
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, EmptyHunyuanLatentVideo, ImageResizeKJ, Int, KSampler, LoadImage, ModelSamplingSD3, SkipLayerGuidanceWanVideo, UNETLoader, VAEDecodeTiled, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanFunControlToVideo, WanVideoTeaCacheKJ]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/wan2.1_fun图生视频(动作迁移)超稳定版_1912025643897552898.json, 视频生成/图生视频/wan2.1_fun图生视频(动作迁移)超稳定版_2046063628947820545.json, 视频生成/图生视频/wan2.1_fun图生视频转绘_1918621087226335233.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_195

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/wan2.1_fun图生视频(动作迁移)超稳定版_1912025643897552898.json、视频生成/图生视频/wan2.1_fun图生视频(动作迁移)超稳定版_2046063628947820545.json、视频生成/图生视频/wan2.1_fun图生视频转绘_1918621087226335233.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `EmptyHunyuanLatentVideo`
- `ImageResizeKJ`
- `Int`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `SkipLayerGuidanceWanVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanFunControlToVideo`
- `WanVideoTeaCacheKJ`

**可变部分**（部分 workflow 才有）：
- `CR Upscale Image` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `RHHiddenNodes` —— 2/3 个有
- `RIFE VFI` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
