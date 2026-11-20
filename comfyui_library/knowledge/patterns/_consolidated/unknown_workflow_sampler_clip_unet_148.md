---
name: unknown_workflow_sampler_clip_unet_148
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.893875
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux2 Klein 9B图像编辑-双图_2012172748742725633.json, 图片生成/图生图/Flux2-Klein 单图编辑版_2015381602594983938.json, 图片生成/图生图/Flux2-Klein 多图编辑版_2015361031995924482.json, 图片生成/图生图/Flux2-Klein+一键扩图_2013231626309869570.json, 图片生成/图生图/Flux2-klein 【扩图&局部重绘】_2013840320462594049.json, 图片生成/图生图/Flux2-klein 扩图&局部重绘_2013122024448729089.json, 图片生成/图生图/Flux2-klein-9b单图编辑_2012455808189079554.json, 图片生成/图生图/klein_9b单图编辑_2013477082466095105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_148

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 9B图像编辑-双图_2012172748742725633.json、图片生成/图生图/Flux2-Klein 单图编辑版_2015381602594983938.json、图片生成/图生图/Flux2-Klein 多图编辑版_2015361031995924482.json、图片生成/图生图/Flux2-Klein+一键扩图_2013231626309869570.json、图片生成/图生图/Flux2-klein 【扩图&局部重绘】_2013840320462594049.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
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
- `ImageConcanate` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 6/8 个有
- `ColorMatch` —— 5/8 个有
- `ConditioningZeroOut` —— 5/8 个有
- `LayerUtility: ImageReel` —— 5/8 个有
- `LayerUtility: ImageReelComposit` —— 5/8 个有
- `FluxResolutionNode` —— 3/8 个有
- `ImagePadForOutpaint` —— 3/8 个有
- `ImpactSwitch` —— 3/8 个有
- `LayerUtility: PurgeVRAM V2` —— 3/8 个有
- `PrimitiveInt` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `easy cleanGpuUsed` —— 3/8 个有
- `DrawMaskOnImage` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `RH_LLMAPI_NODE` —— 2/8 个有
- `ShowText|pysssss` —— 2/8 个有
- `easy seed` —— 2/8 个有
- `MaskColorize` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
