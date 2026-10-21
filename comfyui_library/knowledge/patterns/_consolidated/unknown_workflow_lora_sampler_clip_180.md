---
name: unknown_workflow_lora_sampler_clip_180
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7355
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/StyleSculpt_角色设计(游戏角色设计、动画设定本)_2021892139688398850.json, 图片生成/文生图/图1给姿势，图2给脸｜Flux Klein 双图融合工作流【全节点注释】_2070728938242011138.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_180

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/StyleSculpt_角色设计(游戏角色设计、动画设定本)_2021892139688398850.json、图片生成/文生图/图1给姿势，图2给脸｜Flux Klein 双图融合工作流【全节点注释】_2070728938242011138.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `JDCN_StringToList` —— 1/2 个有
- `JWStringConcat` —— 1/2 个有
- `ProcessString` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
