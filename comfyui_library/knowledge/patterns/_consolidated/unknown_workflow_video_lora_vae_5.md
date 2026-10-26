---
name: unknown_workflow_video_lora_vae_5
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.845
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/最强数字人InfiniteTalk_1986044446821285890.json, 视频生成/图生视频/最新最好的数字人infinitetalk单人_1960712411261153281.json, 视频生成/图生视频/最新最秀infinitetalk单人数字人_1958010362488565762.json, 视频生成/图生视频/电商生成高动态数字人  wan21 rcm_2011973447630462977.json, 视频生成/图生视频/自制-MultiTalk v2 不运镜版_1941390808585236482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae_5

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/最强数字人InfiniteTalk_1986044446821285890.json、视频生成/图生视频/最新最好的数字人infinitetalk单人_1960712411261153281.json、视频生成/图生视频/最新最秀infinitetalk单人数字人_1958010362488565762.json、视频生成/图生视频/电商生成高动态数字人  wan21 rcm_2011973447630462977.json、视频生成/图生视频/自制-MultiTalk v2 不运镜版_1941390808585236482.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
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
- `MultiTalkWav2VecEmbeds` —— 4/5 个有
- `WanVideoImageToVideoMultiTalk` —— 4/5 个有
- `WanVideoSampler` —— 4/5 个有
- `INTConstant` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `PrimitiveStringMultiline` —— 2/5 个有
- `Bjornulf_ShowStringText` —— 1/5 个有
- `FloatConstant` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `ImageUpscaleWithModel` —— 1/5 个有
- `JWFloatToString` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `MathExpression|pysssss` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
