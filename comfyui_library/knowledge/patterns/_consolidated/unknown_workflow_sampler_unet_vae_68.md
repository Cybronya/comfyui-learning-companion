---
name: unknown_workflow_sampler_unet_vae_68
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.862167
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen2.1文生图_2101145781234397185.json, 图片生成/文生图/Qwen_Image_文生图_2102957010739351554.json, 图片生成/文生图/Qwen_image_2.1_文生_2101705296098971649.json, 图片生成/文生图/qwen-image 2.1文生图_2101776581311156225.json, 图片生成/文生图/qwen-image-2.1：官方原版文生图像_2101680006563975169.json, 图片生成/文生图/qwen_image2.文生图_2101942968000278530.json, 图片生成/文生图/qwen_image_2.1 _ 文生图_2103128462868443138.json, 图片生成/文生图/qwen_image_2_1_t2i_2101938471274369025.json, 图片生成/文生图/qwen_image_2_1_文生图_2101842315596886018.json, 图片生成/文生图/qwen_image_2_1文生图_2101884688183947265.json, 图片生成/文生图/【遇见AI】qwen image 2.1文生图基础流_2101841432792363010.json, 视频生成/文生视频/Qwen_image_2.1_文生图_2104447797318733826.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_68

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/Qwen2.1文生图_2101145781234397185.json、图片生成/文生图/Qwen_Image_文生图_2102957010739351554.json、图片生成/文生图/Qwen_image_2.1_文生_2101705296098971649.json、图片生成/文生图/qwen-image 2.1文生图_2101776581311156225.json、图片生成/文生图/qwen-image-2.1：官方原版文生图像_2101680006563975169.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImage21` —— 11/12 个有
- `SaveImageAdvanced` —— 3/12 个有
- `EmptyImage` —— 2/12 个有
- `JjkText` —— 2/12 个有
- `PreviewImage` —— 2/12 个有
- `ConditioningZeroOut` —— 1/12 个有
- `LoadImage` —— 1/12 个有
- `TextEncodeQwenImageEditPlus` —— 1/12 个有
- `TextGenerateLTX2Prompt` —— 1/12 个有
- `easy showAnything` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 12 | 100% |
| 高度 | 1024 | 1024 - 1024 | 12 | 100% |
| 采样步数 | 25 | 25 - 50 | 12 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，12 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 50，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
