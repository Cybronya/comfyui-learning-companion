---
name: unknown_workflow_upscale_sampler_unet
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8629
common_nodes: [CLIPLoader, ClownsharKSampler_Beta, LoadImage, ManualSigmas, PrimitiveStringMultiline, QwenImage21SageAttentionT8, RH_Screenwriter, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, WujiImagePrompt, WujiPromptEditor, WujiUpscaler2, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Qwein-image2.1分镜专用空镜（有人、无人）_2111716013799731201.json, 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5图像反推_2111665215556378626.json, 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5影楼写真九宫格_2111712714950270978.json, 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5网红打卡旅游九宫格_2111702701032689666.json, 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104088591185039361.json, 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2107810644580982786.json, 图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色表情包九宫格_2109274600004734978.json, 图片生成/图生图/qwen-image2.1巨物专用（支持文生、角色参考图生）多模式通用_2106719510433714177.json, 图片生成/文生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2109232941795733506.json, 图片生成/文生图/Qwen-image2.1+Vosr2+DLSS5角色定妆照（文生_图生）_2109237495685799937.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwein-image2.1分镜专用空镜（有人、无人）_2111716013799731201.json、图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5图像反推_2111665215556378626.json、图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5影楼写真九宫格_2111712714950270978.json、图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5网红打卡旅游九宫格_2111702701032689666.json、图片生成/图生图/Qwen-image2.1+Vosr2+DLSS5角色定妆五视图_2104088591185039361.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ClownsharKSampler_Beta`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveStringMultiline`
- `QwenImage21SageAttentionT8`
- `RH_Screenwriter`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WujiImagePrompt`
- `WujiPromptEditor`
- `WujiUpscaler2`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 3/10 个有
- `ImageScaleToTotalPixels` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `AutoCropFaces` —— 2/10 个有
- `Image Comparer (rgthree)` —— 1/10 个有
- `WujiCleaner` —— 1/10 个有
- `easy imageSize` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | bong_tangent | - | 10 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 10 | 100% |
| 采样算法 | -1 | -1 - -1 | 10 | 100% |
| 调度器 | 1 | 1 - 1 | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 1560 | 1024 - 1560 | 3 | 82% |
| 高度 | 904 | 904 - 1024 | 3 | 94% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 bong_tangent，10 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，10 个样本，取值集中（一致性 100%）
- 采样算法 中位数 -1，观测区间 -1 - -1，10 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 1560，观测区间 1024 - 1560，3 个样本，取值集中（一致性 82%）
- 高度 中位数 904，观测区间 904 - 1024，3 个样本，取值集中（一致性 94%）
