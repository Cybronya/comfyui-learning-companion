---
name: unknown_workflow_video_lora_sampler_41
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.853167
common_nodes: [CLIPVisionLoader, DownloadAndLoadWav2VecModel, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/InfiniteTalk With Sa2VA 多人_1988439303661469698.json, 视频生成/图生视频/InfiniteTalk图生视频数字人V3-个人使用版_1969944110868164610.json, 视频生成/图生视频/InfiniteTalk数字人+姿态动作提示词_2018674445128310785.json, 视频生成/图生视频/Infinite对口型数字人 最强音色克隆带语气情感 音频生成数字人 声音克隆_2061786776032866305.json, 视频生成/图生视频/Infinite对口型数字人 最强音色克隆带语气情感 音频生成数字人 声音克隆_2081267787426787330.json, 视频生成/图生视频/Infinite数字人对口型（音频驱动 表情自然 可编辑动作）_2110374253521625090.json, 视频生成/图生视频/LTX-2图片转数字人素材标准化V1_2011699798700728322.json, 视频生成/图生视频/infinite Talk极速高质量提示词调度动作控制图生视频KTV数字人_1961034240169283585.json, 视频生成/图生视频/infinite tetalk音频+图生视频MTV_1959143275817021441.json, 视频生成/图生视频/infinitetalk数字人视频任意人物图片生成唱歌视频动作加强无限循环n分钟内不爆显存_1994005595265105922.json, 视频生成/图生视频/【CQ808】单人静帧图对口型工作流_2011801795986722818.json, 视频生成/图生视频/一键生成最长3500帧万相2.1图生视频（可对口型）_1967057695654207489.json, 视频生成/图生视频/乔帮主-对口型数字人 最强音色克隆带语气情感 音频生成 数字人 声音克隆  情绪参考   Infinite+_2086424507589423105.json, 视频生成/图生视频/图片人物对口型正式版_2002936132511907841.json, 视频生成/图生视频/图生视频 对口型数字人+最强音色克隆带语气情感+音频生成+数字人+声音克隆+情绪参考_2062720243771990018.json, 视频生成/图生视频/对口型数字人 最强音色克隆带语气情感 音频生成 数字人 声音克隆  情绪参考   Infinite+_2061287897743052801.json, 视频生成/图生视频/对口型数字人+最强音色克隆带语气情感+音频生成+数字人+声音克隆+情绪参考_2061971483555098625.json, 视频生成/图生视频/对口型数字人Infinite+talk对口型动态加强高版V3_1981308646988611586.json, 视频生成/图生视频/数字人 对口型最强音色克隆带语气情感 Infinite_2061625584001835010.json, 视频生成/图生视频/数字人 对口型最强音色克隆带语气情感 Infinite_2062437444791918594.json, 视频生成/图生视频/数字人 对口型最强音色克隆带语气情感 Infinite_2062801094731980801.json, 视频生成/图生视频/数字人 对口型最强音色克隆带语气情感 Infinite_2064624284164771842.json, 视频生成/图生视频/数字人 对口型最强音色克隆带语气情感 Infinite_2064954636120973313.json, 视频生成/图生视频/最强的数字人_2079549546333560833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_41

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk With Sa2VA 多人_1988439303661469698.json、视频生成/图生视频/InfiniteTalk图生视频数字人V3-个人使用版_1969944110868164610.json、视频生成/图生视频/InfiniteTalk数字人+姿态动作提示词_2018674445128310785.json、视频生成/图生视频/Infinite对口型数字人 最强音色克隆带语气情感 音频生成数字人 声音克隆_2061786776032866305.json、视频生成/图生视频/Infinite对口型数字人 最强音色克隆带语气情感 音频生成数字人 声音克隆_2081267787426787330.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 24 个 workflow 都包含：
- `CLIPVisionLoader`
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
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 23/24 个有
- `AudioCrop` —— 22/24 个有
- `CR Prompt Text` —— 22/24 个有
- `JWInteger` —— 22/24 个有
- `PreviewAny` —— 22/24 个有
- `JWFloat` —— 18/24 个有
- `LayerUtility: PurgeVRAM V2` —— 17/24 个有
- `easy showAnything` —— 17/24 个有
- `AudioToFPS` —— 16/24 个有
- `SetNode` —— 2/24 个有
- `Any Switch (rgthree)` —— 1/24 个有
- `Apply Whisper` —— 1/24 个有
- `Fast Groups Bypasser (rgthree)` —— 1/24 个有
- `Fast Groups Muter (rgthree)` —— 1/24 个有
- `GetNode` —— 1/24 个有
- `GrowMaskWithBlur` —— 1/24 个有
- `INTConstant` —— 1/24 个有
- `MaskPreview+` —— 1/24 个有
- `MultiTalkSilentEmbeds` —— 1/24 个有
- `OmniVoiceLongformTTS` —— 1/24 个有
- `OmniVoiceMultiSpeakerTTS` —— 1/24 个有
- `OmniVoiceVoiceDesignTTS` —— 1/24 个有
- `OmniVoiceWhisperLoader` —— 1/24 个有
- `PrimitiveInt` —— 1/24 个有
- `Sa2VANodeTpl` —— 1/24 个有
- `SaveAudio` —— 1/24 个有
- `easy cleanGpuUsed` —— 1/24 个有
- `workflow>2` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
