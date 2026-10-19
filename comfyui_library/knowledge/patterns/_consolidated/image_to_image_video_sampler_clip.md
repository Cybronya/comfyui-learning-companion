---
name: image_to_image_video_sampler_clip
type: Image To Image
frequency: 5
level: strong
coverage: 0.8688
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, GetImageSize+, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, ReferenceLatent, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, VideoCombine_Adv, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoMagCache, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1938811982646534145.json, 视频生成/图生视频/1939157311413739522.json, 视频生成/图生视频/1942852835459403777.json, 视频生成/图生视频/1942823594072150017.json, 视频生成/图生视频/1939561508932132865.json]
source: knowledge_consolidation
---

# image_to_image_video_sampler_clip

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1938811982646534145.json、视频生成/图生视频/1939157311413739522.json、视频生成/图生视频/1942852835459403777.json、视频生成/图生视频/1942823594072150017.json、视频生成/图生视频/1939561508932132865.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize+`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `ReferenceLatent`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `VideoCombine_Adv`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoMagCache`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `RH_Translator` —— 4/5 个有
- `GetNode` —— 3/5 个有
- `JWInteger` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `Text` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `ImageScale` —— 2/5 个有
- `LayerUtility: Integer` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `WanVideoVACEStartToEndFrame` —— 2/5 个有
- `FluxKontextImageScale` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `RH_ComfyFluxKontext` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
