---
name: unknown_workflow_video_sampler_vae_116
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.984
common_nodes: [ImageResizeKJ, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.1+视频生视频 lora高清_2041685485076090882.json, 平台全量/Wan视频生视频高质量加速工作流V2（比V1快1倍）_1894660227172839426.json, 平台全量/油画版Wan高质量加速版视频转视频工作流_1906709327091052546.json, 平台全量/通义万相wan2.1视频转绘支持Control 控制_1907050424120303617.json, 平台全量/🦖Wan2.1 视频生视频（更新03014）更新lora高清_1894921636406308866.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_116

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/Wan2.1+视频生视频 lora高清_2041685485076090882.json、平台全量/Wan视频生视频高质量加速工作流V2（比V1快1倍）_1894660227172839426.json、平台全量/油画版Wan高质量加速版视频转视频工作流_1906709327091052546.json、平台全量/通义万相wan2.1视频转绘支持Control 控制_1907050424120303617.json、平台全量/🦖Wan2.1 视频生视频（更新03014）更新lora高清_1894921636406308866.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 4/5 个有
- `Note _O` —— 4/5 个有
- `WanVideoLoraSelect` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `WanVideoExperimentalArgs` —— 3/5 个有
- `WanVideoSLG` —— 3/5 个有
- `FusionText` —— 2/5 个有
- `Note Plus (mtb)` —— 2/5 个有
- `Primitive string multiline [Crystools]` —— 2/5 个有
- `String` —— 2/5 个有
- `GetImageSizeAndCount` —— 1/5 个有
- `TextInput_` —— 1/5 个有
- `WanVideoControlEmbeds` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
