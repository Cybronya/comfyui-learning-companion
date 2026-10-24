---
name: unknown_workflow_sampler_unet_vae_131
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.796375
common_nodes: [CFGGuider, CLIPLoader, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/三图编辑（解禁模型）：Flux.2 Klein 9B_2051654833320542209.json, 图片生成/图生图/仅需四步，建筑效果图一键多风格_2030610127664979970.json, 图片生成/图生图/全能人物照片编辑头发人脸衣服服装更换变装变发型图生图升级版_2074339361214255106.json, 图片生成/图生图/单图编辑（解禁模型）：Flux.2 Klein 9B_2051293761195524098.json, 图片生成/图生图/参考风格生成效果图_2030619395935965186.json, 图片生成/图生图/多图编辑换装电商人物添加人物物品装饰多图合一AI重绘_2074345357949104129.json, 图片生成/图生图/幻影疾驰 • 视觉冲击CG造像师：定格震撼人心的游戏视觉大片_2013554944284037122.json, 图片生成/图生图/课程演示——室内设计（全屋）-终版_2075575000530247681.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_131

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/三图编辑（解禁模型）：Flux.2 Klein 9B_2051654833320542209.json、图片生成/图生图/仅需四步，建筑效果图一键多风格_2030610127664979970.json、图片生成/图生图/全能人物照片编辑头发人脸衣服服装更换变装变发型图生图升级版_2074339361214255106.json、图片生成/图生图/单图编辑（解禁模型）：Flux.2 Klein 9B_2051293761195524098.json、图片生成/图生图/参考风格生成效果图_2030619395935965186.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 7/8 个有
- `CLIPTextEncode` —— 6/8 个有
- `ReferenceLatent` —— 6/8 个有
- `VAEEncode` —— 6/8 个有
- `EmptyFlux2LatentImage` —— 4/8 个有
- `PlaySound|pysssss` —— 4/8 个有
- `PreviewImage` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `ImageInvert` —— 2/8 个有
- `PrimitiveStringMultiline` —— 2/8 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/8 个有
- `AILab_QwenVL` —— 1/8 个有
- `AIO_Preprocessor` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `ImpactSwitch` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `LayerUtility: ImageReel` —— 1/8 个有
- `LayerUtility: ImageReelComposit` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `TEEDPreprocessor` —— 1/8 个有
- `easy imageConcat` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
