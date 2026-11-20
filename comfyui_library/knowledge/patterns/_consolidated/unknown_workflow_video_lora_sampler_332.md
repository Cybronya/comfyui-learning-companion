---
name: unknown_workflow_video_lora_sampler_332
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.888111
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadAudio, MultiTalkModelLoader, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/InfiniteTalk数字人-唱歌自由_2018667682865881089.json, 视频生成/图生视频/Wan2.1对口型数字人_2054610077646114818.json, 视频生成/图生视频/Wan21Animate高质量丝滑单人数字人_1993501240730599426.json, 视频生成/图生视频/infinite Talk极速高质量提示词调度动作控制图生视频KTV数字人_1961034240169283585.json, 视频生成/图生视频/优化版Infinite Talk口型高质量图生视频数字人_1979895392475189249.json, 视频生成/图生视频/商用娱乐地表最强数字人（测颜版）_1988227930037903361.json, 视频生成/图生视频/数字人口播_2006243874485833729.json, 视频生成/图生视频/超强视频对口型（唱歌数字人））_2000589265400721409.json, 视频生成/图生视频/超自然对口型+视频数字人_2000608709594185729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_332

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk数字人-唱歌自由_2018667682865881089.json、视频生成/图生视频/Wan2.1对口型数字人_2054610077646114818.json、视频生成/图生视频/Wan21Animate高质量丝滑单人数字人_1993501240730599426.json、视频生成/图生视频/infinite Talk极速高质量提示词调度动作控制图生视频KTV数字人_1961034240169283585.json、视频生成/图生视频/优化版Infinite Talk口型高质量图生视频数字人_1979895392475189249.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadAudio`
- `MultiTalkModelLoader`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MultiTalkWav2VecEmbeds` —— 8/9 个有
- `WanVideoBlockSwap` —— 8/9 个有
- `WanVideoModelLoader` —— 8/9 个有
- `ImageResizeKJv2` —— 6/9 个有
- `LoadImage` —— 6/9 个有
- `GetImageSizeAndCount` —— 5/9 个有
- `INTConstant` —— 5/9 个有
- `JWInteger` —— 5/9 个有
- `PreviewAny` —— 5/9 个有
- `WanVideoTextEncodeCached` —— 5/9 个有
- `WanVideoTorchCompileSettings` —— 5/9 个有
- `Anything Everywhere` —— 4/9 个有
- `CR Prompt Text` —— 4/9 个有
- `GetImageRangeFromBatch` —— 4/9 个有
- `LoadWanVideoT5TextEncoder` —— 4/9 个有
- `WanVideoEncode` —— 4/9 个有
- `WanVideoTextEncode` —— 4/9 个有
- `easy int` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `VHS_LoadVideo` —— 3/9 个有
- `Audio Duration (mtb)` —— 1/9 个有
- `DF_Int_to_Float` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
