---
name: unknown_workflow_video_lora_vae_3
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.790333
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1986044446821285890.json, 视频生成/图生视频/1958010362488565762.json, 视频生成/图生视频/1958019974432534529.json, 视频生成/图生视频/2011973447630462977.json, 视频生成/图生视频/1941000380694294529.json, 视频生成/图生视频/1941390808585236482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae_3

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1986044446821285890.json、视频生成/图生视频/1958010362488565762.json、视频生成/图生视频/1958019974432534529.json、视频生成/图生视频/2011973447630462977.json、视频生成/图生视频/1941000380694294529.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `MultiTalkWav2VecEmbeds` —— 5/6 个有
- `WanVideoImageToVideoMultiTalk` —— 5/6 个有
- `WanVideoSampler` —— 5/6 个有
- `INTConstant` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 4/6 个有
- `GetNode` —— 2/6 个有
- `MaskPreview+` —— 2/6 个有
- `MathExpression|pysssss` —— 2/6 个有
- `SeparateMasks` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `Bjornulf_ShowStringText` —— 1/6 个有
- `FloatConstant` —— 1/6 个有
- `Int2String` —— 1/6 个有
- `JWFloatToString` —— 1/6 个有
- `MaskPreview` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
