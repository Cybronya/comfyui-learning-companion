---
name: unknown_workflow_video_lora_sampler_393
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8678
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/(KJ版)Wan2.2+multitalk 单人说话_1951530771968372737.json, 视频生成/图生视频/3425帧2000秒！Infinite Talk极速高质量提示词调度动作控制图生视频KTV数字人V3_1958590761962991617.json, 视频生成/图生视频/WH-AI-Studio完美数字人-多人对口型-短剧专用-长视频（动物可用）_2015621252844621826.json, 视频生成/图生视频/WH-AI-Studio（数字人-单人对口型-动物可用） (情感音频生成-运镜完美版)_2015621240408510465.json, 视频生成/图生视频/（完美数字人对口型-短剧专用-长视频）多人物镜头选择指定单人说话（也可指定多个对象说话-动物可用）_2009596955852279810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_393

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/(KJ版)Wan2.2+multitalk 单人说话_1951530771968372737.json、视频生成/图生视频/3425帧2000秒！Infinite Talk极速高质量提示词调度动作控制图生视频KTV数字人V3_1958590761962991617.json、视频生成/图生视频/WH-AI-Studio完美数字人-多人对口型-短剧专用-长视频（动物可用）_2015621252844621826.json、视频生成/图生视频/WH-AI-Studio（数字人-单人对口型-动物可用） (情感音频生成-运镜完美版)_2015621240408510465.json、视频生成/图生视频/（完美数字人对口型-短剧专用-长视频）多人物镜头选择指定单人说话（也可指定多个对象说话-动物可用）_2009596955852279810.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 4/5 个有
- `PreviewAudio` —— 4/5 个有
- `WanVideoImageToVideoMultiTalk` —— 4/5 个有
- `IndexTTS2Run` —— 3/5 个有
- `PreviewAny` —— 3/5 个有
- `TwoWaySwitch` —— 3/5 个有
- `ZML_TextInput` —— 3/5 个有
- `JWInteger` —— 2/5 个有
- `MaskPreview+` —— 2/5 个有
- `SeparateMasks` —— 2/5 个有
- `WanVideoTorchCompileSettings` —— 2/5 个有
- `CR Integer To String` —— 1/5 个有
- `CreateCFGScheduleFloatList` —— 1/5 个有
- `EmptyAudio` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `SaveLatent` —— 1/5 个有
- `WanVideoImageToVideoEncode` —— 1/5 个有
- `WanVideoSetBlockSwap` —— 1/5 个有
- `WanVideoSetLoRAs` —— 1/5 个有
- `easy seed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
