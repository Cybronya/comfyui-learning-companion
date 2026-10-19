---
name: unknown_workflow_video_lora_sampler_51
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.9794
common_nodes: [AudioSeparation, Display Int (rgthree), HuMoEmbeds, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, PreviewAudio, SimpleMath+, SoundFlow_GetLength, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WhisperModelLoader, easy imageRemBg, easy int]
problems: []
missing: []
members: [视频生成/图生视频/2030181913666785281.json, 视频生成/图生视频/2031536388583202818.json, 视频生成/图生视频/1973740275090763777.json, 视频生成/图生视频/1969802648167849986.json, 视频生成/图生视频/1968324192087232514.json, 视频生成/图生视频/1968112609591459841.json, 视频生成/图生视频/1966919494457233409.json, 视频生成/图生视频/1970095013608779777.json, 视频生成/图生视频/2015598941240299522.json, 视频生成/图生视频/1966919364043739138.json, 视频生成/图生视频/2037340771631767553.json, 视频生成/图生视频/2051558209323839489.json, 视频生成/图生视频/2052711289109139457.json, 视频生成/图生视频/2069759679651209218.json, 视频生成/图生视频/1994443189438324738.json, 视频生成/图生视频/1973059244465500161.json, 视频生成/图生视频/2034484341866237954.json, 视频生成/图生视频/2029082504245809153.json, 视频生成/图生视频/2032263750392225793.json, 视频生成/图生视频/2028749472515235842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_51

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/2030181913666785281.json、视频生成/图生视频/2031536388583202818.json、视频生成/图生视频/1973740275090763777.json、视频生成/图生视频/1969802648167849986.json、视频生成/图生视频/1968324192087232514.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 20 个 workflow 都包含：
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
- `INTConstant` —— 19/20 个有
- `SoundFlow_TrimAudio` —— 19/20 个有
- `ImageBatchMulti` —— 18/20 个有
- `RecordAudio` —— 12/20 个有
- `MultiTalkModelLoader` —— 11/20 个有
- `CreateCFGScheduleFloatList` —— 10/20 个有
- `ImageConcanate` —— 10/20 个有
- `ImageFromBatch` —— 10/20 个有
- `MultiTalkWav2VecEmbeds` —— 10/20 个有
- `PreviewImage` —— 10/20 个有
- `WanVideoCombineEmbeds` —— 10/20 个有
- `WanVideoImageToVideoMultiTalk` —— 10/20 个有
- `Wav2VecModelLoader` —— 10/20 个有
- `Display Any (rgthree)` —— 4/20 个有
- `HAIGC_VideoLastFrame` —— 4/20 个有
- `Seed_` —— 4/20 个有
- `Text` —— 4/20 个有
- `ToFloat` —— 4/20 个有
- `WanVideoEncode` —— 4/20 个有
- `CR Prompt Text` —— 2/20 个有
- `AudioBeforeAfterSilence` —— 1/20 个有
- `AudioConcat` —— 1/20 个有
- `ImageAddMulti` —— 1/20 个有
- `JWImageBatchCount` —— 1/20 个有
- `JWInteger` —— 1/20 个有
- `MaxNode` —— 1/20 个有
- `PrimitiveFloat` —— 1/20 个有
- `TextBoxNode_UTK` —— 1/20 个有
- `ZML_ImageBatchToInt` —— 1/20 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/20 个有
- `easy indexTTSGenerateSimple` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
