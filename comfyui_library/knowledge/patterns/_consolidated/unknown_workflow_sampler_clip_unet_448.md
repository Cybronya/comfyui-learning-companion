---
name: unknown_workflow_sampler_clip_unet_448
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.839
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Latent Batch Size, ConstrainImage|pysssss, DepthAnythingV2Preprocessor, DualCLIPLoader, Florence2ModelLoader, Florence2Run, FluxGuidance, KSamplerSelect, LayerFilter: FilmV2, LayerFilter: HDREffects, LayerUtility: TextJoin, LoadImage, PortraitMaster, PortraitMasterMakeup, PortraitMasterSkinDetails, PortraitMasterStylePose, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowText|pysssss, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/洗图V1-dy红薯过审加噪颗粒阴影_2022769389350690818.json, 图片生成/文生图/炼丹所需工作流+打标_1920288590247694337.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_448

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/洗图V1-dy红薯过审加噪颗粒阴影_2022769389350690818.json、图片生成/文生图/炼丹所需工作流+打标_1920288590247694337.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Latent Batch Size`
- `ConstrainImage|pysssss`
- `DepthAnythingV2Preprocessor`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `KSamplerSelect`
- `LayerFilter: FilmV2`
- `LayerFilter: HDREffects`
- `LayerUtility: TextJoin`
- `LoadImage`
- `PortraitMaster`
- `PortraitMasterMakeup`
- `PortraitMasterSkinDetails`
- `PortraitMasterStylePose`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ArgosTranslateTextNode` —— 1/2 个有
- `Batch_joy_caption_two_advanced` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `DeepTranslatorTextNode` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `Joy_caption_two` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `Joy_extra_options` —— 1/2 个有
- `LayerFilter: AddGrain` —— 1/2 个有
- `LayerFilter: MotionBlur` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `SetUnionControlNetType` —— 1/2 个有
- `StringFunction|pysssss` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.5 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| ControlNet 权重 | 0.3 | - | 1 | 100% |
| 宽度 | 768 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
