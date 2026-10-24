---
name: unknown_workflow_sampler_unet_vae_160
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.703333
common_nodes: [CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, PrimitiveStringMultiline, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2102265363466645506.json, 图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2104043025541459969.json, 图片生成/图生图/Minimax H3 人像参考图专用生成器_2112535531715391490.json, 图片生成/图生图/qwen_image_2.1_图编辑_2104046121885720577.json, 图片生成/图生图/qwen_image_2_1_图像编辑-文本换装_2104452144555450369.json, 图片生成/图生图/qwen_image_2_1_手持指定物品_2104438895411818497.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_160

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2102265363466645506.json、图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2104043025541459969.json、图片生成/图生图/Minimax H3 人像参考图专用生成器_2112535531715391490.json、图片生成/图生图/qwen_image_2.1_图编辑_2104046121885720577.json、图片生成/图生图/qwen_image_2_1_图像编辑-文本换装_2104452144555450369.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `EmptyImage` —— 4/6 个有
- `GetNode` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `SeedVR2LoadDiTModel` —— 1/6 个有
- `SeedVR2LoadVAEModel` —— 1/6 个有
- `SeedVR2VideoUpscaler` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 32.5 | 20 - 40 | 6 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 32.5，观测区间 20 - 40，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
