---
name: unknown_workflow_video_sampler_vae_60
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.993778
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/VACE视频转绘美女跳舞_1909879938038624257.json, 视频生成/图生视频/VACE首尾帧图生视频_1915435031794487298.json, 视频生成/图生视频/wan 2.1  视频编辑vace工作流_1907301627349622785.json, 视频生成/图生视频/万相VACE1.3B首尾帧图生视频_1917476719106920449.json, 视频生成/图生视频/万相VACE14B首尾帧图生视频_1929004971717726210.json, 视频生成/图生视频/万相WanVACE-14B图生视频_1923968706664460289.json, 视频生成/图生视频/万相WanVACE-14B首尾帧图生视频_1924687673779212289.json, 视频生成/图生视频/图生视频--VACE14B正式版【动作迁移&图片跳舞】_2057296595577823234.json, 视频生成/图生视频/最新wan2.1 14B视频重绘动作迁移参考图片_1926800707893010433.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_60

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/VACE视频转绘美女跳舞_1909879938038624257.json、视频生成/图生视频/VACE首尾帧图生视频_1915435031794487298.json、视频生成/图生视频/wan 2.1  视频编辑vace工作流_1907301627349622785.json、视频生成/图生视频/万相VACE1.3B首尾帧图生视频_1917476719106920449.json、视频生成/图生视频/万相VACE14B首尾帧图生视频_1929004971717726210.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 9 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTeaCache` —— 8/9 个有
- `WanVideoBlockSwap` —— 6/9 个有
- `WanVideoExperimentalArgs` —— 6/9 个有
- `Int` —— 5/9 个有
- `WanVideoEnhanceAVideo` —— 5/9 个有
- `WanVideoSLG` —— 5/9 个有
- `WanVideoVACEModelSelect` —— 5/9 个有
- `AIO_Preprocessor` —— 4/9 个有
- `VHS_LoadVideo` —— 4/9 个有
- `WanVideoVACEStartToEndFrame` —— 4/9 个有
- `TextInput_` —— 3/9 个有
- `GetImageSizeAndCount` —— 1/9 个有
- `LayerMask: LoadFlorence2Model` —— 1/9 个有
- `LayerUtility: Florence2Image2Prompt` —— 1/9 个有
- `LayerUtility: PurgeVRAM` —— 1/9 个有
- `PreviewImage` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
