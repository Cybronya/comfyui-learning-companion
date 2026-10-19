---
name: unknown_workflow_sampler_clip_vae_35
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7955
common_nodes: [CR Prompt Text, CR Text, FluxResolutionNode, ImageConcanate, ImageResize+, ImageResizeKJv2, ImpactSwitch, JjkText, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewAny, PreviewImage, RH_Jimeng_Image2Image, RH_LLMAPI_NODE, RH_Nano_Banana_Image2Image, RH_Prompter, RH_Sora2_I2V, RH_Translator, SaveImage, SaveVideo, TextCombinerTwo, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1987861383444369409.json, 视频生成/文生视频/向南漫剧场创作_1989943868923760641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_35

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1987861383444369409.json、视频生成/文生视频/向南漫剧场创作_1989943868923760641.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `CR Text`
- `FluxResolutionNode`
- `ImageConcanate`
- `ImageResize+`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `JjkText`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewAny`
- `PreviewImage`
- `RH_Jimeng_Image2Image`
- `RH_LLMAPI_NODE`
- `RH_Nano_Banana_Image2Image`
- `RH_Prompter`
- `RH_Sora2_I2V`
- `RH_Translator`
- `SaveImage`
- `SaveVideo`
- `TextCombinerTwo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 1/2 个有
- `CLIPTextEncode` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `Int` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `NunchakuQwenImageDiTLoader` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `VAEDecode` —— 1/2 个有
- `VAELoader` —— 1/2 个有
- `easy promptConcat` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 3.5 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
