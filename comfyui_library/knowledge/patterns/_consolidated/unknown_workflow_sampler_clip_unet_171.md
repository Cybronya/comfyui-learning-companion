---
name: unknown_workflow_sampler_clip_unet_171
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.92025
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1971438384981983234.json, 视频生成/图生视频/1950499114352103426.json, 视频生成/图生视频/1950096057801859073.json, 视频生成/图生视频/1950206253990592514.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_171

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1971438384981983234.json、视频生成/图生视频/1950499114352103426.json、视频生成/图生视频/1950096057801859073.json、视频生成/图生视频/1950206253990592514.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `SaveAnimatedWEBP` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `SaveWEBM` —— 1/4 个有
- `wanBlockSwap` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 9 | 4 - 20 | 4 | 35% |
| 采样算法 | 2.25 | 1 - 3.5 | 4 | 44% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 9，观测区间 4 - 20，4 个样本，取值分散，一致性仅 35%
- 采样算法 中位数 2.25，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 44%
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
