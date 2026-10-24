---
name: unknown_workflow_sampler_clip_unet_105
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9247
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/产品换背景批量出图_2098992386100785154.json, 图片生成/图生图/人物真实换脸 光影一致_2081923793060188162.json, 图片生成/图生图/图片一键换背景_2082397422550077441.json, 图片生成/图生图/女生发型测试1.0_2025882097881194498.json, 图片生成/图生图/换脸_real-Flux2+Klein+工作流_2090347115141746689.json, 图片生成/图生图/换脸_real-Flux2+Klein+工作流_2091704075195871233.json, 图片生成/图生图/换脸_real-Flux2+Klein+工作流_2091835881744330753.json, 图片生成/图生图/换脸_real-Flux2+Klein+工作流_2092522636768272386.json, 图片生成/图生图/换脸_real-Flux2+Klein+工作流_2100488808281235458.json, 图片生成/图生图/男生发型测试1.0_2028692677126000641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_105

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/产品换背景批量出图_2098992386100785154.json、图片生成/图生图/人物真实换脸 光影一致_2081923793060188162.json、图片生成/图生图/图片一键换背景_2082397422550077441.json、图片生成/图生图/女生发型测试1.0_2025882097881194498.json、图片生成/图生图/换脸_real-Flux2+Klein+工作流_2090347115141746689.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageReel` —— 9/10 个有
- `LayerUtility: ImageReelComposit` —— 9/10 个有
- `ConditioningZeroOut` —— 8/10 个有
- `Image Comparer (rgthree)` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/10 个有
- `SegmentV2` —— 6/10 个有
- `easy imageColorMatch` —— 6/10 个有
- `ShowText|pysssss` —— 3/10 个有
- `easy promptLine` —— 3/10 个有
- `CR Text Concatenate` —— 2/10 个有
- `INTConstant` —— 2/10 个有
- `ImageConcatFromBatch` —— 2/10 个有
- `ImageListToBatch+` —— 2/10 个有
- `ImageScaleToTotalPixels` —— 2/10 个有
- `LoraLoaderModelOnly` —— 2/10 个有
- `Text` —— 2/10 个有
- `CR Latent Batch Size` —— 1/10 个有
- `CR Prompt Text` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
