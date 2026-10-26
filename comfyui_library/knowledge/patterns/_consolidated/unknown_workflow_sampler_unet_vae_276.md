---
name: unknown_workflow_sampler_unet_vae_276
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.642667
common_nodes: [CLIPLoader, ComfyMathExpression, EmptyLatentImage, GetImageSizeAndCount, GetNode, KSampler, LoadImage, PreviewImage, PrimitiveFloat, QwenImage21Cache, ResolutionSelector, SaveImage, SetNode, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [图片生成/图生图/QwenImage2.1 Anything2Realism 任意风格转写实图像生成工作流_2108143936509399042.json, 图片生成/图生图/QwenImage2.1_Anything2Realism_任意风格转写实图像生成工作流_2112740345166524417.json, 图片生成/文生图/QwenImg_2.1 图像编辑+二次采样放大工作流（去提示词增强精简版）_2103134812553961474.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_276

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/QwenImage2.1 Anything2Realism 任意风格转写实图像生成工作流_2108143936509399042.json、图片生成/图生图/QwenImage2.1_Anything2Realism_任意风格转写实图像生成工作流_2112740345166524417.json、图片生成/文生图/QwenImg_2.1 图像编辑+二次采样放大工作流（去提示词增强精简版）_2103134812553961474.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetImageSizeAndCount`
- `GetNode`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `PrimitiveFloat`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/3 个有
- `Load Image From Url (mtb)` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `RH_DLSS5Enhance` —— 2/3 个有
- `Label (rgthree)` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `Textbox` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 25 | 25 - 30 | 3 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 0 - 1 | 3 | 29% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 30，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0 - 1，3 个样本，取值分散，一致性仅 29%
- 风险：重绘幅度 观测到 0，低于常用下限 0.1（）
