---
name: unknown_workflow_sampler_clip_unet_151
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.82225
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EmptySD3LatentImage, FluxGuidance, KSamplerSelect, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [MathExpression|pysssss, easy clearCacheAll, CR SDXL Aspect Ratio, easy cleanGpuUsed]
members: [图片生成/文生图/1966200090299895810.json, 图片生成/文生图/1966306088582811649.json, 图片生成/文生图/1966775723971293186.json, 图片生成/文生图/1966834208146591745.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_151

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1966200090299895810.json、图片生成/文生图/1966306088582811649.json、图片生成/文生图/1966775723971293186.json、图片生成/文生图/1966834208146591745.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FluxGuidance`
- `KSamplerSelect`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `SeedVR2BlockSwap` —— 3/4 个有
- `SeedVR2ExtraArgs` —— 3/4 个有
- `CR SDXL Aspect Ratio` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `SeedVR2GGUF` —— 2/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `SeedVR2` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：MathExpression|pysssss、easy clearCacheAll、CR SDXL Aspect Ratio、easy cleanGpuUsed
