---
name: unknown_workflow_video_lora_sampler_139
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.96525
common_nodes: [AudioSeparation, CreateCFGScheduleFloatList, Display Int (rgthree), HuMoEmbeds, ImageResizeKJv2, LoadAudio, LoadImage, PreviewAudio, SimpleMath+, SoundFlow_GetLength, ToInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader, WhisperModelLoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/1970095013608779777.json, 视频生成/图生视频/1967417931208515586.json, 视频生成/图生视频/2015598941240299522.json, 视频生成/图生视频/1966919364043739138.json, 视频生成/图生视频/2037340771631767553.json, 视频生成/图生视频/2051558209323839489.json, 视频生成/图生视频/2052711289109139457.json, 视频生成/图生视频/2069759679651209218.json, 视频生成/图生视频/1994443189438324738.json, 视频生成/图生视频/2037199894196264961.json, 视频生成/文生视频/1966919444201136129.json, 音频生成/音频生成/12.Humo电商展示+语音_录音_2000793155027038209.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_139

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1970095013608779777.json、视频生成/图生视频/1967417931208515586.json、视频生成/图生视频/2015598941240299522.json、视频生成/图生视频/1966919364043739138.json、视频生成/图生视频/2037340771631767553.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 12 个 workflow 都包含：
- `AudioSeparation`
- `CreateCFGScheduleFloatList`
- `Display Int (rgthree)`
- `HuMoEmbeds`
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
- `INTConstant` —— 11/12 个有
- `ImageConcanate` —— 11/12 个有
- `LoadWanVideoT5TextEncoder` —— 11/12 个有
- `SoundFlow_TrimAudio` —— 11/12 个有
- `WanVideoTextEncode` —— 11/12 个有
- `easy imageRemBg` —— 11/12 个有
- `ImageBatchMulti` —— 10/12 个有
- `PreviewImage` —— 10/12 个有
- `RecordAudio` —— 9/12 个有
- `CR Prompt Text` —— 1/12 个有
- `ImageConcatMulti` —— 1/12 个有
- `JWInteger` —— 1/12 个有
- `PrimitiveFloat` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `WanVideoSetBlockSwap` —— 1/12 个有
- `WanVideoSetLoRAs` —— 1/12 个有
- `WanVideoTextEncodeCached` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
