---
name: unknown_workflow_upscale_sampler_unet_16
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.4515
common_nodes: [CLIPLoader, CR Seed, CR Text, ConditioningZeroOut, Fast Groups Bypasser (rgthree), GetNode, Image Comparer (rgthree), KOOK_SaveJPGImage, KSampler (Efficient), Label (rgthree), LoadImage, PreviewImage, QwenImage21Cache, SetNode, SplitImageWithAlpha, TextEncodeQwenImage21, UNETLoader, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy imageChooser]
problems: []
missing: []
members: [图片生成/图生图/qwen image  2.1 最新扩图_2107769241435987970.json, 图片生成/图生图/一键运行：qwen image  2.1 编辑 （图像选择、文本切换、高清放大）_2107330978216759298.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/qwen image  2.1 最新扩图_2107769241435987970.json、图片生成/图生图/一键运行：qwen image  2.1 编辑 （图像选择、文本切换、高清放大）_2107330978216759298.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：45%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CR Seed`
- `CR Text`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `KOOK_SaveJPGImage`
- `KSampler (Efficient)`
- `Label (rgthree)`
- `LoadImage`
- `PreviewImage`
- `QwenImage21Cache`
- `SetNode`
- `SplitImageWithAlpha`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy imageChooser`

**可变部分**（部分 workflow 才有）：
- `CR Text Input Switch` —— 1/2 个有
- `ImagePadForOutpaint` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LayerFilter: HDREffects` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PromptExpand` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `TESpeedQwenImage21` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
