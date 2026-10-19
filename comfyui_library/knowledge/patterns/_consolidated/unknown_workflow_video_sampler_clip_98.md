---
name: unknown_workflow_video_sampler_clip_98
type: Unknown Workflow
frequency: 6
level: weak
coverage: 0.910833
common_nodes: [CLIPLoader, CLIPTextEncode, JWInteger, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1949911395070599170.json, 视频生成/图生视频/1949991149945708545.json, 视频生成/图生视频/1949874955704033281.json, 视频生成/图生视频/1954509798727413761.json, 视频生成/图生视频/1993525014328705026.json, 视频生成/图生视频/2027632357276131329.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_98

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1949911395070599170.json、视频生成/图生视频/1949991149945708545.json、视频生成/图生视频/1949874955704033281.json、视频生成/图生视频/1954509798727413761.json、视频生成/图生视频/1993525014328705026.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `JWInteger`
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
- `LoraLoaderModelOnly` —— 5/6 个有
- `ColorMatch` —— 1/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `PMRF` —— 1/6 个有
- `TeaCache` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 83% |
| Prompt 约束强度(CFG) | 6 | 6 - 20 | 6 | 44% |
| 采样算法 | 1 | 1 - 3.5 | 6 | 34% |
| 调度器 | lcm | - | 6 | 83% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 83%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 20，6 个样本，取值分散，一致性仅 44%
- 采样算法 中位数 1，观测区间 1 - 3.5，6 个样本，取值分散，一致性仅 34%
- 调度器 最常用 lcm，6 个样本，一致性 83%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
