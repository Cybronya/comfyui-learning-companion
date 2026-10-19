---
name: unknown_workflow_video_sampler_vae_97
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9204
common_nodes: [ImageResizeKJ, Int, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1939674359478788097.json, 视频生成/图生视频/1939674066548920322.json, 视频生成/图生视频/1942491226299904002.json, 视频生成/图生视频/1942491188651831298.json, 视频生成/图生视频/1944595309169397761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_97

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1939674359478788097.json、视频生成/图生视频/1939674066548920322.json、视频生成/图生视频/1942491226299904002.json、视频生成/图生视频/1942491188651831298.json、视频生成/图生视频/1944595309169397761.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageResizeKJ`
- `Int`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `WanVideoLoraSelect` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `RH_Translator` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `ImageUpscaleWithModel` —— 2/5 个有
- `RIFE VFI` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `UpscaleModelLoader` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
