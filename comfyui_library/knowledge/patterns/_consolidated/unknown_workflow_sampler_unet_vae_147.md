---
name: unknown_workflow_sampler_unet_vae_147
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.649
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2102265363466645506.json, 图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2104043025541459969.json, 图片生成/图生图/QWEN IMAGE 2.1 图生图工作流，图片编辑 (带模型下载链接)_2103073592752820226.json, 图片生成/图生图/Qwen Image 2.1 元素移除_2101986892471431170.json, 图片生成/图生图/Qwen Image 2.1 扩图_2101987076421021697.json, 图片生成/图生图/Qwen Image 2.1 扩图_2102016833665724417.json, 图片生成/图生图/Qwen Image 2.1 扩图工作流_2102621542323675137.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_147

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2102265363466645506.json、图片生成/图生图/Fenglairh-Qwen_Image_2.1图像编辑_2104043025541459969.json、图片生成/图生图/QWEN IMAGE 2.1 图生图工作流，图片编辑 (带模型下载链接)_2103073592752820226.json、图片生成/图生图/Qwen Image 2.1 元素移除_2101986892471431170.json、图片生成/图生图/Qwen Image 2.1 扩图_2101987076421021697.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `PreviewImage` —— 5/7 个有
- `SaveImageAdvanced` —— 5/7 个有
- `DrawMaskOnImage` —— 4/7 个有
- `ResizeImageMaskNode` —— 4/7 个有
- `ComfySwitchNode` —— 3/7 个有
- `GetImageSize` —— 3/7 个有
- `ImagePadForOutpaint` —— 3/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `EmptyImage` —— 1/7 个有
- `GrowMaskWithBlur` —— 1/7 个有
- `ResizeMask` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 50 | 25 - 50 | 7 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 50，观测区间 25 - 50，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
