---
name: unknown_workflow_sampler_clip_vae_12
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.863429
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【晨晨的AI应用包005】随机风格生成-通过FLUX2-Klein_2012057296452460546.json, 图片生成/图生图/工作流基础系列2-Klein双（多）图编辑工作流-基础向讲解此工作流_2012071492288258050.json, 图片生成/图生图/工作流基础系列3-Klein局部编辑工作流-基础向讲解此工作流_2044322503283187713.json, 图片生成/图生图/熊熊-Flux2 Klein局部重绘+图片去水印+物品迁移_2044458513019179010.json, 图片生成/图生图/精修Flux-2 Klein_2036724091914293250.json, 图片生成/图生图/精修白底（产品需要调整提示词）_2037844081199550466.json, 图片生成/图生图/精修白底（产品需要调整提示词）_2053018735723724802.json, 图片生成/图生图/组件系列8-FLUX.2-Klein单图编辑_2058753653384765441.json, 图片生成/图生图/自用瓶子修图工作流_2045810602009960450.json, 平台全量/Flux-2-Klein-9B 万能产品修图 产品渲染质感精修 电商产品商业级修复打光 产品精修 旧_2015684553628721153.json, 平台全量/Flux-2实拍图商业级精修（白底）渲染_2028743079615795201.json, 平台全量/产品白底精修（有对应材质可选择）_2047254557352271874.json, 平台全量/节点系列14-抠图系列01-LayerMask_ BiRefNet Ultra V2(Advance)_2037375823220576257.json, 平台全量/节点系列15-🎈FastCanvas_2037484316401340417.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_12

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/【晨晨的AI应用包005】随机风格生成-通过FLUX2-Klein_2012057296452460546.json、图片生成/图生图/工作流基础系列2-Klein双（多）图编辑工作流-基础向讲解此工作流_2012071492288258050.json、图片生成/图生图/工作流基础系列3-Klein局部编辑工作流-基础向讲解此工作流_2044322503283187713.json、图片生成/图生图/熊熊-Flux2 Klein局部重绘+图片去水印+物品迁移_2044458513019179010.json、图片生成/图生图/精修Flux-2 Klein_2036724091914293250.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 13/14 个有
- `UNETLoader` —— 13/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/14 个有
- `Text` —— 12/14 个有
- `EmptyFlux2LatentImage` —— 9/14 个有
- `CR Text` —— 8/14 个有
- `GetImageSize` —— 7/14 个有
- `ImpactSwitch` —— 7/14 个有
- `ShowText` —— 7/14 个有
- `TextCombinerTwo` —— 7/14 个有
- `GetNode` —— 6/14 个有
- `SetNode` —— 6/14 个有
- `PreviewImage` —— 5/14 个有
- `Seed (rgthree)` —— 5/14 个有
- `DrawMaskOnImage` —— 2/14 个有
- `ImageScaleToTotalPixels` —— 2/14 个有
- `LayerMask: BiRefNetUltraV2` —— 2/14 个有
- `LayerMask: LoadBiRefNetModelV2` —— 2/14 个有
- `FastCanvas` —— 1/14 个有
- `FastCanvasTool` —— 1/14 个有
- `Int` —— 1/14 个有
- `MaskPreview` —— 1/14 个有
- `RandomPrompt` —— 1/14 个有
- `ShowText|pysssss` —— 1/14 个有
- `UnetLoaderGGUF` —— 1/14 个有
- `easy imageColorMatch` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
