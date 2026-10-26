---
name: unknown_workflow_sampler_clip_unet_287
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9025
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/3.扩展图片_2050623451928510466.json, 图片生成/图生图/360-全景照片地图编辑查看_2042620819846733826.json, 图片生成/图生图/FLUX2-KLEIN-换头_换脸工作流_2017152699401248770.json, 图片生成/图生图/Flux2 Klein 动漫转写实_2024871399084527618.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_287

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/3.扩展图片_2050623451928510466.json、图片生成/图生图/360-全景照片地图编辑查看_2042620819846733826.json、图片生成/图生图/FLUX2-KLEIN-换头_换脸工作流_2017152699401248770.json、图片生成/图生图/Flux2 Klein 动漫转写实_2024871399084527618.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
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
- `EmptyFlux2LatentImage` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `MuyeTextEditOutput` —— 2/4 个有
- `easy imageConcat` —— 2/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `ConcatTextOfUtils` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImagePadForOutpaint` —— 1/4 个有
- `ResizeImagesByLongerEdge` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `TY360Pasteback` —— 1/4 个有
- `TY360Preview` —— 1/4 个有
- `TY360Roundtrip` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
