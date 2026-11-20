---
name: unknown_workflow_controlnet_sampler_clip_28
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8605
common_nodes: [ApplyFluxControlNet, CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, ImageResize+, Joy_caption, Joy_caption_load, LoadFluxControlNet, LoadImage, PreviewImage, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, XlabsSampler]
problems: []
missing: []
members: [图片生成/反推提示词/FLUX JoyTag 反推渲染工作流_1826100835008057346.json, 图片生成/图生图/复刻万物 FLux+Joy_caption+depthV3_1834626407057223681.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/FLUX JoyTag 反推渲染工作流_1826100835008057346.json、图片生成/图生图/复刻万物 FLux+Joy_caption+depthV3_1834626407057223681.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFluxControlNet`
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `ImageResize+`
- `Joy_caption`
- `Joy_caption_load`
- `LoadFluxControlNet`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `XlabsSampler`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `GetImageSize+` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `LeReS-DepthMapPreprocessor` —— 1/2 个有
- `VAEEncode` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 768 | - | 2 | 67% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
