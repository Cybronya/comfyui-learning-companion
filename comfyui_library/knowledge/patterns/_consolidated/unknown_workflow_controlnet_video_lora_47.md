---
name: unknown_workflow_controlnet_video_lora_47
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.511
common_nodes: [CR Prompt Text, GetNode, ImageConcanate, ImageResizeKJ, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, PrimitiveInt, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/03-05-03-WAN2.1-运镜控制-图生视频-Uni3C_1989933102204153857.json, 视频生成/图生视频/03-05-04-WAN2.1-运镜控制-Uni3C+Omniconsistency风格转绘_1989933159632564226.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_47

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/03-05-03-WAN2.1-运镜控制-图生视频-Uni3C_1989933102204153857.json、视频生成/图生视频/03-05-04-WAN2.1-运镜控制-Uni3C+Omniconsistency风格转绘_1989933159632564226.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `GetNode`
- `ImageConcanate`
- `ImageResizeKJ`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `PrimitiveInt`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `FlashVSR_SM_KSampler` —— 1/2 个有
- `FlashVSR_SM_Model` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `RunningHub OmniConsistency LoraLoader` —— 1/2 个有
- `RunningHub OmniConsistency Sampler` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.39717e+08 | - | 1 | 100% |
| Prompt 约束强度(CFG) | fixed | - | 1 | 100% |
| 采样算法 | 2 | - | 1 | 100% |
| 调度器 | 3.5 | - | 1 | 100% |
| 重绘幅度 | 11 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：采样步数 观测到 8.39717e+08，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
