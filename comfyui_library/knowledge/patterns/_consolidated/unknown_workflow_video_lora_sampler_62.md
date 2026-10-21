---
name: unknown_workflow_video_lora_sampler_62
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.973444
common_nodes: [AudioSeparation, HuMoEmbeds, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [图片生成/文生图/ai MV应用版（30S福音）_2000822453771399170.json, 视频生成/图生视频/2030181913666785281.json, 视频生成/图生视频/2031536388583202818.json, 视频生成/图生视频/1973740275090763777.json, 视频生成/图生视频/1969802648167849986.json, 视频生成/图生视频/1968324192087232514.json, 视频生成/图生视频/1968112609591459841.json, 视频生成/图生视频/1966919494457233409.json, 视频生成/图生视频/1973059244465500161.json, 视频生成/图生视频/2033171510558461953.json, 视频生成/图生视频/2031295926127566850.json, 视频生成/图生视频/2026262067400941570.json, 视频生成/图生视频/2022664705512316929.json, 视频生成/图生视频/2034600586854801410.json, 视频生成/图生视频/2041512808247988226.json, 视频生成/图生视频/2027669520621510658.json, 视频生成/图生视频/2046569919550066689.json, 视频生成/文生视频/双图参考生MTV三分镜视频 Humo+Infinite talk_2048690659820838913.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_62

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/ai MV应用版（30S福音）_2000822453771399170.json、视频生成/图生视频/2030181913666785281.json、视频生成/图生视频/2031536388583202818.json、视频生成/图生视频/1973740275090763777.json、视频生成/图生视频/1969802648167849986.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 18 个 workflow 都包含：
- `AudioSeparation`
- `HuMoEmbeds`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
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

**可变部分**（部分 workflow 才有）：
- `Display Int (rgthree)` —— 17/18 个有
- `ImageBatchMulti` —— 17/18 个有
- `MultiTalkModelLoader` —— 17/18 个有
- `SimpleMath+` —— 17/18 个有
- `SoundFlow_GetLength` —— 17/18 个有
- `SoundFlow_TrimAudio` —— 17/18 个有
- `ToInt` —— 17/18 个有
- `easy int` —— 17/18 个有
- `ImageFromBatch` —— 16/18 个有
- `MultiTalkWav2VecEmbeds` —— 16/18 个有
- `WanVideoCombineEmbeds` —— 16/18 个有
- `WanVideoImageToVideoMultiTalk` —— 16/18 个有
- `Wav2VecModelLoader` —— 16/18 个有
- `easy imageRemBg` —— 16/18 个有
- `PreviewAudio` —— 15/18 个有
- `PreviewImage` —— 13/18 个有
- `RecordAudio` —— 13/18 个有
- `ImageAddMulti` —— 10/18 个有
- `ImageConcanate` —— 9/18 个有
- `AudioConcat` —— 8/18 个有
- `CR Prompt Text` —— 2/18 个有
- `CR Text` —— 2/18 个有
- `CreateCFGScheduleFloatList` —— 2/18 个有
- `PrimitiveFloat` —— 2/18 个有
- `Qwen3TTSModelLoader` —— 2/18 个有
- `Qwen3TTSVoiceDesign` —— 2/18 个有
- `SaveAudio` —— 2/18 个有
- `TextInput_` —— 2/18 个有
- `AudioCrop` —— 1/18 个有
- `AudioCropProcessUTK` —— 1/18 个有
- `CM_FloatUnaryOperation` —— 1/18 个有
- `JWStringGetLine` —— 1/18 个有
- `JWStringSplit` —— 1/18 个有
- `JWStringToFloat` —— 1/18 个有
- `MathExpression|pysssss` —— 1/18 个有
- `PrimitiveString` —— 1/18 个有
- `StringSubstring` —— 1/18 个有
- `TextBoxMira` —— 1/18 个有
- `TextBoxNode_UTK` —— 1/18 个有
- `easy showAnything` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
