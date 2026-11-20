---
name: unknown_workflow_video_sampler_clip_80
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.771875
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ColorMatch, ImageResizeKJv2, ImageScaleBy, KSamplerAdvanced, LoadImage, ModelSamplingSD3, Pick From Batch (mtb), PreviewImage, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo]
problems: []
missing: []
members: [图片生成/文生图/smoothMix图生视频_1983520094011760642.json, 平台全量/头发图生视频 （大幅度摆动）浮云 12.18 替代MJ_2001186817330249730.json, 视频生成/图生视频/Comfy挑战赛8（诡影映画）-Smooth恐怖版图生视频_1983768746911277058.json, 视频生成/图生视频/Dasiwa V9模型VS Wan2.2 Smooth V2模型图生视频对比_2011762813080965122.json, 视频生成/图生视频/Dasiwa Vs Remix V2 VS  Smooth图生视频对比工作流V1_1991464228328521730.json, 视频生成/图生视频/Hunyuanvideo 1.5 12 steps Vs Wan2.2 Smooth图生视频对比V1_1997502737183084545.json, 视频生成/图生视频/Hunyuanvideo Vs Wan2.2 Smooth图生视频对比工作流V1_1992820026646523905.json, 视频生成/图生视频/Wan2.2 Smooth  V1模型VS V2模型图生视频对比_2010545068549083138.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_80

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/smoothMix图生视频_1983520094011760642.json、平台全量/头发图生视频 （大幅度摆动）浮云 12.18 替代MJ_2001186817330249730.json、视频生成/图生视频/Comfy挑战赛8（诡影映画）-Smooth恐怖版图生视频_1983768746911277058.json、视频生成/图生视频/Dasiwa V9模型VS Wan2.2 Smooth V2模型图生视频对比_2011762813080965122.json、视频生成/图生视频/Dasiwa Vs Remix V2 VS  Smooth图生视频对比工作流V1_1991464228328521730.json…）

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
- `ColorMatch`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `Pick From Batch (mtb)`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 7/8 个有
- `JWInteger` —— 7/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `easy cleanGpuUsed` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `AILab_QwenVL` —— 5/8 个有
- `AddLabel` —— 5/8 个有
- `ImageConcanate` —— 5/8 个有
- `LayerUtility: PurgeVRAM` —— 5/8 个有
- `PathchSageAttentionKJ` —— 5/8 个有
- `RH_LLMAPI_NODE` —— 5/8 个有
- `RIFE VFI` —— 5/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `StringConcatenate` —— 4/8 个有
- `UnetLoaderGGUF` —— 3/8 个有
- `BasicScheduler` —— 2/8 个有
- `CFGGuider` —— 2/8 个有
- `DualCLIPLoader` —— 2/8 个有
- `EasyCache` —— 2/8 个有
- `HunyuanVideo15ImageToVideo` —— 2/8 个有
- `KSamplerSelect` —— 2/8 个有
- `ModelPatchTorchSettings` —— 2/8 个有
- `RandomNoise` —— 2/8 个有
- `SamplerCustomAdvanced` —— 2/8 个有
- `VAEDecodeTiled` —— 2/8 个有
- `Label (rgthree)` —— 1/8 个有
- `PDIMAGE_LongerSize` —— 1/8 个有
- `PainterI2V` —— 1/8 个有
- `Power Lora Loader (rgthree)` —— 1/8 个有
- `RunningHub Deepcleaner` —— 1/8 个有
- `mxSlider2D` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 88% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 8 | 87% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler_ancestral | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，8 个样本，取值集中（一致性 87%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
