---
name: unknown_workflow_video_sampler_vae_62
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.898625
common_nodes: [LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan-VACE-图生视频_1933481916970487810.json, 平台全量/CausVid-3步720P视频扩展(Wan2.1&MoviiGen&Skyreels)_1923429151527587842.json, 平台全量/WAN-VACE（视频扩展）_1909169358428643330.json, 平台全量/Wan2.1-VACE视频镜头画面扩展延伸_1988234816409788417.json, 平台全量/视频扩展(Wan2.1-VACE-14B)_1923187127436103682.json, 平台全量/视频的虚拟换装-一步到位-参考编辑_1935181584616050690.json, 视频生成/图生视频/CausVid-3步720P首尾帧(Wan2.1&MoviiGen&Skyreels)_1923394290066575361.json, 视频生成/图生视频/vace-1.3b-1280-causvid-pose-fast_1924012489724317698.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_62

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Wan-VACE-图生视频_1933481916970487810.json、平台全量/CausVid-3步720P视频扩展(Wan2.1&MoviiGen&Skyreels)_1923429151527587842.json、平台全量/WAN-VACE（视频扩展）_1909169358428643330.json、平台全量/Wan2.1-VACE视频镜头画面扩展延伸_1988234816409788417.json、平台全量/视频扩展(Wan2.1-VACE-14B)_1923187127436103682.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoSLG` —— 7/8 个有
- `WanVideoTeaCache` —— 7/8 个有
- `WanVideoVACEModelSelect` —— 7/8 个有
- `ImageResizeKJ` —— 6/8 个有
- `String Literal` —— 6/8 个有
- `VHS_LoadVideo` —— 6/8 个有
- `WanVideoTorchCompileSettings` —— 6/8 个有
- `GetImageSize+` —— 5/8 个有
- `MaskToImage` —— 5/8 个有
- `ImagePadKJ` —— 4/8 个有
- `LoadImage` —— 4/8 个有
- `GetNode` —— 3/8 个有
- `WanVideoLoraSelect` —— 3/8 个有
- `GetImageSizeAndCount` —— 2/8 个有
- `GrowMaskWithBlur` —— 2/8 个有
- `INTConstant` —— 2/8 个有
- `SetNode` —— 2/8 个有
- `WanVideoVACEStartToEndFrame` —— 2/8 个有
- `ImageResize+` —— 1/8 个有
- `ImageScale` —— 1/8 个有
- `ImageToMask` —— 1/8 个有
- `InpaintPreprocessor` —— 1/8 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/8 个有
- `easy int` —— 1/8 个有
- `easy seed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
