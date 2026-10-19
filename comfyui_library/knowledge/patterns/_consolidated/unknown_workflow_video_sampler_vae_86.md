---
name: unknown_workflow_video_sampler_vae_86
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9625
common_nodes: [ImageResizeKJ, LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2020431913210617857.json, 视频生成/图生视频/2029224724693262338.json, 视频生成/图生视频/1916457677722161154.json, 视频生成/图生视频/1928118108420980738.json, 视频生成/图生视频/2067524642499289090.json, 视频生成/图生视频/1934649298468708353.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_86

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2020431913210617857.json、视频生成/图生视频/2029224724693262338.json、视频生成/图生视频/1916457677722161154.json、视频生成/图生视频/1928118108420980738.json、视频生成/图生视频/2067524642499289090.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 5/6 个有
- `ImagePadKJ` —— 5/6 个有
- `LoadWanVideoT5TextEncoder` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `WanVideoEnhanceAVideo` —— 3/6 个有
- `WanVideoExperimentalArgs` —— 3/6 个有
- `WanVideoLoraSelect` —— 3/6 个有
- `WanVideoSLG` —— 3/6 个有
- `WanVideoTeaCache` —— 3/6 个有
- `WanVideoTextEncode` —— 3/6 个有
- `WanVideoTextEncodeCached` —— 3/6 个有
- `easy imageRemBg` —— 3/6 个有
- `SimpleMath+` —— 2/6 个有
- `WanVideoTorchCompileSettings` —— 2/6 个有
- `WanVideoMagCache` —— 1/6 个有
- `WanVideoSetBlockSwap` —— 1/6 个有
- `WanVideoSetLoRAs` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
