---
name: unknown_workflow_sampler_clip_unet_153
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.93275
common_nodes: [BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, SamplerCustom, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VisualizeSigmasKJ]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3导演台音频驱动生成视频_2068946442663849986.json, 数字人/数字人/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-VLOG版_2059146940713103362.json, 视频生成/图生视频/LTX-2.3 导演台2.0视频生成工作流_2081626285859753986.json, 视频生成/图生视频/LTX2.3-MSR-V2全能参考视频生成工作流_2078286762836844545.json, 视频生成/图生视频/LTX2.3-MSR-V2全能参考视频生成工作流（青竹悦可用）_2078750645842178049.json, 视频生成/图生视频/LTX2.3-多图分镜、数字人工作流_2060633763377410049.json, 视频生成/图生视频/LTX2.3-导演台多图分镜、数字人工作流_2069942311760523265.json, 视频生成/图生视频/LTX2.3导演台原生音视频_2068943072121147394.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_153

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/LTX2.3导演台音频驱动生成视频_2068946442663849986.json、数字人/数字人/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-VLOG版_2059146940713103362.json、视频生成/图生视频/LTX-2.3 导演台2.0视频生成工作流_2081626285859753986.json、视频生成/图生视频/LTX2.3-MSR-V2全能参考视频生成工作流_2078286762836844545.json、视频生成/图生视频/LTX2.3-MSR-V2全能参考视频生成工作流（青竹悦可用）_2078750645842178049.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `SamplerCustom`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `LTX2SamplingPreviewOverride` —— 6/8 个有
- `LTXVCropGuides` —— 6/8 个有
- `VHS_VideoCombine` —— 6/8 个有
- `LTXDirector` —— 5/8 个有
- `LTXDirectorGuide` —— 4/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `ModelPreviewOverrideKJ` —— 4/8 个有
- `YusuLTXDirectorGuide` —— 4/8 个有
- `YusuLTXDirector` —— 3/8 个有
- `ComfySwitchNode` —— 2/8 个有
- `CreateVideo` —— 2/8 个有
- `PrimitiveBoolean` —— 2/8 个有
- `SaveVideo` —— 2/8 个有
- `TTResolutionSelector` —— 2/8 个有
- `YusuLTXDirectorCropGuides` —— 2/8 个有
- `孤海注释` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
