---
name: unknown_workflow_video_sampler_clip_96
type: Unknown Workflow
frequency: 7
level: weak
coverage: 0.906143
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2  图生视频_2018573357712674817.json, 视频生成/图生视频/Wan2.2  极速图生视频_2068892657300099074.json, 视频生成/图生视频/Wan2.2 14+图生视频_1949911395070599170.json, 视频生成/图生视频/Wan2.2 14B 6步超极速图生视频_1949992607571206146.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1 浮云_1996104036933910529.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1949877835465932801.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1950344638181892097.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_96

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Wan2.2  图生视频_2018573357712674817.json、视频生成/图生视频/Wan2.2  极速图生视频_2068892657300099074.json、视频生成/图生视频/Wan2.2 14+图生视频_1949911395070599170.json、视频生成/图生视频/Wan2.2 14B 6步超极速图生视频_1949992607571206146.json、视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1 浮云_1996104036933910529.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `Int` —— 2/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `ColorMatch` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `LoadImagesFromURL` —— 1/7 个有
- `PMRF` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `Primitive integer [Crystools]` —— 1/7 个有
- `TeaCache` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 86% |
| Prompt 约束强度(CFG) | 6 | 6 - 20 | 7 | 39% |
| 采样算法 | 1 | 1 - 3.5 | 7 | 36% |
| 调度器 | lcm | - | 7 | 86% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 20，7 个样本，取值分散，一致性仅 39%
- 采样算法 中位数 1，观测区间 1 - 3.5，7 个样本，取值分散，一致性仅 36%
- 调度器 最常用 lcm，7 个样本，一致性 86%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
