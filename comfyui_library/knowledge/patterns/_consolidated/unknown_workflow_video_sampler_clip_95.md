---
name: unknown_workflow_video_sampler_clip_95
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.783
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ColorMatch, ImageResizeKJv2, ImageScaleBy, KSamplerAdvanced, LoadImage, ModelSamplingSD3, Pick From Batch (mtb), PreviewImage, PrimitiveStringMultiline, RIFE VFI, SaveImage, Seed (rgthree), StringConcatenate, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2021178894228918274.json, 视频生成/图生视频/1986011600907841537.json, 视频生成/图生视频/2010728669576171522.json, 视频生成/图生视频/2010689489143861250.json, 视频生成/图生视频/2015436189947400194.json, 视频生成/图生视频/2016124852335288321.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_95

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2021178894228918274.json、视频生成/图生视频/1986011600907841537.json、视频生成/图生视频/2010728669576171522.json、视频生成/图生视频/2010689489143861250.json、视频生成/图生视频/2015436189947400194.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ColorMatch`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LoadImage`
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
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `WanImageToVideo` —— 5/6 个有
- `Int` —— 4/6 个有
- `JWInteger` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `ModelPatchTorchSettings` —— 4/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `UnetLoaderGGUF` —— 4/6 个有
- `CR Prompt Text` —— 3/6 个有
- `Label (rgthree)` —— 3/6 个有
- `SimpleMath+` —— 3/6 个有
- `Text` —— 3/6 个有
- `mxSlider2D` —— 3/6 个有
- `AILab_QwenVL` —— 2/6 个有
- `CR Text Replace` —— 2/6 个有
- `CustomAddLabel` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `MultiTextConcatenate` —— 2/6 个有
- `RH_Utils` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `ShowText` —— 2/6 个有
- `TextBox` —— 2/6 个有
- `easy anythingIndexSwitch` —— 2/6 个有
- `AddLabel` —— 1/6 个有
- `Power Lora Loader (rgthree)` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `WanFirstLastFrameToVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 6 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 6 | 100% |
| 采样算法 | 1 | 1 - 1 | 6 | 100% |
| 调度器 | euler_ancestral | - | 6 | 100% |
| 重绘幅度 | simple | - | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，6 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，6 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，6 个样本，一致性 100%
- 重绘幅度 最常用 simple，6 个样本，一致性 100%
