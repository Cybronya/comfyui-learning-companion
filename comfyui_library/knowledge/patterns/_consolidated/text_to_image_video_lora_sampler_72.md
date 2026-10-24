---
name: text_to_image_video_lora_sampler_72
type: Text To Image
frequency: 10
level: strong
coverage: 0.8139
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/全能插件加速版minimaxH3数字人工作流_2087430084268482561.json, 视频生成/图生视频/商业级360度环绕镜头展示｜产品级运镜一镜到底_2111325834421293058.json, 视频生成/文生视频/8步768p加速新版 MiniMax H3 单采高质量文生视频_2094171689625153537.json, 视频生成/文生视频/8步768p加速新版｜MiniMax H3单采高质量三模视频_2094310836981551107.json, 视频生成/文生视频/Minimax双采全功能视频工作流｜文生视频图生视频视频生视频三合一_2088696202564038657.json, 视频生成/文生视频/全功能双采二选一｜Minimax文生视频图生视频视频生视频_2089019399863889922.json, 视频生成/文生视频/单采高质量加速版｜MiniMax H3去除人物油腻处理_2092550530987020289.json, 视频生成/文生视频/漫剧工作流15秒直出｜Mini Max H3文生图生视频生视频_2088366199813001217.json, 视频生成/视频生视频/双模型加强版二采重绘MiniMax H3全能参考RH兼容版，9图参考图生视频_2106499744423043074.json, 视频生成/视频生视频/双模型加强版二采重绘｜MinimaxH3全能参考图生视频RH兼容版_2106194718110609410.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_72

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/全能插件加速版minimaxH3数字人工作流_2087430084268482561.json、视频生成/图生视频/商业级360度环绕镜头展示｜产品级运镜一镜到底_2111325834421293058.json、视频生成/文生视频/8步768p加速新版 MiniMax H3 单采高质量文生视频_2094171689625153537.json、视频生成/文生视频/8步768p加速新版｜MiniMax H3单采高质量三模视频_2094310836981551107.json、视频生成/文生视频/Minimax双采全功能视频工作流｜文生视频图生视频视频生视频三合一_2088696202564038657.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ModelAttentionBackend` —— 9/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/10 个有
- `MiniMaxH3Unified` —— 7/10 个有
- `VAEDecodeAudio` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `PrimitiveFloat` —— 6/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `ImageResizeKJv2` —— 5/10 个有
- `PT_H3ConcatAVLatent` —— 5/10 个有
- `VAEEncode` —— 5/10 个有
- `easy clearCacheAll` —— 5/10 个有
- `CR Text` —— 4/10 个有
- `LoadImage` —— 4/10 个有
- `ModelPreviewOverrideKJ` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `ComfyMathExpression` —— 3/10 个有
- `GetNode` —— 3/10 个有
- `LoadAudio` —— 3/10 个有
- `MiniMaxChunkFeedForward` —— 3/10 个有
- `MiniMaxH3AVDecodeT8` —— 3/10 个有
- `MiniMaxH3ReferenceToVideo` —— 3/10 个有
- `MiniMaxH3SigmaShift` —— 3/10 个有
- `MiniMaxLowVRAMAttention` —— 3/10 个有
- `VAEEncodeAudio` —— 3/10 个有
- `EasyCache` —— 2/10 个有
- `INTConstant` —— 2/10 个有
- `Label (rgthree)` —— 2/10 个有
- `LoraLoaderBypassModelOnly` —— 2/10 个有
- `ResizeShortestToNode` —— 2/10 个有
- `TrimAudioDuration` —— 2/10 个有
- `UniBlockSwap` —— 2/10 个有
- `UniBlockSwapTE` —— 2/10 个有
- `VHS_LoadVideo` —— 2/10 个有
- `MemoryCleaner` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `SigmasGraph` —— 1/10 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
