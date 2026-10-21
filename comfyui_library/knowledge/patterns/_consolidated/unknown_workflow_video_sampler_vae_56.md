---
name: unknown_workflow_video_sampler_vae_56
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.852625
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1913525261151760386.json, 视频生成/图生视频/1916010425433915394.json, 视频生成/图生视频/1919056662093561858.json, 视频生成/图生视频/1929726931179094017.json, 视频生成/图生视频/1909246222736236546.json, 视频生成/图生视频/1913807733877895170.json, 视频生成/图生视频/1948931774743814145.json, 视频生成/图生视频/1949337300036661249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_56

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1913525261151760386.json、视频生成/图生视频/1916010425433915394.json、视频生成/图生视频/1919056662093561858.json、视频生成/图生视频/1929726931179094017.json、视频生成/图生视频/1909246222736236546.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 8 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoExperimentalArgs` —— 7/8 个有
- `LoadWanVideoClipTextEncoder` —— 6/8 个有
- `WanVideoSLG` —— 6/8 个有
- `WanVideoTorchCompileSettings` —— 6/8 个有
- `VHS_LoadVideo` —— 5/8 个有
- `Florence2ModelLoader` —— 4/8 个有
- `Florence2Run` —— 4/8 个有
- `WanVideoEncode` —— 4/8 个有
- `GetNode` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `WanVideoControlEmbeds` —— 3/8 个有
- `WanVideoLoraSelect` —— 3/8 个有
- `Anything Everywhere` —— 2/8 个有
- `CLIPVisionLoader` —— 2/8 个有
- `DisplayAny` —— 2/8 个有
- `ImagePadForOutpaint` —— 2/8 个有
- `ImageResize+` —— 2/8 个有
- `KepStringLiteral` —— 2/8 个有
- `LayerUtility: PurgeVRAM` —— 2/8 个有
- `AIO_Preprocessor` —— 1/8 个有
- `DF_Integer` —— 1/8 个有
- `Evaluate Integers` —— 1/8 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/8 个有
- `WanVideoUni3C_embeds` —— 1/8 个有
- `WanVideoUniAnimateDWPoseDetector` —— 1/8 个有
- `WanVideoUniAnimatePoseInput` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
