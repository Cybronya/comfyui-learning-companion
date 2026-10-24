---
name: unknown_workflow_sampler_clip_vae_11
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.892231
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX.2 Klein 4B 文生图_2012080117027184642.json, 图片生成/文生图/FLUX.2 Klein 9B 文生图_2012074303356936193.json, 图片生成/文生图/FLUX.2 Turbo_2006076343817084929.json, 图片生成/文生图/FLUX.2 开源啦！ComfyUI 原生支持，图像生成+编辑一体工作流来啦！_1995474199747682305.json, 图片生成/文生图/FLUX.2多图参考编辑_1994778617873883137.json, 图片生成/文生图/FLUX.2祭出加速LoRA：能否再战Z-Image一雪前耻？_2008141326423957505.json, 图片生成/文生图/FLUX2 Dev FP8 8步加速 文生图_图片编辑_2073296125880262657.json, 图片生成/文生图/FLUX2 Dev FP8 文生图_图片编辑_2073281827388874753.json, 图片生成/文生图/FLUX2 混合模型_1993521841442586625.json, 图片生成/文生图/Flux.2+LoRA文生图_1995120190486667265.json, 图片生成/文生图/Flux2 文生图_图生图_图像修改_多图参考工作流_1993868752053796866.json, 图片生成/文生图/flux.2图像编辑测试（单图）_1995053515309506561.json, 图片生成/文生图/flux.2量化+SageAttention加速图像编辑（单图）_1994854140247465985.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_11

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/FLUX.2 Klein 4B 文生图_2012080117027184642.json、图片生成/文生图/FLUX.2 Klein 9B 文生图_2012074303356936193.json、图片生成/文生图/FLUX.2 Turbo_2006076343817084929.json、图片生成/文生图/FLUX.2 开源啦！ComfyUI 原生支持，图像生成+编辑一体工作流来啦！_1995474199747682305.json、图片生成/文生图/FLUX.2多图参考编辑_1994778617873883137.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 13 个 workflow 都包含：
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
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 11/13 个有
- `LoadImage` —— 11/13 个有
- `ReferenceLatent` —— 11/13 个有
- `UNETLoader` —— 11/13 个有
- `VAEEncode` —— 11/13 个有
- `LoraLoaderModelOnly` —— 4/13 个有
- `ModelPatchTorchSettings` —— 4/13 个有
- `PathchSageAttentionKJ` —— 4/13 个有
- `PreviewImage` —— 3/13 个有
- `UnetLoaderGGUF` —— 3/13 个有
- `Int Literal` —— 2/13 个有
- `Label (rgthree)` —— 2/13 个有
- `CR Text` —— 1/13 个有
- `ImageConcanate` —— 1/13 个有
- `PreviewAny` —— 1/13 个有
- `RH_Captioner` —— 1/13 个有
- `RH_Translator` —— 1/13 个有
- `easy int` —— 1/13 个有
- `easy promptLine` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
