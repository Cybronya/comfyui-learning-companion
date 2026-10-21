---
name: unknown_workflow_video_lora_sampler_849
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.921
common_nodes: [CLIPVisionLoader, CR Text Concatenate, ImageCASharpening+, ImageResize+, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2070674585263108098.json, 视频生成/图生视频/1931730238252711938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_849

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2070674585263108098.json、视频生成/图生视频/1931730238252711938.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Text Concatenate`
- `ImageCASharpening+`
- `ImageResize+`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Florence2ModelLoader` —— 1/2 个有
- `Florence2Run` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `WanVideoTeaCache` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
