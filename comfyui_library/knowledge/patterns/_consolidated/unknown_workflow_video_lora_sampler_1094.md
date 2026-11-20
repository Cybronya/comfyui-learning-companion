---
name: unknown_workflow_video_lora_sampler_1094
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8455
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ContextWindowsManual, ImageFromBatch, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveInt, SamplerCustom, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimate2Cache, WanAnimate2ToVideo]
problems: []
missing: []
members: [视频生成/图生视频/WanAnimate2-自动长视频无劣化动作迁移_2116900699735941122.json, 视频生成/图生视频/animate2 动作迁移_2086041332744810498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_1094

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/WanAnimate2-自动长视频无劣化动作迁移_2116900699735941122.json、视频生成/图生视频/animate2 动作迁移_2086041332744810498.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ContextWindowsManual`
- `ImageFromBatch`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `SamplerCustom`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimate2Cache`
- `WanAnimate2ToVideo`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 1/2 个有
- `ComfySwitchNode` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `ImageScale` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `RTXVideoFrameGeneration` —— 1/2 个有
- `RTXVideoSuperResolution` —— 1/2 个有
- `ResizeImagesByLongerEdge` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
