---
name: unknown_workflow_sampler_clip_unet_49
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.865875
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/F2K提取_2016857120255250434.json, 图片生成/图生图/FLUX.2 klein base 版单图编辑_2012465215350251522.json, 图片生成/图生图/FLUX.2 klein base 版双图编辑_2012466611072012290.json, 图片生成/图生图/FLUX.2 klein 蒸馏版单图编辑_2012460463300288514.json, 图片生成/图生图/FLUX.2 klein 蒸馏版双图编辑_2012462098781052930.json, 图片生成/图生图/FLUX.2 设计师专属商品设计全流程工作流_2045722294399537153.json, 图片生成/图生图/FLUX.2-Klein_高清修复_•_真像造像师，定格纤毫毕现的极清人像放大_2096793604470693889.json, 图片生成/图生图/FLUX.2-Klein_高清修复_•_真像造像师，定格纤毫毕现的极清人像放大_2097139140046450689.json, 图片生成/图生图/FLUX.2-Klein：高清修复 • 真像造像师，定格纤毫毕现的极清人像放大_2013555018963619841.json, 图片生成/图生图/FLUX.2-Klein：高清修复 • 真像造像师，高清极清人像放大_2079820337243582466.json, 图片生成/图生图/FLUX.klein 添加真实细节_2036315784296800257.json, 图片生成/图生图/FLUX2 KLEIN 一致性大乱斗 总有一款你会满意的_2051669958836400130.json, 图片生成/图生图/FLUX2 KLEIN 双三图编辑测试工作流 总有一款你会满意的_2055851156420734978.json, 图片生成/图生图/Klein单、双图像编辑_2047571289468051458.json, 图片生成/图生图/参考色改车色输出不同饱和度+明度_2058520449017008130.json, 图片生成/图生图/啊癫 Klein单、双图像编辑_2067285820989599745.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_49

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/F2K提取_2016857120255250434.json、图片生成/图生图/FLUX.2 klein base 版单图编辑_2012465215350251522.json、图片生成/图生图/FLUX.2 klein base 版双图编辑_2012466611072012290.json、图片生成/图生图/FLUX.2 klein 蒸馏版单图编辑_2012460463300288514.json、图片生成/图生图/FLUX.2 klein 蒸馏版双图编辑_2012462098781052930.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ReferenceLatent` —— 15/16 个有
- `VAEEncode` —— 15/16 个有
- `PrimitiveStringMultiline` —— 12/16 个有
- `Image Comparer (rgthree)` —— 11/16 个有
- `LoraLoaderModelOnly` —— 11/16 个有
- `GetImageSize` —— 10/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/16 个有
- `ConditioningZeroOut` —— 9/16 个有
- `ImageScaleToTotalPixels` —— 8/16 个有
- `PlaySound|pysssss` —— 7/16 个有
- `CropWithPadInfo_EditUtils` —— 5/16 个有
- `EditTextEncode_EditUtils` —— 5/16 个有
- `Flux2KleinConfigPreparer_EditUtils` —— 5/16 个有
- `Flux2KleinModelConfig_EditUtils` —— 5/16 个有
- `Flux2KleinOutputExtractor_EditUtils` —— 5/16 个有
- `ImpactSwitch` —— 4/16 个有
- `PrimitiveInt` —— 3/16 个有
- `AdaptiveLongestEdge_EditUtils` —— 2/16 个有
- `Fast Groups Bypasser (rgthree)` —— 2/16 个有
- `PreviewImage` —— 2/16 个有
- `Text Multiline` —— 2/16 个有
- `easy imageSize` —— 2/16 个有
- `CR Text` —— 1/16 个有
- `CR Text Concatenate` —— 1/16 个有
- `CompositorColorPicker` —— 1/16 个有
- `ImageScale` —— 1/16 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/16 个有
- `easy imageColorMatch` —— 1/16 个有
- `easy seed` —— 1/16 个有
- `easy showAnything` —— 1/16 个有
- `workflow>latent` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
