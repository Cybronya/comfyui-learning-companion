---
name: unknown_workflow_video_sampler_vae_28
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.98575
common_nodes: [CR Text, INTConstant, ImpactInt, LoadWanVideoT5TextEncoder, SimpleMath+, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1967630576679358465.json, 视频生成/图生视频/1991002919573102593.json, 视频生成/图生视频/1968580959744479233.json, 视频生成/图生视频/1955641756994846722.json, 视频生成/图生视频/1958079800877469697.json, 视频生成/图生视频/1958076393995251714.json, 视频生成/图生视频/1967120522687418370.json, 视频生成/图生视频/1967414406411849730.json, 视频生成/图生视频/1952313682334298114.json, 视频生成/图生视频/1955569910405632001.json, 视频生成/文生视频/1955636533911961602.json, 视频生成/文生视频/1955577936088895489.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_28

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1967630576679358465.json、视频生成/图生视频/1991002919573102593.json、视频生成/图生视频/1968580959744479233.json、视频生成/图生视频/1955641756994846722.json、视频生成/图生视频/1958079800877469697.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 12 个 workflow 都包含：
- `CR Text`
- `INTConstant`
- `ImpactInt`
- `LoadWanVideoT5TextEncoder`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 10/12 个有
- `ImageResizeKJv2` —— 10/12 个有
- `LoadImage` —— 10/12 个有
- `WanVideoImageToVideoEncode` —— 10/12 个有
- `WanVideoLoraSelect` —— 7/12 个有
- `WanVideoSetLoRAs` —— 7/12 个有
- `WanVideoLoraSelectMulti` —— 5/12 个有
- `easy cleanGpuUsed` —— 4/12 个有
- `WanVideoContextOptions` —— 3/12 个有
- `Note Plus (mtb)` —— 2/12 个有
- `WanVideoEmptyEmbeds` —— 2/12 个有
- `CreateCFGScheduleFloatList` —— 1/12 个有
- `CreateVideo` —— 1/12 个有
- `ImageConcanate` —— 1/12 个有
- `ImageResizeKJ` —— 1/12 个有
- `PreViewVideo` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
