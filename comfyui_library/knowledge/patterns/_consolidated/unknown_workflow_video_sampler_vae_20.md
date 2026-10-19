---
name: unknown_workflow_video_sampler_vae_20
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.830154
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoFreeInitArgs, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1945731956841783297.json, 视频生成/图生视频/1945149080488091650.json, 视频生成/图生视频/1945737650638823425.json, 视频生成/图生视频/1946470385267433473.json, 视频生成/图生视频/1945512354513866754.json, 视频生成/图生视频/1945783808815931394.json, 视频生成/图生视频/2021501136443805698.json, 视频生成/图生视频/1945382790554689537.json, 视频生成/图生视频/1986372877740081153.json, 视频生成/图生视频/1956231253135642625.json, 视频生成/图生视频/1947090217771249666.json, 视频生成/图生视频/1944788668831682561.json, 视频生成/文生视频/1945639434354348033.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_20

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1945731956841783297.json、视频生成/图生视频/1945149080488091650.json、视频生成/图生视频/1945737650638823425.json、视频生成/图生视频/1946470385267433473.json、视频生成/图生视频/1945512354513866754.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoFreeInitArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Primitive integer [Crystools]` —— 12/13 个有
- `ShowText` —— 12/13 个有
- `Text Multiline` —— 12/13 个有
- `WanVideoExperimentalArgs` —— 12/13 个有
- `WanVideoLoraSelect` —— 12/13 个有
- `WanVideoTorchCompileSettings` —— 12/13 个有
- `Fast Groups Bypasser (rgthree)` —— 10/13 个有
- `WanVideoSetRadialAttention` —— 4/13 个有
- `RH_LLMAPI_NODE` —— 2/13 个有
- `DF_Integer` —— 1/13 个有
- `Note Plus (mtb)` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `RH_Captioner` —— 1/13 个有
- `RH_Translator` —— 1/13 个有
- `ShowText|pysssss` —— 1/13 个有
- `Text Concatenate` —— 1/13 个有
- `WanVideoEasyCache` —— 1/13 个有
- `WanVideoLoraSelectMulti` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
