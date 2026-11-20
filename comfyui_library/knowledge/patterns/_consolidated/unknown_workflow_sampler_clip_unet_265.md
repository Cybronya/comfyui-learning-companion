---
name: unknown_workflow_sampler_clip_unet_265
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.729333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/电商详情-普通中文版_1988507050411999234.json, 图片生成/图生图/第二个成熟AI城市设计-klein生成城市设计工作流_2026550405894774785.json, 图片生成/图生图/第二个成熟AI景观设计-klein景观_2022131857361477633.json, 图片生成/文生图/FLUX2-KLEIN _ 文生图+多图编辑大合集_2012077337252204546.json, 图片生成/文生图/FLUX2-KLEIN _ 文生图+多图编辑大合集_2012132446178910209.json, 图片生成/文生图/FLUX2-KLEIN _ 文生图+多图编辑大合集_2015497456603111426.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_265

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/电商详情-普通中文版_1988507050411999234.json、图片生成/图生图/第二个成熟AI城市设计-klein生成城市设计工作流_2026550405894774785.json、图片生成/图生图/第二个成熟AI景观设计-klein景观_2022131857361477633.json、图片生成/文生图/FLUX2-KLEIN _ 文生图+多图编辑大合集_2012077337252204546.json、图片生成/文生图/FLUX2-KLEIN _ 文生图+多图编辑大合集_2012132446178910209.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `LayerUtility: ImageReel` —— 5/6 个有
- `LayerUtility: ImageReelComposit` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `GetImageSize` —— 4/6 个有
- `INTConstant` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `LoraLoaderModelOnly` —— 2/6 个有
- `Int` —— 1/6 个有
- `LayerUtility: TextJoin` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
