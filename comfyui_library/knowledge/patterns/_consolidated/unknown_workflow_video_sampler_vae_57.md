---
name: unknown_workflow_video_sampler_vae_57
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.71825
common_nodes: [GetNode, Int, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1929028780692770818.json, 视频生成/图生视频/1929901376015601665.json, 视频生成/图生视频/1925152993048469505.json, 视频生成/图生视频/1938242650158071810.json, 视频生成/图生视频/1948012879831269378.json, 视频生成/图生视频/2041108387424899074.json, 视频生成/图生视频/1959825451453722625.json, 视频生成/图生视频/1957430449545080834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_57

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1929028780692770818.json、视频生成/图生视频/1929901376015601665.json、视频生成/图生视频/1925152993048469505.json、视频生成/图生视频/1938242650158071810.json、视频生成/图生视频/1948012879831269378.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 8 个 workflow 都包含：
- `GetNode`
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 7/8 个有
- `RHHiddenNodes` —— 7/8 个有
- `JjkText` —— 6/8 个有
- `ColorMatch` —— 5/8 个有
- `GetImageSizeAndCount` —— 5/8 个有
- `WanVideoLoraSelect` —— 5/8 个有
- `WanVideoVACEStartToEndFrame` —— 5/8 个有
- `AIO_Preprocessor` —— 4/8 个有
- `VHS_LoadVideo` —— 4/8 个有
- `DepthAnything_V2` —— 3/8 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 3/8 个有
- `ImageBlur` —— 3/8 个有
- `RH_Captioner` —— 3/8 个有
- `RH_Prompter` —— 3/8 个有
- `VHS_VideoInfoLoaded` —— 3/8 个有
- `WanVideoExperimentalArgs` —— 3/8 个有
- `WanVideoSLG` —— 3/8 个有
- `CM_IntBinaryOperation` —— 2/8 个有
- `Florence2ModelLoader` —— 2/8 个有
- `Florence2Run` —— 2/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `JWInteger` —— 2/8 个有
- `LayerColor: ColorAdapter` —— 1/8 个有
- `LoadAudio` —— 1/8 个有
- `ZipNode` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
