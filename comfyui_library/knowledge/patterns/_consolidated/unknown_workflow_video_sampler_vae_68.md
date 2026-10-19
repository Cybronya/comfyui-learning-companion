---
name: unknown_workflow_video_sampler_vae_68
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.690429
common_nodes: [GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1923394290066575361.json, 视频生成/图生视频/1923694325656711169.json, 视频生成/图生视频/1934473934488162306.json, 视频生成/图生视频/1925467982229590018.json, 视频生成/图生视频/1932748571013697538.json, 视频生成/图生视频/1923563550629875714.json, 视频生成/图生视频/1936291028129206274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_68

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1923394290066575361.json、视频生成/图生视频/1923694325656711169.json、视频生成/图生视频/1934473934488162306.json、视频生成/图生视频/1925467982229590018.json、视频生成/图生视频/1932748571013697538.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 7 个 workflow 都包含：
- `GetImageSizeAndCount`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `WanVideoLoraSelect` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `WanVideoVACEStartToEndFrame` —— 6/7 个有
- `AddLabel` —— 5/7 个有
- `EmptyImage` —— 5/7 个有
- `ImageConcatMulti` —— 5/7 个有
- `VHS_LoadVideo` —— 5/7 个有
- `ImageResizeKJv2` —— 4/7 个有
- `Bookmark (rgthree)` —— 3/7 个有
- `Label (rgthree)` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `ImageResizeKJ` —— 2/7 个有
- `WanVideoUniAnimateDWPoseDetector` —— 2/7 个有
- `INTConstant` —— 1/7 个有
- `ImagePadKJ` —— 1/7 个有
- `ImageResize+` —— 1/7 个有
- `MimicMotionGetPoses` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `String Literal` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `VHS_VideoInfo` —— 1/7 个有
- `WanVideoEnhanceAVideo` —— 1/7 个有
- `WanVideoVRAMManagement` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
