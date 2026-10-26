---
name: unknown_workflow_video_lora_sampler_851
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.788
common_nodes: [BasicScheduler, CLIPTextEncode, CS-LTXGridDirector, DualCLIPLoader, JjkText, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ModelPreviewOverrideKJ, SamplerCustom, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ, YusuLTXDirectorCropGuides, 孤海注释]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-LTX Director-全自动宫格导演台-自动剧情-角色一致性_2080617902188879873.json, 视频生成/图生视频/LTX2.3-LTX Director-全自动宫格导演台-角色一致性-自动剧情_2080573147191005186.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_851

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-LTX Director-全自动宫格导演台-自动剧情-角色一致性_2080617902188879873.json、视频生成/图生视频/LTX2.3-LTX Director-全自动宫格导演台-角色一致性-自动剧情_2080573147191005186.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `CS-LTXGridDirector`
- `DualCLIPLoader`
- `JjkText`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPreviewOverrideKJ`
- `SamplerCustom`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`
- `YusuLTXDirectorCropGuides`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Int` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `RH_Utils` —— 1/2 个有
- `Text` —— 1/2 个有
- `ttN concat` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
