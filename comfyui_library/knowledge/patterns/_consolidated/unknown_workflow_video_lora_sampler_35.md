---
name: unknown_workflow_video_lora_sampler_35
type: Unknown Workflow
frequency: 28
level: moderate
coverage: 0.980643
common_nodes: [AudioSeparation, Display Int (rgthree), HuMoEmbeds, LoadAudio, LoadWanVideoT5TextEncoder, SimpleMath+, SoundFlow_GetLength, SoundFlow_TrimAudio, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WhisperModelLoader, easy int]
problems: []
missing: []
members: [图片生成/图生图/Humo双人合影（可多人）_1966919384042180609.json, 平台全量/Humo双人合影（可多人）_1977292011772497922.json, 平台全量/Humo电商展示+语音by Aiwood_1977302393060761601.json, 平台全量/Humo音频生视频-by Aiwood_1977303980827123713.json, 平台全量/ai MV_1968591393243451394.json, 数字人/数字人/Humo+Infinite talk多段MV直接生成_1968205970318962690.json, 数字人/数字人/Humo音频生视频_1970182473558728705.json, 数字人/数字人/ai MV应用版（圣诞mv）_1996113505415839746.json, 数字人/数字人/ai MV应用版（欧美乡村农场纪事）_1985967514435952642.json, 数字人/数字人/ai+MV应用版（字幕版西海岸）_1996501066583777281.json, 视频生成/图生视频/Humo+Infinite talk 单人参考生视频_2030181913666785281.json, 视频生成/图生视频/Humo+Infinite talk双人--最接近超能视频2.0参考生视频的工作流_2031536388583202818.json, 视频生成/图生视频/Humo+Infinite talk多段MV直接生成_1973740275090763777.json, 视频生成/图生视频/Humo+Infinite talk多段剧情一键生成_1969802648167849986.json, 视频生成/图生视频/Humo+InfiniteTalk 人物MV制作_1968324192087232514.json, 视频生成/图生视频/Humo分段直接生成MV_1968112609591459841.json, 视频生成/图生视频/Humo单人对口型By-Aiwood_1966919494457233409.json, 视频生成/图生视频/Humo单人对口型_1970095013608779777.json, 视频生成/图生视频/MV五分镜直接生成（WAN2.2 Humo+Infinite talk）_1973059244465500161.json, 视频生成/图生视频/字节_Humo高质量多模态视频生成工作流_2033171510558461953.json, 视频生成/图生视频/字节_Humo高质量多模态视频生成工作流（多参）_2031295926127566850.json, 视频生成/图生视频/开源最接近超能视频2.0参考图生视频：Humo+Infinite talk双人工作流_2026262067400941570.json, 视频生成/图生视频/开源最接近超能视频2.0参考生视频的工作流——Humo+Infinite talk双人_2022664705512316929.json, 视频生成/图生视频/开源最接近超能视频2.0参考生视频的工作流——Humo+Infinite talk双人_2034600586854801410.json, 视频生成/图生视频/开源最接近超能视频2.0参考生视频的工作流——Humo+Infinite talk双人_2041512808247988226.json, 视频生成/图生视频/最接近 超能视频2.0 参考生视频 的工作流——Humo+Infinite talk双人_2027669520621510658.json, 视频生成/图生视频/🔥开源最接近超能视频2.0参考生视频——双人_2046569919550066689.json, 视频生成/文生视频/双图参考生MTV三分镜视频 Humo+Infinite talk_2048690659820838913.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_35

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（图片生成/图生图/Humo双人合影（可多人）_1966919384042180609.json、平台全量/Humo双人合影（可多人）_1977292011772497922.json、平台全量/Humo电商展示+语音by Aiwood_1977302393060761601.json、平台全量/Humo音频生视频-by Aiwood_1977303980827123713.json、平台全量/ai MV_1968591393243451394.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 28 个 workflow 都包含：
- `AudioSeparation`
- `Display Int (rgthree)`
- `HuMoEmbeds`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `SoundFlow_GetLength`
- `SoundFlow_TrimAudio`
- `ToInt`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WhisperModelLoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 27/28 个有
- `LoadImage` —— 27/28 个有
- `INTConstant` —— 26/28 个有
- `ImageBatchMulti` —— 25/28 个有
- `easy imageRemBg` —— 25/28 个有
- `PreviewAudio` —— 23/28 个有
- `RecordAudio` —— 22/28 个有
- `MultiTalkModelLoader` —— 21/28 个有
- `ImageFromBatch` —— 20/28 个有
- `MultiTalkWav2VecEmbeds` —— 20/28 个有
- `WanVideoCombineEmbeds` —— 20/28 个有
- `WanVideoImageToVideoMultiTalk` —— 20/28 个有
- `Wav2VecModelLoader` —— 20/28 个有
- `PreviewImage` —— 16/28 个有
- `ImageConcanate` —— 15/28 个有
- `ImageAddMulti` —— 10/28 个有
- `AudioConcat` —— 8/28 个有
- `CreateCFGScheduleFloatList` —— 8/28 个有
- `PrimitiveFloat` —— 4/28 个有
- `CR Prompt Text` —— 3/28 个有
- `CR Text` —— 2/28 个有
- `JWInteger` —— 2/28 个有
- `Qwen3TTSModelLoader` —— 2/28 个有
- `Qwen3TTSVoiceDesign` —— 2/28 个有
- `SaveAudio` —— 2/28 个有
- `TextInput_` —— 2/28 个有
- `Add Subtitles To Frames` —— 1/28 个有
- `Apply Whisper` —— 1/28 个有
- `GetImageSizeAndCount` —— 1/28 个有
- `JWStringGetLine` —— 1/28 个有
- `JWStringSplit` —— 1/28 个有
- `JWStringToFloat` —— 1/28 个有
- `StringSubstring` —— 1/28 个有
- `TextBoxMira` —— 1/28 个有
- `TextBoxNode_UTK` —— 1/28 个有
- `easy mathInt` —— 1/28 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
