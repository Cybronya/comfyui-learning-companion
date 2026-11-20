---
name: unknown_workflow_lora_sampler_clip_109
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.949
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/test-faceswap_2067439662989402114.json, 图片生成/图生图/换脸工作流111_2081385261786812418.json, 图片生成/文生图/Bfs Klein人物换脸V1_2019423087078412290.json, 数字人/数字人/Klein换脸2.0_2026196400396046338.json, 数字人/数字人/短剧资产_Klein_true_V3人物资产制作(角色定版三视图）V2_2086611011628519426.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_109

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/test-faceswap_2067439662989402114.json、图片生成/图生图/换脸工作流111_2081385261786812418.json、图片生成/文生图/Bfs Klein人物换脸V1_2019423087078412290.json、数字人/数字人/Klein换脸2.0_2026196400396046338.json、数字人/数字人/短剧资产_Klein_true_V3人物资产制作(角色定版三视图）V2_2086611011628519426.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `AutoCropFaces` —— 3/5 个有
- `DifferentialDiffusion` —— 3/5 个有
- `ImageConcanate` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `FluxKontextImageScale` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `JWString` —— 1/5 个有
- `LayerUtility: ImageReel` —— 1/5 个有
- `LayerUtility: ImageReelComposit` —— 1/5 个有
- `Load RetinaFace` —— 1/5 个有
- `PreviewAny` —— 1/5 个有
- `SegmentV2` —— 1/5 个有
- `json_to_bbox` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
