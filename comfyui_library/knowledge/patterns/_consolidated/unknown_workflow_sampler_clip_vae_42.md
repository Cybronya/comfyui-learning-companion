---
name: unknown_workflow_sampler_clip_vae_42
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.789667
common_nodes: [CR Prompt Text, CR Text, FluxResolutionNode, ImageConcanate, ImageResize+, ImageResizeKJv2, ImpactSwitch, JjkText, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewAny, PreviewImage, RH_Jimeng_Image2Image, RH_LLMAPI_NODE, RH_Nano_Banana_Image2Image, RH_Prompter, RH_Sora2_I2V, RH_Translator, SaveImage, SaveVideo, TextCombinerTwo, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/漫剧_2010968294735486978.json, 视频生成/图生视频/1987861383444369409.json, 视频生成/文生视频/向南漫剧场创作_1989943868923760641.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_42

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/漫剧_2010968294735486978.json、视频生成/图生视频/1987861383444369409.json、视频生成/文生视频/向南漫剧场创作_1989943868923760641.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
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
- `CLIPLoader` —— 1/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `Int` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `NunchakuQwenImageDiTLoader` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `Seed (rgthree)` —— 1/3 个有
- `VAEDecode` —— 1/3 个有
- `VAELoader` —— 1/3 个有
- `easy promptConcat` —— 1/3 个有

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

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
