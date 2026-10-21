---
name: unknown_workflow_video_lora_sampler_660
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.537667
common_nodes: [CLIPLoader, CLIPTextEncode, DiffusionModelLoaderKJ, DiffusionModelSelector, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, ImageBatchMulti, ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, MaskPreview, MathExpression|pysssss, ModelSamplingSD3, PreviewImage, SetNode, TrimVideoLatent, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame, easy forLoopEnd, easy forLoopStart, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1983372948306337793.json, 视频生成/图生视频/1990992913704394754.json, 视频生成/图生视频/1989490999061827585.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_660

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1983372948306337793.json、视频生成/图生视频/1990992913704394754.json、视频生成/图生视频/1989490999061827585.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `DiffusionModelLoaderKJ`
- `DiffusionModelSelector`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PreviewImage`
- `SetNode`
- `TrimVideoLatent`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 2/3 个有
- `Label (rgthree)` —— 2/3 个有
- `Int` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | lcm | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 lcm，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
