---
name: unknown_workflow_sampler_unet_vae_236
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.7075
common_nodes: [BatchImagesNode, CLIPLoader, ComfySwitchNode, EmptyLatentImage, KSampler, LoadImage, PreviewAny, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1 多图编辑_2104447345671888898.json, 图片生成/图生图/Qwen Image 2.1图片透明分层！ 生成透明图层！艾橘溪_2102196823371898882.json, 图片生成/图生图/Qwen image 2.1 多图编辑_2101841037932191746.json, 图片生成/文生图/qwen-image2.1合集 文生图_单_多图编辑+提示词增强_1938466701136560129.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_236

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 多图编辑_2104447345671888898.json、图片生成/图生图/Qwen Image 2.1图片透明分层！ 生成透明图层！艾橘溪_2102196823371898882.json、图片生成/图生图/Qwen image 2.1 多图编辑_2101841037932191746.json、图片生成/文生图/qwen-image2.1合集 文生图_单_多图编辑+提示词增强_1938466701136560129.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 4 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PreviewAny`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `Latent Switch (JPS)` —— 2/4 个有
- `RH_Translator` —— 2/4 个有
- `GetNode` —— 1/4 个有
- `PrimitiveBoolean` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `SaveImageAdvanced` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `TextCombinerSix` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 50 | 25 - 50 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 50，观测区间 25 - 50，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
