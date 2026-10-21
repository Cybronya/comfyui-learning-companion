---
name: unknown_workflow_video_sampler_clip_9
type: Unknown Workflow
frequency: 25
level: strong
coverage: 0.99716
common_nodes: [CLIPLoader, CLIPTextEncode, INTConstant, ImageResizeKJv2, KSamplerAdvanced, LoadImage, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2007957873501937666.json, 视频生成/图生视频/2069319914443333634.json, 视频生成/图生视频/2043159910917087233.json, 视频生成/图生视频/2007811222472761345.json, 视频生成/图生视频/2011657248396808193.json, 视频生成/图生视频/2033890243190984706.json, 视频生成/图生视频/2021154094072733697.json, 视频生成/图生视频/2041753432205299714.json, 视频生成/图生视频/2008199309795266561.json, 视频生成/图生视频/2077269465192034306.json, 视频生成/图生视频/2077636142706552833.json, 视频生成/图生视频/2077677260378828801.json, 视频生成/图生视频/2078823475380318209.json, 视频生成/图生视频/2079016267759050753.json, 视频生成/图生视频/2071625785936539650.json, 视频生成/图生视频/2072403909544603649.json, 视频生成/图生视频/2074567411587702786.json, 视频生成/图生视频/2074915494896955394.json, 视频生成/图生视频/2075491112214679554.json, 视频生成/图生视频/2075510355111006210.json, 视频生成/图生视频/2075613549606563841.json, 视频生成/图生视频/2075960869892214786.json, 视频生成/图生视频/2076181570117005314.json, 视频生成/图生视频/2020867158913323009.json, 视频生成/图生视频/2046411920428769281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（视频生成/图生视频/2007957873501937666.json、视频生成/图生视频/2069319914443333634.json、视频生成/图生视频/2043159910917087233.json、视频生成/图生视频/2007811222472761345.json、视频生成/图生视频/2011657248396808193.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 25 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingSD3` —— 24/25 个有
- `WanFirstMiddleLastFrameToVideo` —— 24/25 个有
- `ModelPatchTorchSettings` —— 22/25 个有
- `LoraLoaderModelOnly` —— 21/25 个有
- `YC Color Match` —— 4/25 个有
- `ImageScaleBy` —— 2/25 个有
- `RIFE VFI` —— 2/25 个有
- `easy cleanGpuUsed` —— 2/25 个有
- `BerniniConditioning` —— 1/25 个有
- `ComfyMathExpression` —— 1/25 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/25 个有
- `VHS_LoadVideo` —— 1/25 个有
- `VHS_VideoInfoLoaded` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 25 | 96% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 25 | 100% |
| 采样算法 | 1 | 1 - 1 | 25 | 100% |
| 调度器 | euler | - | 25 | 96% |
| 重绘幅度 | beta | - | 25 | 84% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，25 个样本，一致性 96%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，25 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，25 个样本，一致性 96%
- 重绘幅度 最常用 beta，25 个样本，一致性 84%
