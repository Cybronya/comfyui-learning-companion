---
name: unknown_workflow_video_sampler_vae_38
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.809
common_nodes: [ImageResize+, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/03-04-02-WAN2.1-首尾帧生成视频-FLF2V-kijai_1989234731780804609.json, 视频生成/图生视频/03-04-05-WAN2.1-首尾帧生成视频-FUN-INP-14B-kijai_1989234577744990209.json, 视频生成/图生视频/FLF2V首尾帧-wan视频_1913077859026698242.json, 视频生成/图生视频/Wan 2.1 FLF2V模型高动态优化版首尾帧V2_1912568927808094209.json, 视频生成/图生视频/Wan2.1 FLF2V 首尾帧生视频_1928288843513118721.json, 视频生成/图生视频/Wan2.1 Fun FLF2V 首尾帧生视频 Kijai_1930856714751684610.json, 视频生成/图生视频/Wan首尾帧视频生成-kijai版_1904901928008994817.json, 视频生成/图生视频/【Wan2.1系列】FLF2V首尾帧生成视频工作流_1920112646744641537.json, 视频生成/图生视频/【Wan2.1系列】首尾帧生成视频之Fun V1.1 Inp模型 _ 一键生成创意视频！_1920718476594315266.json, 视频生成/图生视频/【首尾帧】Wan2.1 FLF2V首尾帧工作流-KJ版_1913886030926180353.json, 视频生成/图生视频/万相视频Wan2.1超级首尾帧控制_1905171860894437377.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_38

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/03-04-02-WAN2.1-首尾帧生成视频-FLF2V-kijai_1989234731780804609.json、视频生成/图生视频/03-04-05-WAN2.1-首尾帧生成视频-FUN-INP-14B-kijai_1989234577744990209.json、视频生成/图生视频/FLF2V首尾帧-wan视频_1913077859026698242.json、视频生成/图生视频/Wan 2.1 FLF2V模型高动态优化版首尾帧V2_1912568927808094209.json、视频生成/图生视频/Wan2.1 FLF2V 首尾帧生视频_1928288843513118721.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
- `ImageResize+`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoClipTextEncoder` —— 9/11 个有
- `WanVideoExperimentalArgs` —— 9/11 个有
- `WanVideoTorchCompileSettings` —— 9/11 个有
- `GetImageSizeAndCount` —— 8/11 个有
- `SetNode` —— 8/11 个有
- `AddLabel` —— 7/11 个有
- `EmptyImage` —— 7/11 个有
- `GetNode` —— 7/11 个有
- `ImageConcatMulti` —— 7/11 个有
- `WanVideoVRAMManagement` —— 7/11 个有
- `CLIPVisionLoader` —— 6/11 个有
- `WanVideoEnhanceAVideo` —— 4/11 个有
- `CLIPLoader` —— 3/11 个有
- `CLIPTextEncode` —— 3/11 个有
- `WanVideoTextEmbedBridge` —— 3/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `Note Plus (mtb)` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `DF_Integer` —— 1/11 个有
- `ImageUpscaleWithModel` —— 1/11 个有
- `LayerUtility: PurgeVRAM` —— 1/11 个有
- `Text Multiline` —— 1/11 个有
- `Upscale Model Loader` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有
- `easy clearCacheAll` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
