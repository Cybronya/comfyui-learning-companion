---
name: unknown_workflow_controlnet_video_sampler
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.951
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FusionX+Multitalk 数字人_1945004776141807618.json, 视频生成/图生视频/MultiTalk 单人+运镜_1936573145107304450.json, 视频生成/图生视频/MultiTalk对口型（万相实现）+uni3C运镜控制_1937801479434735618.json, 视频生成/图生视频/MultiTalk：超6倍加速，超逼真顶流K歌数字人_1936605606658625537.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_sampler

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/FusionX+Multitalk 数字人_1945004776141807618.json、视频生成/图生视频/MultiTalk 单人+运镜_1936573145107304450.json、视频生成/图生视频/MultiTalk对口型（万相实现）+uni3C运镜控制_1937801479434735618.json、视频生成/图生视频/MultiTalk：超6倍加速，超逼真顶流K歌数字人_1936605606658625537.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 3/4 个有
- `WanVideoLoraSelect` —— 3/4 个有
- `CreateCFGScheduleFloatList` —— 2/4 个有
- `DF_Integer` —— 2/4 个有
- `INTConstant` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `RH_Captioner` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `IndexTTSNode` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `RH_Prompter` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `SaveAudio` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `Text` —— 1/4 个有
- `ttN concat` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
