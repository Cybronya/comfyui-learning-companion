---
name: unknown_workflow_video_lora_sampler_475
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.92325
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2035035563962671105.json, 视频生成/图生视频/2017568784646672385.json, 视频生成/图生视频/2050472487972032513.json, 视频生成/图生视频/2066470344814321666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_475

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2035035563962671105.json、视频生成/图生视频/2017568784646672385.json、视频生成/图生视频/2050472487972032513.json、视频生成/图生视频/2066470344814321666.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 3/4 个有
- `WanFirstLastFrameToVideo` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `Int` —— 2/4 个有
- `ImpactImageInfo` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `VAEDecodeTiled` —— 1/4 个有
- `WanImageToVideo` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 4 | 50% |
| Prompt 约束强度(CFG) | 7 | 6 - 12 | 4 | 69% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，4 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 7，观测区间 6 - 12，4 个样本
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
