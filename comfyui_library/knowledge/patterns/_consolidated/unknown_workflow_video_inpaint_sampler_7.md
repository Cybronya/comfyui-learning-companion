---
name: unknown_workflow_video_inpaint_sampler_7
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.945333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, INTConstant, ImageResizeKJ, KSampler, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanFunInpaintToVideo]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/03-04-03-WAN2.1-首帧生成视频-FUN-INP-1.3B-原生_1989234488586670081.json, 平台全量/03-04-04-WAN2.1-首尾帧生成视频-FUN-INP-14B-原生_1989234532287123458.json, 视频生成/图生视频/2025-04-15 wan1.3b inp img2img_1911833521852481537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_sampler_7

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/03-04-03-WAN2.1-首帧生成视频-FUN-INP-1.3B-原生_1989234488586670081.json、平台全量/03-04-04-WAN2.1-首尾帧生成视频-FUN-INP-14B-原生_1989234532287123458.json、视频生成/图生视频/2025-04-15 wan1.3b inp img2img_1911833521852481537.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `INTConstant`
- `ImageResizeKJ`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFunInpaintToVideo`

**可变部分**（部分 workflow 才有）：
- `ImpactMakeImageBatch` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `CFGZeroStarAndInit` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `WanVideoTeaCacheKJ` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
