---
name: unknown_workflow_video_sampler_vae_77
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.878857
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1947893136549904385.json, 视频生成/图生视频/1948691890660081665.json, 视频生成/图生视频/1907320238373756930.json, 视频生成/图生视频/1930306829082071042.json, 视频生成/图生视频/1905464146912006145.json, 视频生成/图生视频/1921944895412699138.json, 视频生成/文生视频/1917099381894615042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_77

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1947893136549904385.json、视频生成/图生视频/1948691890660081665.json、视频生成/图生视频/1907320238373756930.json、视频生成/图生视频/1930306829082071042.json、视频生成/图生视频/1905464146912006145.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoEnhanceAVideo` —— 6/7 个有
- `WanVideoTorchCompileSettings` —— 6/7 个有
- `CLIPVisionLoader` —— 4/7 个有
- `WanVideoExperimentalArgs` —— 4/7 个有
- `WanVideoLoraSelect` —— 4/7 个有
- `WanVideoSLG` —— 4/7 个有
- `LoadWanVideoClipTextEncoder` —— 3/7 个有
- `WanVideoVRAMManagement` —— 3/7 个有
- `Int` —— 2/7 个有
- `KepStringLiteral` —— 2/7 个有
- `LoadImageFromUrl` —— 2/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `VHS_LoadVideo` —— 2/7 个有
- `WanVideoUniAnimatePoseInput` —— 2/7 个有
- `easy showAnything` —— 2/7 个有
- `PrimitiveInt` —— 1/7 个有
- `TextInputBasic` —— 1/7 个有
- `TextInput_` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
