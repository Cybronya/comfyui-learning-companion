---
name: unknown_workflow_video_sampler_vae_155
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.98
common_nodes: [DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, Int, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Aniwan+FusionX+VACE打造精致wan2.1加速首尾帧_1933695659235303425.json, 视频生成/图生视频/MAGEF+FusionX VACE强一致性控尾帧图生视频万相wan2.1_1943311960978956289.json, 视频生成/图生视频/极致首中尾帧万相wan2.1+FusionX+VACE图生视频_1934272711260856322.json, 视频生成/图生视频/首中尾帧万相wan2.1+VACE+FlashVSR高清丝滑变身图生视频_1981344492861169666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_155

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Aniwan+FusionX+VACE打造精致wan2.1加速首尾帧_1933695659235303425.json、视频生成/图生视频/MAGEF+FusionX VACE强一致性控尾帧图生视频万相wan2.1_1943311960978956289.json、视频生成/图生视频/极致首中尾帧万相wan2.1+FusionX+VACE图生视频_1934272711260856322.json、视频生成/图生视频/首中尾帧万相wan2.1+VACE+FlashVSR高清丝滑变身图生视频_1981344492861169666.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 3/4 个有
- `GetImageSizeAndCount` —— 3/4 个有
- `ImageResizeKJ` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `WanVideoMagCache` —— 3/4 个有
- `ImageBatchMulti` —— 2/4 个有
- `MaskBatchMulti` —— 2/4 个有
- `PMRF` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `WanVideoLoraSelect` —— 2/4 个有
- `WanVideoVACEModelSelect` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `FlashVSRNode` —— 1/4 个有
- `InvSRSampler` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LoadInvSRModels` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `WanVideoEasyCache` —— 1/4 个有
- `WanVideoExtraModelSelect` —— 1/4 个有
- `WanVideoLoraSelectMulti` —— 1/4 个有
- `WanVideoSetRadialAttention` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
