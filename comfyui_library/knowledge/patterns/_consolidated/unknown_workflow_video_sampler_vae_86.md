---
name: unknown_workflow_video_sampler_vae_86
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.930429
common_nodes: [INTConstant, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN-VACE(双图参考)_1909082788321239041.json, 视频生成/图生视频/WAN-VACE(图像参考)_1909078127585468418.json, 视频生成/图生视频/WAN-VACE（首尾帧）_1909172301974089729.json, 视频生成/图生视频/fusionxPhantom两图融合_1933797677106946049.json, 视频生成/图生视频/单图参考(Wan2.1-VACE-14B)_1923226071490359297.json, 视频生成/图生视频/多图参考(Wan2.1-VACE-14B)_1923186184321683457.json, 视频生成/图生视频/多图融合-Phantom-Wan-14B_1927603788339634178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_86

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/WAN-VACE(双图参考)_1909082788321239041.json、视频生成/图生视频/WAN-VACE(图像参考)_1909078127585468418.json、视频生成/图生视频/WAN-VACE（首尾帧）_1909172301974089729.json、视频生成/图生视频/fusionxPhantom两图融合_1933797677106946049.json、视频生成/图生视频/单图参考(Wan2.1-VACE-14B)_1923226071490359297.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
- `INTConstant`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 6/7 个有
- `Image Blank` —— 6/7 个有
- `ImageCompositeMasked` —— 6/7 个有
- `LayerMask: LoadFlorence2Model` —— 6/7 个有
- `LayerMask: ObjectDetectorFL2` —— 6/7 个有
- `LayerMask: SAM2Ultra` —— 6/7 个有
- `String Literal` —— 5/7 个有
- `WanVideoVACEEncode` —— 5/7 个有
- `WanVideoSLG` —— 4/7 个有
- `WanVideoTeaCache` —— 4/7 个有
- `ImageConcanate` —— 2/7 个有
- `ImagePadKJ` —— 2/7 个有
- `KepStringLiteral` —— 2/7 个有
- `LayerUtility: PurgeVRAM V2` —— 2/7 个有
- `WanVideoEncode` —— 2/7 个有
- `WanVideoPhantomEmbeds` —— 2/7 个有
- `WanVideoVACEModelSelect` —— 2/7 个有
- `GetImageSizeAndCount` —— 1/7 个有
- `LayerUtility: PurgeVRAM` —— 1/7 个有
- `MaskPreview+` —— 1/7 个有
- `WanVideoVACEStartToEndFrame` —— 1/7 个有
- `easy ifElse` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
