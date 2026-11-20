---
name: unknown_workflow_controlnet_sampler_clip_23
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.725
common_nodes: [ApplyFluxControlNet, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, LoadFluxControlNet, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, XlabsSampler]
problems: []
missing: []
members: [图片生成/图生图/中文字体设计工作流flux_1954934845668409345.json, 图片生成/文生图/F.1 _ Canny _ 深度 _ HED _ Lora_1890346105614553089.json, 图片生成/文生图/真人转动漫二次元手绘插画_1891797919912341506.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_23

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/中文字体设计工作流flux_1954934845668409345.json、图片生成/文生图/F.1 _ Canny _ 深度 _ HED _ Lora_1890346105614553089.json、图片生成/文生图/真人转动漫二次元手绘插画_1891797919912341506.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `ApplyFluxControlNet`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `LoadFluxControlNet`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `XlabsSampler`

**可变部分**（部分 workflow 才有）：
- `CannyEdgePreprocessor` —— 2/3 个有
- `DepthAnythingV2Preprocessor` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `DF_Text_Box` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `HEDPreprocessor` —— 1/3 个有
- `LoraLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1024 | 3 | 73% |
| 高度 | 1024 | 512 - 1024 | 3 | 72% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1024，3 个样本
- 高度 中位数 1024，观测区间 512 - 1024，3 个样本
