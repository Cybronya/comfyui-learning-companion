---
name: unknown_workflow_video_sampler_clip_85
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.796
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ColorMatch, ImageResizeKJv2, ImageScaleBy, KSamplerAdvanced, ModelSamplingSD3, Pick From Batch (mtb), PreviewImage, PrimitiveStringMultiline, RIFE VFI, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2006660938727952385.json, 视频生成/图生视频/1983333336628273153.json, 视频生成/图生视频/1999362041401966593.json, 视频生成/图生视频/2001138959705047042.json, 视频生成/图生视频/1976151444560707585.json, 视频生成/图生视频/2010551165288714241.json, 视频生成/图生视频/2010540373155782658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_85

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2006660938727952385.json、视频生成/图生视频/1983333336628273153.json、视频生成/图生视频/1999362041401966593.json、视频生成/图生视频/2001138959705047042.json、视频生成/图生视频/1976151444560707585.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ColorMatch`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RIFE VFI`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 6/7 个有
- `JWInteger` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `StringConcatenate` —— 6/7 个有
- `UnetLoaderGGUF` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/7 个有
- `mxSlider2D` —— 3/7 个有
- `ModelPatchTorchSettings` —— 2/7 个有
- `PathchSageAttentionKJ` —— 2/7 个有
- `RH_LLMAPI_NODE` —— 2/7 个有
- `Bjornulf_ShowInt` —— 1/7 个有
- `CR Text List To String` —— 1/7 个有
- `Qwen3_VQA` —— 1/7 个有
- `RHBatchImages:` —— 1/7 个有
- `RHExtractImage` —— 1/7 个有
- `RHUploadZip` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `easy forLoopEnd` —— 1/7 个有
- `easy forLoopStart` —— 1/7 个有
- `easy imageCount` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 57% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 7 | 86% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler_ancestral | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 57%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，7 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
