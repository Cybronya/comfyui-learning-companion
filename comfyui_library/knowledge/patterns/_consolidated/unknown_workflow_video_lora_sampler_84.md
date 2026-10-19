---
name: unknown_workflow_video_lora_sampler_84
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.857765
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1970779502160867329.json, 视频生成/图生视频/1970454235139743746.json, 视频生成/图生视频/2042896857407426562.json, 视频生成/图生视频/2068183194842787841.json, 视频生成/图生视频/2046424551642374146.json, 视频生成/图生视频/2081899378620592130.json, 视频生成/图生视频/2039589897626984450.json, 视频生成/图生视频/2052766629263618049.json, 视频生成/图生视频/2038785334816804866.json, 视频生成/图生视频/2007287894716715010.json, 视频生成/图生视频/2029255220571676673.json, 视频生成/图生视频/2029417074241576961.json, 视频生成/图生视频/1987692626436665345.json, 视频生成/图生视频/1995458566553264130.json, 视频生成/图生视频/2039856506417455105.json, 视频生成/图生视频/2055446577807937537.json, 视频生成/图生视频/2046429315620933634.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_84

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/1970779502160867329.json、视频生成/图生视频/1970454235139743746.json、视频生成/图生视频/2042896857407426562.json、视频生成/图生视频/2068183194842787841.json、视频生成/图生视频/2046424551642374146.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 17 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 16/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 16/17 个有
- `LoadAudio` —— 16/17 个有
- `JWInteger` —— 15/17 个有
- `AudioCrop` —— 13/17 个有
- `JWFloat` —— 12/17 个有
- `AudioToFPS` —— 7/17 个有
- `Bjornulf_ShowInt` —— 7/17 个有
- `MathExpression|pysssss` —— 7/17 个有
- `Int` —— 3/17 个有
- `AddLabel` —— 2/17 个有
- `SimpleMath+` —— 2/17 个有
- `TextToUppercase` —— 2/17 个有
- `ConcatTextOfUtils` —— 1/17 个有
- `IndexTTS2Run` —— 1/17 个有
- `PrimitiveInt` —— 1/17 个有
- `PrimitiveStringMultiline` —— 1/17 个有
- `VHS_LoadAudioUpload` —— 1/17 个有
- `VHS_SplitImages` —— 1/17 个有
- `easy anythingIndexSwitch` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
