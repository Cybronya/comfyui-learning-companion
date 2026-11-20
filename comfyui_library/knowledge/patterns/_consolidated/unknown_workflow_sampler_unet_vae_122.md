---
name: unknown_workflow_sampler_unet_vae_122
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9345
common_nodes: [CFGGuider, CLIPLoader, ConditioningZeroOut, Flux2Scheduler, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/单图编辑（解禁模型）：Flux.2 Klein 9B_2051293761195524098.json, 图片生成/图生图/参考风格生成效果图_2030619395935965186.json, 图片生成/图生图/双图编辑（解禁模型）：Flux.2 Klein 9B_2051467007492665345.json, 图片生成/图生图/双模放大_2076211416096399362.json, 图片生成/图生图/发型迁移与更换_2051141221707468801.json, 图片生成/图生图/渲染级产品精修V5 +自动白底 +细节增强_2084924306483666945.json, 图片生成/图生图/渲染级精修V5_2115722356265152514.json, 平台全量/4K 8K高清放大 Flux2-Klein9b超级皮肤质感 人物写实 皮肤增强质感 去除AI感_2025026532682506241.json, 平台全量/Flux2 Klein 9b 最强动漫转写实真人 皮肤质感修复 优化 史上最强动漫转写实真人_2025012840028971010.json, 平台全量/添加真实感细节 Flux2-Klein9b优化皮肤质感 高清放大 增加细节 去除AI塑料感 优化皮肤_2031184424959741953.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_122

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/单图编辑（解禁模型）：Flux.2 Klein 9B_2051293761195524098.json、图片生成/图生图/参考风格生成效果图_2030619395935965186.json、图片生成/图生图/双图编辑（解禁模型）：Flux.2 Klein 9B_2051467007492665345.json、图片生成/图生图/双模放大_2076211416096399362.json、图片生成/图生图/发型迁移与更换_2051141221707468801.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `ConditioningZeroOut`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/10 个有
- `CLIPTextEncode` —— 8/10 个有
- `Image Comparer (rgthree)` —— 8/10 个有
- `ReferenceLatent` —— 8/10 个有
- `VAEEncode` —— 8/10 个有
- `EmptyFlux2LatentImage` —— 7/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `CR Prompt Text` —— 5/10 个有
- `Int` —— 4/10 个有
- `GetImageSize` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `CR Text Input Switch (4 way)` —— 2/10 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/10 个有
- `DapaoImageAspectRatioResizeNode` —— 1/10 个有
- `GrowMaskWithBlur` —— 1/10 个有
- `ImageInvert` —— 1/10 个有
- `JoinImageWithAlpha` —— 1/10 个有
- `SAM3Segment` —— 1/10 个有
- `TEEDPreprocessor` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
