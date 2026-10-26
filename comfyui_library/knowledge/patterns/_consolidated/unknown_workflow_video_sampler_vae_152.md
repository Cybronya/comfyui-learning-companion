---
name: unknown_workflow_video_sampler_vae_152
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 1
common_nodes: [AIO_Preprocessor, GetImageSizeAndCount, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/All-in-one 视频驱动图片_1965428165915103234.json, 视频生成/图生视频/wan2.1-动作极速迁移-跳舞-功夫-打架等_1952324361430740994.json, 视频生成/文生视频/WAN2.2-AllInOne控制+参考_1963899111291572225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_152

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/All-in-one 视频驱动图片_1965428165915103234.json、视频生成/图生视频/wan2.1-动作极速迁移-跳舞-功夫-打架等_1952324361430740994.json、视频生成/文生视频/WAN2.2-AllInOne控制+参考_1963899111291572225.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `GetImageSizeAndCount`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `WanVideoLoraSelect` —— 2/3 个有
- `ColorMatch` —— 1/3 个有
- `ImageSmartSharpen+` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `SaveImage` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `WanVideoSetLoRAs` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
