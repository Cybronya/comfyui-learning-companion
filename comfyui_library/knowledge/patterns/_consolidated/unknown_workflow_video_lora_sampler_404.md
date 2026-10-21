---
name: unknown_workflow_video_lora_sampler_404
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8624
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2000837178416656386.json, 视频生成/图生视频/2000842508747800577.json, 视频生成/图生视频/2026846377501790209.json, 视频生成/图生视频/2038172701340213249.json, 视频生成/图生视频/2021954787742326786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_404

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2000837178416656386.json、视频生成/图生视频/2000842508747800577.json、视频生成/图生视频/2026846377501790209.json、视频生成/图生视频/2038172701340213249.json、视频生成/图生视频/2021954787742326786.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `WanFirstLastFrameToVideo` —— 4/5 个有
- `ImageResize+` —— 3/5 个有
- `LayerUtility: PurgeVRAM V2` —— 3/5 个有
- `RH_LLMAPI_NODE` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `ImpactInt` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `WanImageToVideo` —— 1/5 个有
- `WanVideoNAG` —— 1/5 个有
- `easy convertAnything` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 8 | 4 - 10 | 5 | 62% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 8，观测区间 4 - 10，5 个样本
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
