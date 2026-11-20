---
name: unknown_workflow_upscale_sampler_unet_5
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.819286
common_nodes: [CLIPLoader, CR Prompt Text, Fast Groups Bypasser (rgthree), INTConstant, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, PreviewImage, QwenImage21Cache, QwenPERewriteT8, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/qwen image2.1 加速版三图图生图_2108114179877068802.json, 图片生成/图生图/qwen image2.1 加速版单图生图（90秒出图）_2108082938335289346.json, 图片生成/图生图/qwen image2.1 加速版双图图生图_2108108729798455297.json, 图片生成/图生图/qwen_image2.1_加速版单图生图90秒出图_2112719052429938689.json, 图片生成/文生图/qwen image2.1加速版文生图（90秒出图）_2108080480087269377.json, 图片生成/文生图/qwen_image2.1加速版文生图90秒出图_2112439839751753729.json, 图片生成/文生图/文生图-qwen image2.1-t8pe加速版_2106329151098671105.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_5

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/qwen image2.1 加速版三图图生图_2108114179877068802.json、图片生成/图生图/qwen image2.1 加速版单图生图（90秒出图）_2108082938335289346.json、图片生成/图生图/qwen image2.1 加速版双图图生图_2108108729798455297.json、图片生成/图生图/qwen_image2.1_加速版单图生图90秒出图_2112719052429938689.json、图片生成/文生图/qwen image2.1加速版文生图（90秒出图）_2108080480087269377.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `PreviewImage`
- `QwenImage21Cache`
- `QwenPERewriteT8`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/7 个有
- `ResizeAndPadImage` —— 4/7 个有
- `EmptyLatentImage` —— 3/7 个有
- `ComfySwitchNode` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 40 - 40 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 40 - 40，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
