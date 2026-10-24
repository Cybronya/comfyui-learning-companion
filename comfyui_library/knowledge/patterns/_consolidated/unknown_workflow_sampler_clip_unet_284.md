---
name: unknown_workflow_sampler_clip_unet_284
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9375
common_nodes: [BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, SamplerCustom, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VisualizeSigmasKJ]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3导演台音频驱动生成视频_2068946442663849986.json, 视频生成/图生视频/LTX2.3-多图分镜、数字人工作流_2060633763377410049.json, 视频生成/图生视频/LTX2.3-导演台多图分镜、数字人工作流_2069942311760523265.json, 视频生成/图生视频/LTX2.3导演台原生音视频_2068943072121147394.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_284

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/LTX2.3导演台音频驱动生成视频_2068946442663849986.json、视频生成/图生视频/LTX2.3-多图分镜、数字人工作流_2060633763377410049.json、视频生成/图生视频/LTX2.3-导演台多图分镜、数字人工作流_2069942311760523265.json、视频生成/图生视频/LTX2.3导演台原生音视频_2068943072121147394.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `SamplerCustom`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 2/4 个有
- `CreateVideo` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PrimitiveBoolean` —— 2/4 个有
- `SaveVideo` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
