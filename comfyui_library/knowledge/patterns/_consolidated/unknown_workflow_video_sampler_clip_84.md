---
name: unknown_workflow_video_sampler_clip_84
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.770875
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, ColorMatch, ImageResizeKJv2, ImageScaleBy, JWInteger, KSamplerAdvanced, ModelSamplingSD3, Pick From Batch (mtb), PreviewImage, PrimitiveStringMultiline, RIFE VFI, SaveImage, Seed (rgthree), StringConcatenate, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2批量图生视频_1999362041401966593.json, 视频生成/图生视频/wanSmooth图生视频_2001138959705047042.json, 视频生成/图生视频/（4+4步）WAN 2.2 Smooth Mix高质量图生视频V2_1976151444560707585.json, 视频生成/图生视频/（最强）Wan2.2 Smooth V2模型全自动提示词图生视频极速版_2010549629842104321.json, 视频生成/图生视频/（最强）Wan2.2 Smooth V2模型半自动提示词图生视频极速版_2010551165288714241.json, 视频生成/图生视频/（最强）Wan2.2 Smooth V2模型图生视频极速版_2010540373155782658.json, 视频生成/图生视频/（自用）Wan2.2 Smooth V2模型图生视频极速版_2010556397150281730.json, 视频生成/图生视频/（自用）Wan2.2 Smooth V2模型图生视频极速版（双模式）_2010559746318802946.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_84

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/wan2.2批量图生视频_1999362041401966593.json、视频生成/图生视频/wanSmooth图生视频_2001138959705047042.json、视频生成/图生视频/（4+4步）WAN 2.2 Smooth Mix高质量图生视频V2_1976151444560707585.json、视频生成/图生视频/（最强）Wan2.2 Smooth V2模型全自动提示词图生视频极速版_2010549629842104321.json、视频生成/图生视频/（最强）Wan2.2 Smooth V2模型半自动提示词图生视频极速版_2010551165288714241.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `ColorMatch`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `JWInteger`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RIFE VFI`
- `SaveImage`
- `Seed (rgthree)`
- `StringConcatenate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `UnetLoaderGGUF` —— 6/8 个有
- `ModelPatchTorchSettings` —— 5/8 个有
- `PathchSageAttentionKJ` —— 5/8 个有
- `mxSlider2D` —— 3/8 个有
- `DuckHideNode` —— 2/8 个有
- `RH_LLMAPI_NODE` —— 2/8 个有
- `TT_img_enc` —— 2/8 个有
- `TT_img_enc_v2` —— 2/8 个有
- `AILab_QwenVL` —— 1/8 个有
- `Any To Any` —— 1/8 个有
- `Bjornulf_ShowInt` —— 1/8 个有
- `Qwen3_VQA` —— 1/8 个有
- `RHBatchImages:` —— 1/8 个有
- `RHExtractImage` —— 1/8 个有
- `RHUploadZip` —— 1/8 个有
- `VHS_SelectFilename` —— 1/8 个有
- `easy anythingIndexSwitch` —— 1/8 个有
- `easy forLoopEnd` —— 1/8 个有
- `easy forLoopStart` —— 1/8 个有
- `easy imageCount` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 88% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 8 | 86% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler_ancestral | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，8 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
