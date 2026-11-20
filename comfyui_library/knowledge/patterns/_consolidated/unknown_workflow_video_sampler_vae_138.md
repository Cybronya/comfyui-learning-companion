---
name: unknown_workflow_video_sampler_vae_138
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.78725
common_nodes: [GetImageSizeAndCount, ImageResize+, Int, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/【丝滑】Wan2.1-VACE-14B首尾帧动画（超详细讲解）_1923066679113543681.json, 平台全量/WAN VACE14B视频扩展_1926212777210245121.json, 平台全量/【视频扩展】Wan2.1_VACE-14B_1924847854966218754.json, 平台全量/视频画面扩展FusionX VACE 极速版（可竖屏改横屏）_1922847248160538626.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_138

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【丝滑】Wan2.1-VACE-14B首尾帧动画（超详细讲解）_1923066679113543681.json、平台全量/WAN VACE14B视频扩展_1926212777210245121.json、平台全量/【视频扩展】Wan2.1_VACE-14B_1924847854966218754.json、平台全量/视频画面扩展FusionX VACE 极速版（可竖屏改横屏）_1922847248160538626.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `GetImageSizeAndCount`
- `ImageResize+`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `ImagePadForOutpaint` —— 3/4 个有
- `ImageToMask` —— 3/4 个有
- `InpaintPreprocessor` —— 3/4 个有
- `MaskToImage` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `RepeatImageBatch` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `WanVideoLoraSelect` —— 3/4 个有
- `WanVideoSetBlockSwap` —— 3/4 个有
- `WanVideoTeaCache` —— 3/4 个有
- `WanVideoVACEModelSelect` —— 3/4 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/4 个有
- `GIMMVFI_interpolate` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `Note _O` —— 1/4 个有
- `WanVideoEnhanceAVideo` —— 1/4 个有
- `WanVideoMagCache` —— 1/4 个有
- `WanVideoVACEStartToEndFrame` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
