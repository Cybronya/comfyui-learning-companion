---
name: unknown_workflow_sampler_unet_vae_41
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.838467
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/QWen2.1文生图基础版_2114665364100571138.json, 图片生成/文生图/Qwen Image 2.1 文生图 25步官流_2101767103564050433.json, 图片生成/文生图/Qwen Image 2.1 文生图标准版_2104437986099294209.json, 图片生成/文生图/Qwen Image 2.1-文生图_2101855895343951873.json, 图片生成/文生图/Qwen Image 2.1文生图_2101560854905970690.json, 图片生成/文生图/Qwen Image 2.1：文生图_2104089249137119233.json, 图片生成/文生图/Qwen Image2.1文生图2609_2106041124522643458.json, 图片生成/文生图/Qwen image 2.1 文生图_2101857655588474882.json, 图片生成/文生图/Qwen-Image-2.1 ComfyUI 原生工作流示例_2101898468049645569.json, 图片生成/文生图/Qwen-Image-2.1 文生图_2102343034200477698.json, 图片生成/文生图/Qwen-Image-2.1 文生图_2102996517320740865.json, 图片生成/文生图/Qwen_Image_2.1文生图_2108748004588085250.json, 图片生成/文生图/Qwen_Image_2.1文生图_2110292134430593026.json, 图片生成/文生图/Y_qwen_image_2.1_t2i_2108495280059535362.json, 图片生成/文生图/qwen image2.1 单图_文生图工作流_2101896635692437505.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_41

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/QWen2.1文生图基础版_2114665364100571138.json、图片生成/文生图/Qwen Image 2.1 文生图 25步官流_2101767103564050433.json、图片生成/文生图/Qwen Image 2.1 文生图标准版_2104437986099294209.json、图片生成/文生图/Qwen Image 2.1-文生图_2101855895343951873.json、图片生成/文生图/Qwen Image 2.1文生图_2101560854905970690.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 14/15 个有
- `SaveImageAdvanced` —— 8/15 个有
- `PrimitiveStringMultiline` —— 7/15 个有
- `ModelAttentionBackend` —— 4/15 个有
- `CR Prompt Text` —— 2/15 个有
- `QwenImage21Cache` —— 2/15 个有
- `Text Multiline` —— 2/15 个有
- `Fast Groups Bypasser (rgthree)` —— 1/15 个有
- `GetImageSize` —— 1/15 个有
- `LoadImage` —— 1/15 个有
- `PrimitiveInt` —— 1/15 个有
- `easy seed` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 15 | 100% |
| 高度 | 1024 | 1024 - 1536 | 15 | 88% |
| 采样步数 | 25 | 25 - 50 | 15 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，15 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1536，15 个样本，取值集中（一致性 88%）
- 采样步数 中位数 25，观测区间 25 - 50，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
