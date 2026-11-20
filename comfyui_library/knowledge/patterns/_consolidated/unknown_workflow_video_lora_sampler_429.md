---
name: unknown_workflow_video_lora_sampler_429
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.883286
common_nodes: [AudioCropProcessUTK, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MelBandRoFormerModelLoader, MelBandRoFormerSampler, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [平台全量/df_scail.json_2074398262207008769.json, 平台全量/视频对口型稳定版_2014253725291913217.json, 数字人/数字人/InfiniteTalk视频对口型_1974353112548945922.json, 数字人/数字人/最新InfiniteTalk 视频对口型数字人说话唱歌单人工作流 视频转视频_1976243284534263810.json, 数字人/数字人/视频对口型-让视频中人物对口型-保持原视频动态_2043639764364042242.json, 数字人/数字人/视频对口型-让视频中人物对口型_2069918268877529089.json, 视频生成/图生视频/影视剧替换人物第四步：视频对口型_2013511051282747393.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_429

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/df_scail.json_2074398262207008769.json、平台全量/视频对口型稳定版_2014253725291913217.json、数字人/数字人/InfiniteTalk视频对口型_1974353112548945922.json、数字人/数字人/最新InfiniteTalk 视频对口型数字人说话唱歌单人工作流 视频转视频_1976243284534263810.json、数字人/数字人/视频对口型-让视频中人物对口型-保持原视频动态_2043639764364042242.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `AudioCropProcessUTK`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 6/7 个有
- `CM_IntToFloat` —— 6/7 个有
- `CR Text` —— 6/7 个有
- `PrimitiveString` —— 6/7 个有
- `CustomAddLabel` —— 3/7 个有
- `INTConstant` —— 1/7 个有
- `ImpactSwitch` —— 1/7 个有
- `LoadImage` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
