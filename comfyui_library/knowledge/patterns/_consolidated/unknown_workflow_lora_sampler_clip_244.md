---
name: unknown_workflow_lora_sampler_clip_244
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.941
common_nodes: [BasicScheduler, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoraLoaderModelOnly, PreviewImage, SamplerCustom, SaveImage, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/02.flux图生图极速版_2000792934989561857.json, 图片生成/文生图/01.flux文生图极速版_2000792865175371778.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_244

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/02.flux图生图极速版_2000792934989561857.json、图片生成/文生图/01.flux文生图极速版_2000792865175371778.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SamplerCustom`
- `SaveImage`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `SDXL Empty Latent Image (rgthree)` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `easy imageScaleDownToSize` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
