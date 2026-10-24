---
name: unknown_workflow_controlnet_sampler_clip_26
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FluxGuidance, InfiniteYouApply, KSamplerSelect, LoadImage, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/InfiniteYou  数字形象衍生_2073036926172622850.json, 图片生成/图生图/InfiniteYou换脸_在线生图_1906014363168198658.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/InfiniteYou  数字形象衍生_2073036926172622850.json、图片生成/图生图/InfiniteYou换脸_在线生图_1906014363168198658.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `InfiniteYouApply`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Joy_caption_two` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `LayerMask: PersonMaskUltra V2` —— 1/2 个有
- `LayerUtility: CropByMask V2` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `ShowText` —— 1/2 个有
- `Text Concatenate (JPS)` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 816 | - | 2 | 94% |
| 高度 | 1088 | - | 2 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 816，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- 高度 中位数 1088，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
