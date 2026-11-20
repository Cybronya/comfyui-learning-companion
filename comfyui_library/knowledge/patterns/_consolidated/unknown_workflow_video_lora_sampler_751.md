---
name: unknown_workflow_video_lora_sampler_751
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7355
common_nodes: [CLIPVisionLoader, ImageCASharpening+, ImageResize+, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1 [360°环绕运镜] 一键式图生视频_2070674585263108098.json, 视频生成/图生视频/wan超酷运镜_1931730238252711938.json, 视频生成/图生视频/【高速跟随运镜】wan2.1图生视频（全自动）_1930913690252718081.json, 视频生成/图生视频/运镜效果wan2.1图生视频_2050075485417295874.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_751

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/wan2.1 [360°环绕运镜] 一键式图生视频_2070674585263108098.json、视频生成/图生视频/wan超酷运镜_1931730238252711938.json、视频生成/图生视频/【高速跟随运镜】wan2.1图生视频（全自动）_1930913690252718081.json、视频生成/图生视频/运镜效果wan2.1图生视频_2050075485417295874.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageCASharpening+`
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
- `PreviewImage` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `WanVideoExperimentalArgs` —— 3/4 个有
- `WanVideoSLG` —— 3/4 个有
- `WanVideoTeaCache` —— 3/4 个有
- `Anything Everywhere` —— 2/4 个有
- `CR Text Concatenate` —— 2/4 个有
- `CogVideoEnhanceAVideo` —— 2/4 个有
- `GetNode` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `Florence2ModelLoader` —— 1/4 个有
- `Florence2Run` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `WanVideoEnhanceAVideo` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
