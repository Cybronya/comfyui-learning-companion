---
name: unknown_workflow_controlnet_video_lora_17
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8565
common_nodes: [Audio Duration (mtb), AudioCrop, AudioSeparation, CLIPVisionLoader, CR Text, DownloadAndLoadWav2VecModel, ImageFromBatch+, ImpactSwitch, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, RHHiddenNodes, RH_LLMAPI_NODE, VHS_DuplicateImages, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy cleanGpuUsed, easy compare, easy ifElse, easy imageScaleDownToSize, easy imageSize, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1936408506675154946.json, 视频生成/图生视频/1941728602893479937.json, 视频生成/图生视频/1937081431380119554.json, 视频生成/图生视频/1936210894722355202.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1936408506675154946.json、视频生成/图生视频/1941728602893479937.json、视频生成/图生视频/1937081431380119554.json、视频生成/图生视频/1936210894722355202.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `ImageFromBatch+`
- `ImpactSwitch`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `RHHiddenNodes`
- `RH_LLMAPI_NODE`
- `VHS_DuplicateImages`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy compare`
- `easy ifElse`
- `easy imageScaleDownToSize`
- `easy imageSize`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/4 个有
- `ImageUpscaleWithModel` —— 2/4 个有
- `RIFE VFI` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有
- `WanVideoContextOptions` —— 2/4 个有
- `WanVideoExperimentalArgs` —— 2/4 个有
- `WanVideoSLG` —— 2/4 个有
- `ACEStepGen` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GenerationParameters` —— 1/4 个有
- `MultiLineLyrics` —— 1/4 个有
- `MultiLinePromptACES` —— 1/4 个有
- `SaveAudio` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
