---
name: unknown_workflow_upscale_sampler_unet_16
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.821
common_nodes: [CLIPLoader, ClownsharKSampler_Beta, ConditioningZeroOut, LoadImage, ManualSigmas, PrimitiveStringMultiline, QwenImage21EditTextEncode_EditUtils, QwenImage21SageAttentionT8, RH_Screenwriter, SaveImage, UNETLoader, VAEDecode, VAELoader, WujiCleaner, WujiImagePrompt, WujiUpscaler2]
problems: []
missing: []
members: [图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器（文生、多图生均可）_2107839506576666626.json, 图片生成/图生图/Qwen-image2.1零偏移单_多图局部遮罩编辑重绘_2107546142769766401.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_16

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器（文生、多图生均可）_2107839506576666626.json、图片生成/图生图/Qwen-image2.1零偏移单_多图局部遮罩编辑重绘_2107546142769766401.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `ClownsharKSampler_Beta`
- `ConditioningZeroOut`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveStringMultiline`
- `QwenImage21EditTextEncode_EditUtils`
- `QwenImage21SageAttentionT8`
- `RH_Screenwriter`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WujiCleaner`
- `WujiImagePrompt`
- `WujiUpscaler2`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RH_RhartImageG25SunburstImageToImage` —— 1/2 个有
- `WujiPromptEditor` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | bong_tangent | - | 2 | 100% |
| Prompt 约束强度(CFG) | 8 | - | 2 | 100% |
| 采样算法 | -1 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 bong_tangent，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 -1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
