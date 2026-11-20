---
name: unknown_workflow_video_lora_sampler_203
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.954417
common_nodes: [CreateCFGScheduleFloatList, HuMoEmbeds, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, PreviewAudio, SimpleMath+, SoundFlow_GetLength, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader, WhisperModelLoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/Humo单人数字人_1967417931208515586.json, 视频生成/图生视频/Humo电商展示+语音_2015598941240299522.json, 视频生成/图生视频/Humo电商展示+语音by Aiwood_1966919364043739138.json, 视频生成/图生视频/Humo电商展示+语音by+Aiwood_2037340771631767553.json, 视频生成/图生视频/Humo电商展示+语音生成_2051558209323839489.json, 视频生成/图生视频/Humo电商展示+语音生成_2052711289109139457.json, 视频生成/图生视频/Humo电商展示+语音生成_2069759679651209218.json, 视频生成/图生视频/Humo电商带货视频制作_1994443189438324738.json, 视频生成/图生视频/电商带货，投喂产品图加模特即可_2037199894196264961.json, 视频生成/文生视频/Humo音频生视频-by Aiwood_1966919444201136129.json, 视频生成/文生视频/humo单图参考+配音_1968279752563937282.json, 音频生成/音频生成/12.Humo电商展示+语音_录音_2000793155027038209.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_203

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Humo单人数字人_1967417931208515586.json、视频生成/图生视频/Humo电商展示+语音_2015598941240299522.json、视频生成/图生视频/Humo电商展示+语音by Aiwood_1966919364043739138.json、视频生成/图生视频/Humo电商展示+语音by+Aiwood_2037340771631767553.json、视频生成/图生视频/Humo电商展示+语音生成_2051558209323839489.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 12 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `HuMoEmbeds`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WhisperModelLoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 11/12 个有
- `Display Int (rgthree)` —— 11/12 个有
- `ImageBatchMulti` —— 11/12 个有
- `PreviewImage` —— 11/12 个有
- `SoundFlow_TrimAudio` —— 11/12 个有
- `ImageConcanate` —— 10/12 个有
- `LoadWanVideoT5TextEncoder` —— 10/12 个有
- `WanVideoTextEncode` —— 10/12 个有
- `easy imageRemBg` —— 10/12 个有
- `RecordAudio` —— 9/12 个有
- `WanVideoSetBlockSwap` —— 2/12 个有
- `WanVideoSetLoRAs` —— 2/12 个有
- `WanVideoTextEncodeCached` —— 2/12 个有
- `ImageConcatMulti` —— 1/12 个有
- `MelBandRoFormerModelLoader` —— 1/12 个有
- `MelBandRoFormerSampler` —— 1/12 个有
- `NormalizeAudioLoudness` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `SaveImage` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
