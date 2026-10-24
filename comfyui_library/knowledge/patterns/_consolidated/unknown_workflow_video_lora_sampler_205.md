---
name: unknown_workflow_video_lora_sampler_205
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.943333
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/超清数字人对口型音乐_2098282192836317186.json, 视频生成/图生视频/Wan Video InfiniteTalk  双人对话_1988149592183234562.json, 视频生成/图生视频/infinitetalk单人图像对口型_1983851965690056706.json, 视频生成/图生视频/infinitetalk单人图像数字人_1987800864440168449.json, 视频生成/图生视频/infinitetalk单人数字人 横版_2082717087134470145.json, 视频生成/图生视频/infinitetalk单人数字人_1961786018880012290.json, 视频生成/图生视频/infinitetalk双人对话（自动识别人物）_2035945836609277954.json, 视频生成/图生视频/infinitetalk图生视频数字人口播_2080575708149145601.json, 视频生成/图生视频/infinitetalk多段mv生成_1968146725170982914.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_205

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（数字人/数字人/超清数字人对口型音乐_2098282192836317186.json、视频生成/图生视频/Wan Video InfiniteTalk  双人对话_1988149592183234562.json、视频生成/图生视频/infinitetalk单人图像对口型_1983851965690056706.json、视频生成/图生视频/infinitetalk单人图像数字人_1987800864440168449.json、视频生成/图生视频/infinitetalk单人数字人 横版_2082717087134470145.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
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
- `LoadAudio` —— 8/9 个有
- `RH_GetAudioDuration` —— 8/9 个有
- `SimpleMath+` —— 8/9 个有
- `WanVideoTorchCompileSettings` —— 7/9 个有
- `easy showAnything` —— 7/9 个有
- `Int` —— 5/9 个有
- `ToInt` —— 5/9 个有
- `AudioCrop` —— 4/9 个有
- `PreviewAudio` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `SoundFlow_TrimAudio` —— 2/9 个有
- `CR Float To Integer` —— 1/9 个有
- `CR SDXL Aspect Ratio` —— 1/9 个有
- `Display Int (rgthree)` —— 1/9 个有
- `ImageBatchMulti` —— 1/9 个有
- `ImageFromBatch` —— 1/9 个有
- `ImpactFloat` —— 1/9 个有
- `MathExpression|pysssss` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `RHHiddenNodes` —— 1/9 个有
- `Text Multiline` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
