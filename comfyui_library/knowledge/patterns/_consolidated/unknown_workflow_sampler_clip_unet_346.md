---
name: unknown_workflow_sampler_clip_unet_346
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.839667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/test-faceswap_2067439662989402114.json, 图片生成/图生图/【去文字】flux-2-klein-9b_2104893740522491906.json, 数字人/数字人/短剧资产_Klein_true_V3人物资产制作(角色定版三视图）V2_2086611011628519426.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_346

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/test-faceswap_2067439662989402114.json、图片生成/图生图/【去文字】flux-2-klein-9b_2104893740522491906.json、数字人/数字人/短剧资产_Klein_true_V3人物资产制作(角色定版三视图）V2_2086611011628519426.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AutoCropFaces` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `DifferentialDiffusion` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `InpaintModelConditioning` —— 1/3 个有
- `JWString` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `Load RetinaFace` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `SegmentV2` —— 1/3 个有
- `json_to_bbox` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
