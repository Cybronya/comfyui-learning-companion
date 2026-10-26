---
name: unknown_workflow_lora_sampler_clip_266
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.955
common_nodes: [BasicScheduler, CLIPTextEncode, CR Text, ConditioningZeroOut, DualCLIPLoader, GrowMaskWithBlur, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/fill局部重绘_1995757604498444289.json, 图片生成/图生图/flux-阿里妈妈局部重绘_1995749087129513985.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_266

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/fill局部重绘_1995757604498444289.json、图片生成/图生图/flux-阿里妈妈局部重绘_1995749087129513985.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `GrowMaskWithBlur`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 1/2 个有
- `CFGGuider` —— 1/2 个有
- `ControlNetInpaintingAliMamaApply` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DifferentialDiffusion` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `InpaintModelConditioning` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
