---
name: unknown_workflow_video_upscale_sampler_13
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.78
common_nodes: [CLIPVisionLoader, CR Text Concatenate, ImageResizeKJv2, ImageScale, ImageUpscaleWithModel, JWInteger, JjkText, LoadImage, LoadWanVideoT5TextEncoder, PlaySound|pysssss, PreviewImage, RH_Captioner, RH_Prompter, RH_Translator, RIFE VFI, SimpleMath+, TextBox, UpscaleModelLoader, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader, easy showAnything, ttN concat]
problems: []
missing: []
members: [视频生成/图生视频/1943848971993485314.json, 视频生成/图生视频/1936709639767511041.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1943848971993485314.json、视频生成/图生视频/1936709639767511041.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Text Concatenate`
- `ImageResizeKJv2`
- `ImageScale`
- `ImageUpscaleWithModel`
- `JWInteger`
- `JjkText`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PlaySound|pysssss`
- `PreviewImage`
- `RH_Captioner`
- `RH_Prompter`
- `RH_Translator`
- `RIFE VFI`
- `SimpleMath+`
- `TextBox`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`
- `easy showAnything`
- `ttN concat`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
