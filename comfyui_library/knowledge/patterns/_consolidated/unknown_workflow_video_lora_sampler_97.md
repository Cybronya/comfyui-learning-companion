---
name: unknown_workflow_video_lora_sampler_97
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.787188
common_nodes: [Audio Duration (mtb), AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, GetImageSizeAndCount, ImageFromBatch+, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PrimitiveInt, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/1.1_infinitetalk视频双人对口型（效果最好）_1994720356055326722.json, 数字人/数字人/1.2_InfiniteTalk视频+音频对口型（效果最好）_1994683257532915714.json, 数字人/数字人/InfiniteTalkV2V 视频对口型数字人说话唱歌_2042253660570263554.json, 数字人/数字人/InfiniteTalk数字人视频生视频2_1978763649466699777.json, 数字人/数字人/InfiniteTalk数字人视频生视频_1958502190061142018.json, 数字人/数字人/InfiniteTalk数字人视频生视频_1982814946415259649.json, 数字人/数字人/InfiniteTalk数字人视频生视频_2001131954474975234.json, 数字人/数字人/infinitetalk图像对口型_1971910981158891521.json, 数字人/数字人/infinitetalk视频双人对口型_1980526429727313921.json, 数字人/数字人/infinitetalk视频对口型（hua）_1998027187120955394.json, 数字人/数字人/infinitetalk视频对口型（hua）_2006207828683395074.json, 数字人/数字人/wan2.1视频对口型（支持超长30秒）_2061334128561315841.json, 数字人/数字人/【808】视频角色对口型_2038885608399048706.json, 数字人/数字人/视频对口型（指定角色）_2036439627673899009.json, 数字人/数字人/视频对口型（指定角色）_2037210359945240577.json, 音频生成/音频生成/视频对口型（指定角色）_2012598659203997698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_97

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（数字人/数字人/1.1_infinitetalk视频双人对口型（效果最好）_1994720356055326722.json、数字人/数字人/1.2_InfiniteTalk视频+音频对口型（效果最好）_1994683257532915714.json、数字人/数字人/InfiniteTalkV2V 视频对口型数字人说话唱歌_2042253660570263554.json、数字人/数字人/InfiniteTalk数字人视频生视频2_1978763649466699777.json、数字人/数字人/InfiniteTalk数字人视频生视频_1958502190061142018.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 16 个 workflow 都包含：
- `Audio Duration (mtb)`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PrimitiveInt`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 15/16 个有
- `WanVideoEncode` —— 15/16 个有
- `AudioCrop` —— 14/16 个有
- `ImageResizeKJv2` —— 14/16 个有
- `CR Text` —— 10/16 个有
- `easy showAnything` —— 10/16 个有
- `WanVideoTorchCompileSettings` —— 9/16 个有
- `easy cleanGpuUsed` —— 8/16 个有
- `GetNode` —— 6/16 个有
- `JjkText` —— 6/16 个有
- `LayerUtility: PurgeVRAM` —— 6/16 个有
- `PreviewAny` —— 6/16 个有
- `PrimitiveString` —— 6/16 个有
- `SetNode` —— 6/16 个有
- `PreviewImage` —— 5/16 个有
- `AILab_MaskPreview` —— 4/16 个有
- `ImageFromBatch` —— 4/16 个有
- `MaskListToMaskBatch` —— 4/16 个有
- `PreviewAudio` —— 4/16 个有
- `RH_Translator` —— 4/16 个有
- `Text` —— 4/16 个有
- `VHS_VideoInfo` —— 4/16 个有
- `easy sam3ModelLoader` —— 4/16 个有
- `easy sam3VideoSegmentation` —— 4/16 个有
- `LoadImage` —— 3/16 个有
- `ImageResize+` —— 2/16 个有
- `SaveImage` —— 2/16 个有
- `VHS_VideoInfoLoaded` —— 2/16 个有
- `FloatConstant` —— 1/16 个有
- `PrimitiveFloat` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
