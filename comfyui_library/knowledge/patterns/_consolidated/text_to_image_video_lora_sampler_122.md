---
name: text_to_image_video_lora_sampler_122
type: Text To Image
frequency: 6
level: strong
coverage: 0.600333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/多图参考生视频｜MiniMax H3图生视频_2090451614204252162.json, 视频生成/图生视频/多图参考生视频｜MiniMax H3图生视频一键直出_2090274287373611010.json, 视频生成/图生视频/心然寻源MiniMax H3多模态参考数字人对口型｜图生视频_2100764134798352386.json, 视频生成/图生视频/打斗单采图生视频｜AITUDOU-MiniMax H3生成_2095847355185717249.json, 视频生成/图生视频/最强文戏低配版｜MINIMAX-H3开源角色一致性生成_2095074002149662722.json, 视频生成/图生视频/音频驱动数字人｜MiniMax H3图生视频口播直出_2090205102572400642.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_122

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/多图参考生视频｜MiniMax H3图生视频_2090451614204252162.json、视频生成/图生视频/多图参考生视频｜MiniMax H3图生视频一键直出_2090274287373611010.json、视频生成/图生视频/心然寻源MiniMax H3多模态参考数字人对口型｜图生视频_2100764134798352386.json、视频生成/图生视频/打斗单采图生视频｜AITUDOU-MiniMax H3生成_2095847355185717249.json、视频生成/图生视频/最强文戏低配版｜MINIMAX-H3开源角色一致性生成_2095074002149662722.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Float` —— 5/6 个有
- `SigmasGraph` —— 4/6 个有
- `Text` —— 4/6 个有
- `Divide [DVB]` —— 3/6 个有
- `FlashVSRNode` —— 3/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `Int` —— 3/6 个有
- `JWInteger` —— 3/6 个有
- `LoadAudio` —— 3/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `ExtendIntermediateSigmas` —— 2/6 个有
- `H3SigmaRefiner` —— 2/6 个有
- `ModelAttentionBackend` —— 2/6 个有
- `ZNGB_AudioCrop` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `SoundFlow_GetLength` —— 1/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
