---
name: unknown_workflow_video_lora_sampler_720
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5255
common_nodes: [CR Prompt Text, Fast Groups Bypasser (rgthree), FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetNode, ImageConcanate, ImageFromBatch+, ImageResizeKJ, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1989234385289359361.json, 视频生成/图生视频/1989933102204153857.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_720

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1989234385289359361.json、视频生成/图生视频/1989933102204153857.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：53%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetNode`
- `ImageConcanate`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ADE_CameraPoseBasic` —— 1/2 个有
- `CameraPoseVisualizer` —— 1/2 个有
- `FloatConstant` —— 1/2 个有
- `INTConstant` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `VHS_VideoInfoLoaded` —— 1/2 个有
- `WanVideoEncode` —— 1/2 个有
- `WanVideoEnhanceAVideo` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoFunCameraEmbeds` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `WanVideoTeaCache` —— 1/2 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/2 个有
- `WanVideoUni3C_embeds` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.39717e+08 | - | 2 | 100% |
| Prompt 约束强度(CFG) | fixed | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 11 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8.39717e+08，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 最常用 fixed，2 个样本，一致性 100%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 8.39717e+08，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
