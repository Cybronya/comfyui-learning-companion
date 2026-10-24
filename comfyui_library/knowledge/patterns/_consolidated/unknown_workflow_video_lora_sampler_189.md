---
name: unknown_workflow_video_lora_sampler_189
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.876
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/InfiniteTalk+wan2.1单图片_视频生成口播数字人视频_1958754013288296450.json, 视频生成/图生视频/InfiniteTalk单人数字人工作流_1957818036982050817.json, 视频生成/图生视频/InfiniteTalk数字人动态加强版（对口型-唱歌）_2015692807259824129.json, 视频生成/图生视频/InfiniteTalk数字人唱歌口播长视频生成_1980248252606013441.json, 视频生成/图生视频/InfiniteTalk数字人长视频（唱歌-对口型）_1957840696807096321.json, 视频生成/图生视频/InfiniteTalk数字人（图片+音频）_1957992360850468865.json, 视频生成/图生视频/SunoV5音乐+InfiniteTalk数字人MV_1983589305073508353.json, 视频生成/图生视频/Y-InfiniteTalk单人图生视频_1958373813031485441.json, 视频生成/图生视频/数字人长视频（唱歌-对口型）_2028126776630710273.json, 音频生成/音频生成/InfiniteTalk单人视频到视频_1958736757212753921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_189

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk+wan2.1单图片_视频生成口播数字人视频_1958754013288296450.json、视频生成/图生视频/InfiniteTalk单人数字人工作流_1957818036982050817.json、视频生成/图生视频/InfiniteTalk数字人动态加强版（对口型-唱歌）_2015692807259824129.json、视频生成/图生视频/InfiniteTalk数字人唱歌口播长视频生成_1980248252606013441.json、视频生成/图生视频/InfiniteTalk数字人长视频（唱歌-对口型）_1957840696807096321.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
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
- `LoadAudio` —— 9/10 个有
- `PrimitiveInt` —— 8/10 个有
- `LoadImage` —— 7/10 个有
- `Audio Duration (mtb)` —— 6/10 个有
- `CR Text` —— 6/10 个有
- `JWIntegerToString` —— 5/10 个有
- `SimpleMath+` —— 5/10 个有
- `WanVideoTorchCompileSettings` —— 5/10 个有
- `ImageFromBatch+` —— 4/10 个有
- `JWInteger` —— 4/10 个有
- `Text Multiline` —— 3/10 个有
- `VHS_LoadVideo` —— 3/10 个有
- `WanVideoEncode` —— 2/10 个有
- `WanVideoUni3C_ControlnetLoader` —— 2/10 个有
- `WanVideoUni3C_embeds` —— 2/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `PreviewAudio` —— 1/10 个有
- `RH_Suno_Single` —— 1/10 个有
- `SaveAudioMP3` —— 1/10 个有
- `String` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
