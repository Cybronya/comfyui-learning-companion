---
name: unknown_workflow_video_sampler_clip_43
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.940273
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/2037082773323780097.json, 视频生成/图生视频/1996401587960561665.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1949877835465932801.json, 视频生成/图生视频/1950344638181892097.json, 视频生成/图生视频/1954509798727413761.json, 视频生成/图生视频/1993525014328705026.json, 视频生成/图生视频/1950026797163438082.json, 视频生成/图生视频/2027632357276131329.json, 视频生成/图生视频/1952642819863318529.json, 视频生成/图生视频/1982023168992919554.json, 视频生成/图生视频/1953391288357978113.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_43

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2037082773323780097.json、视频生成/图生视频/1996401587960561665.json、视频生成/图生视频/Wan2.2 14B+LightX2V 90秒81帧6步超极速图生视频V1_1949877835465932801.json、视频生成/图生视频/1950344638181892097.json、视频生成/图生视频/1954509798727413761.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 10/11 个有
- `PathchSageAttentionKJ` —— 10/11 个有
- `UNETLoader` —— 10/11 个有
- `LayerUtility: PurgeVRAM` —— 8/11 个有
- `JWInteger` —— 7/11 个有
- `MathExpression|pysssss` —— 2/11 个有
- `SaveImage` —— 2/11 个有
- `ConditioningZeroOut` —— 1/11 个有
- `LoadImagesFromURL` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `Primitive integer [Crystools]` —— 1/11 个有
- `UnetLoaderGGUF` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 91% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 11 | 91% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | lcm | - | 11 | 82% |
| 重绘幅度 | simple | - | 11 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 91%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，11 个样本，取值集中（一致性 91%）
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，11 个样本，一致性 82%
- 重绘幅度 最常用 simple，11 个样本，一致性 91%
