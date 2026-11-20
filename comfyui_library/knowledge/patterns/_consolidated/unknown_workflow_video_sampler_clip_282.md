---
name: unknown_workflow_video_sampler_clip_282
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.887
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, EmptyHunyuanLatentVideo, Florence2ModelLoader, Florence2Run, FluxGuidance, GetImageSizeAndCount, HunyuanImageToVideo, ImageBatch, ImageFromBatch, KSamplerSelect, MathExpression|pysssss, ModelSamplingSD3, PreviewImage, RandomNoise, SamplerCustomAdvanced, ShowText|pysssss, String, Text Concatenate, Text Find and Replace, TextEncodeHunyuanVideo_ImageToVideo, TextInput_, UNETLoader, VAEDecode, VAEDecodeTiled, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/文生视频/HunYuan_无限时长工作流_文生视频+图生视频(10秒)_1905235717641916417.json, 视频生成/文生视频/HunYuan_无限时长工作流_文生视频+图生视频(10秒)_1905625750312259585.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_282

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/HunYuan_无限时长工作流_文生视频+图生视频(10秒)_1905235717641916417.json、视频生成/文生视频/HunYuan_无限时长工作流_文生视频+图生视频(10秒)_1905625750312259585.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `EmptyHunyuanLatentVideo`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSizeAndCount`
- `HunyuanImageToVideo`
- `ImageBatch`
- `ImageFromBatch`
- `KSamplerSelect`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ShowText|pysssss`
- `String`
- `Text Concatenate`
- `Text Find and Replace`
- `TextEncodeHunyuanVideo_ImageToVideo`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `SaveAnimatedWEBP` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
