---
name: unknown_workflow_sampler_clip_unet_77
type: Unknown Workflow
frequency: 4
level: weak
coverage: 0.911
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, KSamplerAdvanced, LoadImage, ModelSamplingSD3, SaveVideo, UNETLoader, VAEDecode, VAELoader, WanFirstLastFrameToVideo]
problems: []
missing: []
members: [视频生成/图生视频/1951969161985642497.json, 视频生成/图生视频/1961016346521878529.json, 视频生成/图生视频/1962156046351536130.json, 视频生成/图生视频/2029048647224139778.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_77

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1951969161985642497.json、视频生成/图生视频/1961016346521878529.json、视频生成/图生视频/1962156046351536130.json、视频生成/图生视频/2029048647224139778.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanFirstLastFrameToVideo`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 3/4 个有
- `CLIPVisionLoader` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `Int` —— 2/4 个有
- `LayerUtility: ImageMaskScaleAs` —— 2/4 个有
- `CM_IntToFloat` —— 1/4 个有
- `CR Text` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 50% |
| Prompt 约束强度(CFG) | 20 | 4 - 20 | 4 | 57% |
| 采样算法 | 4 | 1 - 4 | 4 | 60% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 20，观测区间 4 - 20，4 个样本
- 采样算法 中位数 4，观测区间 1 - 4，4 个样本
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
