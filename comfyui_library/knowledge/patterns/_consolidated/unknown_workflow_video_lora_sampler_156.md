---
name: unknown_workflow_video_lora_sampler_156
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.946273
common_nodes: [CLIPVisionLoader, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1945425557527961601.json, 视频生成/图生视频/1946761730153148417.json, 视频生成/图生视频/1944770056771260417.json, 视频生成/图生视频/1946230889756913665.json, 视频生成/图生视频/1945462640925921281.json, 视频生成/图生视频/1936033018391990273.json, 视频生成/图生视频/1946266555401560066.json, 视频生成/图生视频/1944601426138157058.json, 视频生成/图生视频/1946050505720164354.json, 视频生成/图生视频/2008939674751995905.json, 视频生成/图生视频/1946428011036205057.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_156

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/1945425557527961601.json、视频生成/图生视频/1946761730153148417.json、视频生成/图生视频/1944770056771260417.json、视频生成/图生视频/1946230889756913665.json、视频生成/图生视频/1945462640925921281.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoFreeInitArgs` —— 9/11 个有
- `RH_OneShot_Prompter` —— 7/11 个有
- `SimpleMath+` —— 7/11 个有
- `WanVideoApplyNAG` —— 7/11 个有
- `WanVideoEasyCache` —— 7/11 个有
- `WanVideoTextEncodeSingle` —— 7/11 个有
- `WanVideoSetRadialAttention` —— 4/11 个有
- `WanVideoTextEncode` —— 4/11 个有
- `WanVideoVRAMManagement` —— 4/11 个有
- `WanVideoTeaCache` —— 2/11 个有
- `WanVideoTorchCompileSettings` —— 2/11 个有
- `BackgroundEraseNetwork` —— 1/11 个有
- `CR Text` —— 1/11 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/11 个有
- `EG_SZ_CGJS` —— 1/11 个有
- `GIMMVFI_interpolate` —— 1/11 个有
- `LayerMask: BiRefNetUltraV2` —— 1/11 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
