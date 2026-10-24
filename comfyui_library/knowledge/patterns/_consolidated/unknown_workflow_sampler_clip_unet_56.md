---
name: unknown_workflow_sampler_clip_unet_56
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.929429
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX 2 _ 多图编辑_1885166916967780353.json, 图片生成/图生图/FLUX.2 Klein 4B 单图编辑_2012091769122463745.json, 图片生成/图生图/FLUX.2 Klein 4B 双图编辑_2012164713425145858.json, 图片生成/图生图/FLUX.2 Klein 9B 单图编辑_2012087765889978370.json, 图片生成/图生图/FLUX.2 Klein 9B 双图编辑_2012102600216285186.json, 图片生成/图生图/Flux.2 Klein 9B单图编辑_2022512699938181122.json, 图片生成/图生图/Flux.2-支持中文-图片一致性-单图编辑_1993529953790738433.json, 图片生成/图生图/Flux.2-支持中文-图片一致性-单图编辑_1993681359214493697.json, 图片生成/图生图/Flux.2-支持中文-图片一致性-双图编辑_1993678108651880449.json, 图片生成/图生图/Flux2 DEV 多图编辑_1993591604223082497.json, 图片生成/图生图/Flux2.DEV-三角色一场景图编辑_2018937350511923202.json, 图片生成/图生图/Flux2.DEV-多图编辑【一天王者】_1994920372749393922.json, 图片生成/图生图/Flux2DEV单图编辑_1994049571294822402.json, 图片生成/图生图/👾怪獸-FLUX.2多图编辑👾_1993639173827608577.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_56

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/FLUX 2 _ 多图编辑_1885166916967780353.json、图片生成/图生图/FLUX.2 Klein 4B 单图编辑_2012091769122463745.json、图片生成/图生图/FLUX.2 Klein 4B 双图编辑_2012164713425145858.json、图片生成/图生图/FLUX.2 Klein 9B 单图编辑_2012087765889978370.json、图片生成/图生图/FLUX.2 Klein 9B 双图编辑_2012102600216285186.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
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
- `ImageScaleToTotalPixels` —— 8/14 个有
- `Int` —— 8/14 个有
- `ImageConcanate` —— 5/14 个有
- `AddLabel` —— 3/14 个有
- `GetNode` —— 3/14 个有
- `Int Literal` —— 3/14 个有
- `SetNode` —— 3/14 个有
- `easy promptList` —— 3/14 个有
- `PreviewAny` —— 2/14 个有
- `PrimitiveStringMultiline` —— 2/14 个有
- `RH_LLMAPI_NODE` —— 2/14 个有
- `Anything Everywhere3` —— 1/14 个有
- `ConstrainImage|pysssss` —— 1/14 个有
- `LayerUtility: PurgeVRAM` —— 1/14 个有
- `RH_Translator` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
