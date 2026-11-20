---
name: unknown_workflow_sampler_clip_unet_458
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.86
common_nodes: [CLIPTextEncode, DualCLIPLoader, KSampler, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/【琉梦】最强二次元_动漫 文生图 + 简易工作流 + Newbie Image模型 + 快速出图_2016462546584215553.json, 图片生成/文生图/【老金驿站】8B模型Flex2文生图局部重绘Controlnet出图_1917456073752510466.json, 平台全量/ControlNet通用-Flex.2-preview_1917163629534449665.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_458

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/【琉梦】最强二次元_动漫 文生图 + 简易工作流 + Newbie Image模型 + 快速出图_2016462546584215553.json、图片生成/文生图/【老金驿站】8B模型Flex2文生图局部重绘Controlnet出图_1917456073752510466.json、平台全量/ControlNet通用-Flex.2-preview_1917163629534449665.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `Flex2Conditioner` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `DepthAnythingPreprocessor` —— 1/3 个有
- `Fast Groups Muter (rgthree)` —— 1/3 个有
- `FlexLoraLoaderModelOnly` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `RescaleCFG` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 28 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 3 | 24% |
| 采样算法 | res_multistep | - | 3 | 33% |
| 调度器 | linear_quadratic | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 28，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 res_multistep，3 个样本，一致性 33%
- 调度器 最常用 linear_quadratic，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
