---
name: unknown_workflow_sampler_clip_unet_159
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.924625
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/▶2_Flux2Klein-单图及多图编辑_2066881431275663361.json, 图片生成/图生图/【1月】高质量图像编辑 Flux2-Klein-9B_2012162088738758658.json, 图片生成/图生图/【Flux2 Klein】 双图编辑+换装lora版本_2030255334941528065.json, 图片生成/图生图/【Flux2 Klein】 （加密版）双图编辑+换装lora版本_2049724297060552705.json, 图片生成/图生图/【工作台】 双图编辑+换装lora版本（常规）_2075804075794456578.json, 图片生成/图生图/【推荐动漫转真人】Flux2 Klein_史上最强动漫转写实真人_2017575897674551298.json, 图片生成/图生图/一键去水印FLUX2-klein-增强版_2028855059450171393.json, 图片生成/图生图/最强万物迁移 f2k_9b_anything change clothes_2026650952215826434.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_159

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/▶2_Flux2Klein-单图及多图编辑_2066881431275663361.json、图片生成/图生图/【1月】高质量图像编辑 Flux2-Klein-9B_2012162088738758658.json、图片生成/图生图/【Flux2 Klein】 双图编辑+换装lora版本_2030255334941528065.json、图片生成/图生图/【Flux2 Klein】 （加密版）双图编辑+换装lora版本_2049724297060552705.json、图片生成/图生图/【工作台】 双图编辑+换装lora版本（常规）_2075804075794456578.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 7/8 个有
- `ReferenceLatent` —— 7/8 个有
- `VAEEncode` —— 7/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `ImageConcanate` —— 4/8 个有
- `ImageScaleToTotalPixels` —— 4/8 个有
- `easy imageScaleDownToSize` —— 4/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `ConditioningAddImageReference` —— 1/8 个有
- `CustomAddLabel` —— 1/8 个有
- `DuckHideNode` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `Load Lora` —— 1/8 个有
- `PDIMAGE_LongerSize` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `SeedVR2` —— 1/8 个有
- `SeedVR2BlockSwap` —— 1/8 个有
- `SeedVR2ExtraArgs` —— 1/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
