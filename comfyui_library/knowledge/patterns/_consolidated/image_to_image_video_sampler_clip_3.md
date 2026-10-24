---
name: image_to_image_video_sampler_clip_3
type: Image To Image
frequency: 6
level: strong
coverage: 0.8825
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, GetImageSize+, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, ReferenceLatent, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, VideoCombine_Adv, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoMagCache, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext-姐就是女王_1943516280332689409.json, 视频生成/图生视频/Flux-kontext+FusionX-首尾帧视频_1938811982646534145.json, 视频生成/图生视频/FuxionX文生视频：一秒变光头视频_1939157311413739522.json, 视频生成/图生视频/Kontext+FusionX-一秒卡变通自拍_1942852835459403777.json, 视频生成/图生视频/Kontext+FusionX-一秒变自拍_1942823594072150017.json, 视频生成/图生视频/一夜白头-kontext+fusionX_1939561508932132865.json]
source: knowledge_consolidation
---

# image_to_image_video_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Kontext-姐就是女王_1943516280332689409.json、视频生成/图生视频/Flux-kontext+FusionX-首尾帧视频_1938811982646534145.json、视频生成/图生视频/FuxionX文生视频：一秒变光头视频_1939157311413739522.json、视频生成/图生视频/Kontext+FusionX-一秒卡变通自拍_1942852835459403777.json、视频生成/图生视频/Kontext+FusionX-一秒变自拍_1942823594072150017.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `RH_Translator` —— 5/6 个有
- `Text` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `JWInteger` —— 3/6 个有
- `LayerUtility: Integer` —— 3/6 个有
- `SaveImage` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `ImageScale` —— 2/6 个有
- `RH_LLMAPI_NODE` —— 2/6 个有
- `WanVideoVACEStartToEndFrame` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `FluxKontextImageScale` —— 1/6 个有
- `ImageStitch` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `RH_ComfyFluxKontext` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
