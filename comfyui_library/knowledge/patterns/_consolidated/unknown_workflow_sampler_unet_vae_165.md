---
name: unknown_workflow_sampler_unet_vae_165
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.857
common_nodes: [AIO_Preprocessor, CLIPLoader, ComfySwitchNode, EmptyLatentImage, GetImageSize, ImageResizeKJv2, ImageScaleBy, KSampler, Label (rgthree), LoadImage, PreviewImage, QwenImage21Cache, QwenImage21UnionApply, QwenImage21UnionLoader, ResizeImageMaskNode, ResolutionSelector, SaveImage, SeedNode, TextEncodeQwenImage21, Textbox, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen_Image_2.1_CONTROLNET 图像编辑工作流_2104411934979346434.json, 图片生成/文生图/Qwen_Image_2.1_CONTROLNET 图像编辑工作流_2104595395056852994.json, 图片生成/文生图/Qwen_Image_2.1_CONTROLNET 图像编辑工作流_2104885905218691074.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_165

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen_Image_2.1_CONTROLNET 图像编辑工作流_2104411934979346434.json、图片生成/文生图/Qwen_Image_2.1_CONTROLNET 图像编辑工作流_2104595395056852994.json、图片生成/文生图/Qwen_Image_2.1_CONTROLNET 图像编辑工作流_2104885905218691074.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `GetImageSize`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSampler`
- `Label (rgthree)`
- `LoadImage`
- `PreviewImage`
- `QwenImage21Cache`
- `QwenImage21UnionApply`
- `QwenImage21UnionLoader`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveImage`
- `SeedNode`
- `TextEncodeQwenImage21`
- `Textbox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |
| 采样步数 | 40 | 40 - 40 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 40，观测区间 40 - 40，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
