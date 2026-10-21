---
name: unknown_workflow_video_lora_sampler_534
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.875
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR String To Combo, ImageResizeKJ, ImpactInt, ImpactStringSelector, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, RH_Captioner, RH_LLMAPI_NODE, SimpleMath+, SplitStringByDelimiter, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1964309918603988994.json, 视频生成/图生视频/2018166622560718849.json, 视频生成/图生视频/1940692152370311170.json, 视频生成/文生视频/1931150479697620994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_534

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1964309918603988994.json、视频生成/图生视频/2018166622560718849.json、视频生成/图生视频/1940692152370311170.json、视频生成/文生视频/1931150479697620994.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR String To Combo`
- `ImageResizeKJ`
- `ImpactInt`
- `ImpactStringSelector`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `RH_Captioner`
- `RH_LLMAPI_NODE`
- `SimpleMath+`
- `SplitStringByDelimiter`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `JoinStringMulti` —— 2/4 个有
- `JoinStrings` —— 2/4 个有
- `LayerUtility: PurgeVRAM V2` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `Note Plus (mtb)` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | 8 - 20 | 4 | 57% |
| Prompt 约束强度(CFG) | 3.5 | 1 - 6 | 4 | 29% |
| 采样算法 | uni_pc | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，观测区间 8 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 3.5，观测区间 1 - 6，4 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 uni_pc，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
