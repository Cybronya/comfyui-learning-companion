---
name: unknown_workflow_sampler_clip_vae_72
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9175
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DisableNoise, FlipSigmas, FluxDeGuidance, FluxForwardODESampler, FluxReverseODESampler, Get Image Size, Image Comparer (rgthree), InFluxModelSamplingPred, Joy_caption_two, Joy_caption_two_load, LoadImage, NunchakuFluxDiTLoader, OutFluxModelSamplingPred, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/产品精修工作流 （可选多材质精修）_2003658762684669953.json, 图片生成/图生图/精修去褶皱工作流 服装、箱包、帆布袋适用 flux逆采样工作流_1933120693514973186.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_72

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/产品精修工作流 （可选多材质精修）_2003658762684669953.json、图片生成/图生图/精修去褶皱工作流 服装、箱包、帆布袋适用 flux逆采样工作流_1933120693514973186.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DisableNoise`
- `FlipSigmas`
- `FluxDeGuidance`
- `FluxForwardODESampler`
- `FluxReverseODESampler`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `InFluxModelSamplingPred`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `OutFluxModelSamplingPred`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 1/2 个有
- `DualCLIPLoader` —— 1/2 个有
- `Fast Bypasser (rgthree)` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `Int` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `NunchakuTextEncoderLoader` —— 1/2 个有
- `Upscale Model Loader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
