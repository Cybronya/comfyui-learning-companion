---
name: unknown_workflow_video_sampler_clip_135
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.87425
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, KSamplerSelect, LTXVBaseSampler, LTXVConditioning, LoadImage, RandomNoise, STGAdvancedPresets, STGGuiderAdvanced, Set VAE Decoder Noise, VAEDecode, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1924687535736279042.json, 视频生成/图生视频/1922227928325636097.json, 视频生成/图生视频/1921582892873613313.json, 视频生成/图生视频/1921747683382345729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_135

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1924687535736279042.json、视频生成/图生视频/1922227928325636097.json、视频生成/图生视频/1921582892873613313.json、视频生成/图生视频/1921747683382345729.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSamplerSelect`
- `LTXVBaseSampler`
- `LTXVConditioning`
- `LoadImage`
- `RandomNoise`
- `STGAdvancedPresets`
- `STGGuiderAdvanced`
- `Set VAE Decoder Noise`
- `VAEDecode`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 3/4 个有
- `ImageResizeKJ` —— 2/4 个有
- `Int` —— 2/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `LayerUtility: ImageAutoCrop V3` —— 1/4 个有
- `PrimitiveString` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy imageConcat` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
