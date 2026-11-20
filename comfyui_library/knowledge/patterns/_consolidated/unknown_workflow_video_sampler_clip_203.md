---
name: unknown_workflow_video_sampler_clip_203
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.94
common_nodes: [CLIPLoader, CLIPTextEncode, JWInteger, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 14+图生视频_1949911395070599170.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 12步超极速高质量图生视频V1_1949874955704033281.json, 视频生成/图生视频/Wan2.2 14B+LightX2V 6步生视频（无声音）_2056552561905332226.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_203

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 14+图生视频_1949911395070599170.json、视频生成/图生视频/Wan2.2 14B+LightX2V 12步超极速高质量图生视频V1_1949874955704033281.json、视频生成/图生视频/Wan2.2 14B+LightX2V 6步生视频（无声音）_2056552561905332226.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 2/3 个有
- `ColorMatch` —— 1/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `DF_Int_to_Float` —— 1/3 个有
- `Int` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `PMRF` —— 1/3 个有
- `TeaCache` —— 1/3 个有
- `Text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 12 | 6 - 20 | 3 | 55% |
| 采样算法 | 1 | 1 - 3.5 | 3 | 36% |
| 调度器 | lcm | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 12，观测区间 6 - 20，3 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，3 个样本，取值分散，一致性仅 36%
- 调度器 最常用 lcm，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
