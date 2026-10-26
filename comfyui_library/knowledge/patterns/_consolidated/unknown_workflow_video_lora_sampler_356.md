---
name: unknown_workflow_video_lora_sampler_356
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.853143
common_nodes: [BasicScheduler, CLIPTextEncode, DualCLIPLoader, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MelBandRoFormerModelLoader, MelBandRoFormerSampler, PreviewAudio, SamplerCustom, SetLatentNoiseMask, SolidMask, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-多人对话场景效果（多图分镜）_2058444254300696577.json, 视频生成/图生视频/LTX2.3-多人对话场景效果（多图分镜）_2070137230106124289.json, 视频生成/图生视频/LTX2.3-多图分镜导演，支持漫剧、带货视频、数字人等效果_2055882037822795778.json, 视频生成/图生视频/LTX2.3-音乐数字人演唱效果（多图分镜+情绪控制）_2057812163363950593.json, 视频生成/图生视频/ltx2.3导演台 九宫格 半自动图生视频_2069309703959695362.json, 视频生成/图生视频/ltx2.3导演台 去字幕 短剧视频_漫剧视频_电商视频 多宫格 六宫格 九宫格 自动图生视频_2073463668316323840.json, 视频生成/图生视频/ltx2.3导演台 去字幕 短剧视频_漫剧视频_电商视频 多宫格 六宫格 九宫格 自动图生视频_2076823460927598594.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_356

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-多人对话场景效果（多图分镜）_2058444254300696577.json、视频生成/图生视频/LTX2.3-多人对话场景效果（多图分镜）_2070137230106124289.json、视频生成/图生视频/LTX2.3-多图分镜导演，支持漫剧、带货视频、数字人等效果_2055882037822795778.json、视频生成/图生视频/LTX2.3-音乐数字人演唱效果（多图分镜+情绪控制）_2057812163363950593.json、视频生成/图生视频/ltx2.3导演台 九宫格 半自动图生视频_2069309703959695362.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler`
- `PreviewAudio`
- `SamplerCustom`
- `SetLatentNoiseMask`
- `SolidMask`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `LTXDirectorGuide` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `GuHaiAutoImageSplit` —— 4/7 个有
- `LTXDirector` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `CR Text` —— 3/7 个有
- `CS-LTXGridDirector` —— 3/7 个有
- `Label (rgthree)` —— 3/7 个有
- `PreviewAny` —— 3/7 个有
- `RHHiddenNodes` —— 3/7 个有
- `RH_LLMAPI_Pro_Node` —— 3/7 个有
- `YusuLTXDirectorGuide` —— 2/7 个有
- `孤海注释` —— 2/7 个有
- `LTXVChunkFeedForward` —— 1/7 个有
- `PathchSageAttentionKJ` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
