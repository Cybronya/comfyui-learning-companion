---
name: unknown_workflow_video_lora_sampler_915
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.441
common_nodes: [AILab_QwenVL, BasicGuider, BasicScheduler, BiRefNetRMBG, CLIPLoader, CR Text, ComfyMathExpression, CreateVideo, EasyCache, FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetVideoComponents, ImageFromBatch+, JjkText, JoinStrings, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PreviewAny, PreviewImage, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, RunningHub Deepcleaner, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, VideoFrameSelector]
problems: []
missing: []
members: [视频生成/图生视频/角色替换+动作迁移+面部表情=爆款复刻_2099026530998509569.json, 视频生成/图生视频/角色替换+动作迁移+面部表情=爆款复刻_2103311101395030017.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_915

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/角色替换+动作迁移+面部表情=爆款复刻_2099026530998509569.json、视频生成/图生视频/角色替换+动作迁移+面部表情=爆款复刻_2103311101395030017.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：44%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `BasicGuider`
- `BasicScheduler`
- `BiRefNetRMBG`
- `CLIPLoader`
- `CR Text`
- `ComfyMathExpression`
- `CreateVideo`
- `EasyCache`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetVideoComponents`
- `ImageFromBatch+`
- `JjkText`
- `JoinStrings`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `RunningHub Deepcleaner`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `VideoFrameSelector`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4.01887e+08 | - | 2 | 24% |
| Prompt 约束强度(CFG) | randomize | - | 2 | 100% |
| 采样算法 | 3 | - | 2 | 100% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 11 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 4.01887e+08，样本不足，未给区间，2 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 最常用 randomize，2 个样本，一致性 100%
- 采样算法 中位数 3，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 7.05552e+08，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
