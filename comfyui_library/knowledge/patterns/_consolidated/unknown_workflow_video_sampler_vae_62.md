---
name: unknown_workflow_video_sampler_vae_62
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.970625
common_nodes: [GetImageSizeAndCount, INTConstant, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, String Literal, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN-VACE（首尾帧）_1909172301974089729.json, 视频生成/图生视频/图生视频---WAN-VACE（首尾帧）_2043935340162981889.json, 视频生成/图生视频/开源Sota级3图首尾帧组合（Phantom+VACE）_1934543155603644418.json, 视频生成/图生视频/开源Sota级首尾帧组合（Phantom+VACE）_1934460404364111874.json, 视频生成/图生视频/极速生成 --图生视频---WAN-VACE（首尾帧）_2044216380353945602.json, 视频生成/图生视频/超级多模态万物消失特效_1937073203258773506.json, 视频生成/图生视频/首尾帧 图生视频_2044595167281291265.json, 视频生成/图生视频/首尾帧图生视频_2044749490703310849.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_62

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/WAN-VACE（首尾帧）_1909172301974089729.json、视频生成/图生视频/图生视频---WAN-VACE（首尾帧）_2043935340162981889.json、视频生成/图生视频/开源Sota级3图首尾帧组合（Phantom+VACE）_1934543155603644418.json、视频生成/图生视频/开源Sota级首尾帧组合（Phantom+VACE）_1934460404364111874.json、视频生成/图生视频/极速生成 --图生视频---WAN-VACE（首尾帧）_2044216380353945602.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `String Literal`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/8 个有
- `MaskPreview+` —— 5/8 个有
- `WanVideoSLG` —— 3/8 个有
- `WanVideoTeaCache` —— 3/8 个有
- `WanVideoVACEModelSelect` —— 3/8 个有
- `GetImageRangeFromBatch` —— 2/8 个有
- `ImageBatchMulti` —— 2/8 个有
- `MaskBatchMulti` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `LoadWanVideoClipTextEncoder` —— 1/8 个有
- `WanVideoImageClipEncode` —— 1/8 个有
- `WanVideoLoraSelect` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
