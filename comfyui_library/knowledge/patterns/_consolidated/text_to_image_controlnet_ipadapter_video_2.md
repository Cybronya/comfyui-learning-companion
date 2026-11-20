---
name: text_to_image_controlnet_ipadapter_video_2
type: Text To Image
frequency: 2
level: weak
coverage: 0.8215
common_nodes: [ACN_AdvancedControlNetApply, ADE_AnimateDiffLoRALoader, ADE_AnimateDiffSamplingSettings, ADE_ApplyAnimateDiffModelSimple, ADE_LoadAnimateDiffModel, ADE_LoopedUniformContextOptions, ADE_MultivalDynamic, ADE_UseEvolvedSampling, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, EmptyLatentImage, IPAdapterAdvanced, IPAdapterUnifiedLoader, ImageResize+, InvertMask, KSampler, LeReS-DepthMapPreprocessor, LineArtPreprocessor, LoadImage, LoraLoader, MaskPreview+, MaskToImage, PrepImageForClipVision, PreviewImage, VAEDecode, VHS_LoadVideo, VHS_VideoCombine, easy imageRemBg, easy seed]
problems: []
missing: []
members: [平台全量/视频转绘（万物材质跳舞）_1909787928523145217.json, 视频生成/文生视频/视频转绘（万物跳舞）_1885667172683796482.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_ipadapter_video_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/视频转绘（万物材质跳舞）_1909787928523145217.json、视频生成/文生视频/视频转绘（万物跳舞）_1885667172683796482.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `ACN_AdvancedControlNetApply`
- `ADE_AnimateDiffLoRALoader`
- `ADE_AnimateDiffSamplingSettings`
- `ADE_ApplyAnimateDiffModelSimple`
- `ADE_LoadAnimateDiffModel`
- `ADE_LoopedUniformContextOptions`
- `ADE_MultivalDynamic`
- `ADE_UseEvolvedSampling`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `EmptyLatentImage`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `ImageResize+`
- `InvertMask`
- `KSampler`
- `LeReS-DepthMapPreprocessor`
- `LineArtPreprocessor`
- `LoadImage`
- `LoraLoader`
- `MaskPreview+`
- `MaskToImage`
- `PrepImageForClipVision`
- `PreviewImage`
- `VAEDecode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy imageRemBg`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 1/2 个有
- `IFRNet VFI` —— 1/2 个有
- `ImageUpscaleWithModel` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.8 | - | 2 | 100% |
| LoRA 文本强度 | 0.8 | - | 2 | 100% |
| 采样步数 | 10 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | lcm | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
