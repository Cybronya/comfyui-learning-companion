---
name: unknown_workflow_upscale_sampler_unet_3
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.8205
common_nodes: [CLIPLoader, Fast Groups Bypasser (rgthree), INTConstant, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, PreviewImage, QwenImage21Cache, ResolutionSelector, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/qwen image2.1 加速版三图图生图_2108114179877068802.json, 图片生成/图生图/qwen image2.1 加速版单图生图（90秒出图）_2108082938335289346.json, 图片生成/图生图/qwen image2.1 加速版双图图生图_2108108729798455297.json, 图片生成/图生图/qwen_image2.1_加速版单图生图90秒出图_2112719052429938689.json, 图片生成/图生图/qwen_image2.1_加速版单图生图90秒出图_2114998186719932417.json, 图片生成/图生图/角色三视图_Qwen_image_2.1_2116667200378593281.json, 图片生成/文生图/qwen image2.1加速版文生图（90秒出图）_2108080480087269377.json, 图片生成/文生图/qwen_image2.1加速版文生图90秒出图_2112439839751753729.json, 图片生成/文生图/qwen_image2.1加速版文生图90秒出图_2114998535027511298.json, 图片生成/文生图/文生图-qwen image2.1-t8pe加速版_2106329151098671105.json, 图片生成/文生图/文生图-qwen_image2.1-t8pe加速版_2116696483385921537.json, 平台全量/角色三视图_Qwen_image_2.1_2117471005680693250.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_3

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/qwen image2.1 加速版三图图生图_2108114179877068802.json、图片生成/图生图/qwen image2.1 加速版单图生图（90秒出图）_2108082938335289346.json、图片生成/图生图/qwen image2.1 加速版双图图生图_2108108729798455297.json、图片生成/图生图/qwen_image2.1_加速版单图生图90秒出图_2112719052429938689.json、图片生成/图生图/qwen_image2.1_加速版单图生图90秒出图_2114998186719932417.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `PreviewImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 10/12 个有
- `QwenPERewriteT8` —— 10/12 个有
- `easy cleanGpuUsed` —— 10/12 个有
- `LoadImage` —— 7/12 个有
- `EmptyLatentImage` —— 5/12 个有
- `ResizeAndPadImage` —— 5/12 个有
- `ComfySwitchNode` —— 2/12 个有
- `EmptyFlux2LatentImage` —— 2/12 个有
- `easy showAnything` —— 2/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 25 - 40 | 12 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 25 - 40，12 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
