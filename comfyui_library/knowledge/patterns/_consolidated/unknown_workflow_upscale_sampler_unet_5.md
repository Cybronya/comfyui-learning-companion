---
name: unknown_workflow_upscale_sampler_unet_5
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.9054
common_nodes: [CLIPLoader, CR Text, CR Text Concatenate, EmptyLatentImage, ImageScale, KSampler, PreviewImage, QZ_ResolutionPreset, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMathDual+, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy seed]
problems: []
missing: []
members: [图片生成/文生图/Qwen-Image-2.1_场景4K_2102075769441841154.json, 图片生成/文生图/Qwen-Image-2.1_场景4K_2102318498000236546.json, 图片生成/文生图/Qwen-Image-2.1_场景4K_2104846279191908354.json, 图片生成/文生图/Qwen-Image-2.1_场景4K_2104852149804036097.json, 图片生成/文生图/Qwen-Image-2.1_场景4K_2104856521967493121.json, 图片生成/文生图/Qwen-Image-2.1_场景4K_2105190125805334530.json, 图片生成/文生图/Qwen-Image-2.1_场景4K_2105192484572844034.json, 图片生成/文生图/Qwen-Image-2.1_场景4K_2108027574453628929.json, 图片生成/文生图/Qwen-Image-2.1_场景4K_2114994148393709570.json, 平台全量/Qwen-Image-2.1_场景4K_2117443046194368514.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_5

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Qwen-Image-2.1_场景4K_2102075769441841154.json、图片生成/文生图/Qwen-Image-2.1_场景4K_2102318498000236546.json、图片生成/文生图/Qwen-Image-2.1_场景4K_2104846279191908354.json、图片生成/文生图/Qwen-Image-2.1_场景4K_2104852149804036097.json、图片生成/文生图/Qwen-Image-2.1_场景4K_2104856521967493121.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `CR Text Concatenate`
- `EmptyLatentImage`
- `ImageScale`
- `KSampler`
- `PreviewImage`
- `QZ_ResolutionPreset`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMathDual+`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 2048 | 2048 - 2048 | 10 | 100% |
| 高度 | 1152 | 1152 - 1152 | 10 | 100% |
| 采样步数 | 25 | 25 - 25 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 2048，观测区间 2048 - 2048，10 个样本，取值集中（一致性 100%）
- 高度 中位数 1152，观测区间 1152 - 1152，10 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
