---
name: unknown_workflow_video_lora_sampler_730
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.936333
common_nodes: [ImageResize+, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1 [360°环绕运镜] 一键式图生视频_2070674585263108098.json, 视频生成/图生视频/wan2.2首尾帧，kj加速版_1953644450683736065.json, 视频生成/图生视频/wan超酷运镜_1931730238252711938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_730

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/wan2.1 [360°环绕运镜] 一键式图生视频_2070674585263108098.json、视频生成/图生视频/wan2.2首尾帧，kj加速版_1953644450683736065.json、视频生成/图生视频/wan超酷运镜_1931730238252711938.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageResize+`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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
- `CLIPVisionLoader` —— 2/3 个有
- `CR Text Concatenate` —— 2/3 个有
- `INTConstant` —— 2/3 个有
- `ImageCASharpening+` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `Florence2ModelLoader` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LoadWanVideoClipTextEncoder` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `WanVideoEnhanceAVideo` —— 1/3 个有
- `WanVideoExperimentalArgs` —— 1/3 个有
- `WanVideoSLG` —— 1/3 个有
- `WanVideoTeaCache` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
