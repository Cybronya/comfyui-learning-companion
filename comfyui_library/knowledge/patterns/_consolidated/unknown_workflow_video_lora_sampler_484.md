---
name: unknown_workflow_video_lora_sampler_484
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9965
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1982352195704233985.json, 视频生成/图生视频/1982294061598023681.json, 视频生成/图生视频/1988112429857021954.json, 视频生成/图生视频/1987623183782187010.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_484

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1982352195704233985.json、视频生成/图生视频/1982294061598023681.json、视频生成/图生视频/1988112429857021954.json、视频生成/图生视频/1987623183782187010.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
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
- `INTConstant` —— 3/4 个有
- `ImageBatchMulti` —— 3/4 个有
- `WanFirstMiddleLastFrameToVideo` —— 3/4 个有
- `WanMultiFrameRefToVideo` —— 3/4 个有
- `GetImageRangeFromBatch` —— 2/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `ImageSharpen` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `ImpactImageInfo` —— 1/4 个有
- `Int` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `WanFourFrameReferenceUltimate` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 100% |
| Prompt 约束强度(CFG) | 5 | 5 - 5 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 5，观测区间 5 - 5，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
