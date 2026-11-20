---
name: unknown_workflow_video_sampler_vae_181
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.611333
common_nodes: [ADE_CameraPoseBasic, CameraPoseVisualizer, GetNode, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoFunCameraEmbeds, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/【Wan2.1系列】轻松生成电影级运镜画面！Fun Camera模型实战解析轻松掌握运镜_1921554498571943938.json, 平台全量/阿里Wan2.1图生视频运镜控制_1919936152940515330.json, 视频生成/图生视频/03-05-01-WAN2.1-运镜控制-图生视频-FUN-CameralControl_1989234385289359361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_181

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/【Wan2.1系列】轻松生成电影级运镜画面！Fun Camera模型实战解析轻松掌握运镜_1921554498571943938.json、平台全量/阿里Wan2.1图生视频运镜控制_1919936152940515330.json、视频生成/图生视频/03-05-01-WAN2.1-运镜控制-图生视频-FUN-CameralControl_1989234385289359361.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 3 个 workflow 都包含：
- `ADE_CameraPoseBasic`
- `CameraPoseVisualizer`
- `GetNode`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoFunCameraEmbeds`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `ImageResizeKJ` —— 2/3 个有
- `WanVideoEnhanceAVideo` —— 2/3 个有
- `WanVideoSLG` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `CR Text` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `FlashVSR_SM_KSampler` —— 1/3 个有
- `FlashVSR_SM_Model` —— 1/3 个有
- `FloatConstant` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `ImageFromBatch+` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `Int` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有

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
