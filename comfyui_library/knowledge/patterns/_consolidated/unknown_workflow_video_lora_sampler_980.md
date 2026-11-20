---
name: unknown_workflow_video_lora_sampler_980
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.686
common_nodes: [AIO_Preprocessor, Anything Everywhere, BasicScheduler, CLIPLoader, CLIPTextEncode, Fast Groups Muter (rgthree), GetNode, ImageResizeKJ, ImageScale, InstructPixToPixConditioning, KSamplerSelect, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, ModelSamplingSD3, RIFE VFI, SamplerCustom, SetNode, SplitSigmas, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_SelectImages, VHS_VideoCombine, WanVideoControlEmbeds, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.1 depth 控制_1902645599588528130.json, 视频生成/文生视频/动态控制_1937034897288515586.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_980

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Wan2.1 depth 控制_1902645599588528130.json、视频生成/文生视频/动态控制_1937034897288515586.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：69%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `ImageResizeKJ`
- `ImageScale`
- `InstructPixToPixConditioning`
- `KSamplerSelect`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `RIFE VFI`
- `SamplerCustom`
- `SetNode`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_SelectImages`
- `VHS_VideoCombine`
- `WanVideoControlEmbeds`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
