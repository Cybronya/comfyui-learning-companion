---
name: unknown_workflow_sampler_clip_unet_54
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.783714
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/003.FLUX.2智能综合008.局部重绘-手动遮罩_2035253833063993346.json, 图片生成/图生图/AI扩图_2046771337133297665.json, 图片生成/图生图/F2K-渲染级产品精修V5版｜零偏移｜自动白底｜可选扣图_2074792058958729218.json, 图片生成/图生图/F2K-渲染级产品精修V5版｜零偏移｜自动白底｜可选扣图_2089727296331669505.json, 图片生成/图生图/F2K-渲染级产品精修V5版｜零偏移｜自动白底｜可选扣图_2089727975360126978.json, 图片生成/图生图/F2K亚秒级商业产品白底精修V2.0｜带扣图开关_2089629118886404097.json, 图片生成/图生图/F2K亚秒级商业产品白底精修V2.0｜带扣图开关_2091716631025250306.json, 图片生成/图生图/F2K亚秒级商业产品白底精修V2.0｜带扣图开关_2092058726743240706.json, 图片生成/图生图/F2K亚秒级商业产品白底精修V2.0｜带扣图开关_2092609760863543297.json, 图片生成/图生图/Flux2-Klein亚秒级商业产品白底精修生图带扣图开关_2097139554640814081.json, 图片生成/图生图/Flux2-Klein亚秒级商业产品白底精修生图带扣图开关_2097236497970851841.json, 图片生成/图生图/Flux2-Klein亚秒级商业产品白底精修生图（带扣图开关）_2091113137687846913.json, 图片生成/图生图/Flux2-Klein亚秒级商业产品白底精修生图（带扣图开关）_2091132661388632065.json, 图片生成/图生图/flux2-渲染级产品精修V5版｜零偏移｜自动白底｜可选扣图_2085639645777453057.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_54

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/003.FLUX.2智能综合008.局部重绘-手动遮罩_2035253833063993346.json、图片生成/图生图/AI扩图_2046771337133297665.json、图片生成/图生图/F2K-渲染级产品精修V5版｜零偏移｜自动白底｜可选扣图_2074792058958729218.json、图片生成/图生图/F2K-渲染级产品精修V5版｜零偏移｜自动白底｜可选扣图_2089727296331669505.json、图片生成/图生图/F2K-渲染级产品精修V5版｜零偏移｜自动白底｜可选扣图_2089727975360126978.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 13/14 个有
- `LoraLoaderModelOnly` —— 13/14 个有
- `Fast Groups Bypasser (rgthree)` —— 12/14 个有
- `GetNode` —— 12/14 个有
- `ImpactInt` —— 8/14 个有
- `孤海注释` —— 8/14 个有
- `LayerMask: BiRefNetUltra` —— 7/14 个有
- `PreviewImage` —— 5/14 个有
- `CR Prompt Text` —— 4/14 个有
- `CR Text Input Switch (4 way)` —— 4/14 个有
- `LayerMask: BiRefNetUltraV2` —— 4/14 个有
- `LayerMask: LoadBiRefNetModel` —— 4/14 个有
- `easy int` —— 4/14 个有
- `DifferentialDiffusion` —— 2/14 个有
- `InpaintModelConditioning` —— 2/14 个有
- `PlaySound|pysssss` —— 2/14 个有
- `GrowMaskWithBlur` —— 1/14 个有
- `ImagePadForOutpaint` —— 1/14 个有
- `LanPaint_MaskBlend` —— 1/14 个有
- `easy imageRemBg` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
