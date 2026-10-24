---
name: unknown_workflow_sampler_unet_vae_29
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.768647
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 2.1 文生图标准版_2104437986099294209.json, 图片生成/文生图/Qwen Image 2.1 标准文生图工作流_2101851852332687361.json, 图片生成/文生图/Qwen Image 2.1-文生图_2101855895343951873.json, 图片生成/文生图/Qwen Image 2.1文生图_2101560854905970690.json, 图片生成/文生图/Qwen Image 2.1文生图_2101902260690313218.json, 图片生成/文生图/Qwen Image 2.1透明图层+文生图！_2101836586576072706.json, 图片生成/文生图/Qwen Image 2.1：文生图_2104089249137119233.json, 图片生成/文生图/Qwen image 2.1 文生图_2101857655588474882.json, 图片生成/文生图/Qwen-Image-2.1 ComfyUI 原生工作流示例_2101898468049645569.json, 图片生成/文生图/Qwen-Image-2.1 文生图_2102343034200477698.json, 图片生成/文生图/Qwen-Image-2.1 文生图_2102996517320740865.json, 图片生成/文生图/Qwen-Image-2.1透明图层（文生图）_2109536947332014082.json, 图片生成/文生图/Qwen-image2.1文生图工作流_2101888147331305473.json, 图片生成/文生图/Qwen2.1_BF16_文生图官方工作流_2101860361765998594.json, 图片生成/文生图/Qwen_Image2.1_文生图-提示词增强_2101869061239033857.json, 图片生成/文生图/image_qwen_image_2_1_t2i_2101968376938717186.json, 图片生成/文生图/【qwen_image_2.1】文生图 角色资料卡_2109474485958172674.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_29

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/Qwen Image 2.1 文生图标准版_2104437986099294209.json、图片生成/文生图/Qwen Image 2.1 标准文生图工作流_2101851852332687361.json、图片生成/文生图/Qwen Image 2.1-文生图_2101855895343951873.json、图片生成/文生图/Qwen Image 2.1文生图_2101560854905970690.json、图片生成/文生图/Qwen Image 2.1文生图_2101902260690313218.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 16/17 个有
- `SaveImageAdvanced` —— 8/17 个有
- `PrimitiveStringMultiline` —— 7/17 个有
- `JjkText` —— 4/17 个有
- `PreviewAny` —— 4/17 个有
- `孤海注释` —— 3/17 个有
- `ModelAttentionBackend` —— 2/17 个有
- `TextGenerate` —— 2/17 个有
- `TextGenerateLTX2Prompt` —— 2/17 个有
- `CR Prompt Text` —— 1/17 个有
- `QwenImage21Cache` —— 1/17 个有
- `StringConcatenate` —— 1/17 个有
- `忽略多组孤海` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | 8 - 60 | 17 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 17 | 100% |
| 采样算法 | euler | - | 17 | 100% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 1024 | 1024 - 1600 | 17 | 87% |
| 高度 | 1024 | 1024 - 2000 | 17 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 35，观测区间 8 - 60，17 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，17 个样本，一致性 100%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1600，17 个样本，取值集中（一致性 87%）
- 高度 中位数 1024，观测区间 1024 - 2000，17 个样本
