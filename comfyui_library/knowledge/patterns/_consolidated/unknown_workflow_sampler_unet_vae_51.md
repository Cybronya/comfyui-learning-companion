---
name: unknown_workflow_sampler_unet_vae_51
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.781071
common_nodes: [CLIPLoader, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen image2.1-多功能图像编辑_2104767444010225665.json, 图片生成/图生图/Qwen-Image-2.1 图片编辑总控_2101868365479497729.json, 图片生成/图生图/Qwen-Image2.1 角色资产4格详图+SEEDVR2放大_2112370809275768834.json, 图片生成/图生图/Qwen-Image2.1 角色资产三视图生成_2112411740599308289.json, 图片生成/图生图/Qwen-image21-图像编辑_2103256220042874881.json, 图片生成/图生图/qwen image2.1 加速版三图图生图_2108114179877068802.json, 图片生成/图生图/qwen image2.1 加速版单图生图（90秒出图）_2108082938335289346.json, 图片生成/图生图/qwen image2.1 加速版双图图生图_2108108729798455297.json, 图片生成/图生图/qwen_image2.1_加速版单图生图90秒出图_2112719052429938689.json, 图片生成/图生图/【AI军火商】全网最强角色资产4格详图制作【Qwen-Image2.1】_2108004428056973313.json, 图片生成/图生图/角色资产4格详图制作【Qwen-Image2.1】_2107476393411039233.json, 图片生成/文生图/qwen image2.1加速版文生图（90秒出图）_2108080480087269377.json, 图片生成/文生图/qwen_image2.1加速版文生图90秒出图_2112439839751753729.json, 图片生成/文生图/文生图-qwen image2.1-t8pe加速版_2106329151098671105.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_51

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen image2.1-多功能图像编辑_2104767444010225665.json、图片生成/图生图/Qwen-Image-2.1 图片编辑总控_2101868365479497729.json、图片生成/图生图/Qwen-Image2.1 角色资产4格详图+SEEDVR2放大_2112370809275768834.json、图片生成/图生图/Qwen-Image2.1 角色资产三视图生成_2112411740599308289.json、图片生成/图生图/Qwen-image21-图像编辑_2103256220042874881.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 13/14 个有
- `QwenImage21Cache` —— 13/14 个有
- `LoadImage` —— 11/14 个有
- `PreviewImage` —— 11/14 个有
- `SeedVR2LoadDiTModel` —— 11/14 个有
- `SeedVR2LoadVAEModel` —— 11/14 个有
- `SeedVR2VideoUpscaler` —— 11/14 个有
- `EmptyLatentImage` —— 10/14 个有
- `CR Prompt Text` —— 8/14 个有
- `ComfySwitchNode` —— 8/14 个有
- `INTConstant` —— 7/14 个有
- `QwenPERewriteT8` —— 7/14 个有
- `easy cleanGpuUsed` —— 7/14 个有
- `PrimitiveStringMultiline` —— 5/14 个有
- `ResizeAndPadImage` —— 4/14 个有
- `PrimitiveBoolean` —— 3/14 个有
- `Label (rgthree)` —— 2/14 个有
- `LoraLoaderModelOnly` —— 2/14 个有
- `Seed (rgthree)` —— 2/14 个有
- `孤海注释` —— 2/14 个有
- `easy showAnything` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 10 | 100% |
| 高度 | 1024 | 1024 - 1024 | 10 | 100% |
| 采样步数 | 40 | 25 - 40 | 14 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，10 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 25 - 40，14 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
