---
name: unknown_workflow_sampler_clip_vae_76
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.857667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/flux2 8步加速Lora出图_1993716048765583362.json, 图片生成/文生图/flux2-ftp8 workflow_1993525727769411585.json, 图片生成/文生图/flux2_Klein_v2 文生图至四图参考图生图_2013238859747827714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_76

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/flux2 8步加速Lora出图_1993716048765583362.json、图片生成/文生图/flux2-ftp8 workflow_1993525727769411585.json、图片生成/文生图/flux2_Klein_v2 文生图至四图参考图生图_2013238859747827714.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 2/3 个有
- `ClipLoaderGGUF` —— 2/3 个有
- `ModelPatchTorchSettings` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `UnetLoaderGGUF` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `CFGGuider` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `LoaderGGUF` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `VaeGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
