---
name: unknown_workflow_video_lora_sampler_246
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.881625
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2035035563962671105.json, 视频生成/图生视频/2067237434458468353.json, 视频生成/图生视频/2026835055515017218.json, 视频生成/图生视频/2056759291427778562.json, 视频生成/图生视频/2017568784646672385.json, 视频生成/图生视频/2050472487972032513.json, 视频生成/图生视频/2067255627071709185.json, 视频生成/图生视频/2066470344814321666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_246

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2035035563962671105.json、视频生成/图生视频/2067237434458468353.json、视频生成/图生视频/2026835055515017218.json、视频生成/图生视频/2056759291427778562.json、视频生成/图生视频/2017568784646672385.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
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
- `ImageResize+` —— 4/8 个有
- `WanFirstLastFrameToVideo` —— 4/8 个有
- `WanImageToVideo` —— 4/8 个有
- `easy showAnything` —— 3/8 个有
- `Int` —— 2/8 个有
- `ImpactImageInfo` —— 1/8 个有
- `UnetLoaderGGUF` —— 1/8 个有
- `VAEDecodeTiled` —— 1/8 个有
- `easy clearCacheAll` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 50% |
| Prompt 约束强度(CFG) | 8 | 6 - 12 | 8 | 74% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 50%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 12，8 个样本
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
