---
name: unknown_workflow_sampler_unet_vae_117
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8007
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image 2.1 人物换脸_2110662194005372929.json, 图片生成/图生图/Qwen image 2.1 人物替换 _ 姿势复刻_2109882087112269826.json, 图片生成/图生图/Qwen image 2.1 换装_2109875920243871745.json, 图片生成/图生图/Qwen image2.1  换头（注释内有模型和lora下载链接）_2111046058527780865.json, 图片生成/图生图/Qwen image2.1-多功能图像编辑_2104767444010225665.json, 图片生成/图生图/Qwen-image21-图像编辑_2103256220042874881.json, 图片生成/图生图/QwenImage2.1 千问图像2.1 任意姿态生成_2103489835767001089.json, 图片生成/图生图/QwenImage2.1图像编辑_2101863711043579906.json, 图片生成/图生图/QwenImage2.1图像编辑_2114889444028403714.json, 图片生成/图生图/▶Qwen-image21-图像编辑（无位移）_2112039096406331394.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_117

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1 人物换脸_2110662194005372929.json、图片生成/图生图/Qwen image 2.1 人物替换 _ 姿势复刻_2109882087112269826.json、图片生成/图生图/Qwen image 2.1 换装_2109875920243871745.json、图片生成/图生图/Qwen image2.1  换头（注释内有模型和lora下载链接）_2111046058527780865.json、图片生成/图生图/Qwen image2.1-多功能图像编辑_2104767444010225665.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `QwenImage21Cache` —— 9/10 个有
- `Image Comparer (rgthree)` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `ImageScaleToTotalPixels` —— 6/10 个有
- `LoraLoaderModelOnly` —— 6/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `Seed (rgthree)` —— 6/10 个有
- `CR Text` —— 3/10 个有
- `ImageConcanate` —— 3/10 个有
- `Latent Switch (JPS)` —— 3/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `easy loraStack` —— 3/10 个有
- `easy loraStackApply` —— 3/10 个有
- `Label (rgthree)` —— 2/10 个有
- `PreviewImage` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 10 | 100% |
| 高度 | 1024 | 1024 - 1024 | 10 | 100% |
| 采样步数 | 25 | 8 - 30 | 10 | 52% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，10 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 8 - 30，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
