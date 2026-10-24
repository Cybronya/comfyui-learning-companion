---
name: unknown_workflow_video_lora_sampler_203
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.900444
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageRangeFromBatch, ImageResizeKJv2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Infinitetalk视频转数字人-动态更强更自然_2043528487876694017.json, 视频生成/图生视频/InfiniteTalk数字人 _ 视频生视频-自动对口型（支持唱歌_说话）高动态_1992841755221618690.json, 视频生成/图生视频/数字人口播_2006243874485833729.json, 视频生成/图生视频/超强视频对口型（唱歌数字人））_2000589265400721409.json, 视频生成/图生视频/超自然对口型+视频数字人_2000608709594185729.json, 音频生成/音频生成/InfiniteTalk数字人-唱歌自由_2046674996084346882.json, 音频生成/音频生成/超强视频对口型唱歌数字人_2100410279401181185.json, 音频生成/音频生成/超强视频对口型唱歌数字人_2100497922336055297.json, 音频生成/音频生成/超自然对口型 视频数字人_2000587001097224194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_203

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/Infinitetalk视频转数字人-动态更强更自然_2043528487876694017.json、视频生成/图生视频/InfiniteTalk数字人 _ 视频生视频-自动对口型（支持唱歌_说话）高动态_1992841755221618690.json、视频生成/图生视频/数字人口播_2006243874485833729.json、视频生成/图生视频/超强视频对口型（唱歌数字人））_2000589265400721409.json、视频生成/图生视频/超自然对口型+视频数字人_2000608709594185729.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `GetImageRangeFromBatch`
- `ImageResizeKJv2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_LoadVideo` —— 8/9 个有
- `Anything Everywhere` —— 7/9 个有
- `INTConstant` —— 7/9 个有
- `WanVideoTorchCompileSettings` —— 7/9 个有
- `easy int` —— 7/9 个有
- `Float to Int` —— 2/9 个有
- `SimpleMath+` —— 2/9 个有
- `SoundFlow_GetLength` —— 2/9 个有
- `Getter` —— 1/9 个有
- `ImageConcanate` —— 1/9 个有
- `Int` —— 1/9 个有
- `LoadImage` —— 1/9 个有
- `PrimitiveInt` —— 1/9 个有
- `Setter` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
