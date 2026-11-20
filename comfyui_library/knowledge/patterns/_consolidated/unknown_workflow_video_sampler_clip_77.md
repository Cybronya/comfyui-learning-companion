---
name: unknown_workflow_video_sampler_clip_77
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.495375
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJ, LoadImage, SetNode, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoDiffusionForcingSampler, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoTeaCache, WanVideoTextEmbedBridge, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/AI电影一镜到底无限时长——skyreels_DF_1914826098448789506.json, 平台全量/视频变长（实测5秒变30秒）SkyReels V2_1916394711811031041.json, 视频生成/图生视频/25-04-25 skyreels_df_生成超长视频_1915096994971586561.json, 视频生成/图生视频/For循环无限长度视频生成-SkyReels-V2_1915667745395118081.json, 视频生成/图生视频/SkyReels DF 14B扩散强制模型长视频生成V1_1914710497503997953.json, 视频生成/图生视频/SkyReels DF 14B扩散强制模型长视频生成_1914972676837048321.json, 视频生成/图生视频/SkyReels V2突破AI视频5秒魔咒-无限时长电影级视频_1914635301778616321.json, 视频生成/图生视频/SkyReels V2视频生成_1914863994480357378.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_77

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/AI电影一镜到底无限时长——skyreels_DF_1914826098448789506.json、平台全量/视频变长（实测5秒变30秒）SkyReels V2_1916394711811031041.json、视频生成/图生视频/25-04-25 skyreels_df_生成超长视频_1915096994971586561.json、视频生成/图生视频/For循环无限长度视频生成-SkyReels-V2_1915667745395118081.json、视频生成/图生视频/SkyReels DF 14B扩散强制模型长视频生成V1_1914710497503997953.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：50%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJ`
- `LoadImage`
- `SetNode`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoDiffusionForcingSampler`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `WanVideoTextEmbedBridge`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageBatchMulti` —— 7/8 个有
- `VHS_LoadVideo` —— 7/8 个有
- `LoadWanVideoT5TextEncoder` —— 6/8 个有
- `WanVideoTextEncode` —— 6/8 个有
- `WanVideoVRAMManagement` —— 5/8 个有
- `PreviewImage` —— 3/8 个有
- `Primitive integer [Crystools]` —— 2/8 个有
- `easy clearCacheAll` —— 2/8 个有
- `LayerUtility: PurgeVRAM V2` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `String Literal` —— 1/8 个有
- `Text Load Line From File` —— 1/8 个有
- `VHS_VideoInfo` —— 1/8 个有
- `easy batchAnything` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy forLoopEnd` —— 1/8 个有
- `easy forLoopStart` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
