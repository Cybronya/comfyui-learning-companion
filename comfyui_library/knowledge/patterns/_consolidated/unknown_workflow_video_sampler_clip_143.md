---
name: unknown_workflow_video_sampler_clip_143
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.92625
common_nodes: [CLIPLoader, CLIPTextEncode, JWInteger, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1949911395070599170.json, 视频生成/图生视频/1949991149945708545.json, 视频生成/图生视频/1996104036933910529.json, 视频生成/图生视频/2009159986848473089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_143

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1949911395070599170.json、视频生成/图生视频/1949991149945708545.json、视频生成/图生视频/1996104036933910529.json、视频生成/图生视频/2009159986848473089.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 3/4 个有
- `ColorMatch` —— 1/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `PMRF` —— 1/4 个有
- `TeaCache` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 75% |
| Prompt 约束强度(CFG) | 6 | 6 - 20 | 4 | 36% |
| 采样算法 | 1 | 1 - 3.5 | 4 | 33% |
| 调度器 | lcm | - | 4 | 75% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 20，4 个样本，取值分散，一致性仅 36%
- 采样算法 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 调度器 最常用 lcm，4 个样本，一致性 75%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
