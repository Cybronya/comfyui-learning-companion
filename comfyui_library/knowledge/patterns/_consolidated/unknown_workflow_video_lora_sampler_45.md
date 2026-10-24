---
name: unknown_workflow_video_lora_sampler_45
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.979
common_nodes: [AudioSeparation, Display Int (rgthree), HuMoEmbeds, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, PreviewAudio, SimpleMath+, SoundFlow_GetLength, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WhisperModelLoader, easy imageRemBg, easy int]
problems: []
missing: []
members: [图片生成/图生图/Humo双人合影（可多人）_1966919384042180609.json, 视频生成/图生视频/Humo+Infinite talk 单人参考生视频_2030181913666785281.json, 视频生成/图生视频/Humo+Infinite talk双人--最接近超能视频2.0参考生视频的工作流_2031536388583202818.json, 视频生成/图生视频/Humo+Infinite talk多段MV直接生成_1973740275090763777.json, 视频生成/图生视频/Humo+Infinite talk多段剧情一键生成_1969802648167849986.json, 视频生成/图生视频/Humo+InfiniteTalk 人物MV制作_1968324192087232514.json, 视频生成/图生视频/Humo分段直接生成MV_1968112609591459841.json, 视频生成/图生视频/Humo单人对口型By-Aiwood_1966919494457233409.json, 视频生成/图生视频/Humo单人对口型_1970095013608779777.json, 视频生成/图生视频/Humo电商展示+语音_2015598941240299522.json, 视频生成/图生视频/Humo电商展示+语音by Aiwood_1966919364043739138.json, 视频生成/图生视频/Humo电商展示+语音by+Aiwood_2037340771631767553.json, 视频生成/图生视频/Humo电商展示+语音生成_2051558209323839489.json, 视频生成/图生视频/Humo电商展示+语音生成_2052711289109139457.json, 视频生成/图生视频/Humo电商展示+语音生成_2069759679651209218.json, 视频生成/图生视频/Humo电商带货视频制作_1994443189438324738.json, 视频生成/图生视频/MV五分镜直接生成（WAN2.2 Humo+Infinite talk）_1973059244465500161.json, 视频生成/图生视频/上传音频生成对应口播视频—Humo+Infinite+talk 优化后_2034484341866237954.json, 视频生成/图生视频/上传音频生成对应口播视频—Humo+Infinite+talk_2029082504245809153.json, 视频生成/图生视频/上传音频生成对应口播视频—Humo+Infinite+talk_2032263750392225793.json, 视频生成/图生视频/电商专用：口播视频—Humo+Infinite talk+IndexTTS_2028749472515235842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_45

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/Humo双人合影（可多人）_1966919384042180609.json、视频生成/图生视频/Humo+Infinite talk 单人参考生视频_2030181913666785281.json、视频生成/图生视频/Humo+Infinite talk双人--最接近超能视频2.0参考生视频的工作流_2031536388583202818.json、视频生成/图生视频/Humo+Infinite talk多段MV直接生成_1973740275090763777.json、视频生成/图生视频/Humo+Infinite talk多段剧情一键生成_1969802648167849986.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 21 个 workflow 都包含：
- `AudioSeparation`
- `Display Int (rgthree)`
- `HuMoEmbeds`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewAudio`
- `SimpleMath+`
- `SoundFlow_GetLength`
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
- `easy imageRemBg`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 20/21 个有
- `SoundFlow_TrimAudio` —— 20/21 个有
- `ImageBatchMulti` —— 19/21 个有
- `RecordAudio` —— 13/21 个有
- `CreateCFGScheduleFloatList` —— 11/21 个有
- `ImageConcanate` —— 11/21 个有
- `MultiTalkModelLoader` —— 11/21 个有
- `PreviewImage` —— 11/21 个有
- `ImageFromBatch` —— 10/21 个有
- `MultiTalkWav2VecEmbeds` —— 10/21 个有
- `WanVideoCombineEmbeds` —— 10/21 个有
- `WanVideoImageToVideoMultiTalk` —— 10/21 个有
- `Wav2VecModelLoader` —— 10/21 个有
- `Display Any (rgthree)` —— 4/21 个有
- `HAIGC_VideoLastFrame` —— 4/21 个有
- `Seed_` —— 4/21 个有
- `Text` —— 4/21 个有
- `ToFloat` —— 4/21 个有
- `WanVideoEncode` —— 4/21 个有
- `CR Prompt Text` —— 2/21 个有
- `AudioBeforeAfterSilence` —— 1/21 个有
- `AudioConcat` —— 1/21 个有
- `ImageAddMulti` —— 1/21 个有
- `JWImageBatchCount` —— 1/21 个有
- `JWInteger` —— 1/21 个有
- `MaxNode` —— 1/21 个有
- `PrimitiveFloat` —— 1/21 个有
- `TextBoxNode_UTK` —— 1/21 个有
- `ZML_ImageBatchToInt` —— 1/21 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/21 个有
- `easy indexTTSGenerateSimple` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
