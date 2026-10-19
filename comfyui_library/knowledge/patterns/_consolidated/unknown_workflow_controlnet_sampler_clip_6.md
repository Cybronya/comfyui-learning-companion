---
name: unknown_workflow_controlnet_sampler_clip_6
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6625
common_nodes: [ApplyFluxControlNet, CLIPTextEncodeFlux, DepthAnythingV2Preprocessor, DualCLIPLoader, EmptyLatentImage, LoadFluxControlNet, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, XlabsSampler]
problems: []
missing: []
members: [图片生成/文生图/F.1 _ Canny _ 深度 _ HED _ Lora_1890346105614553089.json, 图片生成/文生图/真人转动漫二次元手绘插画_1891797919912341506.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/F.1 _ Canny _ 深度 _ HED _ Lora_1890346105614553089.json、图片生成/文生图/真人转动漫二次元手绘插画_1891797919912341506.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFluxControlNet`
- `CLIPTextEncodeFlux`
- `DepthAnythingV2Preprocessor`
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
- `CannyEdgePreprocessor` —— 1/2 个有
- `HEDPreprocessor` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 896 | - | 2 | 86% |
| 高度 | 1024 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 896，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
