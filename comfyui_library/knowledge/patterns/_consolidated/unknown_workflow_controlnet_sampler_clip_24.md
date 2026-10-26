---
name: unknown_workflow_controlnet_sampler_clip_24
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.872333
common_nodes: [AIO_Preprocessor, CR Apply ControlNet, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetLoader, DeepTranslatorCLIPTextEncodeNode, EmptyLatentImage, ImageConcanate, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/冬季阁楼变换夏季_1926070547745034241.json, 图片生成/图生图/夏季风景变换成冬季_1926074170881576961.json, 图片生成/图生图/真人转动漫_1926077741802672130.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_24

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/冬季阁楼变换夏季_1926070547745034241.json、图片生成/图生图/夏季风景变换成冬季_1926074170881576961.json、图片生成/图生图/真人转动漫_1926077741802672130.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CR Apply ControlNet`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetLoader`
- `DeepTranslatorCLIPTextEncodeNode`
- `EmptyLatentImage`
- `ImageConcanate`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `VAELoader` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 3 | 100% |
| 采样算法 | dpmpp_2m | - | 3 | 100% |
| 调度器 | karras | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1536 | 1536 - 1536 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，3 个样本，取值集中（一致性 100%）
