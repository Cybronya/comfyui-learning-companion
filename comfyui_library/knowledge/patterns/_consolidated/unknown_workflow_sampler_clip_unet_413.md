---
name: unknown_workflow_sampler_clip_unet_413
type: Unknown Workflow
frequency: 3
level: weak
coverage: 0.934
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CreateVideo, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader, WanFirstLastFrameToVideo]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2-14B 首尾帧官方最新工作流_1951969161985642497.json, 视频生成/图生视频/wan2.2-14B 首尾帧视频工作流_1961016346521878529.json, 视频生成/图生视频/▶WAN2.2首尾帧生视频_2029048647224139778.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_413

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/wan2.2-14B 首尾帧官方最新工作流_1951969161985642497.json、视频生成/图生视频/wan2.2-14B 首尾帧视频工作流_1961016346521878529.json、视频生成/图生视频/▶WAN2.2首尾帧生视频_2029048647224139778.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CreateVideo`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanFirstLastFrameToVideo`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/3 个有
- `LayerUtility: ImageMaskScaleAs` —— 2/3 个有
- `CM_IntToFloat` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `MathExpression|pysssss` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 20 | 4 - 20 | 3 | 49% |
| 采样算法 | 4 | 1 - 4 | 3 | 53% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 20，观测区间 4 - 20，3 个样本，取值分散，一致性仅 49%
- 采样算法 中位数 4，观测区间 1 - 4，3 个样本
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
