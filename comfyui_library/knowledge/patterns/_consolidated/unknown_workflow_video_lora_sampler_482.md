---
name: unknown_workflow_video_lora_sampler_482
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9314
common_nodes: [CreateCFGScheduleFloatList, HuMoEmbeds, INTConstant, ImageResizeKJv2, LoadAudio, LoadImage, PreviewAudio, SimpleMath+, SoundFlow_GetLength, SoundFlow_TrimAudio, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader, WhisperModelLoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/Humo单人数字人_1967417931208515586.json, 视频生成/图生视频/电商带货，投喂产品图加模特即可_2037199894196264961.json, 视频生成/文生视频/Humo音频生视频-by Aiwood_1966919444201136129.json, 视频生成/文生视频/humo单图参考+配音_1968279752563937282.json, 音频生成/音频生成/12.Humo电商展示+语音_录音_2000793155027038209.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_482

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Humo单人数字人_1967417931208515586.json、视频生成/图生视频/电商带货，投喂产品图加模特即可_2037199894196264961.json、视频生成/文生视频/Humo音频生视频-by Aiwood_1966919444201136129.json、视频生成/文生视频/humo单图参考+配音_1968279752563937282.json、音频生成/音频生成/12.Humo电商展示+语音_录音_2000793155027038209.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `HuMoEmbeds`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `PreviewAudio`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WhisperModelLoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `AudioSeparation` —— 4/5 个有
- `Display Int (rgthree)` —— 4/5 个有
- `ImageBatchMulti` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `ImageConcanate` —— 3/5 个有
- `LoadWanVideoT5TextEncoder` —— 3/5 个有
- `RecordAudio` —— 3/5 个有
- `WanVideoTextEncode` —— 3/5 个有
- `easy imageRemBg` —— 3/5 个有
- `WanVideoSetBlockSwap` —— 2/5 个有
- `WanVideoSetLoRAs` —— 2/5 个有
- `WanVideoTextEncodeCached` —— 2/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `MelBandRoFormerModelLoader` —— 1/5 个有
- `MelBandRoFormerSampler` —— 1/5 个有
- `NormalizeAudioLoudness` —— 1/5 个有
- `PrimitiveStringMultiline` —— 1/5 个有
- `SaveImage` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
