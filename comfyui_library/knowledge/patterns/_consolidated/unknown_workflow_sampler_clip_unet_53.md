---
name: unknown_workflow_sampler_clip_unet_53
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7434
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ImageResizeKJv2, ImageScaleBy, KSamplerAdvanced, LoadImage, ModelSamplingSD3, Pick From Batch (mtb), UNETLoader, VAEDecode, VAELoader, WanImageToVideo, easy cleanGpuUsed, easy showAnything]
problems: []
missing: [Label (rgthree), Pick From Batch (mtb), RIFE VFI, easy cleanGpuUsed, Power Lora Loader (rgthree), Seed (rgthree)]
members: [图片生成/文生图/1983520094011760642.json, 视频生成/图生视频/1983768746911277058.json, 视频生成/图生视频/1983771744160915457.json, 视频生成/图生视频/2011762813080965122.json, 视频生成/图生视频/2016059757810950146.json, 视频生成/图生视频/2010545068549083138.json, 视频生成/图生视频/2010549629842104321.json, 视频生成/图生视频/1979918269014511617.json, 视频生成/图生视频/2010556397150281730.json, 视频生成/图生视频/2010559746318802946.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_53

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/1983520094011760642.json、视频生成/图生视频/1983768746911277058.json、视频生成/图生视频/1983771744160915457.json、视频生成/图生视频/2011762813080965122.json、视频生成/图生视频/2016059757810950146.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanImageToVideo`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 9/10 个有
- `JWInteger` —— 9/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/10 个有
- `LoraLoaderModelOnly` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `RIFE VFI` —— 9/10 个有
- `SaveImage` —— 9/10 个有
- `Seed (rgthree)` —— 9/10 个有
- `StringConcatenate` —— 9/10 个有
- `UnetLoaderGGUF` —— 9/10 个有
- `VHS_VideoCombine` —— 9/10 个有
- `ColorMatch` —— 7/10 个有
- `PreviewImage` —— 7/10 个有
- `ModelPatchTorchSettings` —— 6/10 个有
- `PathchSageAttentionKJ` —— 6/10 个有
- `RH_LLMAPI_NODE` —— 4/10 个有
- `TT_img_enc` —— 4/10 个有
- `TT_img_enc_v2` —— 4/10 个有
- `AILab_QwenVL` —— 3/10 个有
- `AddLabel` —— 2/10 个有
- `Any To Any` —— 2/10 个有
- `DuckHideNode` —— 2/10 个有
- `ImageConcanate` —— 2/10 个有
- `LayerUtility: PurgeVRAM` —— 2/10 个有
- `Qwen3_VQA` —— 2/10 个有
- `VHS_SelectFilename` —— 2/10 个有
- `mxSlider2D` —— 2/10 个有
- `Label (rgthree)` —— 1/10 个有
- `Power Lora Loader (rgthree)` —— 1/10 个有
- `Text Concatenate` —— 1/10 个有
- `TextInput_` —— 1/10 个有
- `easy anythingIndexSwitch` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 70% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 10 | 86% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | euler_ancestral | - | 10 | 100% |
| 重绘幅度 | simple | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 70%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，10 个样本，取值集中（一致性 86%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，10 个样本，一致性 100%
- 重绘幅度 最常用 simple，10 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：Label (rgthree)、Pick From Batch (mtb)、RIFE VFI、easy cleanGpuUsed、Power Lora Loader (rgthree)
