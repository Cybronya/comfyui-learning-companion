---
name: unknown_workflow_sampler_clip_unet_30
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.922
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/F2K-9B一键换头、换脸_2019369641709150209.json, 图片生成/图生图/FLUX2 Klein 双图编辑_2014610246840360961.json, 图片生成/图生图/FLUX2Klein 单图编辑_2026497012299993090.json, 图片生成/图生图/FLUX新王炸 Klein 双图编辑版_2012806080375562241.json, 图片生成/图生图/FLUX新王炸 Klein 图像编辑版 急速10秒出图_2048574540699148289.json, 图片生成/图生图/FLUX新王炸 Klein 图像编辑版 急速10秒出图_2048599240196235266.json, 图片生成/图生图/FLUX新王炸 Klein 图像编辑版_2016046164730187778.json, 图片生成/图生图/Flux 2 klein 9b 换头工作流_2013818759424778241.json, 图片生成/图生图/Flux 2 klein 9b 换头工作流_2015981757341900802.json, 图片生成/图生图/Flux2 Klein 双重增强现实_2067152624360706049.json, 图片生成/图生图/Flux2 Klein 增强现实LoRA_2020393021082181633.json, 图片生成/图生图/Flux2 Klein 增强现实LoRA_2033162072971812866.json, 图片生成/图生图/Flux2 Klein 增强现实（超还原cosplay)_2026115898070798337.json, 图片生成/图生图/Flux2 Klein9B 图像编辑工作流 加强了一致性 林耀3.6_2029755418074947585.json, 图片生成/图生图/Flux2-Klein扩图工作流_2052313109414592514.json, 图片生成/图生图/Flux2-Klein扩图工作流_2085318245518766082.json, 图片生成/图生图/Flux2-Klein照片扩图_2105520911993626625.json, 图片生成/图生图/Flux2-klein 单图编辑之胸围调节器_2021575947543121921.json, 图片生成/图生图/Flux2_Klein_9B高清放大Lora方法_2027577843588276226.json, 图片生成/图生图/klein-9b面部一致性增强与东方审美lora_2035090544275234817.json, 图片生成/图生图/klein克莱因转赛璐珞_2018983559482052610.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_30

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/F2K-9B一键换头、换脸_2019369641709150209.json、图片生成/图生图/FLUX2 Klein 双图编辑_2014610246840360961.json、图片生成/图生图/FLUX2Klein 单图编辑_2026497012299993090.json、图片生成/图生图/FLUX新王炸 Klein 双图编辑版_2012806080375562241.json、图片生成/图生图/FLUX新王炸 Klein 图像编辑版 急速10秒出图_2048574540699148289.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 21 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `PreviewImage` —— 19/21 个有
- `ConditioningZeroOut` —— 18/21 个有
- `EmptyFlux2LatentImage` —— 18/21 个有
- `ImageScaleToTotalPixels` —— 16/21 个有
- `Image Comparer (rgthree)` —— 14/21 个有
- `LayerUtility: ImageReel` —— 14/21 个有
- `LayerUtility: ImageReelComposit` —— 14/21 个有
- `CR Text` —— 13/21 个有
- `LoraLoaderModelOnly` —— 11/21 个有
- `ImagePadForOutpaint` —— 4/21 个有
- `easy imageScaleDownToSize` —— 4/21 个有
- `ImageConcanate` —— 3/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/21 个有
- `Anything Everywhere3` —— 1/21 个有
- `BetterFilmGrain` —— 1/21 个有
- `ImageAndMaskPreview` —— 1/21 个有
- `ImageApplyLUT+` —— 1/21 个有
- `ImageSharpen` —— 1/21 个有
- `LayerMask: HumanPartsUltra` —— 1/21 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/21 个有
- `easy seed` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
