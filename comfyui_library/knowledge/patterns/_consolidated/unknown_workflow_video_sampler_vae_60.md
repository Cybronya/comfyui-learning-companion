---
name: unknown_workflow_video_sampler_vae_60
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9135
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1979771248119025665.json, 视频生成/图生视频/1976854157967740929.json, 视频生成/图生视频/1977734210951729153.json, 视频生成/图生视频/2000380802502455298.json, 视频生成/图生视频/1999041056794628098.json, 视频生成/图生视频/1999430361350275074.json, 视频生成/图生视频/2007414676862279682.json, 视频生成/图生视频/1998599416028258305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_60

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/1979771248119025665.json、视频生成/图生视频/1976854157967740929.json、视频生成/图生视频/1977734210951729153.json、视频生成/图生视频/2000380802502455298.json、视频生成/图生视频/1999041056794628098.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `WanVideoClipVisionEncode` —— 7/8 个有
- `WanVideoImageToVideoEncode` —— 7/8 个有
- `WanVideoSetLoRAs` —— 7/8 个有
- `WanVideoLoraSelect` —— 6/8 个有
- `RepeatImageBatch` —— 5/8 个有
- `SplineEditor` —— 5/8 个有
- `WanVideoAddWanMoveTracks` —— 5/8 个有
- `WanVideoTorchCompileSettings` —— 5/8 个有
- `WanVideoWanDrawWanMoveTracks` —— 5/8 个有
- `CR Text` —— 3/8 个有
- `GetImageSizeAndCount` —— 3/8 个有
- `INTConstant` —— 3/8 个有
- `PrimitiveInt` —— 3/8 个有
- `easy cleanGpuUsed` —— 3/8 个有
- `ImageFromBatch+` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/8 个有
- `LayerUtility: TextBox` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `WanVideoEmptyEmbeds` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
