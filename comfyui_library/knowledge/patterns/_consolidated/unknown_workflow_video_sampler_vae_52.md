---
name: unknown_workflow_video_sampler_vae_52
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 1
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/VACE首尾帧图生视频_1915435031794487298.json, 视频生成/图生视频/万相VACE1.3B首尾帧图生视频_1917476719106920449.json, 视频生成/图生视频/万相VACE14B首尾帧图生视频_1929004971717726210.json, 视频生成/图生视频/万相WanVACE-14B图生视频_1923968706664460289.json, 视频生成/图生视频/万相WanVACE-14B首尾帧图生视频_1924687673779212289.json, 视频生成/图生视频/热门AI视频拆解之小明剑魔_1918479213039386625.json, 视频生成/图生视频/首尾帧-(Wan2.1-VACE-14B)_1923033044188319745.json, 视频生成/文生视频/CausVid-3步720文生视频(Wan2.1&MoviiGen&Skyreels)_1923393888814624770.json, 视频生成/文生视频/Self Forcing-文生图&图生视频_1933051482759630849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_52

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/VACE首尾帧图生视频_1915435031794487298.json、视频生成/图生视频/万相VACE1.3B首尾帧图生视频_1917476719106920449.json、视频生成/图生视频/万相VACE14B首尾帧图生视频_1929004971717726210.json、视频生成/图生视频/万相WanVACE-14B图生视频_1923968706664460289.json、视频生成/图生视频/万相WanVACE-14B首尾帧图生视频_1924687673779212289.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 9 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `WanVideoTorchCompileSettings` —— 8/9 个有
- `WanVideoBlockSwap` —— 7/9 个有
- `WanVideoExperimentalArgs` —— 7/9 个有
- `WanVideoVACEModelSelect` —— 7/9 个有
- `WanVideoVACEStartToEndFrame` —— 7/9 个有
- `WanVideoEnhanceAVideo` —— 6/9 个有
- `WanVideoSLG` —— 6/9 个有
- `Int` —— 5/9 个有
- `GetImageSizeAndCount` —— 3/9 个有
- `INTConstant` —— 3/9 个有
- `String Literal` —— 3/9 个有
- `DepthAnythingPreprocessor` —— 1/9 个有
- `LayerMask: LoadFlorence2Model` —— 1/9 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/9 个有
- `LayerUtility: PurgeVRAM` —— 1/9 个有
- `RH_Captioner` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有
- `WanVideoLoraSelect` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
