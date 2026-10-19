---
name: unknown_workflow_controlnet_video_lora_11
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.776286
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, SimpleMath+, VHS_DuplicateImages, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1989961958185160706.json, 视频生成/图生视频/1940583682262413314.json, 视频生成/图生视频/1949675886216925185.json, 视频生成/图生视频/1936961854306439170.json, 视频生成/图生视频/1953292063418814466.json, 视频生成/图生视频/1957680451332796417.json, 音频生成/音频生成/Wan2.1  Multitalk音乐数字人_1938926634802012162.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_11

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1989961958185160706.json、视频生成/图生视频/1940583682262413314.json、视频生成/图生视频/1949675886216925185.json、视频生成/图生视频/1936961854306439170.json、视频生成/图生视频/1953292063418814466.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `SimpleMath+`
- `VHS_DuplicateImages`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `MultiTalkWav2VecEmbeds` —— 6/7 个有
- `WanVideoContextOptions` —— 6/7 个有
- `WanVideoEncode` —— 6/7 个有
- `WanVideoTextEncode` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `CR Text` —— 5/7 个有
- `INTConstant` —— 5/7 个有
- `JWIntegerToString` —— 5/7 个有
- `LayerUtility: PurgeVRAM V2` —— 5/7 个有
- `VHS_LoadVideo` —— 5/7 个有
- `WanVideoTorchCompileSettings` —— 5/7 个有
- `easy anythingIndexSwitch` —— 5/7 个有
- `ImageResizeKJ` —— 4/7 个有
- `RH_Captioner` —— 4/7 个有
- `WanVideoEnhanceAVideo` —— 4/7 个有
- `WanVideoSLG` —— 4/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `ImageScale` —— 2/7 个有
- `ImageUpscaleWithModel` —— 2/7 个有
- `JWInteger` —— 2/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `PlaySound|pysssss` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `RH_GetAudioDuration` —— 2/7 个有
- `RH_Translator` —— 2/7 个有
- `RIFE VFI` —— 2/7 个有
- `Text Concatenate` —— 2/7 个有
- `UpscaleModelLoader` —— 2/7 个有
- `WanVideoExperimentalArgs` —— 2/7 个有
- `easy compare` —— 2/7 个有
- `easy ifElse` —— 2/7 个有
- `easy imageScaleDownToSize` —— 2/7 个有
- `easy imageSize` —— 2/7 个有
- `GetNode` —— 1/7 个有
- `ImageFromBatch+` —— 1/7 个有
- `ImpactInt` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `easy convertAnything` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
