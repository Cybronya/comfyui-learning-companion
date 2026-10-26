---
name: unknown_workflow_sampler_clip_unet_54
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.913867
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX.2 Klein 4B 文生图_2012080117027184642.json, 图片生成/文生图/FLUX.2 Klein 9B 文生图_2012074303356936193.json, 图片生成/文生图/FLUX.2 开源啦！ComfyUI 原生支持，图像生成+编辑一体工作流来啦！_1995474199747682305.json, 图片生成/文生图/FLUX.2多图参考编辑_1994778617873883137.json, 图片生成/文生图/FLUX.2祭出加速LoRA：能否再战Z-Image一雪前耻？_2008141326423957505.json, 图片生成/文生图/FLUX2 Dev FP8 文生图_图片编辑_2073281827388874753.json, 图片生成/文生图/FLUX2 混合模型_1993521841442586625.json, 图片生成/文生图/FLUX2 混合模型_1993527380123860994.json, 图片生成/文生图/FLUX2-多参考一致性创意场景合成_2090769208387923969.json, 图片生成/文生图/Flux.2+LoRA文生图_1995120190486667265.json, 图片生成/文生图/Flux.2文生哪吒_1994791173480964097.json, 图片生成/文生图/flux2-ftp8 workflow_1993525727769411585.json, 图片生成/文生图/flux2_文生图+图片参考_1993696007951237121.json, 图片生成/文生图/【AI小兵哥】Flux.2-多图编辑工作流_1994221492407828481.json, 图片生成/文生图/最强开源 FLUX2系列合集_1993708586574479361.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_54

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/FLUX.2 Klein 4B 文生图_2012080117027184642.json、图片生成/文生图/FLUX.2 Klein 9B 文生图_2012074303356936193.json、图片生成/文生图/FLUX.2 开源啦！ComfyUI 原生支持，图像生成+编辑一体工作流来啦！_1995474199747682305.json、图片生成/文生图/FLUX.2多图参考编辑_1994778617873883137.json、图片生成/文生图/FLUX.2祭出加速LoRA：能否再战Z-Image一雪前耻？_2008141326423957505.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 13/15 个有
- `LoadImage` —— 13/15 个有
- `ReferenceLatent` —— 13/15 个有
- `VAEEncode` —— 13/15 个有
- `PreviewImage` —— 4/15 个有
- `LoraLoaderModelOnly` —— 3/15 个有
- `ApplySageAttention` —— 2/15 个有
- `CR Text` —— 2/15 个有
- `Int Literal` —— 2/15 个有
- `Label (rgthree)` —— 2/15 个有
- `ModelPatchTorchSettings` —— 2/15 个有
- `UnetLoaderGGUF` —— 2/15 个有
- `easy int` —— 2/15 个有
- `DeepTranslatorTextNode` —— 1/15 个有
- `EasyCache` —— 1/15 个有
- `ImageConcanate` —— 1/15 个有
- `ImpactInt` —— 1/15 个有
- `RH_Captioner` —— 1/15 个有
- `TTResolutionSelector` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有
- `easy showAnything` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
