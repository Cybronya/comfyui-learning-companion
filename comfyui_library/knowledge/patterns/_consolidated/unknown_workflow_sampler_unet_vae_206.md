---
name: unknown_workflow_sampler_unet_vae_206
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.810571
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, ResolutionSelector, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Qwen_Image_2.1_文生图_纯净官流40步无PE_2107976735823323137.json, 图片生成/文生图/Qwen_Image_2.1文生图_2108748004588085250.json, 图片生成/文生图/Qwen_Image_2.1文生图_2110292134430593026.json, 图片生成/文生图/Qwen_Image_文生图_2102957010739351554.json, 图片生成/文生图/Qwen_image_2.1_文生_2101705296098971649.json, 图片生成/文生图/Y_qwen_image_2.1_t2i_2108495280059535362.json, 图片生成/文生图/qwen image2.1 单图_文生图工作流_2101896635692437505.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_206

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Qwen_Image_2.1_文生图_纯净官流40步无PE_2107976735823323137.json、图片生成/文生图/Qwen_Image_2.1文生图_2108748004588085250.json、图片生成/文生图/Qwen_Image_2.1文生图_2110292134430593026.json、图片生成/文生图/Qwen_Image_文生图_2102957010739351554.json、图片生成/文生图/Qwen_image_2.1_文生_2101705296098971649.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 5/7 个有
- `ModelAttentionBackend` —— 3/7 个有
- `SaveImageAdvanced` —— 3/7 个有
- `EmptyImage` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `QwenImage21Cache` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 40 | 25 - 45 | 7 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 7 | 100% |
| 高度 | 1024 | 1024 - 1024 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 40，观测区间 25 - 45，7 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，7 个样本，取值集中（一致性 100%）
