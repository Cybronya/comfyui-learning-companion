---
name: unknown_workflow_sampler_clip_unet_475
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8665
common_nodes: [CLIPLoader, CLIPTextEncode, ClipLoaderGGUF, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/flux2 8步加速Lora出图_1993716048765583362.json, 图片生成/文生图/flux2_Klein_v2 文生图至四图参考图生图_2013238859747827714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_475

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/flux2 8步加速Lora出图_1993716048765583362.json、图片生成/文生图/flux2_Klein_v2 文生图至四图参考图生图_2013238859747827714.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ClipLoaderGGUF`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `CFGGuider` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `LoaderGGUF` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `VaeGGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
