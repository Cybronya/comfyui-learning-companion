---
name: unknown_workflow_sampler_clip_unet_68
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.910833
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/F2K-9B一键换头、换脸_2019369641709150209.json, 图片生成/图生图/FLUX2 Klein 双图编辑_2014610246840360961.json, 图片生成/图生图/FLUX新王炸 Klein 双图编辑版_2012806080375562241.json, 图片生成/图生图/FLUX新王炸 Klein 图像编辑版 急速10秒出图_2048574540699148289.json, 图片生成/图生图/FLUX新王炸 Klein 图像编辑版 急速10秒出图_2048599240196235266.json, 图片生成/图生图/FLUX新王炸 Klein 图像编辑版_2016046164730187778.json, 图片生成/图生图/Flux 2 klein 9b 换头工作流_2013818759424778241.json, 图片生成/图生图/Flux 2 klein 9b 换头工作流_2015981757341900802.json, 图片生成/图生图/Flux2 Klein 9B图像编辑-双图_2012172748742725633.json, 图片生成/图生图/Flux2-klein-9b单图编辑_2012455808189079554.json, 图片生成/图生图/klein_9b单图编辑_2013477082466095105.json, 图片生成/图生图/啊癫 Flux2 Klein 多图编辑_2014340581073362945.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_68

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/F2K-9B一键换头、换脸_2019369641709150209.json、图片生成/图生图/FLUX2 Klein 双图编辑_2014610246840360961.json、图片生成/图生图/FLUX新王炸 Klein 双图编辑版_2012806080375562241.json、图片生成/图生图/FLUX新王炸 Klein 图像编辑版 急速10秒出图_2048574540699148289.json、图片生成/图生图/FLUX新王炸 Klein 图像编辑版 急速10秒出图_2048599240196235266.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 12 个 workflow 都包含：
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
- `ImageScaleToTotalPixels` —— 10/12 个有
- `ConditioningZeroOut` —— 9/12 个有
- `LayerUtility: ImageReel` —— 9/12 个有
- `LayerUtility: ImageReelComposit` —— 9/12 个有
- `PreviewImage` —— 9/12 个有
- `CR Text` —— 6/12 个有
- `ImageConcanate` —— 6/12 个有
- `Image Comparer (rgthree)` —— 5/12 个有
- `FluxResolutionNode` —— 4/12 个有
- `ImpactSwitch` —— 4/12 个有
- `easy cleanGpuUsed` —— 4/12 个有
- `LayerUtility: PurgeVRAM V2` —— 3/12 个有
- `PrimitiveInt` —— 3/12 个有
- `PrimitiveStringMultiline` —— 3/12 个有
- `RH_LLMAPI_NODE` —— 3/12 个有
- `ShowText|pysssss` —— 2/12 个有
- `Anything Everywhere3` —— 1/12 个有
- `EmptyLatentImage` —— 1/12 个有
- `ImageAndMaskPreview` —— 1/12 个有
- `ImpactInt` —— 1/12 个有
- `KOOK_ImageCompression` —— 1/12 个有
- `LayerMask: HumanPartsUltra` —— 1/12 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/12 个有
- `LayerUtility: PurgeVRAM` —— 1/12 个有
- `Text Multiline` —— 1/12 个有
- `easy imageScaleDownToSize` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
