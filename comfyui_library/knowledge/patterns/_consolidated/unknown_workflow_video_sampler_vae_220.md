---
name: unknown_workflow_video_sampler_vae_220
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8325
common_nodes: [CLIPVisionLoader, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, RH_Captioner, RH_Translator, ShowText|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/AniWan+Lightx2v-rank128图生视频动漫视频_1945737650638823425.json, 视频生成/图生视频/FusionX-Q8-图生视频（极速）_1944957100570370049.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_220

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/AniWan+Lightx2v-rank128图生视频动漫视频_1945737650638823425.json、视频生成/图生视频/FusionX-Q8-图生视频（极速）_1944957100570370049.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `RH_Captioner`
- `RH_Translator`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `DF_Integer` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `RH_Prompter` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoFreeInitArgs` —— 1/2 个有
- `WanVideoImageResizeToClosest` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
