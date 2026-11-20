---
name: unknown_workflow_sampler_clip_unet_274
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.843
common_nodes: [BasicGuider, CLIPTextEncode, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, SeedVR2BlockSwap, SeedVR2ExtraArgs, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX2 文生图+SeedVR2放大_1993640194488336386.json, 图片生成/文生图/FlUX-SRPO文生图_1966834208146591745.json, 图片生成/文生图/Flux SRPO二阶段真实感文生图V2_1966200090299895810.json, 图片生成/文生图/flux文生图（厨房风格模型 含例子示例整理）20260114_2011004615533268994.json, 图片生成/文生图/文生图（厨房风格模型）_2000758286930542594.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_274

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/FLUX2 文生图+SeedVR2放大_1993640194488336386.json、图片生成/文生图/FlUX-SRPO文生图_1966834208146591745.json、图片生成/文生图/Flux SRPO二阶段真实感文生图V2_1966200090299895810.json、图片生成/文生图/flux文生图（厨房风格模型 含例子示例整理）20260114_2011004615533268994.json、图片生成/文生图/文生图（厨房风格模型）_2000758286930542594.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `CLIPTextEncode`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 4/5 个有
- `DualCLIPLoader` —— 4/5 个有
- `EmptySD3LatentImage` —— 4/5 个有
- `ModelSamplingFlux` —— 4/5 个有
- `SeedVR2` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `PreviewImage` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `LoraLoaderModelOnly` —— 2/5 个有
- `CLIPLoader` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `EmptyFlux2LatentImage` —— 1/5 个有
- `Flux2Scheduler` —— 1/5 个有
- `GGUFLoaderKJ` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `SeedVR2GGUF` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
