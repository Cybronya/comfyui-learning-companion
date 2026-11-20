---
name: unknown_workflow_video_sampler_vae_210
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CR Text, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, LayerUtility: PurgeVRAM V2, LoadWanVideoT5TextEncoder, RH_OneShot_Prompter, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoMagCache, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/最强文生视频FusionX最强文生视频+自动扩写提示词+补针流畅运行万相wan2.1_1933801723888586754.json, 视频生成/图生视频/精致图生视频FusionX+VACE万相wan2.1加补帧流畅加速版_1933792108618633218.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_210

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/最强文生视频FusionX最强文生视频+自动扩写提示词+补针流畅运行万相wan2.1_1933801723888586754.json、视频生成/图生视频/精致图生视频FusionX+VACE万相wan2.1加补帧流畅加速版_1933792108618633218.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `LayerUtility: PurgeVRAM V2`
- `LoadWanVideoT5TextEncoder`
- `RH_OneShot_Prompter`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoMagCache`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 1/2 个有
- `Int` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `WanVideoEmptyEmbeds` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有
- `WanVideoVACEEncode` —— 1/2 个有
- `WanVideoVACEStartToEndFrame` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
