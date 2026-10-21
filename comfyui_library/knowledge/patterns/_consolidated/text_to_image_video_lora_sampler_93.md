---
name: text_to_image_video_lora_sampler_93
type: Text To Image
frequency: 8
level: strong
coverage: 0.59625
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3多模态参考数字人对口型图生视频处理工具_2101006638630129665.json, 视频生成/图生视频/MiniMax H3官方工作流首尾帧生成视频｜图生视频_2090425354019229697.json, 视频生成/图生视频/MiniMax H3打斗单采｜高质量图生视频生成_2095594939815129089.json, 视频生成/图生视频/MiniMaxH38高动态加速流｜人物场景类特效图生视频_2092030919111692289.json, 视频生成/图生视频/心然寻源MiniMax H3多模态参考数字人对口型｜图生视频_2100764134798352386.json, 视频生成/图生视频/最强文戏低配版｜MINIMAX-H3开源角色一致性生成_2095074002149662722.json, 视频生成/图生视频/首尾帧生成视频｜MiniMax H3官方工作流图生视频_2090268705291849730.json, 视频生成/文生视频/多参考生成视频｜MiniMax H3官方工作流一键直出_2090147863308357634.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_93

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多模态参考数字人对口型图生视频处理工具_2101006638630129665.json、视频生成/图生视频/MiniMax H3官方工作流首尾帧生成视频｜图生视频_2090425354019229697.json、视频生成/图生视频/MiniMax H3打斗单采｜高质量图生视频生成_2095594939815129089.json、视频生成/图生视频/MiniMaxH38高动态加速流｜人物场景类特效图生视频_2092030919111692289.json、视频生成/图生视频/心然寻源MiniMax H3多模态参考数字人对口型｜图生视频_2100764134798352386.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 8 个 workflow 都包含：
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
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `LoadAudio` —— 5/8 个有
- `PreviewImage` —— 5/8 个有
- `VAEDecodeAudio` —— 5/8 个有
- `PrimitiveFloat` —— 4/8 个有
- `Text` —— 4/8 个有
- `CR Prompt Text` —— 3/8 个有
- `Float` —— 3/8 个有
- `MiniMaxH3AVDecodeT8` —— 3/8 个有
- `ExtendIntermediateSigmas` —— 2/8 个有
- `H3SigmaRefiner` —— 2/8 个有
- `ModelAttentionBackend` —— 2/8 个有
- `PreviewAudio` —— 2/8 个有
- `RunningHub Deepcleaner` —— 2/8 个有
- `SigmasGraph` —— 2/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `ZNGB_AudioCrop` —— 2/8 个有
- `FloatConstant` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `Text Multiline` —— 1/8 个有
- `easy clearCacheAll` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
